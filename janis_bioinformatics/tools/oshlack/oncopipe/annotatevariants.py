from janis_core import StringFormatter

from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.ensembl import VepCacheLatest, FilterVep_98_3


class OncopipeAnnotateVariants(BioinformaticsWorkflow):
    def id(self) -> str:
        return "oncopipe_AnnotateVariants"

    def friendly_name(self):
        return "Oncopipe: OncopipeAnnotateVariants"

    def constructor(self):

        # TODO: work out 'target_gene_file'

        # [
        #   vep
        #   + vepfilter
        #   + report_vep_cleanup
        #   + report_vep_text,
        #   + vepvcf +
        #   vepfiltervcf
        #   , [
        #       chr_rename + liftover + oncotator_format,
        #       report_vep_vcf_cleanup + report_vep
        #   ]
        # ]
        self.input("variants", Vcf())

        self.step(
            "vep",
            VepCacheLatest(
                inputFile=self.variants,
                symbol=True,
                filterCommon=True,
                sift="b",
                polyphen="b",
                outputFilename="generated.txt",
                vcf=False,
            ),
        )

        self.step(
            "vepfilter",
            FilterVep_98_3(
                input_file=self.vep.out,
                format="tab",
                filter=StringFormatter(
                    "SYMBOL in {target_gene_file}", target_gene_file="FILE"
                ),
            ),
        )

        self.step(
            "vepvcf",
            VepCacheLatest(
                inputFile=self.vepfilter,
                symbol=True,
                filterCommon=True,
                alleleNumber=True,
                sift="b",
                polyphen="b",
            ),
        )


OncopipeAnnotateVariants().translate("wdl")
