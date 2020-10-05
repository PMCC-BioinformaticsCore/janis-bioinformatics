from janis_core import WorkflowBuilder, WorkflowMetadata

# data types
from janis_bioinformatics.data_types import BamBai, Bed, FastaWithDict
from janis_core import String

from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bioinformaticstoolbase import (
    BioinformaticsWorkflowBuilder,
)
from janis_bioinformatics.tools.gatk3 import GATK3DepthOfCoverageLatest
from janis_bioinformatics.tools.pmac import AddSymToDepthOfCoverageLatest


class AnnotateDepthOfCoverage_0_1_0(BioinformaticsWorkflow):
    def id(self) -> str:
        return "AnnotateDepthOfCoverage"

    def friendly_name(self):
        return "Annotate GATK3 DepthOfCoverage Workflow"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def bind_metadata(self):
        return WorkflowMetadata(version="v0.1.0", contributors=["Jiaan Yu"])

    def constructor(self):

        self.input("bam", BamBai)
        self.input("bed", Bed)
        self.input("reference", FastaWithDict)
        # self.input("outputprefix", String)
        self.input("sample_name", String)

        self.step(
            "gatk3depthofcoverage",
            GATK3DepthOfCoverageLatest(
                reference=self.reference,
                bam=self.bam,
                intervals=self.bed,
                countType="COUNT_FRAGMENTS_REQUIRE_SAME_BASE",
                summaryCoverageThreshold=[1, 50, 100, 300, 500],
                outputPrefix=self.sample_name,
            ),
        )

        self.step(
            "addsymtodepthofcoverage",
            AddSymToDepthOfCoverageLatest(
                inputFile=self.gatk3depthofcoverage.sampleIntervalSummary,
                bed=self.bed,
                outputFilename=self.sample_name,
            ),
        )

        self.output(
            "out", source=self.addsymtodepthofcoverage.out, output_name=self.sample_name
        )

        self.output(
            "out_sample_summary", source=self.gatk3depthofcoverage.sampleSummary, output_name=self.sample_name
        )
