from abc import ABC
from ..gatk3toolbase import GATK3ToolBase
from janis_bioinformatics.data_types import BamBai, FastaWithDict, Bed

from janis_unix import TextFile

from janis_core import (
    ToolInput,
    ToolOutput,
    ToolMetadata,
    InputSelector,
    String,
    Int,
    Array,
    Boolean,
    File,
    Float,
    Filename,
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
        return [
            ToolInput(
                "bam",
                BamBai(),
                prefix="-I",
                doc="Input file containing sequence  data (BAM or CRAM)",
                secondaries_present_as={".bai": "^.bai"},
                position=10,
            ),
            ToolInput(
                "reference", FastaWithDict(), prefix="-R", doc="Reference sequence file"
            ),
            ToolInput(
                "outputPrefix",
                String(),
                prefix="-o",
                doc="An output file created by the walker. Will overwrite contents if file exists",
            ),
            ToolInput(
                "intervals",
                File(optional=True),
                prefix="-L",
                doc="One or more genomic intervals over which to operate",
            ),
            ToolInput(
                "excludeIntervals",
                File(optional=True),
                prefix="--excludeIntervals",
                doc="One or more genomic intervals to exclude from processing",
            ),
            *self.additional_args,
        ]

    def outputs(self):
        return [
            ToolOutput(
                "sample", TextFile(), glob=InputSelector("outputPrefix"), doc="",
            ),
            ToolOutput(
                "sampleCumulativeCoverageCounts",
                TextFile(),
                glob=InputSelector("outputPrefix")
                + ".sample_cumulative_coverage_counts",
                doc="",
            ),
            ToolOutput(
                "sampleCumulativeCoverageProportions",
                TextFile(),
                glob=InputSelector("outputPrefix")
                + ".sample_cumulative_coverage_proportions",
                doc="",
            ),
            ToolOutput(
                "sampleIntervalStatistics",
                TextFile(),
                glob=InputSelector("outputPrefix") + ".sample_interval_statistics",
                doc="",
            ),
            ToolOutput(
                "sampleIntervalSummary",
                TextFile(),
                glob=InputSelector("outputPrefix") + ".sample_interval_summary",
                doc="",
            ),
            ToolOutput(
                "sampleStatistics",
                TextFile(),
                glob=InputSelector("outputPrefix") + ".sample_statistics",
                doc="",
            ),
            ToolOutput(
                "sampleSummary",
                TextFile(),
                glob=InputSelector("outputPrefix") + ".sample_summary",
                doc="",
            ),
        ]

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=date(2020, 4, 9),
            dateUpdated=date(2020, 4, 9),
            institution="Broad Institute",
            doi=None,
            citation="",
            keywords=["gatk", "gatk3", "DepthOfCoverage"],
            documentationUrl="https://github.com/broadinstitute/gatk-docs/blob/master/gatk3-tooldocs/3.8-0/org_broadinstitute_gatk_engine_CommandLineGATK.html",
            documentation="""Overview
This tool processes a set of bam files to determine coverage at different levels of partitioning and aggregation. Coverage can be analyzed per locus, per interval, per gene, or in total; can be partitioned by sample, by read group, by technology, by center, or by library; and can be summarized by mean, median, quartiles, and/or percentage of bases covered to or beyond a threshold. Additionally, reads and bases can be filtered by mapping or base quality score.

Input
One or more bam files (with proper headers) to be analyzed for coverage statistics
(Optional) A REFSEQ file to aggregate coverage to the gene level (for information about creating the REFSEQ Rod, please consult the online documentation)
Output
Tables pertaining to different coverage summaries. Suffix on the table files declares the contents:

no suffix: per locus coverage
_summary: total, mean, median, quartiles, and threshold proportions, aggregated over all bases
_statistics: coverage histograms (# locus with X coverage), aggregated over all bases
_interval_summary: total, mean, median, quartiles, and threshold proportions, aggregated per interval
_interval_statistics: 2x2 table of # of intervals covered to >= X depth in >=Y samples
_gene_summary: total, mean, median, quartiles, and threshold proportions, aggregated per gene
_gene_statistics: 2x2 table of # of genes covered to >= X depth in >= Y samples
_cumulative_coverage_counts: coverage histograms (# locus with >= X coverage), aggregated over all bases
_cumulative_coverage_proportions: proprotions of loci with >= X coverage, aggregated over all bases""",
        )

    additional_args = [
        # Engine parameters
        ToolInput(
            "argFile",
            File(optional=True),
            prefix="--arg_file",
            doc="Reads arguments from the specified file",
        ),
        ToolInput(
            "showFullBamList",
            Boolean(optional=True),
            prefix="--showFullBamList",
            doc="Emit list of input BAM/CRAM files to log",
        ),
        ToolInput(
            "read_buffer_size",
            Int(optional=True),
            prefix="--read_buffer_size",
            doc="Number of reads per SAM file to buffer in memory",
        ),
        ToolInput(
            "read_filter",
            Boolean(optional=True),
            prefix="--read_filter",
            doc="Filters to apply to reads before analysis",
        ),
        ToolInput(
            "disable_read_filter",
            Boolean(optional=True),
            prefix="--disable_read_filter",
            doc="Read filters to disable",
        ),
        ToolInput(
            "interval_set_rule",
            String(optional=True),
            prefix="--interval_set_rule",
            doc="Set merging approach to use for combining interval inputs (UNION|INTERSECTION)",
        ),
        ToolInput(
            "interval_merging",
            String(optional=True),
            prefix="--interval_merging",
            doc="Set merging approach to use for combining interval inputs (UNION|INTERSECTION)",
        ),
        ToolInput(
            "interval_padding",
            Int(optional=True),
            prefix="--interval_padding",
            doc="Amount of padding (in bp) to add to each interval",
        ),
        ToolInput(
            "nonDeterministicRandomSeed",
            Boolean(optional=True),
            prefix="--nonDeterministicRandomSeed",
            doc="Use a non-deterministic random seed",
        ),
        ToolInput(
            "maxRuntime",
            String(optional=True),
            prefix="--maxRuntime",
            doc="Unit of time used by maxRuntime (NANOSECONDS|MICROSECONDS|SECONDS|MINUTES|HOURS|DAYS)",
        ),
        ToolInput(
            "downsampling_type",
            String(optional=True),
            prefix="--downsampling_type",
            doc="Type of read downsampling to employ at a given locus (NONE|ALL_READS|BY.sample)",
        ),
        ToolInput(
            "downsample_to_fraction",
            Float(optional=True),
            prefix="--downsample_to_fraction",
            doc="Fraction of reads to downsample to Target coverage threshold for downsampling to coverage",
        ),
        ToolInput(
            "baq",
            String(optional=True),
            prefix="--baq",
            doc="Type of BAQ calculation to apply in the engine (OFF|CALCULATE_AS_NECESSARY|RECALCULATE)",
        ),
        # ToolInput("baqGapOpenPenalty", Type(?), prefix="--baqGapOpenPenalty", doc="BAQ gap open penalty"),
        ToolInput(
            "refactor_NDN_cigar_string",
            Boolean(optional=True),
            prefix="--refactor_NDN_cigar_string",
            doc="Reduce NDN elements in CIGAR string",
        ),
        ToolInput(
            "fixMisencodedQuals",
            Boolean(optional=True),
            prefix="--fixMisencodedQuals",
            doc="Fix mis-encoded base quality scores",
        ),
        ToolInput(
            "allowPotentiallyMisencodedQuals",
            Boolean(optional=True),
            prefix="--allowPotentiallyMisencodedQuals",
            doc="Ignore warnings about base quality score encoding",
        ),
        ToolInput(
            "useOriginalQualities",
            Boolean(optional=True),
            prefix="--useOriginalQualities",
            doc="Use the base quality scores from the OQ tag",
        ),
        ToolInput(
            "defaultBaseQualities",
            Int(optional=True),
            prefix="--defaultBaseQualities",
            doc="Assign a default base quality",
        ),
        ToolInput(
            "performanceLog",
            Filename(),
            prefix="--performanceLog",
            doc="Write GATK runtime performance log to this file",
        ),
        ToolInput(
            "BQSR",
            File(optional=True),
            prefix="--BQSR",
            doc="Input covariates table file for on-the-fly base quality score recalibration",
        ),
        # ToolInput("quantize_quals", Int(optional=True), prefix="--quantize_quals", doc="Quantize quality scores to a given number of levels (with -BQSR)"),
        # ToolInput("static_quantized_quals", Type(optional=True), prefix="--static_quantized_quals", doc="Use static quantized quality scores to a given number of levels (with -BQSR)"),
        ToolInput(
            "disable_indel_quals",
            Boolean(optional=True),
            prefix="--disable_indel_quals",
            doc="Disable printing of base insertion and deletion tags (with -BQSR)",
        ),
        ToolInput(
            "emit_original_quals",
            Boolean(optional=True),
            prefix="--emit_original_quals",
            doc="Emit the OQ tag with the original base qualities (with -BQSR)",
        ),
        ToolInput(
            "preserve_qscores_less_than",
            Int(optional=True),
            prefix="--preserve_qscores_less_than",
            doc="Don't recalibrate bases with quality scores less than this threshold (with -BQSR)",
        ),
        # ToolInput("globalQScorePrior", Type(optional=True), prefix="--globalQScorePrior", doc="globalQScorePrior")
        # Tool specific parameters
        ToolInput(
            "countType",
            String(optional=True),
            prefix="--countType",
            doc="overlapping reads from the same  fragment be handled? (COUNT_READS|COUNT_FRAGMENTS|COUNT_FRAGMENTS_REQUIRE_SAME_BASE)",
        ),
        ToolInput(
            "summaryCoverageThreshold",
            Array(Int(), optional=True),
            prefix="-ct",
            doc="Coverage threshold (in percent) for summarizing statistics",
            prefix_applies_to_all_elements=True,
        ),
    ]
