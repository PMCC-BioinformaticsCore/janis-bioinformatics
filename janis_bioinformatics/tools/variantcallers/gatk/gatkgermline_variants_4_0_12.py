from datetime import date

from janis_core import String
from janis_bioinformatics.tools import gatk4
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common import SplitMultiAllele


class GatkGermlineVariantCaller_4_0_12(BioinformaticsWorkflow):
    def id(self):
        return "GATK4_GermlineVariantCaller"

    def friendly_name(self):
        return "GATK4 Germline Variant Caller"

    @staticmethod
    def tool_provider():
        return "Variant Callers"

    def bind_metadata(self):
        self.metadata.version = "4.0.12.0"
        self.metadata.dateCreated = date(2019, 2, 1)
        self.metadata.contributors = ["Michael Franklin"]
        self.metadata.keywords = ["variants", "gatk", "gatk4", "variant caller"]
        self.metadata.documentation = """
        This is a VariantCaller based on the GATK Best Practice pipelines. It uses the GATK4 toolkit, specifically 4.0.12.0.

        It has the following steps:

        1. BaseRecalibrator
        2. ApplyBQSR
        3. HaplotypeCaller
        4. SplitMultiAllele
                """.strip()

    def constructor(self):

        self.input("bam", BamBai)
        self.input(
            "intervals",
            Bed(optional=True),
            doc="This optional interval supports processing by regions. If this input resolves "
            "to null, then GATK will process the whole genome per each tool's spec",
        )

        self.input("reference", FastaWithDict)

        self.input("snps_dbsnp", VcfTabix)
        self.input("snps_1000gp", VcfTabix)
        self.input("knownIndels", VcfTabix)
        self.input("millsIndels", VcfTabix)

        self.step(
            "baseRecalibrator",
            gatk4.Gatk4BaseRecalibrator_4_0(
                bam=self.bam,
                intervals=self.intervals,
                reference=self.reference,
                knownSites=[
                    self.snps_dbsnp,
                    self.snps_1000gp,
                    self.knownIndels,
                    self.millsIndels,
                ],
            ),
        )
        self.step(
            "applyBQSR",
            gatk4.Gatk4ApplyBqsr_4_0(
                bam=self.bam,
                intervals=self.intervals,
                recalFile=self.baseRecalibrator.out,
                reference=self.reference,
            ),
        )
        self.step(
            "haplotypeCaller",
            gatk4.Gatk4HaplotypeCaller_4_0(
                inputRead=self.applyBQSR,
                intervals=self.intervals,
                reference=self.reference,
                dbsnp=self.snps_dbsnp,
            ),
        )
        self.step(
            "splitMultiAllele",
            SplitMultiAllele(reference=self.reference, vcf=self.haplotypeCaller),
        )

        self.output("out", source=self.splitMultiAllele)


if __name__ == "__main__":
    vc = GatkGermlineVariantCaller_4_0_12().translate("wdl", to_console=True)
    # print(vc.translate("cwl"))
