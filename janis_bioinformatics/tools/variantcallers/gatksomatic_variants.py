from datetime import date
from janis_core import Step, Input, Output, String

from janis_bioinformatics.tools import gatk4
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common import SplitMultiAllele


class GatkSomaticVariantCaller(BioinformaticsWorkflow):
    @staticmethod
    def tool_provider():
        return "Variant Callers"

    def __init__(self):
        super(GatkSomaticVariantCaller, self).__init__(
            "GATK4_SomaticVariantCaller",
            "GATK4 Somatic Variant Caller",
            doc="GATK4 based variant caller: (BaseRecal + Mutect 2)",
        )

        self._metadata.version = "4.0.12.0"
        self._metadata.dateCreated = date(2019, 2, 1)
        self._metadata.maintainer = "Michael Franklin"
        self._metadata.maintainerEmail = "michael.franklin@petermac.org"
        self._metadata.keywords = [
            "variants",
            "gatk",
            "gatk4",
            "variant caller",
            "somatic",
        ]
        self._metadata.documentation = """
This is a VariantCaller based on the GATK Best Practice pipelines. It uses the GATK4 toolkit, specifically 4.0.12.0.

It has the following steps:

1. Base Recalibrator x 2
3. Mutect2
4. SplitMultiAllele
        """.strip()

        normal = Input("normalBam", BamBai())
        tumor = Input("tumorBam", BamBai())

        normalname = Input("normalName", String())
        tumorname = Input("tumorName", String())

        intervals = Input(
            "intervals",
            Bed(optional=True),
            doc="This optional intervals file supports processing by regions. If this file resolves "
            "to null, then GATK will process the whole genome per each tool's spec",
        )
        reference = Input("reference", FastaWithDict())

        snps_dbsnp = Input("snps_dbsnp", VcfTabix())
        snps_1000gp = Input("snps_1000gp", VcfTabix())
        known_indels = Input("knownIndels", VcfTabix())
        mills_indels = Input("millsIndels", VcfTabix())

        s1_recal_normal = Step(
            "baseRecalibrator_normal", gatk4.Gatk4BaseRecalibrator_4_0()
        )
        s1_recal_tumor = Step(
            "baseRecalibrator_tumor", gatk4.Gatk4BaseRecalibrator_4_0()
        )

        s2_applybqsr_normal = Step("applyBQSR_normal", gatk4.Gatk4ApplyBqsr_4_0())
        s2_applybqsr_tumor = Step("applyBQSR_tumor", gatk4.Gatk4ApplyBqsr_4_0())

        s3_mutect2 = Step("mutect2", gatk4.GatkMutect2_4_0())
        s4_split = Step("splitMultiAllele", SplitMultiAllele())

        # S1: BaseRecalibrator(s)

        for inp, baseRecal, applyBQSR in [
            (normal, s1_recal_normal, s2_applybqsr_normal),
            (tumor, s1_recal_tumor, s2_applybqsr_tumor),
        ]:
            self.add_edges(
                [
                    (inp, baseRecal.bam),
                    (intervals, baseRecal.intervals),
                    (reference, baseRecal.reference),
                    (snps_dbsnp, baseRecal.knownSites),
                    (snps_1000gp, baseRecal.knownSites),
                    (known_indels, baseRecal.knownSites),
                    (mills_indels, baseRecal.knownSites),
                ]
            )

            self.add_edges(
                [
                    (inp, applyBQSR.bam),
                    (intervals, applyBQSR.intervals),
                    (baseRecal.out, applyBQSR.recalFile),
                    (reference, applyBQSR.reference),
                ]
            )

        # S2: Mutect2
        self.add_edges(
            [
                (s2_applybqsr_normal.out, s3_mutect2.normal),
                (s2_applybqsr_tumor.out, s3_mutect2.tumor),
                (normalname, s3_mutect2.normalName),
                (tumorname, s3_mutect2.tumorName),
                (intervals, s3_mutect2.intervals),
                (reference, s3_mutect2.reference),
            ]
        )

        # S3: SplitMultiAllele
        self.add_edges(
            [(reference, s4_split.reference), (s3_mutect2.out, s4_split.vcf)]
        )

        self.add_edge(s4_split.out, Output("out"))


if __name__ == "__main__":
    vc = GatkSomaticVariantCaller().translate("wdl", to_console=True)
    # print(vc.translate("cwl"))
