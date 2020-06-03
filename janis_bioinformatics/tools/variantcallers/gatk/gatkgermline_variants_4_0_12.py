from datetime import date

from janis_bioinformatics.tools import gatk4
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common import SplitMultiAlleleNormaliseVcf
from janis_bioinformatics.tools.pmac import AddBamStatsGermline_0_1_0


class GatkGermlineVariantCaller_4_0_12(BioinformaticsWorkflow):
    def id(self):
        return "GATK4_GermlineVariantCaller"

    def friendly_name(self):
        return "GATK4 Germline Variant Caller"

    def tool_provider(self):
        return "Variant Callers"

    def bind_metadata(self):
        self.metadata.version = "4.0.12.0"
        self.metadata.dateCreated = date(2019, 2, 1)
        self.metadata.contributors = ["Michael Franklin", "Jiaan Yu"]
        self.metadata.keywords = ["variants", "gatk", "gatk4", "variant caller"]
        self.metadata.documentation = """
        This is a VariantCaller based on the GATK Best Practice pipelines. It uses the GATK4 toolkit, specifically 4.0.12.0.

        It has the following steps:

        1. BaseRecalibrator
        2. ApplyBQSR
        3. HaplotypeCaller
        4. SplitMultiAlleleNormaliseVcf
        5. AddBamStatsGermline
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
        self.input("known_indels", VcfTabix)
        self.input("mills_indels", VcfTabix)

        # self.step(
        #     "split_bam",
        #     gatk4.Gatk4SplitReads_4_1_3(bam=self.bam, intervals=self.intervals),
        # )

        self.step(
            "base_recalibrator",
            gatk4.Gatk4BaseRecalibrator_4_1_3(
                bam=self.bam,
                intervals=self.intervals,
                reference=self.reference,
                knownSites=[
                    self.snps_dbsnp,
                    self.snps_1000gp,
                    self.known_indels,
                    self.mills_indels,
                ],
            ),
        )
        self.step(
            "apply_bqsr",
            gatk4.Gatk4ApplyBqsr_4_1_3(
                bam=self.bam,
                intervals=self.intervals,
                recalFile=self.base_recalibrator.out,
                reference=self.reference,
            ),
        )
        self.step(
            "haplotype_caller",
            gatk4.Gatk4HaplotypeCaller_4_1_3(
                inputRead=self.apply_bqsr,
                intervals=self.intervals,
                reference=self.reference,
                dbsnp=self.snps_dbsnp,
                pairHmmImplementation="LOGLESS_CACHING",
            ),
        )
        self.step(
            "splitnormalisevcf",
            SplitMultiAlleleNormaliseVcf(
                compressedTabixVcf=self.haplotype_caller.out, reference=self.reference
            ),
        )
        self.step(
            "addbamstats",
            AddBamStatsGermline_0_1_0(bam=self.bam, vcf=self.splitnormalisevcf.out),
        )

        self.output("variants", source=self.haplotype_caller.out)
        self.output("out_bam", source=self.haplotype_caller.bam)
        self.output("out", source=self.addbamstats.out)


if __name__ == "__main__":
    vc = GatkGermlineVariantCaller_4_0_12().translate("wdl", to_console=True)
    # print(vc.translate("cwl"))
