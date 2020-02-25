from janis_core import File, String, Float, Int, Boolean

from janis_bioinformatics.data_types import FastaWithDict, BamBai, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import BcfToolsAnnotate_1_5
from janis_bioinformatics.tools.common import SplitMultiAllele
from janis_bioinformatics.tools.vardict import VarDictSomatic_1_6_0
from janis_bioinformatics.tools.pmac import TrimIUPAC_0_0_5


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
                chromNamesAreNumbers=True,
                vcfFormat=True,
                chromColumn=1,
                regStartCol=2,
                geneEndCol=3,
            ),
        )
        self.step(
            "annotate",
            BcfToolsAnnotate_1_5(file=self.vardict.out, headerLines=self.header_lines),
        )
        self.step(
            "split_multi_allele",
            SplitMultiAllele(reference=self.reference, vcf=self.annotate.out),
        )
        self.step("trim", TrimIUPAC_0_0_5(vcf=self.split_multi_allele.out))

        self.output("vardict_variants", source=self.vardict.out)
        self.output("out", source=self.trim.out)


if __name__ == "__main__":
    v = VardictSomaticVariantCaller()
    v.translate("wdl", with_resource_overrides=False)
    # print(v.generate_resources_file("wdl", { "CaptureType": "targeted" }))
