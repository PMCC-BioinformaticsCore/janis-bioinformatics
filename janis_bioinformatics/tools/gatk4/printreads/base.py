from abc import ABC
from typing import List

from janis_core import ToolOutput, ToolInput, Filename, InputSelector
from janis_bioinformatics.data_types.bam import Bam, BamBai
from ..gatk4toolbase import Gatk4ToolBase
from janis_core import ToolMetadata


class Gatk4PrintReadsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "PrintReads"

    @staticmethod
    def tool():
        return "Gatk4PrintReads"

    def friendly_name(self):
        return "GATK4: Print Reads"

    def inputs(self):
        return [ToolInput("bam", Bam()), ToolInput("outputFilename", Filename())]

    def outputs(self) -> List[ToolOutput]:
        return [ToolOutput("out", BamBai(), glob=InputSelector("outputFilename"))]

    def metadata(self):
        from datetime import date

        return ToolMetadata(
            creator="Michael Franklin",
            maintainer="Michael Franklin",
            maintainerEmail="michael.franklin@petermac.org",
            dateCreated=date(2018, 12, 24),
            dateUpdated=date(2019, 1, 24),
            institution="Broad Institute",
            doi=None,
            citation="See https://software.broadinstitute.org/gatk/documentation/article?id=11027 for more information",
            keywords=["gatk", "gatk4", "broad", "print reads"],
            documentationUrl="https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_PrintReads.php",
            documentation="""
Write reads from SAM format file (SAM/BAM/CRAM) that pass criteria to a new file.
A common use case is to subset reads by genomic interval using the -L argument. 
Note when applying genomic intervals, the tool is literal and does not retain mates 
of paired-end reads outside of the interval, if any. Data with missing mates will fail 
ValidateSamFile validation with MATE_NOT_FOUND, but certain tools may still analyze the data. 
If needed, to rescue such mates, use either FilterSamReads or ExtractOriginalAlignmentRecordsByNameSpark.

By default, PrintReads applies the WellformedReadFilter at the engine level. 
What this means is that the tool does not print reads that fail the WellformedReadFilter filter. 
You can similarly apply other engine-level filters to remove specific types of reads 
with the --read-filter argument. See documentation category 'Read Filters' for a list of
 available filters. To keep reads that do not pass the WellformedReadFilter, either 
 disable the filter with --disable-read-filter or disable all default filters with 
 ``--disable-tool-default-read-filters``.

The reference is strictly required when handling CRAM files.""",
        )
