from abc import ABC

from janis_core import ToolInput, String, Int, ToolOutput, Float, Stdout, ToolMetadata

from janis_bioinformatics.data_types import CompressedVcf
from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools.vcflib.vcflibtoolbase import VcfLibToolBase


class VcfRandomSampleBase(VcfLibToolBase, ABC):
    def tool(self):
        return "vcfrandomsample"

    def friendly_name(self):
        return "VcfLib: Vcf Random Sampling"

    def base_command(self):
        return "vcfrandomsample"

    def inputs(self):
        return [
            ToolInput("vcf", CompressedVcf, position=3),
            ToolInput(
                "rate", Float, prefix="-t", doc="base sampling probability per locus"
            ),
            ToolInput(
                "scaleBy",
                String(optional=True),
                prefix="-s",
                doc="scale sampling likelihood by this Float info field",
            ),
            ToolInput("seed", Int(), prefix="-p", doc="use this random seed"),
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
            documentation="usage: vcfrandomsample [options] [<vcf file>]\n\noptions:\n\t-r, --rate RATE \tbase sampling probability per locus\n\t-s, --scale-by KEY\scale sampling likelihood by this Float info field\n\t-p, --random-seed N\tuse this random seed",
        )
