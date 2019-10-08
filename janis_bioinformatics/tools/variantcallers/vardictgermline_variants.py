from janis_core import File, String, Float

from janis_bioinformatics.data_types import FastaWithDict, BamBai, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bcftools import BcfToolsAnnotate_1_5
from janis_bioinformatics.tools.common import SplitMultiAllele
from janis_bioinformatics.tools.pmac import TrimIUPAC_0_0_4
from janis_bioinformatics.tools.vardict import VarDictGermline_1_6_0


class VardictGermlineVariantCaller(BioinformaticsWorkflow):
    def id(self):
        return "vardictGermlineVariantCaller"

    def friendly_name(self):
        return "Vardict Germline Variant Caller"

    @staticmethod
    def tool_provider():
        return "Variant Callers"

    @staticmethod
    def version():
        return "v0.1.0"

    def constructor(self):

        self.input("bam", BamBai)
        self.input("intervals", Bed)

        self.input("sampleName", String)
        self.input("alleleFreqThreshold", Float, default=0.5)
        self.input("headerLines", File)

        self.input("reference", FastaWithDict)

        self.step(
            "vardict",
            VarDictGermline_1_6_0(
                intervals=self.intervals,
                bam=self.bam,
                reference=self.reference,
                sampleName=self.sampleName,
                var2vcfSampleName=self.sampleName,
                alleleFreqThreshold=self.alleleFreqThreshold,
                var2vcfAlleleFreqThreshold=self.alleleFreqThreshold,
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
            "split", SplitMultiAllele(vcf=self.annotate.out, reference=self.reference)
        )
        self.step("trim", TrimIUPAC_0_0_4(vcf=self.split.out))

        self.output("vardictVariants", source=self.vardict.out)
        self.output("out", source=self.trim.out)


if __name__ == "__main__":
    v = VardictGermlineVariantCaller()
    v.translate("wdl", with_resource_overrides=False)
    # print(v.generate_resources_file("wdl", { "CaptureType": "targeted" }))
