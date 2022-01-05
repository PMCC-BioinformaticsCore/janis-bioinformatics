from abc import ABC
from typing import Dict, Any, List

from janis_core import (
    CommandTool,
    ToolInput,
    ToolArgument,
    ToolOutput,
    InputSelector,
    StringFormatter,
    Filename,
    ToolMetadata,
    File,
    String,
)
from janis_bioinformatics.tools import BioinformaticsTool
from janis_bioinformatics.data_types import Vcf


class ReplaceNFusionVcfBase(BioinformaticsTool, ABC):
    """
    replace_N_fusion_vcf.py --input $input_vcf > $output_vcf
    """

    def tool(self):
        return "PMacReplaceNFusionVcf"

    def base_command(self):
        return ["replace_N_fusion_vcf.py"]

    def inputs(self):
        return [
            ToolInput("vcf", Vcf, prefix="--input", position=2),
            ToolInput(
                "outputFilename",
                Filename(
                    InputSelector("vcf", remove_file_extension=True),
                    extension=".vcf",
                ),
                position=5,
            ),
        ]

    def arguments(self):
        return [
            ToolArgument(
                ">",
                position=4,
                shell_quote=False,
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [ToolOutput("out", Vcf, glob=InputSelector("outputFilename"))]

    def friendly_name(self) -> str:
        return "Peter Mac: replace_N_fusion_vcf.py"

    def bind_metadata(self) -> ToolMetadata:
        from datetime import datetime

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2021, 1, 5),
            dateUpdated=datetime(2021, 1, 5),
            citation=None,
            doi=None,
            documentation="""
Copy the REF base over to ALT colum for breakends sv
Usage: replace_N_fusion_vcf.py --input $input_vcf > $output_vcf
""",
        )
