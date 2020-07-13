from abc import ABC
from typing import Dict, Any
from janis_core import get_value_for_hints_and_ordered_resource_tuple
from ..gatk4toolbase import Gatk4ToolBase
from janis_bioinformatics.data_types import BamBai, FastaWithDict, Bed
from janis_unix import TextFile

from janis_core import (
    ToolInput,
    Filename,
    ToolOutput,
    String,
    InputSelector,
    CaptureType,
    ToolMetadata,
    Array,
    Int,
    Boolean,
)
from janis_unix import Tsv

CORES_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.CHROMOSOME: 1,
            CaptureType.EXOME: 1,
            CaptureType.THIRTYX: 1,
            CaptureType.NINETYX: 1,
            CaptureType.THREEHUNDREDX: 1,
        },
    )
]

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.CHROMOSOME: 16,
            CaptureType.EXOME: 16,
            CaptureType.THIRTYX: 16,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class Gatk4DepthOfCoverageBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "DepthOfCoverage"

    def friendly_name(self):
        return "GATK4: Generate coverage summary information for reads data"

    def tool(self):
        return "Gatk4DepthOfCoverage"

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 1

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 8

    def inputs(self):
        return [
            *super(Gatk4DepthOfCoverageBase, self).inputs(),
            ToolInput(
                "bam",
                BamBai(),
                prefix="-I",
                doc="The SAM/BAM/CRAM file containing reads.",
                secondaries_present_as={".bai": "^.bai"},
            ),
            ToolInput(
                "reference", FastaWithDict(), prefix="-R", doc="Reference sequence"
            ),
            ToolInput(
                "outputPrefix",
                String(),
                prefix="-O",
                doc="An output file created by the walker. Will overwrite contents if file exists",
            ),
            ToolInput(
                "intervals",
                Array(Bed),
                prefix="--intervals",
                doc="-L (BASE) One or more genomic intervals over which to operate",
                prefix_applies_to_all_elements=True,
            ),
            *self.additional_args,
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out_sample",
                TextFile(optional=True),
                glob=InputSelector("outputPrefix"),
                doc="per locus coverage",
            ),
            ToolOutput(
                "out_sampleCumulativeCoverageCounts",
                TextFile(),
                glob=InputSelector("outputPrefix")
                + ".sample_cumulative_coverage_counts",
                doc="coverage histograms (# locus with >= X coverage), aggregated over all bases",
            ),
            ToolOutput(
                "out_sampleCumulativeCoverageProportions",
                TextFile(),
                glob=InputSelector("outputPrefix")
                + ".sample_cumulative_coverage_proportions",
                doc="proprotions of loci with >= X coverage, aggregated over all bases",
            ),
            ToolOutput(
                "out_sampleIntervalStatistics",
                TextFile(),
                glob=InputSelector("outputPrefix") + ".sample_interval_statistics",
                doc="total, mean, median, quartiles, and threshold proportions, aggregated per interval",
            ),
            ToolOutput(
                "out_sampleIntervalSummary",
                TextFile(),
                glob=InputSelector("outputPrefix") + ".sample_interval_summary",
                doc="2x2 table of # of intervals covered to >= X depth in >=Y samples",
            ),
            ToolOutput(
                "out_sampleStatistics",
                TextFile(),
                glob=InputSelector("outputPrefix") + ".sample_statistics",
                doc="coverage histograms (# locus with X coverage), aggregated over all bases",
            ),
            ToolOutput(
                "out_sampleSummary",
                TextFile(),
                glob=InputSelector("outputPrefix") + ".sample_summary",
                doc="total, mean, median, quartiles, and threshold proportions, aggregated over all bases",
            ),
        ]

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=date(2020, 7, 10),
            dateUpdated=date(2020, 7, 10),
            institution="Broad Institute",
            doi=None,
            citation="See https://software.broadinstitute.org/gatk/documentation/article?id=11027 for more information",
            keywords=["gatk", "gatk4", "broad"],
            documentationUrl="https://gatk.broadinstitute.org/hc/en-us/articles/360041851491-DepthOfCoverage-BETA-",
            documentation="""
Generate coverage summary information for reads data

Category Coverage Analysis
Overview
Assess sequence coverage by a wide array of metrics, partitioned by sample, read group, or library
This tool processes a set of bam files to determine coverage at different levels of partitioning and aggregation. Coverage can be analyzed per locus, per interval, per gene, or in total; can be partitioned by sample, by read group, by technology, by center, or by library; and can be summarized by mean, median, quartiles, and/or percentage of bases covered to or beyond a threshold. Additionally, reads and bases can be filtered by mapping or base quality score.""".strip(),
        )

    additional_args = [
        ToolInput(
            "countType",
            String(optional=True),
            prefix="--count-type",
            doc="overlapping reads from the same  fragment be handled? (COUNT_READS|COUNT_FRAGMENTS|COUNT_FRAGMENTS_REQUIRE_SAME_BASE)",
        ),
        ToolInput(
            "summaryCoverageThreshold",
            Array(Int(), optional=True),
            prefix="--summary-coverage-threshold",
            doc="Coverage threshold (in percent) for summarizing statistics",
            prefix_applies_to_all_elements=True,
        ),
        ToolInput(
            "omitDepthOutputAtEachBase",
            Boolean(optional=True),
            prefix="--omit-depth-output-at-each-base",
            doc="Do not output depth of coverage at each base",
        ),
        ToolInput(
            "omitGenesNotEntirelyCoveredByTraversal",
            Boolean(optional=True),
            prefix="--omit-genes-not-entirely-covered-by-traversal",
            doc="Do not output gene summary if it was not completely covered by traversal intervals",
        ),
        ToolInput(
            "omitIntervalStatistics",
            Boolean(optional=True),
            prefix="--omit-interval-statistics",
            doc="Do not calculate per-interval statistics",
        ),
        ToolInput(
            "omitLocusTable",
            Boolean(optional=True),
            prefix="--omit-locus-table",
            doc="Do not calculate per-sample per-depth counts of loci",
        ),
        ToolInput(
            "omitPerSampleStatistics",
            Boolean(optional=True),
            prefix="--omit-per-sample-statistics",
            doc="Do not output the summary files per-sample",
        ),
    ]
