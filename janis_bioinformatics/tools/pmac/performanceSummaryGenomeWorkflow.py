import os
from datetime import datetime
from janis_core import String
from janis_core import WorkflowMetadata

# data types
from janis_core.tool.test_classes import TTestCase

from janis_bioinformatics.data_types import BamBai, Bed
from janis_unix.data_types import TextFile
from janis_bioinformatics.tools import BioinformaticsWorkflow, BioinformaticsTool
from janis_bioinformatics.tools.bedtools import (
    BedToolsGenomeCoverageBedLatest,
    BedToolsCoverageBedLatest,
)
from janis_bioinformatics.tools.gatk4 import Gatk4CollectInsertSizeMetricsLatest
from janis_bioinformatics.tools.pmac import (
    PerformanceSummaryLatest,
    GeneCoveragePerSampleLatest,
)
from janis_bioinformatics.tools.samtools import (
    SamToolsFlagstatLatest,
    SamToolsViewLatest,
)


class PerformanceSummaryGenome_0_1_0(BioinformaticsWorkflow):
    def id(self) -> str:
        return "PerformanceSummaryGenome"

    def friendly_name(self):
        return "Performance summary workflow (whole genome)"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def bind_metadata(self):
        return WorkflowMetadata(
            version="v0.1.0",
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2020, 4, 28),
            dateUpdated=datetime(2020, 6, 12),
        )

    def constructor(self):

        # Inputs
        self.input("bam", BamBai)
        # Pending to multiple outputs with same prefix
        self.input("sample_name", String)
        self.input("genome_file", TextFile)

        # Steps - Performance Summary
        self.step(
            "gatk4collectinsertsizemetrics",
            Gatk4CollectInsertSizeMetricsLatest(
                bam=self.bam,
            ),
        )
        self.step("bamflagstat", SamToolsFlagstatLatest(bam=self.bam))
        self.step(
            "samtoolsview",
            SamToolsViewLatest(sam=self.bam, doNotOutputAlignmentsWithBitsSet="0x400"),
        )
        self.step("rmdupbamflagstat", SamToolsFlagstatLatest(bam=self.samtoolsview.out))
        self.step(
            "bedtoolsgenomecoveragebed",
            BedToolsGenomeCoverageBedLatest(
                inputBam=self.samtoolsview.out,
                genome=self.genome_file,
            ),
        )
        # Give all the output files to performance summary script
        self.step(
            "performancesummary",
            PerformanceSummaryLatest(
                flagstat=self.bamflagstat.out,
                collectInsertSizeMetrics=self.gatk4collectinsertsizemetrics.out,
                coverage=self.bedtoolsgenomecoveragebed.out,
                rmdupFlagstat=self.rmdupbamflagstat.out,
                genome=True,
                outputPrefix=self.sample_name,
            ),
        )

        self.output("performanceSummaryOut", source=self.performancesummary.out)

    def tests(self):
        return [
            TTestCase(
                name="basic",
                input={
                    "bam": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.markduped.bam",
                    ),
                    "genome_file": os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1.genome_file.txt",
                    ),
                    "sample_name": "NA12878-BRCA1",
                    "samtoolsview_doNotOutputAlignmentsWithBitsSet": "0x400",
                    "performancesummary_genome": True,
                },
                output=TextFile.basic_test(
                    tag="performanceSummaryOut",
                    min_size=948,
                    line_count=2,
                    md5="575354942cfb8d0367725f9020181443",
                    expected_file_path=os.path.join(
                        BioinformaticsTool.test_data_path(),
                        "wgsgermline_data",
                        "NA12878-BRCA1_performance_summary.csv",
                    ),
                ),
            )
        ]
