from janis_core import String
from janis_core import WorkflowMetadata

# data types
from janis_bioinformatics.data_types import BamBai, Bed
from janis_unix.data_types import TextFile
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.bedtools import (
    BedToolsCoverageBedLatest,
    BedToolsIntersectBedLatest,
)
from janis_bioinformatics.tools.gatk4 import Gatk4CollectInsertSizeMetrics_4_1_2
from janis_bioinformatics.tools.pmac import (
    PerformanceSummaryLatest,
    GeneCoveragePerSampleLatest,
)
from janis_bioinformatics.tools.samtools import (
    SamToolsFlagstatLatest,
    SamToolsViewLatest,
)


class PerformanceSummaryTargeted_0_1_0(BioinformaticsWorkflow):
    def id(self) -> str:
        return "PerformanceSummaryTargeted"

    def friendly_name(self):
        return "Performance summary workflow (targeted bed)"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def bind_metadata(self):
        return WorkflowMetadata(version="v0.1.0", contributors=["Jiaan Yu"])

    def constructor(self):

        # Inputs
        self.input("bam", BamBai)
        self.input("genecoverage_bed", Bed)
        self.input("region_bed", Bed)
        self.input("sample_name", String)
        self.input("genome_file", TextFile)
        # Steps
        # Add a step to remove secondary alignments
        self.step(
            "rmsecondaryalignments",
            SamToolsViewLatest(sam=self.bam, doNotOutputAlignmentsWithBitsSet="0x100"),
        )

        self.step(
            "gatk4collectinsertsizemetrics",
            Gatk4CollectInsertSizeMetrics_4_1_2(bam=self.rmsecondaryalignments,),
        )
        self.step(
            "bamflagstat", SamToolsFlagstatLatest(bam=self.rmsecondaryalignments.out)
        )
        self.step(
            "samtoolsview",
            SamToolsViewLatest(
                sam=self.rmsecondaryalignments.out,
                doNotOutputAlignmentsWithBitsSet="0x400",
            ),
        )
        self.step("rmdupbamflagstat", SamToolsFlagstatLatest(bam=self.samtoolsview.out))
        self.step(
            "bedtoolsintersectbed",
            BedToolsIntersectBedLatest(
                inputABam=self.samtoolsview.out,
                inputBBed=self.region_bed,
                genome=self.genome_file,
                sorted=True,
            ),
        )
        self.step(
            "targetbamflagstat",
            SamToolsFlagstatLatest(bam=self.bedtoolsintersectbed.out),
        )
        self.step(
            "bedtoolscoveragebed",
            BedToolsCoverageBedLatest(
                inputABed=self.region_bed,
                inputBBam=self.bedtoolsintersectbed.out,
                genome=self.genome_file,
                sorted=True,
                histogram=True,
            ),
        )
        # Give all the output files to performance summary script
        self.step(
            "performancesummary",
            PerformanceSummaryLatest(
                flagstat=self.bamflagstat.out,
                collectInsertSizeMetrics=self.gatk4collectinsertsizemetrics.out,
                targetFlagstat=self.targetbamflagstat.out,
                coverage=self.bedtoolscoveragebed.out,
                rmdupFlagstat=self.rmdupbamflagstat.out,
                outputPrefix=self.sample_name,
            ),
        )

        # Steps - Gene Coverage
        self.step(
            "bedtoolscoverage",
            BedToolsCoverageBedLatest(
                inputABed=self.genecoverage_bed,
                inputBBam=self.samtoolsview.out,
                genome=self.genome_file,
                sorted=True,
                histogram=True,
            ),
        )
        self.step(
            "genecoverage",
            GeneCoveragePerSampleLatest(
                sampleName=self.sample_name,
                bedtoolsOutputPath=self.bedtoolscoverage.out,
            ),
        )

        # Outputs
        self.output("out", source=self.performancesummary.out)
        self.output("geneFileOut", source=self.genecoverage.geneFileOut)
        self.output("regionFileOut", source=self.genecoverage.regionFileOut)
