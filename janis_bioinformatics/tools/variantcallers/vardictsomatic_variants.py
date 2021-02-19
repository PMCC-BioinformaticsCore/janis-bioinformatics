from datetime import datetime
from janis_core import File, String, Float, WorkflowMetadata
from janis_unix.tools import UncompressArchive

from janis_bioinformatics.data_types import FastaWithDict, BamBai, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import BcfToolsAnnotate_1_5
from janis_bioinformatics.tools.common import SplitMultiAllele, FilterVardictSomaticVcf
from janis_bioinformatics.tools.htslib import BGZipLatest, TabixLatest
from janis_bioinformatics.tools.vardict import VarDictSomatic_1_6_0
from janis_bioinformatics.tools.pmac.trimiupac.versions import TrimIUPAC_0_0_5


class VardictSomaticVariantCaller(BioinformaticsWorkflow):
    def id(self):
        return "vardictSomaticVariantCaller"

    def friendly_name(self):
        return "Vardict Somatic Variant Caller"

    def tool_provider(self):
        return "Variant Callers"

    def version(self):
        return "v0.1.0"

    def constructor(self):

        self.input("normal_bam", BamBai)
        self.input("tumor_bam", BamBai)

        self.input("normal_name", String)
        self.input("tumor_name", String)

        self.input("intervals", Bed)

        self.input("allele_freq_threshold", Float(), 0.05)
        self.input("header_lines", File)

        self.input("reference", FastaWithDict)

        self.step(
            "vardict",
            VarDictSomatic_1_6_0(
                normalBam=self.normal_bam,
                tumorBam=self.tumor_bam,
                intervals=self.intervals,
                reference=self.reference,
                normalName=self.normal_name,
                tumorName=self.tumor_name,
                alleleFreqThreshold=self.allele_freq_threshold,
                vcfFormat=True,
                chromColumn=1,
                regStartCol=2,
                geneEndCol=3,
                threads=4,
            ),
        )
        self.step(
            "annotate",
            BcfToolsAnnotate_1_5(vcf=self.vardict.out, headerLines=self.header_lines),
        )
        self.step("compressvcf", BGZipLatest(file=self.annotate.out, stdout=True))
        self.step("tabixvcf", TabixLatest(inp=self.compressvcf.out))

        self.step(
            "splitnormalisevcf",
            SplitMultiAllele(vcf=self.annotate.out, reference=self.reference),
        )
        self.step("trim", TrimIUPAC_0_0_5(vcf=self.splitnormalisevcf.out))
        self.step("filterpass", FilterVardictSomaticVcf(vcf=self.trim.out))

        self.output("variants", source=self.tabixvcf.out)
        self.output("out", source=self.filterpass.out)

    def bind_metadata(self):
        return WorkflowMetadata(
            contributors=["Michael Franklin", "Jiaan Yu"],
            dateCreated=datetime(2019, 6, 12),
            dateUpdated=datetime(2020, 7, 14),
            documentation="",
        )


if __name__ == "__main__":
    v = VardictSomaticVariantCaller()
    v.translate("wdl", with_resource_overrides=False)
    # print(v.generate_resources_file("wdl", { "CaptureType": "targeted" }))
