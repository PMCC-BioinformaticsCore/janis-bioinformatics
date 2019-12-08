from datetime import date

from janis_core import String
from janis_bioinformatics.tools import gatk4
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common import SplitMultiAllele


class GatkSomaticVariantCaller_4_0_12(BioinformaticsWorkflow):
    def id(self):
        return "GATK4_SomaticVariantCaller"

    def friendly_name(self):
        return "GATK4 Somatic Variant Caller"

    def tool_provider(self):
        return "Variant Callers"

    def constructor(self):

        self.input("normalBam", BamBai)
        self.input("tumorBam", BamBai)

        self.input("normalName", str)
        self.input("tumorName", str)

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
            "baseRecalibrator_normal",
            gatk4.Gatk4BaseRecalibrator_4_0(),
            ignore_missing=True,
        )
        self.step(
            "baseRecalibrator_tumor",
            gatk4.Gatk4BaseRecalibrator_4_0(),
            ignore_missing=True,
        )

        self.step("applyBQSR_normal", gatk4.Gatk4ApplyBqsr_4_0(), ignore_missing=True)
        self.step("applyBQSR_tumor", gatk4.Gatk4ApplyBqsr_4_0(), ignore_missing=True)

        # S1: BaseRecalibrator(s)

        for inp, baseRecal, applyBQSR in [
            (self.normalBam, self.baseRecalibrator_normal, self.applyBQSR_normal),
            (self.tumorBam, self.baseRecalibrator_tumor, self.applyBQSR_tumor),
        ]:
            baseRecal["bam"] = inp
            baseRecal["intervals"] = self.intervals
            baseRecal["reference"] = self.reference
            baseRecal["knownSites"] = [
                self.snps_dbsnp,
                self.snps_1000gp,
                self.knownIndels,
                self.millsIndels,
            ]

            applyBQSR["recalFile"] = baseRecal.out
            applyBQSR["bam"] = inp
            applyBQSR["intervals"] = self.intervals
            applyBQSR["reference"] = self.reference

        self.step(
            "mutect2",
            gatk4.GatkMutect2_4_0(
                normal=self.applyBQSR_normal.out,
                tumor=self.applyBQSR_tumor.out,
                normalName=self.normalName,
                tumorName=self.tumorName,
                intervals=self.intervals,
                reference=self.reference,
            ),
        )
        self.step(
            "splitMultiAllele",
            SplitMultiAllele(reference=self.reference, vcf=self.mutect2.out),
        )

        self.output("out", source=self.splitMultiAllele.out)

    def bind_metadata(self):
        self.metadata.version = "4.0.12.0"
        self.metadata.dateCreated = date(2019, 2, 1)
        self.metadata.dateUpdated = date(2019, 9, 13)

        self.metadata.contributors = ["Michael Franklin"]
        self.metadata.keywords = [
            "variants",
            "gatk",
            "gatk4",
            "variant caller",
            "somatic",
        ]
        self.metadata.documentation = """
        This is a VariantCaller based on the GATK Best Practice pipelines. It uses the GATK4 toolkit, specifically 4.0.12.0.

        It has the following steps:

        1. Base Recalibrator x 2
        3. Mutect2
        4. SplitMultiAllele
                """.strip()


if __name__ == "__main__":
    vc = GatkSomaticVariantCaller_4_0_12().translate("wdl", to_console=True)
    # print(vc.translate("cwl"))
