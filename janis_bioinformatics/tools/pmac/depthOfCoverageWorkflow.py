from janis_core import WorkflowBuilder

# data types
from janis_bioinformatics.data_types import BamBai, Bed, FastaWithDict
from janis_core import String

from janis_bioinformatics.tools.gatk3 import GATK3DepthOfCoverageLatest
from janis_bioinformatics.tools.pmac import AddSymToDepthOfCoverageLatest

depthOfCoverageWorkflow_0_1_0 = WorkflowBuilder("depthOfCoverageWorkflow")

depthOfCoverageWorkflow_0_1_0.input("bam", BamBai)
depthOfCoverageWorkflow_0_1_0.input("bed", Bed)
depthOfCoverageWorkflow_0_1_0.input("reference", FastaWithDict)
depthOfCoverageWorkflow_0_1_0.input("outputprefix", String)

depthOfCoverageWorkflow_0_1_0.step(
    "gatk3depthofcoverage",
    GATK3DepthOfCoverageLatest(
        reference=depthOfCoverageWorkflow_0_1_0.reference,
        bam=depthOfCoverageWorkflow_0_1_0.bam,
        intervals=depthOfCoverageWorkflow_0_1_0.bed,
        countType="COUNT_FRAGMENTS_REQUIRE_SAME_BASE",
        summaryCoverageThreshold=[1, 50, 100, 300, 500],
        outputPrefix=depthOfCoverageWorkflow_0_1_0.outputprefix,
    ),
)

depthOfCoverageWorkflow_0_1_0.step(
    "addsymtodepthofcoverage",
    AddSymToDepthOfCoverageLatest(
        inputFile=depthOfCoverageWorkflow_0_1_0.gatk3depthofcoverage.sampleIntervalSummary,
        bed=depthOfCoverageWorkflow_0_1_0.bed,
        outputFilename=depthOfCoverageWorkflow_0_1_0.outputprefix,
    ),
)

depthOfCoverageWorkflow_0_1_0.output(
    "out", source=depthOfCoverageWorkflow_0_1_0.addsymtodepthofcoverage.out
)
