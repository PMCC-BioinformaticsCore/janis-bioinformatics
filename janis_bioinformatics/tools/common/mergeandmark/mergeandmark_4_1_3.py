from janis_core import Array, Boolean, Int

from janis_bioinformatics.data_types import BamBai
from janis_bioinformatics.tools.gatk4 import (
    Gatk4MarkDuplicates_4_1_3,
    Gatk4MergeSamFiles_4_1_3,
)
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsWorkflow


class MergeAndMarkBams_4_1_3(BioinformaticsWorkflow):
    def id(self):
        return "mergeAndMarkBams"

    def friendly_name(self):
        return "Merge and Mark Duplicates"

    @staticmethod
    def version():
        return "4.1.3"

    @staticmethod
    def tool_provider():
        return "common"

    def constructor(self):

        self.input("bams", Array(BamBai()))
        self.input("createIndex", Boolean, default=True)
        self.input("maxRecordsInRam", Int, default=5000000)

        self.step(
            "mergeSamFiles",
            Gatk4MergeSamFiles_4_1_3(
                bams=self.bams,
                useThreading=True,
                createIndex=self.createIndex,
                maxRecordsInRam=self.maxRecordsInRam,
                validationStringency="SILENT",
            ),
        )

        self.step(
            "markDuplicates",
            Gatk4MarkDuplicates_4_1_3(
                bam=self.mergeSamFiles.out,
                createIndex=self.createIndex,
                maxRecordsInRam=self.maxRecordsInRam,
            ),
        )
        self.output("out", source=self.markDuplicates.out)


if __name__ == "__main__":
    MergeAndMarkBams_4_1_3().translate("wdl")
