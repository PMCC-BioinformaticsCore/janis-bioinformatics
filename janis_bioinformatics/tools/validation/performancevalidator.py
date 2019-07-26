from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_core import Step, Input, Output, Array, Boolean
from janis_bioinformatics.data_types import Vcf, VcfIdx
from janis_bioinformatics.tools.gatk4 import Gatk4GenotypeConcordanceLatest
from janis_bioinformatics.tools.htslib import BGZip_1_2_1, Tabix_1_2_1


class PerformanceValidator_1_2_1(BioinformaticsWorkflow):
    def __init__(self):
        super(PerformanceValidator_1_2_1, self).__init__(
            "performanceValidator", friendly_name="Performance Validator"
        )

        inp = Input("vcf", Vcf())
        inp_truth = Input("truth", VcfIdx())
        inp_intervals = Input("intervals", Array(Vcf()))

        bgzip = Step("bgzip", BGZip_1_2_1())
        tabix = Step("tabix", Tabix_1_2_1())
        genotypeconcord = Step("genotypeconcord", Gatk4GenotypeConcordanceLatest())

        self.add_edges(
            [
                (inp, bgzip.file),
                (bgzip.out, tabix.file),
                (tabix.out, genotypeconcord.callVCF),
                (inp_truth, genotypeconcord.truthVCF),
                (inp_intervals, genotypeconcord.intervals),
            ]
        )

        self.add_edge(Input("treatMissingSitesAsHomeRef", Boolean(), default=True),
                      genotypeconcord.treatMissingSitesAsHomeRef)

        self.add_edges(
            [
                (genotypeconcord.summaryMetrics, Output("summaryMetrics")),
                (genotypeconcord.detailMetrics, Output("detailMetrics")),
                (genotypeconcord.contingencyMetrics, Output("contingencyMetrics")),
            ]
        )

    @staticmethod
    def version():
        return "1.2.1"

    @staticmethod
    def tool_provider():
        return "Peter MacCallum Cancer Centre"


if __name__ == "__main__":
    print(PerformanceValidator_1_2_1().help())
