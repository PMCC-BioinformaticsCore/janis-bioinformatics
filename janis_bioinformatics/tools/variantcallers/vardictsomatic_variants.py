from janis_core import File, String, Float, Int, Boolean
from janis_bioinformatics.tools.pmac import TrimIUPAC_0_0_4

from janis_bioinformatics.data_types import FastaWithDict, BamBai, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import BcfToolsAnnotate_1_5
from janis_bioinformatics.tools.common import SplitMultiAllele
from janis_bioinformatics.tools.vardict import VarDictSomatic_1_6_0


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

        self.input("normalBam", BamBai)
        self.input("tumorBam", BamBai)

        self.input("normalName", String)
        self.input("tumorName", String)

        self.input("intervals", Bed)

        self.input("alleleFreqThreshold", Float(), 0.05)
        self.input("headerLines", File)

        self.input("reference", FastaWithDict)

        self.step(
            "vardict",
            VarDictSomatic_1_6_0(
                normalBam=self.normalBam,
                tumorBam=self.tumorBam,
                intervals=self.intervals,
                reference=self.reference,
                normalName=self.normalName,
                tumorName=self.tumorName,
                alleleFreqThreshold=self.alleleFreqThreshold,
                chromNamesAreNumbers=True,
                vcfFormat=True,
                chromColumn=1,
                regStartCol=2,
                geneEndCol=3,
            ),
        )
        self.step(
            "annotate",
            BcfToolsAnnotate_1_5(file=self.vardict.out, headerLines=self.headerLines),
        )
        self.step(
            "split", SplitMultiAllele(reference=self.reference, vcf=self.annotate.out)
        )
        self.step("trim", TrimIUPAC_0_0_4(vcf=self.split.out))

        self.output("vardictVariants", source=self.vardict.out)
        self.output("out", source=self.trim.out)


if __name__ == "__main__":
    v = VardictSomaticVariantCaller()
    v.translate("wdl", with_resource_overrides=False)
    # print(v.generate_resources_file("wdl", { "CaptureType": "targeted" }))
