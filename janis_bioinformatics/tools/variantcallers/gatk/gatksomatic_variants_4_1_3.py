from datetime import date

from janis_core import String
from janis_bioinformatics.tools import gatk4
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common import SplitMultiAllele


class GatkSomaticVariantCaller_4_1_3(BioinformaticsWorkflow):
    def id(self):
        return "GATK4_SomaticVariantCaller"

    def friendly_name(self):
        return "GATK4 Somatic Variant Caller"

    def tool_provider(self):
        return "Variant Callers"

    def constructor(self):

        self.input("normal_bam", BamBai)
        self.input("tumor_bam", BamBai)

        self.input("normal_name", str)
        self.input("tumor_name", str)

        self.input(
            "intervals",
            Bed(optional=True),
            doc="This optional intervals file supports processing by regions. If this file resolves "
            "to null, then GATK will process the whole genome per each tool's spec",
        )
        self.input("reference", FastaWithDict)

        self.input("snps_dbsnp", VcfTabix)
        self.input("snps_1000gp", VcfTabix)
        self.input("known_indels", VcfTabix)
        self.input("mills_indels", VcfTabix)

        # we'll create the steps, and then assign their inputs later
        self.step(
            "base_recalibrator_normal",
            gatk4.Gatk4BaseRecalibrator_4_1_3(),
            ignore_missing=True,
        )
        self.step(
            "base_recalibrator_tumor",
            gatk4.Gatk4BaseRecalibrator_4_1_3(),
            ignore_missing=True,
        )

        self.step(
            "apply_bqsr_normal", gatk4.Gatk4ApplyBqsr_4_1_3(), ignore_missing=True
        )
        self.step("apply_bqsr_tumor", gatk4.Gatk4ApplyBqsr_4_1_3(), ignore_missing=True)

        # S1: BaseRecalibrator(s)

        for inp, base_recal, applyBQSR in [
            (self.normal_bam, self.base_recalibrator_normal, self.apply_bqsr_normal),
            (self.tumor_bam, self.base_recalibrator_tumor, self.apply_bqsr_tumor),
        ]:
            base_recal["bam"] = inp
            base_recal["intervals"] = self.intervals
            base_recal["reference"] = self.reference
            base_recal["knownSites"] = [
                self.snps_dbsnp,
                self.snps_1000gp,
                self.known_indels,
                self.mills_indels,
            ]

            applyBQSR["recalFile"] = base_recal.out
            applyBQSR["bam"] = inp
            applyBQSR["intervals"] = self.intervals
            applyBQSR["reference"] = self.reference

        self.step(
            "mutect2",
            gatk4.GatkMutect2_4_1_3(
                normalBams=self.apply_bqsr_normal.out,
                tumorBams=self.apply_bqsr_tumor.out,
                normalSample=self.normal_name,
                # tumorName=self.tumorName,
                intervals=self.intervals,
                reference=self.reference,
            ),
        )
        self.step(
            "split_multi_allele",
            SplitMultiAllele(reference=self.reference, vcf=self.mutect2.out),
        )

        self.output("out", source=self.split_multi_allele.out)

    def bind_metadata(self):
        self.metadata.version = "4.1.3.0"
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
    vc = GatkSomaticVariantCaller_4_1_3().translate("wdl", to_console=True)
    # print(vc.translate("cwl"))
