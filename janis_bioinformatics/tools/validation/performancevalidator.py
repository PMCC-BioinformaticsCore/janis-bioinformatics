from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_core import Array, Boolean
from janis_bioinformatics.data_types import Vcf, VcfIdx
from janis_bioinformatics.tools.gatk4 import Gatk4GenotypeConcordanceLatest
from janis_bioinformatics.tools.htslib import BGZip_1_2_1, Tabix_1_2_1


class PerformanceValidator_1_2_1(BioinformaticsWorkflow):
    def constructor(self):

        self.input("vcf", Vcf)
        self.input("truth", VcfIdx)
        self.input("intervals", Array(Vcf()))

        self.step("bgzip", BGZip_1_2_1(file=self.vcf))
        self.step("tabix", Tabix_1_2_1(file=self.bgzip))
        self.step(
            "genotypeConcord",
            Gatk4GenotypeConcordanceLatest(
                callVCF=self.tabix,
                truthVCF=self.truth,
                intervals=self.intervals,
                treatMissingSitesAsHomeRef=True,
            ),
        )

        self.output("summaryMetrics", source=self.genotypeConcord.summaryMetrics)
        self.output("detailMetrics", source=self.genotypeConcord.detailMetrics)
        self.output(
            "contingencyMetrics", source=self.genotypeConcord.contingencyMetrics
        )

    def id(self):
        return "performanceValidator"

    def friendly_name(self):
        return "Performance Validator"

    @staticmethod
    def version():
        return "1.2.1"

    @staticmethod
    def tool_provider():
        return "Peter MacCallum Cancer Centre"


if __name__ == "__main__":
    print(PerformanceValidator_1_2_1().help())
