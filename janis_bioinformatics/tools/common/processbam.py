from janis_core import Workflow, Step, Input, Output, Array, String, Boolean, Int

import janis_bioinformatics.tools.gatk4 as GATK4
from janis_bioinformatics.data_types import BamBai


class MergeAndMarkBams_4_0(Workflow):
    @staticmethod
    def version():
        return "4.0.12"

    def __init__(self):
        Workflow.__init__(self, "processbamfiles", friendly_name="Process BAM Files")

        inp = Input("bams", Array(BamBai()))

        s1_merge = Step("mergeSamFiles", GATK4.Gatk4MergeSamFiles_4_0())
        s2_mark = Step("markDuplicates", GATK4.Gatk4MarkDuplicates_4_0())

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


if __name__ == "__main__":
    MergeAndMarkBams_4_0().translate("wdl")
