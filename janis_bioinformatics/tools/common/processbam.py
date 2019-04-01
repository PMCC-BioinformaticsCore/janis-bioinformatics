from janis import Workflow, Step, Input, Output, Array, Directory
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, VcfIdx, Bed

import janis_bioinformatics.tools.gatk4 as GATK4


class MergeAndMarkBams_4_0(Workflow):

    @staticmethod
    def version():
        return "4.0.12"

    def __init__(self):
        Workflow.__init__(self, "processbamfiles", friendly_name="Process BAM Files")

        inp = Input("bams", Array(BamBai()))

        s1_merge = Step("mergeSamFiles", GATK4.Gatk4MergeSamFiles_4_0())
        s2_mark = Step("markDuplicates", GATK4.Gatk4MarkDuplicates_4_0())

        # S1: MergeSamFiles
        self.add_edge(inp, s1_merge.bams)
        self.add_default_value(s1_merge.useThreading, True)
        self.add_default_value(s1_merge.createIndex, True)
        self.add_default_value(s1_merge.maxRecordsInRam, 5000000)
        self.add_default_value(s1_merge.validationStringency, "SILENT")

        # S2: MarkDuplicates
        self.add_edge(s1_merge.out, s2_mark.bam)
        self.add_default_value(s2_mark.createIndex, True)
        self.add_default_value(s2_mark.maxRecordsInRam, 5000000)

        # Outputs
        self.add_edges([
            (s2_mark.out, Output("out"))
        ])


if __name__ == "__main__":
    MergeAndMarkBams_4_0().dump_translation("wdl")
