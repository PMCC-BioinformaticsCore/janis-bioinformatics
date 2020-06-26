from abc import ABC
from typing import Any, Dict

from janis_core import (
    ToolInput,
    ToolOutput,
    ToolMetadata,
    String,
    Int,
    Filename,
    InputSelector,
)

from janis_core import Array, InputSelector
from janis_bioinformatics.data_types import Fasta
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool

from ..data_types import WhisperIdx


class WhisperIndexBase(BioinformaticsTool, ABC):
    def tool(self):
        return "WhisperIndex"

    def friendly_name(self):
        return "Whisper-Index"

    def tool_provider(self):
        return "Whisper"

    def base_command(self):
        return ["whindex", "whisper-index"]

    def inputs(self):
        return [
            ToolInput("index_name", String, position=2, doc="name of the index",),
            ToolInput("fasta", Array(Fasta), position=3, doc="FASTA files to index",),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out", WhisperIdx, glob="whisper-index/" + InputSelector("index_name")
            )
        ]

    def memory(self, hints: Dict[str, Any]):
        return 8

    def cpus(self, hints: Dict[str, Any]):
        return 1

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
