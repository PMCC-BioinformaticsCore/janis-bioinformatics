from datetime import date
from janis_core import Step, Input, Output

from janis_bioinformatics.tools import gatk4
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common import SplitMultiAllele


class GatkGermlineVariantCaller(BioinformaticsWorkflow):
    @staticmethod
    def tool_provider():
        return "Variant Callers"

    def __init__(self):
        super(GatkGermlineVariantCaller, self).__init__(
            "GATK4_GermlineVariantCaller",
            "GATK4 Germline Variant Caller",
            doc="GATK4 based variant caller: (BaseRecal + ApplyBQSR + Haplotype)",
        )

        self._metadata.version = "4.0.12.0"
        self._metadata.dateCreated = date(2019, 2, 1)
        self._metadata.maintainer = "Michael Franklin"
        self._metadata.maintainerEmail = "michael.franklin@petermac.org"
        self._metadata.keywords = ["variants", "gatk", "gatk4", "variant caller"]
        self._metadata.documentation = """
This is a VariantCaller based on the GATK Best Practice pipelines. It uses the GATK4 toolkit, specifically 4.0.12.0.

It has the following steps:

1. BaseRecalibrator
2. ApplyBQSR
3. HaplotypeCaller
4. SplitMultiAllele
        """.strip()

        bam = Input("bam", BamBai())
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

        s1_recal = Step("baseRecalibrator", gatk4.Gatk4BaseRecalibrator_4_0())
        s2_bqsr = Step("applyBQSR", gatk4.Gatk4ApplyBqsr_4_0())
        s3_haplo = Step("haplotypeCaller", gatk4.Gatk4HaplotypeCaller_4_0())
        s4_split = Step("splitMultiAllele", SplitMultiAllele())

        # S1: BaseRecalibrator
        self.add_edge(bam, s1_recal.bam)
        self.add_edge(intervals, s1_recal.intervals)
        self.add_edge(reference, s1_recal.reference)
        self.add_edges(
            [
                (snps_dbsnp, s1_recal.knownSites),
                (snps_1000gp, s1_recal.knownSites),
                (known_indels, s1_recal.knownSites),
                (mills_indels, s1_recal.knownSites),
            ]
        )

        # S2: ApplyBQSR
        self.add_edges(
            [
                (bam, s2_bqsr.bam),
                (intervals, s2_bqsr.intervals),
                (s1_recal.out, s2_bqsr.recalFile),
                (reference, s2_bqsr.reference),
            ]
        )

        # S3: HaplotypeCaller
        self.add_edges(
            [
                (s2_bqsr.out, s3_haplo.inputRead),
                (intervals, s3_haplo.intervals),
                (reference, s3_haplo.reference),
                (snps_dbsnp, s3_haplo.dbsnp),
            ]
        )

        # S4: SplitMultiAllele
        self.add_edges([(reference, s4_split.reference), (s3_haplo.out, s4_split.vcf)])

        self.add_edge(s4_split.out, Output("out"))


if __name__ == "__main__":
    vc = GatkGermlineVariantCaller().translate("wdl", to_console=True)
    # print(vc.translate("cwl"))
