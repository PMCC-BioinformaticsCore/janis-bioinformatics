from janis_core import WorkflowBuilder, WorkflowMetadata

# data types
from janis_bioinformatics.data_types import Vcf, BamBai

from janis_core import String

from janis_bioinformatics.tools import BioinformaticsWorkflow

from janis_bioinformatics.tools.bioinformaticstoolbase import (
    BioinformaticsWorkflowBuilder,
)
from janis_bioinformatics.tools.pmac import AddBamStatsLatest
from janis_bioinformatics.tools.samtools import SamToolsMpileupLatest


class AddBamStatsGermline_0_1_0(BioinformaticsWorkflow):
    def id(self) -> str:
        return "AddBamStatsGermline"

    def friendly_name(self):
        return "Annotate Bam Stats to Germline Vcf Workflow"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def bind_metadata(self):
        return WorkflowMetadata(version="v0.1.0", contributors=["Jiaan Yu"])

    def constructor(self):

        # self.input("sample_name", String)
        self.input("bam", BamBai)
        self.input("vcf", Vcf)

        self.step(
            "samtoolsmpileup",
            SamToolsMpileupLatest(
                bam=self.bam,
                positions=self.vcf,
                countOrphans=True,
                noBAQ=True,
                minBQ=0,
                maxDepth=10000,
            ),
        )

        self.step(
            "addbamstats",
            AddBamStatsLatest(
                inputVcf=self.vcf,
                mpileup=self.samtoolsmpileup.out,
                type="germline",
                outputFilename="out.vcf",
            ),
        )

        self.output("out", source=self.addbamstats.out, output_name="addbasmtats.vcf")
