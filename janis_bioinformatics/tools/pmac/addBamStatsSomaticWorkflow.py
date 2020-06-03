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


class AddBamStatsSomatic_0_1_0(BioinformaticsWorkflow):
    def id(self) -> str:
        return "AddBamStatsSomatic"

    def friendly_name(self):
        return "Annotate Bam Stats to Somatic Vcf Workflow"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def bind_metadata(self):
        return WorkflowMetadata(version="v0.1.0", contributors=["Jiaan Yu"])

    def constructor(self):

        self.input("normal_id", String)
        self.input("tumor_id", String)
        self.input("normal_bam", BamBai)
        self.input("tumor_bam", BamBai)
        self.input("vcf", Vcf)

        self.step(
            "tumor", self.process_subpipeline(vcf=self.vcf, bam=self.tumor_bam,),
        )

        self.step(
            "normal", self.process_subpipeline(vcf=self.vcf, bam=self.normal_bam,),
        )

        self.step(
            "addbamstats",
            AddBamStatsLatest(
                inputVcf=self.vcf,
                tumorMpileup=self.tumor.out,
                normalMpileup=self.normal.out,
                normalID=self.normal_id,
                tumorID=self.tumor_id,
                type="somatic",
                outputFilename="out.vcf",
            ),
        )

        self.output(
            "out",
            source=self.addbamstats.out,
            output_folder="vcf",
            output_name="addbamstats",
        )

    @staticmethod
    def process_subpipeline(**connections):
        w = WorkflowBuilder("somatic_subpipeline")
        w.input("vcf", Vcf)
        w.input("bam", BamBai)
        w.step(
            "samtools_mpileup",
            SamToolsMpileupLatest(
                bam=w.bam,
                positions=w.vcf,
                countOrphans=True,
                noBAQ=True,
                minBQ=0,
                maxDepth=10000,
            ),
        )
        w.output("out", source=w.samtools_mpileup.out)
        return w(**connections)
