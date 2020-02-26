from janis_core import WorkflowBuilder

# data types
from janis_bioinformatics.data_types import Bam, Bed
from janis_core import String
from janis_bioinformatics.tools.samtools import (
    SamToolsFlagstatLatest,
    SamToolsViewLatest,
)
from janis_bioinformatics.tools.bedtools import (
    BedToolsCoverageBedLatest,
    BedToolsIntersectBedLatest,
)
from janis_bioinformatics.tools.gatk4 import Gatk4CollectInsertSizeMetricsLatest
from janis_bioinformatics.tools.pmac import PerformanceSummaryLatest

w = WorkflowBuilder("performanceSummaryWorkflow")

# Inputs
w.input("bam", Bam)
w.input("bed", Bed)
w.input("outputFilename", String)

# Steps
w.step(
    "gatk4collectinsertsizemetrics",
    Gatk4CollectInsertSizeMetricsLatest(
        bam=w.bam,
        outputFilename="insertsizemetrics.txt",
        outputHistogram="insertsizemetrics.pdf",
    ),
)
w.step("bamflagstat", SamToolsFlagstatLatest(bam=w.bam))
w.step(
    "samtoolsview",
    SamToolsViewLatest(sam=w.bam, doNotOutputAlignmentsWithBitsSet="0x400"),
)
w.step("rmdupbamflagstat", SamToolsFlagstatLatest(bam=w.samtoolsview.out))
w.step(
    "bedtoolsintersectbed",
    BedToolsIntersectBedLatest(inputABam=w.samtoolsview.out, inputBBed=w.bed),
)
w.step("targetbamflagstat", SamToolsFlagstatLatest(bam=w.bedtoolsintersectbed.out,))
w.step(
    "bedtoolscoveragebed",
    BedToolsCoverageBedLatest(
        inputABed=w.bed, inputBBam=w.bedtoolsintersectbed.out, histogram=True
    ),
)
# Give all the output files to performance summary script
w.step(
    "performancesummary",
    PerformanceSummaryLatest(
        flagstat=w.bamflagstat.out,
        collectInsertSizeMetrics=w.gatk4collectinsertsizemetrics.out,
        targetFlagstat=w.targetbamflagstat.out,
        coverage=w.bedtoolscoveragebed.out,
        rmdupFlagstat=w.rmdupbamflagstat.out,
        outputFilename=w.outputFilename,
    ),
)

w.output("out", source=w.performancesummary.out)
