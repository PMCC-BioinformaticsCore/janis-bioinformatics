from typing import List, Dict, Any

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
    CaptureType,
    get_value_for_hints_and_ordered_resource_tuple,
)
from janis_bioinformatics.data_types import CompressedVcf

BWA_MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 8,
            CaptureType.EXOME: 12,
            CaptureType.CHROMOSOME: 12,
            CaptureType.THIRTYX: 16,
            CaptureType.NINETYX: 20,
            CaptureType.THREEHUNDREDX: 24,
        },
    )
]

BWA_CORES_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 1,
            CaptureType.EXOME: 1,
            CaptureType.CHROMOSOME: 1,
            CaptureType.THIRTYX: 1,
            CaptureType.NINETYX: 1,
            CaptureType.THREEHUNDREDX: 1,
        },
    )
]


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
            ToolInput("genome", String, position=6),
            ToolInput("manta_filter", Int(optional=True), position=7),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput(
                "out",
                File,
                glob=StringFormatter(
                    "{output_dir}/{tumor_name}--{normal_name}.pdf",
                    output_dir=InputSelector("output_dir"),
                    tumor_name=InputSelector("tumor_name"),
                    normal_name=InputSelector("normal_name"),
                ),
            )
        ]

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, BWA_MEM_TUPLE)
        if val:
            return val
        return 16

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, BWA_CORES_TUPLE)
        if val:
            return val
        return 1

    def skip_test(cls) -> bool:
        return True

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
