from abc import ABC
from ..gatk3toolbase import GATK3ToolBase
from janis_bioinformatics.data_types import (
    BamBai,
    FastaWithDict,
    Bed
)

from janis_unix import TextFile

from janis_core import (
    ToolInput,
    ToolOutput,
    ToolMetadata,
    InputSelector,
    String,
    Int,
    Array
)

class GATK3DepthOfCoverageBase(GATK3ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "DepthOfCoverage"

    def friendly_name(self):
        return "GATK3 DepthOfCoverage: Determine coverage at different levels of partitioning and aggregation."

    def tool(self):
        return "Gatk3DepthOfCoverage"
    
    def inputs(self):
        return[
            ToolInput("bam", BamBai(), prefix="-I", doc="Input file containing sequence  data (BAM or CRAM)", secondaries_present_as={".bai": "^.bai"}, position=10,
            ),
            ToolInput("reference", FastaWithDict(), prefix="-R", doc="Reference sequence file"),
            ToolInput("outputFilename", String(), prefix="-o", doc="An output file created by the walker. Will overwrite contents if file exists"),
            ToolInput("interval", Bed(optional=True), prefix="-L", doc="Only bed is supported. One or more genomic intervals over which to operate"),
            ToolInput("countType", String(optional=True), prefix="--countType", doc="overlapping reads from the same  fragment be handled? (COUNT_READS|COUNT_FRAGMENTS|COUNT_FRAGMENTS_REQUIRE_SAME_BASE)"),
            ToolInput("summaryCoverageThreshold", Array(Int(), optional=True), prefix="-ct", doc="Coverage threshold (in percent) for summarizing statistics", prefix_applies_to_all_elements=True)
        ]

    def outputs(self):
        return [
                ToolOutput("out", TextFile(), glob=InputSelector("outputFilename"), doc=""),

                ToolOutput("sampleCumulativeCoverageCounts", TextFile(extension=".sample_cumulative_coverage_counts"), glob=InputSelector("outputFilename") + ".sample_cumulative_coverage_counts", doc=""),

                ToolOutput("sampleCumulativeCoverageProportions", TextFile(extension=".sample_cumulative_coverage_proportions"), glob=InputSelector("outputFilename") + ".sample_cumulative_coverage_proportions", doc=""),

                ToolOutput("sampleIntervalStatistics", TextFile(extension=".sample_interval_statistics"), glob=InputSelector("outputFilename") + ".sample_interval_statistics", doc=""),

                ToolOutput("sampleIntervalSummary", TextFile(extension=".sample_interval_summary"), glob=InputSelector("outputFilename") + ".sample_interval_summary", doc=""),

                ToolOutput("sampleStatistics", TextFile(extension=".sample_statistics"), glob=InputSelector("outputFilename") + ".sample_statistics", doc=""),

                ToolOutput("sampleSummary", TextFile(extension=".sample_summary"), glob=InputSelector("outputFilename") + ".sample_summary", doc=""),
        ]
