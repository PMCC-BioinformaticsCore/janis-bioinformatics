from datetime import date

from janis_unix.tools import UncompressArchive
from janis_bioinformatics.tools import gatk4
from janis_bioinformatics.data_types import FastaWithDict, BamBai, VcfTabix, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.common import SplitMultiAllele


class GatkGermlineVariantCaller_4_1_3(BioinformaticsWorkflow):
    def id(self):
        return "GATK4_GermlineVariantCaller"

    def friendly_name(self):
        return "GATK4 Germline Variant Caller"

    def tool_provider(self):
        return "Variant Callers"

    def bind_metadata(self):
        self.metadata.version = "4.1.3.0"
        self.metadata.dateCreated = date(2019, 9, 1)
        self.metadata.dateUpdated = date(2019, 9, 13)

        self.metadata.contributors = ["Michael Franklin", "Jiaan"]
        self.metadata.keywords = ["variants", "gatk", "gatk4", "variant caller"]
        self.metadata.documentation = """
        This is a VariantCaller based on the GATK Best Practice pipelines. It uses the GATK4 toolkit, specifically 4.1.3.

        It has the following steps:

        1. Split Bam based on intervals (bed)
        2. HaplotypeCaller
        3. SplitMultiAllele
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

        self.step(
            "split_bam",
            gatk4.Gatk4SplitReads_4_1_3(bam=self.bam, intervals=self.intervals),
        )

        self.step(
            "haplotype_caller",
            gatk4.Gatk4HaplotypeCaller_4_1_3(
                inputRead=self.split_bam.out,
                intervals=self.intervals,
                reference=self.reference,
                dbsnp=self.snps_dbsnp,
                pairHmmImplementation="LOGLESS_CACHING",
            ),
        )
        self.step("uncompressvcf", UncompressArchive(file=self.haplotype_caller.out))
        self.step(
            "splitnormalisevcf",
            SplitMultiAllele(vcf=self.uncompressvcf.out, reference=self.reference),
        )

        self.output("variants", source=self.haplotype_caller.out)
        self.output("out_bam", source=self.haplotype_caller.bam)
        self.output("out", source=self.splitnormalisevcf.out)


if __name__ == "__main__":
    vc = GatkGermlineVariantCaller_4_1_3().translate("wdl", to_console=True)
    # print(vc.translate("cwl"))
