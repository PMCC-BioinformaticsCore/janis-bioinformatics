from datetime import date

from janis_bioinformatics.data_types import BedTabix, CramCrai, FastaWithDict
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import (
    BcfToolsIndex_1_9 as BcfToolsIndex,
    BcfToolsNorm_1_9 as BcfToolsNorm,
)
from janis_bioinformatics.tools.illumina.manta.manta import MantaCram_1_5_0 as Manta
from janis_bioinformatics.tools.illumina.strelkasomatic.strelkasomatic import (
    StrelkaSomaticCram_2_9_10 as Strelka,
)
from janis_core import Boolean


class Strelka2PassWorkflowStep1(BioinformaticsWorkflow):
    def id(self):
        return "Strelka2PassWorkflowStep1"

    def friendly_name(self):
        return "Strelka 2Pass analysis step1"

    @staticmethod
    def tool_provider():
        return "Dawson Labs"

    @staticmethod
    def version():
        return "0.1"

    def bind_metadata(self):
        self.metadata.version = "0.1"
        self.metadata.dateCreated = date(2019, 10, 11)
        self.metadata.dateUpdated = date(2019, 10, 11)

        self.metadata.contributors = ["Sebastian Hollizeck"]
        self.metadata.keywords = [
            "variants",
            "strelka2",
            "variant caller",
            "multi sample",
        ]
        self.metadata.documentation = """
        This is the first step for joint somatic variant calling
        based on a 2pass analysis common in RNASeq.

        It runs manta and strelka on the bams as is best practice
        for somatic variant calling with strelka2

        It also normalises and indexes the output vcfs
                """.strip()

    def constructor(self):

        self.input("normalBam", CramCrai)
        self.input("tumorBam", CramCrai)

        self.input("reference", FastaWithDict)
        self.input("callRegions", BedTabix(optional=True))
        self.input("exome", Boolean(optional=True), default=False)

        self.step(
            "manta",
            Manta(
                bam=self.normalBam,
                tumorBam=self.tumorBam,
                reference=self.reference,
                callRegions=self.callRegions,
                exome=self.exome,
            ),
        )
        self.step(
            "strelka",
            Strelka(
                indelCandidates=self.manta.candidateSmallIndels,
                normalBam=self.normalBam,
                tumorBam=self.tumorBam,
                reference=self.reference,
                callRegions=self.callRegions,
                exome=self.exome,
            ),
        )
        self.step(
            "normaliseSNVs",
            BcfToolsNorm(vcf=self.strelka.snvs, reference=self.reference),
        )
        self.step("indexSNVs", BcfToolsIndex(vcf=self.normaliseSNVs.out))

        self.step(
            "normaliseINDELs",
            BcfToolsNorm(vcf=self.strelka.indels, reference=self.reference),
        )
        self.step("indexINDELs", BcfToolsIndex(vcf=self.normaliseINDELs.out))

        self.output("diploid", source=self.manta.diploidSV)
        self.output("candIndels", source=self.manta.candidateSmallIndels)
        self.output("indels", source=self.indexINDELs.out)
        self.output("snvs", source=self.indexSNVs.out)
        self.output("somaticSVs", source=self.manta.somaticSVs)


if __name__ == "__main__":

    wf = Strelka2PassWorkflowStep1()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
