from janis_core import WorkflowBuilder

# data types
from janis_bioinformatics.data_types import BamBai, Bed
from janis_core import String
from janis_bioinformatics.tools.samtools import (
    SamToolsFlagstatLatest,
    SamToolsViewLatest,
)
from janis_bioinformatics.tools.bedtools import (
    BedToolsGenomeCoverageBedLatest,
    BedToolsCoverageBedLatest,
)

from janis_bioinformatics.tools.gatk4 import Gatk4CollectInsertSizeMetricsLatest
from janis_bioinformatics.tools.pmac import (
    PerformanceSummaryLatest,
    GeneCoveragePerSampleLatest,
)

wf = WorkflowBuilder("PerformanceSummaryGenome", version="v0.1.0")
# workflow construction
PerformanceSummaryGenome_0_1_0 = wf

# Inputs
wf.input("bam", BamBai)
wf.input("bed", Bed)
wf.input("sampleName", String)

# Steps - Performance Summary
wf.step(
    "gatk4collectinsertsizemetrics",
    Gatk4CollectInsertSizeMetricsLatest(
        bam=wf.bam,
        outputFilename="insertsizemetrics.txt",
        outputHistogram="insertsizemetrics.pdf",
    ),
)
wf.step(
    "bamflagstat", SamToolsFlagstatLatest(bam=wf.bam),
)
wf.step(
    "samtoolsview",
    SamToolsViewLatest(sam=wf.bam, doNotOutputAlignmentsWithBitsSet="0x400",),
)
wf.step(
    "rmdupbamflagstat", SamToolsFlagstatLatest(bam=wf.samtoolsview.out),
)
wf.step(
    "bedtoolsgenomecoveragebed",
    BedToolsGenomeCoverageBedLatest(inputBam=wf.samtoolsview.out),
)
# Give all the output files to performance summary script
wf.step(
    "performancesummary",
    PerformanceSummaryLatest(
        flagstat=wf.bamflagstat.out,
        collectInsertSizeMetrics=wf.gatk4collectinsertsizemetrics.out,
        coverage=wf.bedtoolsgenomecoveragebed.out,
        rmdupFlagstat=wf.rmdupbamflagstat.out,
        genome=True,
        outputFilename=wf.sampleName,
    ),
)

# Steps - Gene Coverage
wf.step(
    "bedtoolscoverage",
    BedToolsCoverageBedLatest(
        inputABed=wf.bed, inputBBam=wf.samtoolsview.out, histogram=True,
    ),
)
wf.step(
    "genecoverage",
    GeneCoveragePerSampleLatest(
        sampleName=wf.sampleName,
        bedtoolsOutputPath=wf.bedtoolscoverage.out,
        outputGeneFile="gene.txt",
        outputRegionFile="region.txt",
    ),
)

wf.output(
    "performanceSummaryOut", source=wf.performancesummary.out,
)
wf.output(
    "geneFileOut", source=wf.genecoverage.geneFileOut,
)
wf.output(
    "regionFileOut", source=wf.genecoverage.regionFileOut,
)
