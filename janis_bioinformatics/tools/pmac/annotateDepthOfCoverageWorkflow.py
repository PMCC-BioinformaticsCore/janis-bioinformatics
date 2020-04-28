from janis_core import WorkflowBuilder

# data types
from janis_bioinformatics.data_types import BamBai, Bed, FastaWithDict
from janis_core import String

from janis_bioinformatics.tools.bioinformaticstoolbase import (
    BioinformaticsWorkflowBuilder,
)
from janis_bioinformatics.tools.gatk3 import GATK3DepthOfCoverageLatest
from janis_bioinformatics.tools.pmac import AddSymToDepthOfCoverageLatest

wf = BioinformaticsWorkflowBuilder(
    "AnnotateDepthOfCoverage",
    friendly_name="Annotate GATK3 DepthOfCoverage Workflow",
    version="v0.1.0",
    tool_provider="Peter MacCallum Cancer Centre",
)
# workflow construction
AnnotateDepthOfCoverage_0_1_0 = wf

wf.input("bam", BamBai)
wf.input("bed", Bed)
wf.input("reference", FastaWithDict)
# wf.input("outputprefix", String)
wf.input("sample_name", String)

wf.step(
    "gatk3depthofcoverage",
    GATK3DepthOfCoverageLatest(
        reference=wf.reference,
        bam=wf.bam,
        intervals=wf.bed,
        countType="COUNT_FRAGMENTS_REQUIRE_SAME_BASE",
        summaryCoverageThreshold=[1, 50, 100, 300, 500],
        outputPrefix=wf.sample_name,
    ),
)

wf.step(
    "addsymtodepthofcoverage",
    AddSymToDepthOfCoverageLatest(
        inputFile=wf.gatk3depthofcoverage.sampleIntervalSummary,
        bed=wf.bed,
        outputFilename=wf.sample_name,
    ),
)

wf.output("out", source=wf.addsymtodepthofcoverage.out, output_name=wf.sample_name)
