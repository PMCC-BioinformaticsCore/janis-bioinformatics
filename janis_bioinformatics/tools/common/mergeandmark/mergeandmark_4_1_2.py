from datetime import datetime
from janis_core import Array, Boolean, Int, String, ToolMetadata

from janis_bioinformatics.data_types import BamBai
from janis_bioinformatics.tools.gatk4 import (
    Gatk4MarkDuplicates_4_1_2,
    Gatk4MergeSamFiles_4_1_2,
)
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsWorkflow


class MergeAndMarkBams_4_1_2(BioinformaticsWorkflow):
    def id(self):
        return "mergeAndMarkBams"

    def friendly_name(self):
        return "Merge and Mark Duplicates"

    def version(self):
        return "4.1.2"

    def tool_provider(self):
        return "common"

    def constructor(self):

        self.input("bams", Array(BamBai()))
        self.input("createIndex", Boolean, default=True)
        self.input("maxRecordsInRam", Int, default=5000000)
        self.input("sampleName", String(optional=True))

        self.step(
            "mergeSamFiles",
            Gatk4MergeSamFiles_4_1_2(
                bams=self.bams,
                useThreading=True,
                createIndex=self.createIndex,
                maxRecordsInRam=self.maxRecordsInRam,
                validationStringency="SILENT",
                sampleName=self.sampleName,
            ),
        )

        self.step(
            "markDuplicates",
            Gatk4MarkDuplicates_4_1_2(
                bam=self.mergeSamFiles.out,
                createIndex=self.createIndex,
                maxRecordsInRam=self.maxRecordsInRam,
                outputPrefix=self.sampleName,
            ),
        )
        self.output("out", source=self.markDuplicates.out)

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2020, 6, 26),
            dateUpdated=datetime(2020, 11, 6),
            documentation="",
        )


if __name__ == "__main__":
    MergeAndMarkBams_4_1_2().translate("wdl")
