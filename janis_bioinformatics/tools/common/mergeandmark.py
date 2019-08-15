from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsWorkflow
from janis_core import Workflow, Step, Input, Output, Array, String, Boolean, Int

from janis_bioinformatics.tools.gatk4 import Gatk4MergeSamFiles_4_0, Gatk4MarkDuplicates_4_0
from janis_bioinformatics.data_types import BamBai


class MergeAndMarkBams_4_0(BioinformaticsWorkflow):
    @staticmethod
    def version():
        return "4.0.12"

    @staticmethod
    def tool_provider():
        return "common"

    def __init__(self):
        super().__init__("mergeAndMarkBams", friendly_name="Merge and Mark Duplicates")

        inp = Input("bams", Array(BamBai()))

        s1_merge = Step("mergeSamFiles", Gatk4MergeSamFiles_4_0())
        s2_mark = Step("markDuplicates", Gatk4MarkDuplicates_4_0())

        gatk_create_index = Input("createIndex", Boolean(), default=True)
        max_recs_in_ram = Input("maxRecordsInRam", Int(), default=5000000)

        # S1: MergeSamFiles
        self.add_edge(inp, s1_merge.bams)
        self.add_edges(
            [
                (Input("useThreading", Boolean(), default=True), s1_merge.useThreading),
                (gatk_create_index, s1_merge.createIndex),
                (max_recs_in_ram, s1_merge.maxRecordsInRam),
                (
                    Input("validationStringency", String(), default="SILENT"),
                    s1_merge.validationStringency,
                ),
            ]
        )

        # S2: MarkDuplicates
        self.add_edge(s1_merge.out, s2_mark.bam)
        self.add_edges(
            [
                (gatk_create_index, s2_mark.createIndex),
                (max_recs_in_ram, s2_mark.maxRecordsInRam),
            ]
        )

        # Outputs
        self.add_edges([(s2_mark.out, Output("out"))])
