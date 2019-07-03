from janis import Step, Input, Output, Array, String

from janis_bioinformatics.tools.pappenfuss import Gridss_2_2_3
from janis_bioinformatics.tools.samtools import SamToolsView_1_7

from janis_bioinformatics.data_types import FastaWithDict, BamBai, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import BcfToolsView_1_5
from janis_bioinformatics.tools.common import SplitMultiAllele
from janis_bioinformatics.tools.illumina import StrelkaGermline_2_9_10, Manta_1_5_0


class GridssGermlineVariantCaller(BioinformaticsWorkflow):

    @staticmethod
    def tool_provider():
        return "Variant Callers"

    def __init__(self):
        super(GridssGermlineVariantCaller, self).__init__("gridssGermlineVariantCaller",
                                                           "Gridss Germline Variant Caller", doc=None)
        bam = Input("bam", BamBai())
        reference = Input("reference", FastaWithDict())
        blacklist = Input("blacklist", Bed())

        doNotOutputAlignmentsWithBitsSet = Input("doNotOutputAlignmentsWithBitsSet", String(), default="0x100",
                                                 include_in_inputs_file_if_none=False)

        samtools = Step("samtools", SamToolsView_1_7())
        gridss = Step("gridss", Gridss_2_2_3())

        self.add_edges([
            (bam, samtools.sam), # ignore warning until union types are a thing
            (doNotOutputAlignmentsWithBitsSet, samtools.doNotOutputAlignmentsWithBitsSet)
        ])

        self.add_edges([
            (bam, gridss.bams),
            (reference, gridss.reference),
            (blacklist, gridss.blacklist)
        ])

        self.add_edges([
            (Output("vcf"), gridss.vcf),
            (Output("assembly"), gridss.assembly)
        ])


if __name__ == "__main__":
    w = GridssGermlineVariantCaller()

    w.translate("wdl", to_disk=True, should_validate=True)
