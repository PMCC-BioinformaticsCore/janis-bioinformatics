from typing import List

from janis_core import (
    CommandTool,
    ToolInput,
    ToolArgument,
    ToolOutput,
    WildcardSelector,
    ToolMetadata,
    File,
    String,
)
from janis_bioinformatics.data_types import CompressedVcf


class CircosPlot(CommandTool):
    """
    Command: Rscript /config/binaries/pmc-scripts/dev/$circos_plot $tumor_name $normal_name $facets_file $sv_file
    Output: PDF file: ${tumor_name}--${normal_name}.pdf
    """

    def tool(self):
        return "PMacCircosPlot"

    def base_command(self):
        return []

    def inputs(self):
        return [
            ToolInput("script", File, position=2),
            ToolInput("tumor_name", String, position=3),
            ToolInput("normal_name", String, position=4),
            ToolInput("facets_file", File, position=5),
            ToolInput("sv_file", CompressedVcf, position=6),
        ]

    def arguments(self):
        return [
            ToolArgument(
                ". /etc/profile.d/modules.sh; module load R/4.0.2;",
                position=0,
                shell_quote=False,
            ),
            ToolArgument(
                "Rscript",
                position=1,
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [ToolOutput("out", File, glob=WildcardSelector("*.pdf"))]

    def container(self) -> str:
        # this means you'll need to run with --allow-empty-container
        return None

    def version(self) -> str:
        return "v0.1.0"

    def tool_provider(self):
        return "Peter Mac"

    def friendly_name(self) -> str:
        return "Peter Mac: Circos plot"

    def bind_metadata(self) -> ToolMetadata:
        from datetime import datetime

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2021, 7, 9),
            dateUpdated=datetime(2021, 7, 9),
            citation=None,
            doi=None,
            documentation="""
Rscript /config/binaries/pmc-scripts/dev/$circos_plot $tumor_name $normal_name $facets_file $sv_file
""",
        )


if __name__ == "__main__":
    CircosPlot().translate("wdl", allow_empty_container=True)
