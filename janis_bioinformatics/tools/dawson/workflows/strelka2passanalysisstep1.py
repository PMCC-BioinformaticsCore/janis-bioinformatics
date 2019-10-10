from janis_bioinformatics.data_types import FastaWithDict, BamBai, BedTabix
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.illumina import Manta_1_5_0, StrelkaSomatic_2_9_10
from janis_bioinformatics.tools.bcftools import BcfToolsNorm_1_9


class Strelka2PassWorkflowStep1(BioinformaticsWorkflow):
    def id(self):
        return "Strelka2PassWorkflowStep1"

    def friendly_name(self):
        return "Strelka 2Pass analysis step 1"

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

        self.step(
            "manta",
            Manta_1_5_0(
                bam=self.normalBam,
                tumorBam=self.tumorBam,
                reference=self.reference,
                callRegions=self.intervals,
            ),
        )
        self.step(
            "strelka",
            StrelkaSomatic_2_9_10(
                indelCandidates=self.manta.candidateSmallIndels,
                normalBam=self.normalBam,
                tumorBam=self.tumorBam,
                reference=self.reference,
                callRegions=self.intervals,
            ),
        )
        self.step(
            "normaliseSNVs",
            BcfToolsNorm_1_9(vcf=self.strelka.snvs),
        )
        w.step("indexSNVS", BcfToolsIndex_1_9(vcf=self.normaliseSNVs.out))

        self.step(
            "normaliseINDELs",
            BcfToolsNorm_1_9(vcf=self.strelka.indels),
        )
        w.step("indexINDELs", BcfToolsIndex_1_9(vcf=self.normaliseINDELs.out))

        self.output("diploid", source=self.manta.diploidSV)
        self.output("candIndels", source=self.manta.candidateSmallIndels)
        self.output("indels", source=self.normaliseINDELs.out)
        self.output("out", source=self.normaliseSNVs.out)


if __name__ == "__main__":

    wf = Strelka2PassWorkflowStep1()
    wdl = wf.translate("wdl", to_console=True, to_disk=False, write_inputs_file=False)
