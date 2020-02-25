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
from ..bedtoolstoolbase import BedToolsToolBase
from janis_core import ToolMetadata

class BedToolsIntersectBedBase(BedToolsToolBase, ABC):
    def bind_metadata(self):

        self.metadata.dateUpdated = date(2020, 2, 1)
        self.metadata.doi = ""
        self.metadata.citation = ""
        self.metadata.documentationUrl = ""
        self.metadata.documentation = ""
    
    def tool(self):
        return "bedtoolsintersectBed"

    def friendly_name(self):
        return "BEDTools: intersectBed"

    def base_command(self):
        return ["intersectBed"]
    
    def inputs(self):
        return [
            *self.additional_inputs,
            ToolInput("inputABam", Bam(), prefix="-a",
            doc="input file a: only bam is supported at the moment"),
            ToolInput("inputBBed", Array(Bed()), prefix="-b", 
            doc="input file b: only bed is supported at the moment. May be followed with multiple databases and/or  wildcard (*) character(s). "),
        ]
    
    def outputs(self):
        return [
            ToolOutput("out", Stdout(Bam))
        ]

    additional_inputs = [
            ToolInput("writeOriginalA", Boolean(optional=True), prefix="-wa",
            doc="Write the original entry in A for each overlap."),
            ToolInput("writeOriginalB", Boolean(optional=True), prefix="-wb",
            doc="Write the original entry in B for each overlap. - Useful for knowing _what_ A overlaps. Restricted by -f  and -r."),
            ToolInput("leftOuterJoin", Boolean(optional=True), prefix="-loj", doc="Perform a 'left outer join'. That is, for each feature in A report each overlap with B.  If no overlaps are found, report a NULL feature for B."),
            ToolInput("writeOriginalAB", Boolean(optional=True), prefix="-wo", doc="Write the original A and B entries plus the number of base pairs of overlap between the two features. - Overlaps restricted by -f and -r. Only A features with overlap are reported."),
            ToolInput("writeABBase", Boolean(optional=True), prefix="-wao", doc="Write the original A and B entries plus the number of base pairs of overlap between the two features. - Overlapping features restricted by -f and -r. However, A features w/o overlap are also reported with a NULL B feature and overlap = 0."),
            ToolInput("modeu", Boolean(optional=True), prefix="-u", doc="Write the original A entry _once_ if _any_ overlaps found in B. - In other words, just report the fact >=1 hit was found. - Overlaps restricted by -f and -r."),
            ToolInput("modec", Boolean(optional=True), prefix="-c", doc="For each entry in A, report the number of overlaps with B. - Reports 0 for A entries that have no overlap with B. - Overlaps restricted by -f, -F, -r, and -s."),
            ToolInput("modeC", Boolean(optional=True), prefix="-C", doc="-C	For each entry in A, separately report the number of - overlaps with each B file on a distinct line. - Reports 0 for A entries that have no overlap with B. - Overlaps restricted by -f, -F, -r, and -s."),
            ToolInput("modev", Boolean(optional=True), prefix="-v", doc="Only report those entries in A that have _no overlaps_ with B. - Similar to 'grep -v' (an homage)."),
            #ToolInput("ubam")
            ToolInput("strandedness", Boolean(optional=True), prefix="-s", doc="Require same strandedness.  That is, only report hits in B that overlap A on the _same_ strand. - By default, overlaps are reported without respect to strand."),
            ToolInput("differentStrandedness", Boolean(optional=True), prefix="-S", doc="Require different strandedness.  That is, only report hits in B that overlap A on the _opposite_ strand. - By default, overlaps are reported without respect to strand."),
            ToolInput("fractionA", Float(optional=True), prefix="-f", doc="Minimum overlap required as a fraction of A. - Default is 1E-9 (i.e., 1bp). - FLOAT (e.g. 0.50)"),
            ToolInput("fractionB", Float(optional=True), prefix="-F", doc="Minimum overlap required as a fraction of B. - Default is 1E-9 (i.e., 1bp). - FLOAT (e.g. 0.50)"),
            ToolInput("reciprocalFraction", Boolean(optional=True), prefix="-r", doc="Require that the fraction overlap be reciprocal for A AND B. - In other words, if -f is 0.90 and -r is used, this requires that B overlap 90% of A and A _also_ overlaps 90% of B."),
            ToolInput("minFraction", Boolean(optional=True), prefix="-r",
            doc="Require that the minimum fraction be satisfied for A OR B. - In other words, if -e is used with -f 0.90 and -F 0.10 this requires that either 90% of A is covered OR 10% of  B is covered. Without -e, both fractions would have to be satisfied."),
            ToolInput("split", Boolean(optional=True), prefix="-split", doc="Treat 'split' BAM or BED12 entries as distinct BED intervals."),
            ToolInput("genome", File(optional=True), prefix="-g",
            doc="Provide a genome file to enforce consistent chromosome sort order across input files. Only applies when used with -sorted option."),
            ToolInput("noNameCheck", Boolean(optional=True), prefix="-nonamecheck", doc="For sorted data, don't throw an error if the file has different naming conventions for the same chromosome. ex. 'chr1' vs 'chr01'."),
            ToolInput("sorted", Boolean(optional=True), prefix="-sorted", doc="Use the 'chromsweep' algorithm for sorted (-k1,1 -k2,2n) input."),
            #ToolInput("names", Arrary(list), prefix="-names", doc="When using multiple databases, provide an alias for each that will appear instead of a fileId when also printing the DB record."),
            #ToolInput("fileNames", Array(list), prefix="-filenames", doc="When using multiple databases, show each complete filename instead of a fileId when also printing the DB record."),
            ToolInput("sortOut", Boolean(optional=True), prefix="-sortout", doc="When using multiple databases, sort the output DB hits for each record."),
            #ToolInput("bed", prefix="-bed", doc="If using BAM input, write output as BED."),
            ToolInput("header", Boolean(optional=True), prefix="-header", doc="Print the header from the A file prior to results."),
            ToolInput("noBuf", Boolean(optional=True), prefix="-nobuf", doc="Disable buffered output. Using this option will cause each line of output to be printed as it is generated, rather than saved in a buffer. This will make printing large output files noticeably slower, but can be useful in conjunction with other software tools and scripts that need to process one line of bedtools output at a time."),
            ToolInput("bufMem", Int(optional=True), prefix="-iobuf", doc="Specify amount of memory to use for input buffer. Takes an integer argument. Optional suffixes K/M/G supported. Note: currently has no effect with compressed files.")

    ]
