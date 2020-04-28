from janis_core import WorkflowBuilder

# data types
from janis_bioinformatics.data_types import BamBai, Bed
from janis_core import String

from janis_bioinformatics.tools.bioinformaticstoolbase import (
    BioinformaticsWorkflowBuilder,
)
from janis_bioinformatics.tools.samtools import (
    SamToolsFlagstatLatest,
    SamToolsViewLatest,
)
from janis_bioinformatics.tools.bedtools import (
    BedToolsCoverageBedLatest,
    BedToolsIntersectBedLatest,
)
from janis_bioinformatics.tools.gatk4 import Gatk4CollectInsertSizeMetricsLatest
from janis_bioinformatics.tools.pmac import (
    PerformanceSummaryLatest,
    GeneCoveragePerSampleLatest,
)

wf = BioinformaticsWorkflowBuilder(
    "PerformanceSummaryTargeted",
    friendly_name="Performance summary workflow (targeted bed)",
    version="v0.1.0",
    tool_provider="Peter MacCallum Cancer Centre",
)
# workflow construction
PerformanceSummaryTargeted_0_1_0 = wf

# Inputs
wf.input("bam", BamBai)
wf.input("bed", Bed)
wf.input("sample_name", String)

# Steps
wf.step(
    "gatk4collectinsertsizemetrics",
    Gatk4CollectInsertSizeMetricsLatest(
        bam=wf.bam,
        outputFilename="insertsizemetrics.txt",
        outputHistogram="insertsizemetrics.pdf",
    ),
)
wf.step("bamflagstat", SamToolsFlagstatLatest(bam=wf.bam))
wf.step(
    "samtoolsview",
    SamToolsViewLatest(sam=wf.bam, doNotOutputAlignmentsWithBitsSet="0x400"),
)
wf.step("rmdupbamflagstat", SamToolsFlagstatLatest(bam=wf.samtoolsview.out))
wf.step(
    "bedtoolsintersectbed",
    BedToolsIntersectBedLatest(inputABam=wf.samtoolsview.out, inputBBed=wf.bed),
)
wf.step("targetbamflagstat", SamToolsFlagstatLatest(bam=wf.bedtoolsintersectbed.out))
wf.step(
    "bedtoolscoveragebed",
    BedToolsCoverageBedLatest(
        inputABed=wf.bed, inputBBam=wf.bedtoolsintersectbed.out, histogram=True
    ),
)
# Give all the output files to performance summary script
wf.step(
    "performancesummary",
    PerformanceSummaryLatest(
        flagstat=wf.bamflagstat.out,
        collectInsertSizeMetrics=wf.gatk4collectinsertsizemetrics.out,
        targetFlagstat=wf.targetbamflagstat.out,
        coverage=wf.bedtoolscoveragebed.out,
        rmdupFlagstat=wf.rmdupbamflagstat.out,
        outputPrefix=wf.sample_name,
    ),
)

# Steps - Gene Coverage
wf.step(
    "bedtoolscoverage",
    BedToolsCoverageBedLatest(
        inputABed=wf.bed, inputBBam=wf.samtoolsview.out, histogram=True
    ),
)
wf.step(
    "genecoverage",
    GeneCoveragePerSampleLatest(
        sampleName=wf.sample_name,
        bedtoolsOutputPath=wf.bedtoolscoverage.out,
        outputGeneFile="gene.txt",
        outputRegionFile="region.txt",
    ),
)

# Outputs
wf.output("out", source=wf.performancesummary.out)
wf.output("geneFileOut", source=wf.genecoverage.geneFileOut)
wf.output("regionFileOut", source=wf.genecoverage.regionFileOut)
