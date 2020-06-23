from abc import ABC

from janis_core import ToolInput, Boolean, ToolOutput, Stdout, Int
from janis_core import ToolMetadata

from janis_bioinformatics.data_types import CompressedVcf
from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools.vcflib.vcflibtoolbase import VcfLibToolBase


class VcfStreamSortBase(VcfLibToolBase, ABC):
    @staticmethod
    def tool():
        return "vcfstreamsort"

    def friendly_name(self):
        return "VcfLib: VcfStreamSort"

    @staticmethod
    def base_command():
        return "vcfstreamsort"

    def inputs(self):
        return [
            ToolInput("vcf", Vcf, position=3),
            ToolInput(
                "inMemoryFlag",
                Boolean(optional=True),
                prefix="-a",
                default=False,
                doc="load all sites and then sort in memory",
            ),
            ToolInput(
                "windowSize",
                Int(optional=True),
                prefix="-w",
                doc="number of sites to sort (default 10000)",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", Stdout(Vcf), doc="VCF output")]

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
            documentation="usage: vcfallelicprimitives [options] [file]\n\noptions:\n\t-m, --use-mnps\tRetain MNPs as separate events (default: false)\n\t-t, --tag-parsed FLAG\tTag records which are split apart of a complex allele with this flag",
        )
