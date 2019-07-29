from janis_core import Step, Input, File, String, Float, Int, Boolean, Output
from janis_bioinformatics.tools.pmac import TrimIUPAC_0_0_4

from janis_bioinformatics.data_types import FastaWithDict, BamBai, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import BcfToolsAnnotate_1_5
from janis_bioinformatics.tools.common import SplitMultiAllele
from janis_bioinformatics.tools.vardict.vardictsomatic import VarDictSomatic_1_5_8


class VardictSomaticVariantCaller(BioinformaticsWorkflow):
    @staticmethod
    def tool_provider():
        return "Variant Callers"

    @staticmethod
    def version():
        return "v0.1.0"

    def __init__(self):
        super(VardictSomaticVariantCaller, self).__init__(
            "vardictSomaticVariantCaller", "Vardict Somatic Variant Caller", doc=None
        )

        normalBam = Input("normalBam", BamBai())
        tumorBam = Input("tumorBam", BamBai())

        normalname = Input("normalName", String())
        tumorname = Input("tumorName", String())

        intervals = Input("intervals", Bed())

        allele_freq_threshold = Input("alleleFreqThreshold", Float(), 0.05)
        header_lines = Input("headerLines", File())

        reference = Input("reference", FastaWithDict())

        vardict = Step("vardict", VarDictSomatic_1_5_8())
        annotate = Step("annotate", BcfToolsAnnotate_1_5())
        split = Step("split", SplitMultiAllele())
        trim = Step("trim", TrimIUPAC_0_0_4())

        # S1: vardict
        self.add_edges(
            [
                (normalBam, vardict.normalBam),
                (tumorBam, vardict.tumorBam),
                (intervals, vardict.intervals),
                (reference, vardict.reference),
                (normalname, vardict.normalName),
                (tumorname, vardict.tumorName),
                (allele_freq_threshold, vardict.alleleFreqThreshold),
            ]
        )

        self.add_edges(
            [
                (
                    Input("chromNamesAreNumbers", Boolean(), default=True),
                    vardict.chromNamesAreNumbers,
                ),
                (Input("vcfFormat", Boolean(), default=True), vardict.vcfFormat),
                (Input("chromColumn", Int(), default=1), vardict.chromColumn),
                (Input("regStartCol", Int(), default=2), vardict.regStartCol),
                (Input("geneEndCol", Int(), default=3), vardict.geneEndCol),
            ]
        )
        # S2: annotate
        self.add_edges(
            [(vardict.out, annotate.file), (header_lines, annotate.headerLines)]
        )

        # S3: split
        self.add_edges([(reference, split.reference), (annotate.out, split.vcf)])

        # S4: trim
        self.add_edge(split.out, trim.vcf)

        self.add_edges(
            [(vardict.out, Output("vardictVariants")), (trim.out, Output("out"))]
        )


if __name__ == "__main__":
    v = VardictSomaticVariantCaller()
    v.translate("wdl", with_resource_overrides=False)
    # print(v.generate_resources_file("wdl", { "CaptureType": "targeted" }))
