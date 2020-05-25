from typing import List, Optional, Union
from janis_core import (
    ToolInput,
    ToolArgument,
    ToolOutput,
    Filename,
    InputSelector,
    WildcardSelector,
)

from janis_bioinformatics.data_types import Fastq, FastqGz, FastqPair, FastqGzPair
from .base import TrimmomaticBase


class TrimmomaticPairedEndBase(TrimmomaticBase):
    def tool(self) -> str:
        return "trimmomaticPairedEnd"

    def arguments(self) -> Optional[List[ToolArgument]]:
        return [ToolArgument("PE", position=0)]

    def inputs(self) -> List[ToolInput]:
        return [
            *super().inputs(),
            ToolInput("inp", FastqPair, position=5, separator=" "),
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
        return [
            ToolOutput("pairedOut", FastqGzPair, glob=WildcardSelector("*P.fastq.gz")),
            ToolOutput(
                "unpairedOut", FastqGzPair, glob=WildcardSelector("*U.fastq.gz")
            ),
        ]
