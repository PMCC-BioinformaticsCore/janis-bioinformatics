from abc import ABC

from janis_core import (
    ToolInput,
    String,
    Boolean,
    File,
    Filename,
    Array,
    Int,
    ToolOutput,
    InputSelector,
)
from janis_bioinformatics.data_types import FastaWithDict, CompressedVcf
from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools.vcflib.vcflibtoolbase import VcfToolsToolBase
from janis_core import ToolMetadata


class VcfAllelicPrimitivesBase(VcfToolsToolBase, ABC):
    @staticmethod
    def tool():
        return "vcfallelicprimitives"

    def friendly_name(self):
        return "VcfLib: VcfAllelicPrimitives"

    @staticmethod
    def base_command():
        return "vcfallelicprimitives"

    def inputs(self):
        return [
            ToolInput("vcf", CompressedVcf, position=3),
            ToolInput(
                "useMnpsFlag",
                Boolean(optional=True),
                prefix="-m",
                default=False,
                doc="Retain MNPs as separate events (default: false)",
            ),
            ToolInput(
                "tagParsed",
                String(optional=True),
                prefix="-t",
                doc="Tag records which are split apart of a complex allele with this flag",
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
