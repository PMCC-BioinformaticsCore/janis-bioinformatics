from janis_core import Boolean
from janis_unix.tools import UncompressArchive

from janis_bioinformatics.data_types import FastaWithDict, BamBai, BedTabix
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common import (
    SplitMultiAllele,
    ConcatStrelkaSomaticVcf,
)
from janis_bioinformatics.tools.htslib import BGZipLatest, TabixLatest
from janis_bioinformatics.tools.illumina import Manta_1_5_0, StrelkaSomatic_2_9_10
from janis_bioinformatics.tools.pmac import ExtractStrelkaSomaticADDP_0_0_9
from janis_bioinformatics.tools.vcftools import VcfToolsvcftoolsLatest


class IlluminaSomaticVariantCaller(BioinformaticsWorkflow):
    def id(self):
        return "strelkaSomaticVariantCaller"

    def friendly_name(self):
        return "Strelka Somatic Variant Caller"

    def tool_provider(self):
        return "Variant Callers"

    def version(self):
        return "v0.1.1"

    def constructor(self):

        self.input("normal_bam", BamBai)
        self.input("tumor_bam", BamBai)

        self.input("reference", FastaWithDict)
        self.input("intervals", BedTabix(optional=True))

        self.input("is_exome", Boolean(optional=True))

        self.step(
            "manta",
            Manta_1_5_0(
                bam=self.normal_bam,
                tumorBam=self.tumor_bam,
                reference=self.reference,
                callRegions=self.intervals,
                exome=self.is_exome,
            ),
        )
        self.step(
            "strelka",
            StrelkaSomatic_2_9_10(
                indelCandidates=self.manta.candidateSmallIndels,
                normalBam=self.normal_bam,
                tumorBam=self.tumor_bam,
                reference=self.reference,
                callRegions=self.intervals,
                exome=self.is_exome,
            ),
        )
        self.step(
            "concatvcf",
            ConcatStrelkaSomaticVcf(
                headerVcfs=[self.strelka.snvs, self.strelka.indels],
                contentVcfs=[self.strelka.snvs, self.strelka.indels],
            ),
        )
        self.step("tabixvcf", TabixLatest(inp=self.concatvcf.out))

        self.step("uncompressvcf", UncompressArchive(file=self.concatvcf.out))
        self.step(
            "splitnormalisevcf",
            SplitMultiAllele(vcf=self.uncompressvcf.out, reference=self.reference),
        )
        self.step(
            "extractaddp",
            ExtractStrelkaSomaticADDP_0_0_9(vcf=self.splitnormalisevcf.out),
        )

        self.step(
            "filterpass",
            VcfToolsvcftoolsLatest(
                vcf=self.extractaddp.out,
                removeFileteredAll=True,
                recode=True,
                recodeINFOAll=True,
            ),
        )

        self.output("sv", source=self.manta.diploidSV)
        self.output("variants", source=self.tabixvcf.out)
        self.output("out", source=self.filterpass.out)
