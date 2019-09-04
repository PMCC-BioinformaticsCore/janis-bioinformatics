from janis_core import File, String, Float, Int, Boolean
from janis_bioinformatics.tools.pmac import TrimIUPAC_0_0_4

from janis_bioinformatics.data_types import FastaWithDict, BamBai, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.vardict import VarDictGermline_1_5_8
from janis_bioinformatics.tools.bcftools import BcfToolsAnnotate_1_5
from janis_bioinformatics.tools.common import SplitMultiAllele


class VardictGermlineVariantCaller(BioinformaticsWorkflow):
    @staticmethod
    def tool_provider():
        return "Variant Callers"

    @staticmethod
    def version():
        return "v0.1.0"

    def __init__(self):
        super().__init__(
            "vardictGermlineVariantCaller", name="Vardict Germline Variant Caller"
        )

        self.input("bam", BamBai)
        self.input("intervals", Bed)

        self.input("sampleName", String)
        self.input("allelFreqThreshold", Float, default=0.5)
        self.input("headerLines", File)

        self.input("reference", FastaWithDict)

        self.step(
            "vardict",
            VarDictGermline_1_5_8,
            intervals=self.intervals,
            bam=self.bam,
            reference=self.reference,
            sampleName=self.sampleName,
            var2vcfSampleName=self.sampleName,
            alleleFreqThreshold=self.allelFreqThreshold,
            var2vcfAlleleFreqThreshold=self.allelFreqThreshold,
            chromNamesAreNumbers=True,
            vcfFormat=True,
            chromColumn=1,
            regStartCol=2,
            geneEndCol=3,
        )
        self.step(
            "annotate",
            BcfToolsAnnotate_1_5,
            file=self.vardict.out,
            headerLines=self.headerLines,
        )
        self.step(
            "split", SplitMultiAllele, vcf=self.annotate.out, reference=self.reference
        )
        self.step("trim", TrimIUPAC_0_0_4, vcf=self.split.out)

        self.output("vardictVariants", source=self.vardict.out)
        self.output("out", source=self.trim.out)


if __name__ == "__main__":
    v = VardictGermlineVariantCaller()
    v.translate("wdl", with_resource_overrides=False)
    # print(v.generate_resources_file("wdl", { "CaptureType": "targeted" }))
