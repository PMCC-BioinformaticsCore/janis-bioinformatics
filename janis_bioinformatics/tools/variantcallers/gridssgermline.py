from janis_core import Step, Input, Output, String

from janis_bioinformatics.data_types import FastaWithDict, BamBai, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.pappenfuss import Gridss_2_4_0
from janis_bioinformatics.tools.samtools import SamToolsView_1_7


class GridssGermlineVariantCaller(BioinformaticsWorkflow):
    @staticmethod
    def tool_provider():
        return "Variant Callers"

    def __init__(self):
        super(GridssGermlineVariantCaller, self).__init__(
            "gridssGermlineVariantCaller", "Gridss Germline Variant Caller", doc=None
        )
        bam = Input("bam", BamBai())
        reference = Input("reference", FastaWithDict())
        blacklist = Input("blacklist", Bed())

        doNotOutputAlignmentsWithBitsSet = Input(
            "doNotOutputAlignmentsWithBitsSet",
            String(),
            default="0x100",
            include_in_inputs_file_if_none=False,
        )

        samtools = Step("samtools", SamToolsView_1_7())
        gridss = Step("gridss", Gridss_2_4_0())

        self.add_edges(
            [
                (bam, samtools.sam),  # ignore warning until union types are a thing
                (
                    doNotOutputAlignmentsWithBitsSet,
                    samtools.doNotOutputAlignmentsWithBitsSet,
                ),
            ]
        )

        self.add_edges(
            [
                (bam, gridss.bams),
                (reference, gridss.reference),
                (blacklist, gridss.blacklist),
            ]
        )

        self.add_edges(
            [(gridss.out, Output("vcf")), (gridss.assembly, Output("assembly"))]
        )


if __name__ == "__main__":
    w = GridssGermlineVariantCaller()

    w.translate("wdl", to_disk=True, should_validate=True)
