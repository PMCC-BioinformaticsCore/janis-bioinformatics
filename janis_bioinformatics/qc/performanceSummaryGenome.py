from janis_core import WorkflowBuilder

# data types
from janis_bioinformatics.data_types import Bam, Bed
from janis_core import String
from janis_bioinformatics.tools.samtools import (
    SamToolsFlagstatLatest,
    SamToolsViewLatest,
)
from janis_bioinformatics.tools.bedtools import BedToolsGenomeCoverageBedLatest

from janis_bioinformatics.tools.gatk4 import Gatk4CollectInsertSizeMetricsLatest
from janis_bioinformatics.tools.pmac import PerformanceSummaryLatest

w = WorkflowBuilder("performanceSummaryGenomeWorkflow")

# Inputs
w.input("bam", Bam)
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
    "bedtoolsgenomecoveragebed",
    BedToolsGenomeCoverageBedLatest(inputBam=w.samtoolsview.out),
)
# Give all the output files to performance summary script
w.step(
    "performancesummary",
    PerformanceSummaryLatest(
        flagstat=w.bamflagstat.out,
        collectInsertSizeMetrics=w.gatk4collectinsertsizemetrics.out,
        coverage=w.bedtoolsgenomecoveragebed.out,
        rmdupFlagstat=w.rmdupbamflagstat.out,
        genome=True,
        outputFilename=w.outputFilename,
    ),
)

w.output("out", source=w.performancesummary.out)
