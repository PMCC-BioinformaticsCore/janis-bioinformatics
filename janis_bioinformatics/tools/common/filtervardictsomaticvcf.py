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
)
from janis_bioinformatics.data_types import Vcf, CompressedVcf, VcfTabix
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class FileVardictSomaticVcf(BioinformaticsTool):
    def tool(self) -> str:
        return "FileVardictSomaticVcf"

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
            ToolInput("vcf", Vcf(optional=True), position=1),
            ToolInput("compressedVcf", CompressedVcf(optional=True), position=1),
            ToolInput("compressedIndexVcf", VcfTabix(optional=True), position=1),
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf.gz", suffix=".filter"),
                prefix="-o",
                position=3,
                shell_quote=False,
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput("out", CompressedVcf(), glob=InputSelector("outputFilename"),)
        ]

    def arguments(self):
        return [
            ToolArgument(
                "bcftools filter -e STATUS=GERMLINE -O z -o - ",
                position=0,
                shell_quote=False,
            ),
            ToolArgument(
                "| bcftools filter -i FILTER==PASS -O z", position=2, shell_quote=False
            ),
        ]

    def doc(self):
        return """Filter somatic vardict vcf by removing the variants marks with "Germline", and variants without a "PASS" quality.
        Bash command:
        bcftools filter -e STATUS=GERMLINE -O z -o - $vcf | bcftools filter -i FILTER==PASS -O z -o $out_vcf"""
