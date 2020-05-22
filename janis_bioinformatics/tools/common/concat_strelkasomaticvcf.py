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


class ConcatStrelkaSomaticVcf(BioinformaticsTool):
    def tool(self) -> str:
        return "ConcatStrelkaSomaticVcf"

    def tool_provider(self):
        return "common"

    def version(self):
        return "0.1.16"

    def container(self):
        return "biocontainers/vcftools:v0.1.16-1-deb_cv1"

    def base_command(self):
        return None

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput("headerVcfs", Array(VcfTabix), position=1),
            ToolInput("contentVcfs", Array(VcfTabix), position=4),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [ToolOutput("out", Stdout(Vcf),)]

    def arguments(self):
        return [
            ToolArgument("vcf-concat", position=0, shell_quote=False),
            ToolArgument("| grep '^##' > header.vcf;", position=2, shell_quote=False),
            ToolArgument("vcf-merge", position=3, shell_quote=False),
            ToolArgument(
                "| grep -v '^##' > content.vcf; cat header.vcf content.vcf",
                position=5,
                shell_quote=False,
            ),
        ]

    def doc(self):
        return """Uncompress and concat the SNV and INDEL vcfs from strelka somatic variant calling.
        Command:
        vcf-concat $vcf1.gz $vcf2.gz > header.vcf;
        vcf-merge $vcf1.gz $vcf2.gz > content.vcf;
        cat header.vcf content.vcf - """
