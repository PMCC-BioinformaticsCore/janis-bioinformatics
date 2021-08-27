from typing import List

from janis_core import (
    CommandTool,
    ToolInput,
    ToolOutput,
    ToolMetadata,
    File,
    String,
    StringFormatter,
    Int,
    InputSelector,
)
from janis_bioinformatics.data_types import CompressedVcf


class CircosPlotBase(CommandTool):
    """
    Command: Rscript /app/circos_plot/circos_plot_facets_manta.R $tumor_name \
$normal_name $facets_file $sv_file $out_dir $manta_filter[optional]
    Output: PDF file: ${tumor_name}--${normal_name}.pdf
    """

    def tool(self):
        return "CircosPlot"

    def friendly_name(self) -> str:
        return "Circos Plot"

    def base_command(self):
        return "Rscript /app/circos_plot/circos_plot_facets_manta.R"

    def inputs(self):
        return [
            ToolInput("tumor_name", String, position=1),
            ToolInput("normal_name", String, position=2),
            ToolInput("facets_file", File, position=3),
            ToolInput("sv_file", CompressedVcf, position=4),
            ToolInput("output_dir", String(optional=True), default=".", position=5),
            ToolInput("manta_filter", Int(optional=True), position=6),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput(
                "out",
                File,
                glob=StringFormatter(
                    "{tumor_name}--{normal_name}.pdf",
                    tumor_name=InputSelector("tumor_name"),
                    normal_name=InputSelector("normal_name"),
                ),
            )
        ]

    def bind_metadata(self) -> ToolMetadata:
        from datetime import datetime

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2021, 7, 9),
            dateUpdated=datetime(2021, 8, 27),
            citation=None,
            doi=None,
            documentation="""Command: Rscript /app/circos_plot/circos_plot_facets_manta.R \
$tumor_name $normal_name $facets_file $sv_file $out_dir $manta_filter[optional]
    Output: PDF file: ${tumor_name}--${normal_name}.pdf
""",
        )
