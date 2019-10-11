from janis_bioinformatics.data_types import FastaWithDict, BamBai, BedTabix
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.illumina import Manta_1_5_0, StrelkaSomatic_2_9_10
from janis_bioinformatics.tools.bcftools import BcfToolsNorm_1_9, BcfToolsIndex_1_9


class Strelka2PassWorkflowStep2(BioinformaticsWorkflow):
    def id(self):
        return "Strelka2PassWorkflowStep2"

    def friendly_name(self):
        return "Strelka 2Pass analysis step 2"

    @staticmethod
    def tool_provider():
        return "Dawons Labs"

    @staticmethod
    def version():
        return "0.1"

    def constructor(self):

        self.input("normalBam", BamBai)
        self.input("tumorBam", BamBai)

        self.input("reference", FastaWithDict)
        self.input("intervals", BedTabix(optional=True))

        self.input("indelCandidates", Array(VcfTabix))
        self.input("strelkaSNVs", Array(VcfTabix))

        self.step(
            "strelka2pass",
            StrelkaSomatic_2_9_10(
                indelCandidates=self.indelCandidates,
                forcedgt=self.strelkaSNVs,
                normalBam=self.normalBam,
                tumorBam=self.tumorBam,
                reference=self.reference,
                callRegions=self.intervals,
            ),
        )
        self.step("normaliseSNVs", BcfToolsNorm_1_9(vcf=self.strelka2pass.snvs))
        self.step("indexSNVs", BcfToolsIndex_1_9(vcf=self.normaliseSNVs.out))

        self.step("normaliseINDELs", BcfToolsNorm_1_9(vcf=self.strelka2pass.indels))
        self.step("indexINDELs", BcfToolsIndex_1_9(vcf=self.normaliseINDELs.out))

        self.output("indels", source=self.indexINDELs.out)
        self.output("snvs", source=self.indexSNVs.out)
