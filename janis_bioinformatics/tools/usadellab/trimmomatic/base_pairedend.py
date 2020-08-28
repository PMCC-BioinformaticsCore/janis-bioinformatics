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
                "outputFilename_R1",
                Filename(
                    prefix=InputSelector("sampleName"),
                    suffix="_R1.trimmed",
                    extension=".fastq.gz",
                ),
                position=6,
            ),
            ToolInput(
                "outputFilenameUnpaired_R1",
                Filename(
                    prefix=InputSelector("sampleName"),
                    suffix="_R1.unpaired",
                    extension=".fastq.gz",
                ),
                position=7,
            ),
            ToolInput(
                "outputFilename_R2",
                Filename(
                    prefix=InputSelector("sampleName"),
                    suffix="_R2.trimmed",
                    extension=".fastq.gz",
                ),
                position=8,
            ),
            ToolInput(
                "outputFilenameUnpaired_R2",
                Filename(
                    prefix=InputSelector("sampleName"),
                    suffix="_R2.unpaired",
                    extension=".fastq.gz",
                ),
                position=9,
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput(
                "pairedOut", FastqGzPair, glob=WildcardSelector("*trimmed.fastq.gz")
            ),
            ToolOutput(
                "unpairedOut", FastqGzPair, glob=WildcardSelector("*unpaired.fastq.gz")
            ),
        ]
