from typing import List, Optional, Union
from janis_core import ToolInput, ToolArgument, ToolOutput, Filename, InputSelector

from janis_bioinformatics.data_types import Fastq, FastqGz
from .base import TrimmomaticBase


class TrimmomaticSingleEndBase(TrimmomaticBase):
    def tool(self) -> str:
        return "trimmomaticSingleEnd"

    def arguments(self) -> Optional[List[ToolArgument]]:
        return [ToolArgument("SE", position=0)]

    def inputs(self) -> List[ToolInput]:
        return [
            *super().inputs(),
            ToolInput("inp", Fastq, position=5),
            ToolInput(
                "outputFilename",
                Filename(
                    prefix=InputSelector("sampleName"),
                    suffix=".trimmed",
                    extension=".fastq.gz",
                ),
                position=6,
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [ToolOutput("out", FastqGz, glob=InputSelector("outputFilename"))]
