from datetime import date

from janis_bioinformatics.data_types import BedTabix, BamBai, FastaFai, VcfTabix
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import (
    BcfToolsIndex_1_9 as BcfToolsIndex,
    BcfToolsNorm_1_9 as BcfToolsNorm,
)
from janis_bioinformatics.tools.illumina.strelkasomatic.strelkasomatic import (
    StrelkaSomatic_2_9_10 as Strelka,
)
from janis_core import Array, Boolean, File


class Strelka2PassWorkflowStep2(BioinformaticsWorkflow):
    def id(self):
        return "Strelka2PassWorkflowStep2"

    def friendly_name(self):
        return "Strelka 2Pass analysis step 2"

    def tool_provider(self):
        return "Dawson Labs"

    def version(self):
        return "0.1"

    def bind_metadata(self):
        self.metadata.version = "0.1"
        self.metadata.dateCreated = date(2019, 10, 11)
        self.metadata.dateUpdated = date(2020, 8, 4)

        self.metadata.contributors = ["Sebastian Hollizeck"]
        self.metadata.keywords = [
            "variants",
            "strelka2",
            "variant caller",
            "multi sample",
        ]
        self.metadata.documentation = """
        This is the second step for joint somatic variant calling
        based on a 2pass analysis common in RNASeq.

        It runs strelka2 again with the variants found in all of the other samples as input to be forced to genotype these.

        It also normalises and indexes the output vcfs
                """.strip()

    def constructor(self):

        self.input("normalBam", BamBai)
        self.input("tumorBam", BamBai)

        self.input("reference", FastaFai)
        self.input("callRegions", BedTabix(optional=True))
        self.input("exome", Boolean(optional=True), default=False)
        self.input("configStrelka", File(optional=True))

        self.input("indelCandidates", Array(VcfTabix))
        self.input("strelkaSNVs", Array(VcfTabix))
        # self.input("strelkaIndels", Array(VcfTabix))

        self.step(
            "strelka2pass",
            Strelka(
                indelCandidates=self.indelCandidates,
                # indelCandidates=self.strelkaIndels,
                forcedgt=self.strelkaSNVs,
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
            BcfToolsNorm(vcf=self.strelka2pass.snvs, reference=self.reference),
        )
        self.step("indexSNVs", BcfToolsIndex(vcf=self.normaliseSNVs.out))

        self.step(
            "normaliseINDELs",
            BcfToolsNorm(vcf=self.strelka2pass.indels, reference=self.reference),
        )
        self.step("indexINDELs", BcfToolsIndex(vcf=self.normaliseINDELs.out))

        self.output("indels", source=self.indexINDELs.out)
        self.output("snvs", source=self.indexSNVs.out)


if __name__ == "__main__":

    wf = Strelka2PassWorkflowStep2()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
