from janis_core import Boolean

from janis_bioinformatics.data_types import FastaWithDict, BamBai, BedTabix
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common import (
    SplitMultiAlleleNormaliseVcf,
    UncompressVcf,
)
from janis_bioinformatics.tools.illumina import StrelkaGermline_2_9_10, Manta_1_5_0
from janis_bioinformatics.tools.vcftools import VcfToolsvcftoolsLatest


class IlluminaGermlineVariantCaller(BioinformaticsWorkflow):
    def id(self):
        return "strelkaGermlineVariantCaller"

    def friendly_name(self):
        return "Strelka Germline Variant Caller"

    def tool_provider(self):
        return "Variant Callers"

    def version(self):
        return "v0.1.0"

    def constructor(self):

        self.input("bam", BamBai)
        self.input("reference", FastaWithDict)
        self.input("intervals", BedTabix(optional=True))
        self.input("is_exome", Boolean(optional=True))

        self.step(
            "manta",
            Manta_1_5_0(
                bam=self.bam,
                reference=self.reference,
                callRegions=self.intervals,
                exome=self.is_exome,
            ),
        )

        self.step(
            "strelka",
            StrelkaGermline_2_9_10(
                bam=self.bam,
                reference=self.reference,
                indelCandidates=self.manta.candidateSmallIndels,
                callRegions=self.intervals,
                exome=self.is_exome,
            ),
        )

        self.step(
            "uncompressvcf", UncompressVcf(vcfTabix=self.strelka.variants, stdout=True,)
        )

        self.step(
            "splitnormalisevcf",
            SplitMultiAlleleNormaliseVcf(
                vcf=self.uncompressvcf.out, reference=self.reference
            ),
        )

        self.step(
            "fileterpass",
            VcfToolsvcftoolsLatest(
                vcf=self.splitnormalisevcf.out,
                prefix="out",
                removeFileteredAll=True,
                recode=True,
                recodeINFOAll=True,
            ),
        )

        self.output("diploid", source=self.manta.diploidSV)
        self.output("variants", source=self.strelka.variants)
        self.output("out", source=self.fileterpass.out)


if __name__ == "__main__":

    wf = IlluminaGermlineVariantCaller()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
