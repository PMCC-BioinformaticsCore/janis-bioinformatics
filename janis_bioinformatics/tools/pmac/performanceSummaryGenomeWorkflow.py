from janis_core import String
from janis_core import WorkflowMetadata

# data types
from janis_bioinformatics.data_types import BamBai, Bed
from janis_unix.data_types import TextFile
from janis_bioinformatics.tools import BioinformaticsWorkflow
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
        return WorkflowMetadata(version="v0.1.0", contributors=["Jiaan Yu"])

    def constructor(self):

        # Inputs
        self.input("bam", BamBai)
        self.input("bed", Bed)
        # Pending to multiple outputs with same prefix
        self.input("sample_name", String)
        self.input("genome_file", TextFile)

        # Steps - Performance Summary
        self.step(
            "gatk4collectinsertsizemetrics",
            Gatk4CollectInsertSizeMetricsLatest(bam=self.bam,),
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
                inputBam=self.samtoolsview.out, genome=self.genome_file, sorted=True,
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

        # Steps - Gene Coverage
        self.step(
            "bedtoolscoverage",
            BedToolsCoverageBedLatest(
                inputABed=self.bed,
                inputBBam=self.samtoolsview.out,
                histogram=True,
                genome=self.genome_file,
                sorted=True,
            ),
        )
        self.step(
            "genecoverage",
            GeneCoveragePerSampleLatest(
                sampleName=self.sample_name,
                bedtoolsOutputPath=self.bedtoolscoverage.out,
                genome=self.genome_file,
                sorted=True,
            ),
        )

        self.output("performanceSummaryOut", source=self.performancesummary.out)
        self.output("geneFileOut", source=self.genecoverage.geneFileOut)
        self.output("regionFileOut", source=self.genecoverage.regionFileOut)
