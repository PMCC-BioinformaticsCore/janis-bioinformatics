from abc import ABC

from janis_core import ToolInput, ToolOutput, Stdout, ToolMetadata

from janis_bioinformatics.data_types import CompressedVcf
from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools.vcflib.vcflibtoolbase import VcfToolsToolBase


class VcfCombineBase(VcfToolsToolBase, ABC):
    @staticmethod
    def tool():
        return "vcfcombine"

    def friendly_name(self):
        return "VcfLib: VcfCombine"

    @staticmethod
    def base_command():
        return "vcfcombine"

    def inputs(self):
        return [
            ToolInput("vcf", CompressedVcf, position=3),
            ToolInput(
                "region",
                String(optional=True),
                prefix="-r",
                doc="A region specifier of the form chrN:x-y to bound the merge",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", Stdout(), doc="VCF output")]

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Sebastian Hollizeck"],
            dateCreated=date(2019, 10, 18),
            dateUpdated=date(2019, 10, 18),
            institution=None,
            doi=None,
            citation=None,
            keywords=["freebayes", "bayesian", "variant calling"],
            documentationUrl="https://github.com/vcflib/vcflib",
            documentation="usage: vcfcombine [vcf file] [vcf file] ...\n\n options:\n-h --help\tThis text.\n-r --region REGION\tA region specifier of the form chrN:x-y to bound the merge\n\nCombines VCF files positionally, combining samples when sites and alleles are identical. Any number of VCF files may be combined. The INFO field and other columns are taken from one of the files which are combined when records in multiple files match. Alleles must have identical ordering to be combined into one record. If they do not, multiple records will be emitted",
        )
