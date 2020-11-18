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

        self.metadata.contributors = ["Jiaan Yu"]
        self.metadata.dateUpdated = date(2020, 2, 26)
        self.metadata.dateCreated = date(2020, 2, 20)
        self.metadata.doi = None
        self.metadata.citation = None
        self.metadata.keywords = ["bedtools", "coverageBed", "coverage"]
        self.metadata.documentationUrl = (
            "https://bedtools.readthedocs.io/en/latest/content/tools/coverage.html"
        )
        self.metadata.documentation = """The bedtools coverage tool computes both the depth and breadth of coverage of features in file B on the features in file A. For example, bedtools coverage can compute the coverage of sequence alignments (file B) across 1 kilobase (arbitrary) windows (file A) tiling a genome of interest. One advantage that bedtools coverage offers is that it not only counts the number of features that overlap an interval in file A, it also computes the fraction of bases in the interval in A that were overlapped by one or more features. Thus, bedtools coverage also computes the breadth of coverage observed for each interval in A."""

    def tool(self):
        return "bedtoolsCoverageBed"

    def friendly_name(self):
        return "BEDTools: coverageBed"

    def base_command(self):
        return ["coverageBed"]

    def inputs(self):
        return [
            *self.additional_inputs,
            ToolInput(
                "inputABed",
                Bed(),
                prefix="-a",
                doc="input file a: only bed is supported. May be followed with multiple databases and/or  wildcard (*) character(s). ",
            ),
            ToolInput(
                "inputBBam",
                Bam(),
                prefix="-b",
                doc="input file b: only bam is supported.",
            ),
            ToolInput(
                "histogram",
                Boolean(optional=True),
                prefix="-hist",
                doc="Report a histogram of coverage for each feature in A as well as a summary histogram for _all_ features in A. Output (tab delimited) after each feature in A: 1) depth 2) # bases at depth 3) size of A 4) % of A at depth.",
            ),
            ToolInput(
                "depth",
                Boolean(optional=True),
                prefix="-d",
                doc="Report the depth at each position in each A feature. Positions reported are one based.  Each position and depth follow the complete A feature.",
            ),
            ToolInput(
                "counts",
                Boolean(optional=True),
                prefix="-counts",
                doc="Only report the count of overlaps, don't compute fraction, etc.",
            ),
            ToolInput(
                "mean",
                Boolean(optional=True),
                prefix="-mean",
                doc="Report the mean depth of all positions in each A feature.",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", Stdout(TextFile))]

    additional_inputs = [
        ToolInput(
            "strandedness",
            Boolean(optional=True),
            prefix="-s",
            doc="Require same strandedness.  That is, only report hits in B that overlap A on the _same_ strand. - By default, overlaps are reported without respect to strand.",
        ),
        ToolInput(
            "differentStrandedness",
            Boolean(optional=True),
            prefix="-S",
            doc="Require different strandedness.  That is, only report hits in B that overlap A on the _opposite_ strand. - By default, overlaps are reported without respect to strand.",
        ),
        ToolInput(
            "fractionA",
            Float(optional=True),
            prefix="-f",
            doc="Minimum overlap required as a fraction of A. - Default is 1E-9 (i.e., 1bp). - FLOAT (e.g. 0.50)",
        ),
        ToolInput(
            "fractionB",
            Float(optional=True),
            prefix="-F",
            doc="Minimum overlap required as a fraction of B. - Default is 1E-9 (i.e., 1bp). - FLOAT (e.g. 0.50)",
        ),
        ToolInput(
            "reciprocalFraction",
            Boolean(optional=True),
            prefix="-r",
            doc="Require that the fraction overlap be reciprocal for A AND B. - In other words, if -f is 0.90 and -r is used, this requires that B overlap 90% of A and A _also_ overlaps 90% of B.",
        ),
        ToolInput(
            "minFraction",
            Boolean(optional=True),
            prefix="-r",
            doc="Require that the minimum fraction be satisfied for A OR B. - In other words, if -e is used with -f 0.90 and -F 0.10 this requires that either 90% of A is covered OR 10% of  B is covered. Without -e, both fractions would have to be satisfied.",
        ),
        ToolInput(
            "split",
            Boolean(optional=True),
            prefix="-split",
            doc="Treat 'split' BAM or BED12 entries as distinct BED intervals.",
        ),
        ToolInput(
            "genome",
            File(optional=True),
            prefix="-g",
            doc="Provide a genome file to enforce consistent chromosome sort order across input files. Only applies when used with -sorted option.",
        ),
        ToolInput(
            "noNameCheck",
            Boolean(optional=True),
            prefix="-nonamecheck",
            doc="For sorted data, don't throw an error if the file has different naming conventions for the same chromosome. ex. 'chr1' vs 'chr01'.",
        ),
        ToolInput(
            "sorted",
            Boolean(optional=True),
            prefix="-sorted",
            doc="Use the 'chromsweep' algorithm for sorted (-k1,1 -k2,2n) input.",
        ),
        ToolInput(
            "header",
            Boolean(optional=True),
            prefix="-header",
            doc="Print the header from the A file prior to results.",
        ),
        ToolInput(
            "noBuf",
            Boolean(optional=True),
            prefix="-nobuf",
            doc="Disable buffered output. Using this option will cause each line of output to be printed as it is generated, rather than saved in a buffer. This will make printing large output files noticeably slower, but can be useful in conjunction with other software tools and scripts that need to process one line of bedtools output at a time.",
        ),
        ToolInput(
            "bufMem",
            Int(optional=True),
            prefix="-iobuf",
            doc="Specify amount of memory to use for input buffer. Takes an integer argument. Optional suffixes K/M/G supported. Note: currently has no effect with compressed files.",
        ),
    ]
