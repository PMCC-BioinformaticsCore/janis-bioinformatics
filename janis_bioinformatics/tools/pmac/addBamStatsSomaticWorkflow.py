import os
from datetime import datetime
from janis_core import WorkflowBuilder, WorkflowMetadata

# data types
from janis_core.tool.test_classes import TTestCase

from janis_bioinformatics.data_types import Vcf, BamBai
from janis_bioinformatics.data_types import FastaWithDict

from janis_core import String

from janis_bioinformatics.tools import BioinformaticsWorkflow

from janis_bioinformatics.tools.bioinformaticstoolbase import (
    BioinformaticsWorkflowBuilder,
    BioinformaticsTool,
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
        return WorkflowMetadata(
            version="v0.1.0",
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2020, 6, 4),
            dateUpdated=datetime(2020, 8, 10),
        )

    def constructor(self):

        self.input("normal_id", String)
        self.input("tumor_id", String)
        self.input("normal_bam", BamBai)
        self.input("tumor_bam", BamBai)
        self.input("reference", FastaWithDict)
        self.input("vcf", Vcf)

        self.step(
            "tumor",
            self.process_subpipeline(
                vcf=self.vcf,
                bam=self.tumor_bam,
                reference=self.reference,
            ),
        )

        self.step(
            "normal",
            self.process_subpipeline(
                vcf=self.vcf,
                bam=self.normal_bam,
                reference=self.reference,
            ),
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
        w = WorkflowBuilder("samtools_mpileup_subpipeline")
        w.input("vcf", Vcf)
        w.input("bam", BamBai)
        w.input("reference", FastaWithDict)
        w.step(
            "samtools_mpileup",
            SamToolsMpileupLatest(
                bam=w.bam,
                positions=w.vcf,
                reference=w.reference,
                countOrphans=True,
                noBAQ=True,
                minBQ=0,
                maxDepth=10000,
            ),
        )
        w.output("out", source=w.samtools_mpileup.out)
        return w(**connections)

    def tests(self):
        parent_dir = "https://swift.rc.nectar.org.au/v1/AUTH_4df6e734a509497692be237549bbe9af/janis-test-data/bioinformatics"
        germline_data = f"{parent_dir}/wgsgermline_data"
        somatic_data = f"{parent_dir}/wgssomatic_data"
        return [
            TTestCase(
                name="basic",
                input={
                    "normal_id": "NA24385-BRCA1",
                    "tumor_id": "NA12878-NA24385-mixture",
                    "normal_bam": f"{somatic_data}/NA24385-BRCA1.markduped.bam",
                    "tumor_bam": f"{somatic_data}/NA12878-NA24385-mixture.markduped.bam",
                    "reference": f"{germline_data}/Homo_sapiens_assembly38.chr17.fasta",
                    "vcf": f"{somatic_data}/uncompressed.stdout",
                },
                output=Vcf.basic_test(
                    "out",
                    44094,
                    156,
                    ["GATKCommandLine"],
                    "5fc0e861893e0a23f974808265a6917e",
                ),
            )
        ]
