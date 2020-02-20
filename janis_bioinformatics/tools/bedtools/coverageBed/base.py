from abc import ABC
from typing import List, Dict, Any
from datetime import date

from janis_core import get_value_for_hints_and_ordered_resource_tuple, ToolArgument
from janis_core import (
    ToolOutput,
    ToolInput,
    Boolean,
    Int,
    String,
    File,
    Array,
    Float,
    Stdout,
    CaptureType,
)
from janis_bioinformatics.data_types import Bam, Bed
from janis_unix import TextFile

from ..bedtoolstoolbase import BedToolsToolBase
from janis_core import ToolMetadata

class BedToolsCoverageBedBase(BedToolsToolBase, ABC):
    def bind_metadata(self):

        self.metadata.dateUpdated = date(2020, 2, 20)
        self.metadata.doi = ""
        self.metadata.citation = ""
        self.metadata.documentationUrl = ""
        self.metadata.documentation = ""

    def tool(self):
        return "bedtoolsCoverageBed"

    def friendly_name(self):
        return "BEDTools: coverageBed"

    def base_command(self):
        return ["coverageBed"]

    def inputs(self):
        return [
            *self.additional_inputs,
            ToolInput("inputABam", Bam(), prefix="-a",
            doc="input file a: only bam is supported at the moment"),
            ToolInput("inputBBed", Array(Bed()), prefix="-b", 
            doc="input file b: only bed is supported at the moment. May be followed with multiple databases and/or  wildcard (*) character(s). "),
            ToolInput("histogram", Boolean(optional=True), prefix="-hist", doc="Report a histogram of coverage for each feature in A as well as a summary histogram for _all_ features in A. Output (tab delimited) after each feature in A: 1) depth 2) # bases at depth 3) size of A 4) % of A at depth.")
        ]

    def outputs(self):
        return [
            ToolOutput("out", Stdout(TextFile))
        ]

    additional_inputs = []