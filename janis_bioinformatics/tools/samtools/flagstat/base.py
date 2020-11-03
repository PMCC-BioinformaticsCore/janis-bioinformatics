import os
import operator
from abc import ABC

from janis_core import (
    ToolInput,
    Filename,
    Int,
    String,
    Boolean,
    ToolOutput,
    Array,
    InputSelector,
    WildcardSelector,
    Stdout,
)
from janis_unix import TextFile
from janis_bioinformatics.data_types.bam import Bam
from janis_bioinformatics.tools.samtools.samtoolstoolbase import SamToolsToolBase
from janis_core import ToolMetadata

from janis_core.tool.test_classes import TTestCompared, TTestExpectedOutput, TTestCase


class SamToolsFlagstatBase(SamToolsToolBase, ABC):
    def tool(self):
        return "SamToolsFlagstat"

    @classmethod
    def samtools_command(cls):
        return "flagstat"

    def inputs(self):
        return [
            ToolInput("bam", Bam(), position=10),
            ToolInput(
                "threads",
                Int(optional=True),
                position=5,
                prefix="-@",
                doc="Number of BAM compression threads to use in addition to main thread [0].",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", Stdout(TextFile))]

    def friendly_name(self):
        return "SamTools: Flagstat"

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=date(2020, 2, 14),
            dateUpdated=date(2020, 2, 14),
            institution="Samtools",
            doi=None,
            citation=None,
            keywords=["samtools", "flagstat"],
            documentationUrl="http://www.htslib.org/doc/samtools.html#COMMANDS_AND_OPTIONS",
            documentation="""Does a full pass through the input file to calculate and print statistics to stdout.

Provides counts for each of 13 categories based primarily on bit flags in the FLAG field. Each category in the output is broken down into QC pass and QC fail. In the default output format, these are presented as "#PASS + #FAIL" followed by a description of the category.

The first row of output gives the total number of reads that are QC pass and fail (according to flag bit 0x200). For example:

122 + 28 in total (QC-passed reads + QC-failed reads)

Which would indicate that there are a total of 150 reads in the input file, 122 of which are marked as QC pass and 28 of which are marked as "not passing quality controls"

Following this, additional categories are given for reads which are:

secondary     0x100 bit set

supplementary     0x800 bit set

duplicates     0x400 bit set

mapped     0x4 bit not set

paired in sequencing     0x1 bit set

read1     both 0x1 and 0x40 bits set

read2     both 0x1 and 0x80 bits set

properly paired     both 0x1 and 0x2 bits set and 0x4 bit not set

with itself and mate mapped     0x1 bit set and neither 0x4 nor 0x8 bits set

singletons     both 0x1 and 0x8 bits set and bit 0x4 not set

And finally, two rows are given that additionally filter on the reference name (RNAME), mate reference name (MRNM), and mapping quality (MAPQ) fields:

with mate mapped to a different chr     0x1 bit set and neither 0x4 nor 0x8 bits set and MRNM not equal to RNAME

with mate mapped to a different chr (mapQ>=5)     0x1 bit set and neither 0x4 nor 0x8 bits set and MRNM not equal to RNAME and MAPQ >= 5)""".strip(),
        )

    def tests(self):
        return [
            TTestCase(
                name="basic",
                input={
                    "bam": os.path.join(SamToolsToolBase.test_data_path(), "small.bam"),
                },
                output=[
                    TTestExpectedOutput(
                        tag="out",
                        compared=TTestCompared.FileMd5,
                        operator=operator.eq,
                        expected_value="dc58fe92a9bb0c897c85804758dfadbf",
                    ),
                    TTestExpectedOutput(
                        tag="out",
                        compared=TTestCompared.FileContent,
                        operator=operator.contains,
                        expected_value="19384 + 0 in total (QC-passed reads + QC-failed reads)",
                    ),
                    TTestExpectedOutput(
                        tag="out",
                        compared=TTestCompared.LineCount,
                        operator=operator.eq,
                        expected_value=13,
                    ),
                ],
            )
        ]
