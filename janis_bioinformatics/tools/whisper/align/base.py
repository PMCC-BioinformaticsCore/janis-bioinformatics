from abc import ABC
from typing import Any, Dict

from janis_core import (
    ToolInput,
    ToolOutput,
    ToolMetadata,
    Stdout,
)

from janis_bioinformatics.data_types import FastqGzPair, Bam
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool

from ..data_types import WhisperIdx

class WhisperAlignBase(BioinformaticsTool, ABC):
    def tool(self):
        return "whisperAlign"

    def friendly_name(self):
        return "Whisper-Align"

    def tool_provider(self):
        return "Whisper"

    def base_command(self):
        return ["whisper", "-stdout", "-t", "4", "-store-BAM"]

    def inputs(self):
        return [
            ToolInput(
                "index",
                WhisperIdx,
                position=2,
                doc="base name for whisper index",
            ),
            ToolInput(
                "fastq",
                FastqGzPair,
                position=3,
                doc="Paired end fastq reads",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", Stdout(Bam()))]

    def memory(self, hints: Dict[str, Any]):
        return 8

    def cpus(self, hints: Dict[str, Any]):
        return 4

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Thomas Conway"],
            dateCreated=date(2020, 6, 16),
            dateUpdated=date(2020, 6, 16),
            institution="Refresh Bio",
            doi="https://doi.org/10.1101/2019.12.18.881292",
            citation="Deorowicz, S., Gudyś, A. (2019) Whisper 2: indel-sensitive short read mapping, biorXiv",
            keywords=["whisper", "index", "reference"],
            documentationUrl="https://github.com/refresh-bio/Whisper",
            documentation="Builds a whisper index",
        )
