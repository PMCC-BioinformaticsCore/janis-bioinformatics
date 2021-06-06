from datetime import datetime
from typing import List

from janis_core import (
    ToolInput,
    ToolOutput,
    ToolArgument,
    Array,
    Stdout,
    Filename,
    InputSelector,
    String,
    ToolMetadata,
)
from janis_bioinformatics.data_types import Vcf, CompressedVcf, VcfTabix
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class FilterVardictSomaticVcf(BioinformaticsTool):
    def tool(self) -> str:
        return "FilterVardictSomaticVcf"

    def friendly_name(self):
        return "Filter Vardict Somatic Vcf"

    def tool_provider(self):
        return "common"

    def version(self):
        return "v1.9"

    def container(self):
        return "biocontainers/bcftools:v1.9-1-deb_cv1"

    def base_command(self):
        return None

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput("vcf", Vcf(), position=1),
            ToolInput(
                "outputFilename",
                Filename(
                    prefix=InputSelector("vcf", remove_file_extension=True),
                    extension=".vcf",
                    suffix=".filter",
                ),
                prefix="-o",
                position=3,
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput(
                "out",
                Vcf(),
                InputSelector("outputFilename"),
            )
        ]

    def arguments(self):
        return [
            ToolArgument(
                "bcftools filter -e 'STATUS=\"GERMLINE\"' -o - ",
                position=0,
                shell_quote=False,
            ),
            ToolArgument(
                "| bcftools filter -i 'FILTER==\"PASS\"'",
                position=2,
                shell_quote=False,
            ),
        ]

    def doc(self):
        return """Filter somatic vardict vcf by removing the variants marks with "Germline", and variants without a "PASS" quality.
        Bash command:
        bcftools filter -e STATUS=GERMLINE -o - $vcf | bcftools filter -i FILTER==PASS -o $out_vcf"""

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Jiaan Yu", "Michael Franklin"],
            dateCreated=datetime(2020, 6, 4),
            dateUpdated=datetime(2020, 11, 9),
            documentation="",
        )
