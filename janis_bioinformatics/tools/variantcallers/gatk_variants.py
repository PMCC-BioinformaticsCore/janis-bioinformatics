from janis import Step, Input, Output

import janis_bioinformatics.tools.gatk4 as GATK4
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common import SplitMultiAllele


class GatkVariantCaller(BioinformaticsWorkflow):

    @staticmethod
    def tool_provider():
        return "Broad Institute (GATK)"

    def __init__(self):
        super(GatkVariantCaller, self).__init__("GATK4_VariantCaller", "GATK4 Variant Caller",
                                                 doc="GATK4 based variant caller: (BaseRecal + ApplyBQSR + Haplotype)")

        bam = Input("bam", BamBai())
        intervals = Input("intervals", Bed())
        reference = Input("reference", FastaWithDict())

        snps_dbsnp = Input("snps_dbsnp", VcfTabix())
        snps_1000gp = Input("snps_1000gp", VcfTabix())
        known_indels = Input("knownIndels", VcfTabix())
        mills_indels = Input("millsIndels", VcfTabix())

        s1_recal = Step("baseRecalibrator", GATK4.Gatk4BaseRecalibrator_4_0())
        s2_bqsr = Step("applyBQSR", GATK4.Gatk4ApplyBqsr_4_0())
        s3_haplo = Step("haplotypeCaller", GATK4.Gatk4HaplotypeCaller_4_0())
        s4_split = Step("splitMultiAllele", SplitMultiAllele())

        # S1: BaseRecalibrator
        self.add_edge(bam, s1_recal.bam)
        self.add_edge(intervals, s1_recal.intervals)
        self.add_edge(reference, s1_recal.reference)
        self.add_edges([
            (snps_dbsnp, s1_recal.knownSites),
            (snps_1000gp, s1_recal.knownSites),
            (known_indels, s1_recal.knownSites),
            (mills_indels, s1_recal.knownSites),
        ])

        # S2: ApplyBQSR
        self.add_edges([
            (bam, s2_bqsr.bam),
            (intervals, s2_bqsr.intervals),
            (s1_recal.out, s2_bqsr.recalFile),
            (reference, s2_bqsr.reference)
        ])

        # S3: HaplotypeCaller
        self.add_edges([
            (s2_bqsr.out, s3_haplo.inputRead),
            (intervals, s3_haplo.intervals),
            (reference, s3_haplo.reference),
            (snps_dbsnp, s3_haplo.dbsnp)
        ])

        # S4: SplitMultiAllele
        self.add_edges([
            (reference, s4_split.reference),
            (s3_haplo.out, s4_split.vcf)
        ])

        self.add_edge(s4_split.out, Output("out"))


if __name__ == "__main__":
    vc = GatkVariantCaller()
    # print(vc.dump_translation("cwl"))
