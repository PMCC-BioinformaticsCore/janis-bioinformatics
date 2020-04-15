from janis_core import String, Logger, Array

from janis_bioinformatics.data_types import FastaWithDict, BamBai, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.papenfuss import Gridss_2_5_1, Gridss_2_6_3
from janis_bioinformatics.tools.samtools import SamToolsView_1_7


class GridssGermlineVariantCaller(BioinformaticsWorkflow):
    def id(self):
        return "gridssGermlineVariantCaller"

    def friendly_name(self):
        return "Gridss Germline Variant Caller"

    def tool_provider(self):
        return "Variant Callers"

    def constructor(self):

        self.input("bam", BamBai)
        self.input("reference", FastaWithDict)
        self.input("blacklist", Bed)

        # Steps

        self.step(
            "samtools",
            SamToolsView_1_7(sam=self.bam, doNotOutputAlignmentsWithBitsSet="0x100"),
        )
        self.step(
            "gridss",
            Gridss_2_6_3(
                bams=[self.samtools.out],
                reference=self.reference,
                blacklist=self.blacklist,
            ),
        )

        self.output("out", source=self.gridss.out)
        self.output("assembly", source=self.gridss.assembly)


if __name__ == "__main__":
    w = GridssGermlineVariantCaller()

    w.translate("wdl")
