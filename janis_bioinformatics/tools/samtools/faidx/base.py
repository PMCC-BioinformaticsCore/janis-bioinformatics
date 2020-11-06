import os
import operator
from abc import ABC
from datetime import date

from janis_core import ToolInput, ToolOutput, InputSelector
from janis_core import ToolMetadata

from janis_bioinformatics.data_types import Fasta, FastaFai
from ..samtoolstoolbase import SamToolsToolBase

from janis_core.tool.test_classes import (
    TTestPreprocessor,
    TTestExpectedOutput,
    TTestCase,
)


class SamToolsFaidxBase(SamToolsToolBase, ABC):
    def tool(self):
        return "SamToolsFaidx"

    @classmethod
    def samtools_command(cls):
        return "faidx"

    def inputs(self):
        return [ToolInput("reference", Fasta, position=1, localise_file=True)]

    def outputs(self):
        return [ToolOutput("out", FastaFai, glob=InputSelector("reference"))]

    def friendly_name(self):
        return "SamTools: faidx"

    def bind_metadata(self):
        self.metadata = ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=date(2020, 2, 14),
            dateUpdated=date(2020, 2, 14),
            institution="Samtools",
            doi=None,
            citation=None,  # find citation
            keywords=["samtools", "faidx"],
            documentationUrl="http://www.htslib.org/doc/samtools.html#COMMANDS_AND_OPTIONS",
            documentation="""""",
        )
        return self.metadata

    def tests(self):
        return [
            TTestCase(
                name="basic",
                input={
                    "reference": os.path.join(
                        SamToolsToolBase.test_data_path(), "hg38-brca1.fasta"
                    ),
                },
                output=[
                    TTestExpectedOutput(
                        tag="out",
                        preprocessor=TTestPreprocessor.FileMd5,
                        operator=operator.eq,
                        expected_value="768915f0ceff3bae0bac0ace5f7ccad0",
                    ),
                ],
            )
        ]
