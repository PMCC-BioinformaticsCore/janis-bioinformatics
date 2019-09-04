from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsWorkflow
from janis_core import Workflow, Array, String, Boolean, Int

from janis_bioinformatics.tools.gatk4 import (
    Gatk4MergeSamFiles_4_0,
    Gatk4MarkDuplicates_4_0,
)
from janis_bioinformatics.data_types import BamBai


class MergeAndMarkBams_4_0(BioinformaticsWorkflow):
    @staticmethod
    def version():
        return "4.0.12"

    @staticmethod
    def tool_provider():
        return "common"

    def __init__(self):
        super().__init__("mergeAndMarkBams", name="Merge and Mark Duplicates")

        self.input("bams", Array(BamBai()))
        self.input("createIndex", Boolean, default=True)
        self.input("maxRecordsInRam", Int, default=5000000)

        self.step(
            "mergeSamFiles",
            Gatk4MergeSamFiles_4_0,
            bams=self.bams,
            useThreading=True,
            createIndex=self.createIndex,
            maxRecordsInRam=self.maxRecordsInRam,
            validationStringency="SILENT",
        )

        self.step(
            "markDuplicates",
            Gatk4MarkDuplicates_4_0,
            bam=self.mergeSamFiles.out,
            createIndex=self.createIndex,
            maxRecordsInRam=self.maxRecordsInRam,
        )
        self.output("out", source=self.markDuplicates.out)


if __name__ == "__main__":
    MergeAndMarkBams_4_0().translate("wdl")
