from typing import List

from janis_core import (
    ToolInput,
    ToolOutput,
    ToolArgument,
    Array,
    Stdout,
)
from janis_bioinformatics.data_types import Vcf, VcfTabix
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class VcfMergeHeader(BioinformaticsTool):
    def tool(self) -> str:
        return "VcfMergeHeader"

    def tool_provider(self):
        return "common"

    def version(self):
        return "0.1.16"

    def container(self):
        return "biocontainers/vcftools:v0.1.16-1-deb_cv1"

    def base_command(self):
        return None

    def arguments(self):
        return [
            ToolArgument("vcf-merge", position=0, shell_quote=False),
            ToolArgument("| grep '^##' ", position=3, shell_quote=False),
        ]

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput("vcfTabix", Array(VcfTabix), position=1),
        ]

    def outputs(self):
        return [ToolOutput("out", Stdout(Vcf))]
