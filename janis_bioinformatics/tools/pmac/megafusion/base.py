from abc import ABC
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
from janis_unix import Tsv

from janis_bioinformatics.tools import BioinformaticsTool
from janis_bioinformatics.data_types import Vcf


class MegaFusionBase(BioinformaticsTool, ABC):
    """""
    MegaFusion.py --sample $sample --json $json \
        --fusion $fusion --contig $contig > $output_vcf
    """ ""

    def tool(self):
        return "PMacMegaFusion"

    def base_command(self):
        return ["MegaFusion.py"]

    def inputs(self):
        return [
            ToolInput("sample", String(optional=True), prefix="--sample", position=2),
            ToolInput("json", File, prefix="--json", position=2),
            ToolInput(
                "fusion",
                Tsv,
                prefix="--fusion",
                position=2,
            ),
            ToolInput("toolVersion", String, prefix="--tool_version", position=2),
            ToolInput("contig", File(optional=True), prefix="--contig", position=2),
            ToolInput(
                "outputFilename",
                Filename(
                    InputSelector("fusion", remove_file_extension=True),
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

    def outputs(self):
        return [ToolOutput("out", Vcf, glob=InputSelector("outputFilename"))]

    def friendly_name(self) -> str:
        return "Peter Mac: MegaFusion.py"

    def bind_metadata(self) -> ToolMetadata:
        from datetime import datetime

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2021, 1, 5),
            dateUpdated=datetime(2021, 1, 5),
            citation=None,
            doi=None,
            documentation="""
Convert RNA fusion files to SV VCF. MegaFusion accepts a fusion transcript 
file produced from any tool (such as Arriba), as well as a JSON file, 
specifying which columns to put in the output vcf file.
Usage: MegaFusion.py --sample $sample --json $json \
        --fusion $fusion --contig $contig > $output_vcf
""",
        )
