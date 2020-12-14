from datetime import date

from janis_bioinformatics.data_types import BedTabix, FastaFai
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import (
    BcfToolsIndex_1_9 as BcfToolsIndex,
    BcfToolsNorm_1_9 as BcfToolsNorm,
)

from janis_core import Boolean, File


class Strelka2PassWorkflowStep1(BioinformaticsWorkflow):
    def id(self):
        return "Strelka2PassWorkflowStep1"

    def friendly_name(self):
        return "Strelka 2Pass analysis step1"

    def tool_provider(self):
        return "Dawson Labs"

    def version(self):
        return "0.1.1"

    def bind_metadata(self):
        self.metadata.version = "0.1.1"
        self.metadata.dateCreated = date(2019, 10, 11)
        self.metadata.dateUpdated = date(2020, 12, 10)

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

    # this is a way to get the tool without spagetti code in bam and cram format
    def getMantaTool(self):
        from janis_bioinformatics.tools.illumina.manta.manta import Manta_1_5_0 as Manta

        return Manta

    def getStrelka2Tool(self):
        from janis_bioinformatics.tools.illumina.strelkasomatic.strelkasomatic import (
            StrelkaSomatic_2_9_10 as Strelka,
        )

        return Strelka

    def getStrelka2InputType(self):
        from janis_bioinformatics.data_types import BamBai

        return BamBai

    def constructor(self):

        self.input("normalBam", self.getStrelka2InputType())
        self.input("tumorBam", self.getStrelka2InputType())

        self.input("reference", FastaFai)
        self.input("callRegions", BedTabix(optional=True))
        self.input("exome", Boolean(optional=True), default=False)
        self.input("configStrelka", File(optional=True))

        self.step(
            "manta",
            self.getMantaTool()(
                bam=self.normalBam,
                tumorBam=self.tumorBam,
                reference=self.reference,
                callRegions=self.callRegions,
                exome=self.exome,
            ),
        )
        self.step(
            "strelka",
            self.getStrelka2Tool()(
                indelCandidates=self.manta.candidateSmallIndels,
                normalBam=self.normalBam,
                tumorBam=self.tumorBam,
                reference=self.reference,
                callRegions=self.callRegions,
                exome=self.exome,
                config=self.configStrelka,
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
