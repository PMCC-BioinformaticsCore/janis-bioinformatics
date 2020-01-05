from abc import ABC
from datetime import date

from janis_core import (
    ToolInput,
    ToolOutput,
    ToolArgument,
    Int,
    InputSelector,
    CpuSelector,
)
from janis_core import ToolMetadata

from janis_bioinformatics.data_types.bam import Bam, BamBai
from ..samtoolstoolbase import SamToolsToolBase


class SamToolsIndexBase(SamToolsToolBase, ABC):
    def tool(self):
        return "SamToolsIndex"

    @classmethod
    def samtools_command(cls):
        return "index"

    def inputs(self):
        return [
            *super(SamToolsIndexBase, self).inputs(),
            *SamToolsIndexBase.additional_inputs,
            ToolInput("bam", Bam, position=10, localise_file=True),
            ToolInput(
                "threads",
                Int(optional=True),
                prefix="-@",
                default=CpuSelector(),
                position=10,
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", BamBai, glob=InputSelector("bam"))]

    def friendly_name(self):
        return "SamTools: Index"

    def bind_metadata(self):
        self.metadata = ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=date(2019, 12, 17),
            dateUpdated=date(2019, 12, 17),
            institution="Samtools",
            doi=None,
            citation=None,  # find citation
            keywords=["samtools", "index"],
            documentationUrl="http://www.htslib.org/doc/samtools.html#COMMANDS_AND_OPTIONS",
            documentation="""""",
        )
        return self.metadata

    def arguments(self):
        return [ToolArgument("-b", position=4, doc="Output in the BAM format.")]

    additional_inputs = []
