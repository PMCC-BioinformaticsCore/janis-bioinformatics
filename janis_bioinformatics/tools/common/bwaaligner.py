from janis_bioinformatics.data_types import FastqGzPair, FastaWithDict
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common.bwamem_samtoolsview import BwaMem_SamToolsView
from janis_bioinformatics.tools.cutadapt import CutAdapt_1_18
from janis_bioinformatics.tools.gatk4 import Gatk4SortSam_4_1_3


class BwaAligner(BioinformaticsWorkflow):
    def id(self):
        return "BwaAligner"

    def friendly_name(self):
        return "Align and sort reads"

    @staticmethod
    def tool_provider():
        return "common"

    @staticmethod
    def version():
        return "1.0.0"

    def constructor(self):

        # Inputs
        self.input("name", str)
        self.input("reference", FastaWithDict)
        self.input("fastq", FastqGzPair)

        # Steps
        self.step(
            "cutadapt",
            CutAdapt_1_18(
                fastq=self.fastq,
                adapter=None,
                adapter_g=None,
                removeMiddle5Adapter=None,
                removeMiddle3Adapter=None,
                qualityCutoff=15,
                minReadLength=50,
            ),
        )

        self.step(
            "bwamem",
            BwaMem_SamToolsView(
                reads=self.cutadapt.out,
                sampleName=self.name,
                reference=self.reference,
                markShorterSplits=True,
            ),
        )

        self.step(
            "sortsam",
            Gatk4SortSam_4_1_3(
                bam=self.bwamem.out,
                sortOrder="coordinate",
                createIndex=True,
                validationStringency="SILENT",
                maxRecordsInRam=5000000,
                tmpDir=".",
            ),
        )

        # outputs
        self.output("out", source=self.sortsam)

    def bind_metadata(self):
        self.metadata.documentation = "Align sorted bam with this subworkflow consisting of BWA Mem + SamTools + Gatk4SortSam"
        self.metadata.creator = "Michael Franklin"
        self.metadata.dateCreated = "2018-12-24"
        self.metadata.version = "1.1"


if __name__ == "__main__":
    w = BwaAligner()

    w.translate("wdl", with_resource_overrides=True)

    # print(build_resources_input(w, "wdl", {CaptureType.KEY: CaptureType.CHROMOSOME}))

    # print(AlignSortedBam().help())

    # import shepherd
    #
    # task = shepherd.from_workflow(w, engine=shepherd.Cromwell(), env="pmac")
    # print(task.outputs)
