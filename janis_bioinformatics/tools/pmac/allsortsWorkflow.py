from janis_core import Directory, File, String, WorkflowMetadata, StringFormatter

from janis_bioinformatics.data_types import FastqGzPair

from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.pmac import GenerateCountsForALLSorts_0_1_2
from janis_bioinformatics.tools.star import StarAlignReads_2_5_3
from janis_bioinformatics.tools.subread import featureCounts_2_0_1
from janis_bioinformatics.tools.oshlack import AllSorts_0_1_0


class ALLSortsWorkflow_0_1_0(BioinformaticsWorkflow):
    def id(self) -> str:
        return "ALLSortsWorkflow"

    def friendly_name(self):
        return "ALLSorts Workflow"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def bind_metadata(self):
        return WorkflowMetadata(version="v0.1.0", contributors=["Jiaan Yu"])

    def constructor(self):

        self.input("sample_name", String)
        self.input("reads", FastqGzPair)
        self.input("genomeDir", Directory)
        self.input("gtf", File)

        self.step(
            "star",
            StarAlignReads_2_5_3(
                readFilesIn=self.reads,
                genomeDir=self.genomeDir,
                limitOutSJcollapsed=3000000,  # lots of splice junctions may need more than default 1M buffer
                readFilesCommand="zcat",
                outSAMtype=["BAM", "Unsorted"],
                outSAMunmapped="Within",
                outSAMattributes="Standard",
            ),
        )

        self.step(
            "featureCounts",
            featureCounts_2_0_1(
                bam=[self.star.out_bam.assert_not_null()],
                annotationFile=self.gtf,
                attributeType="gene_name",
            ),
        )

        # A script that transforms featurecounts output to allsorts input
        self.step(
            "transformation",
            GenerateCountsForALLSorts_0_1_2(
                inp=[self.featureCounts.out],
                type="featureCounts",
                samples=[self.sample_name],
            ),
        )

        self.step(
            "allsorts",
            AllSorts_0_1_0(samples=self.transformation.out, destination="."),
        )

        self.output(
            "out_gene_counts",
            source=self.featureCounts.out,
            output_name=StringFormatter(
                "{sample_name}_feature_counts", sample_name=self.sample_name
            ),
        )

        self.output(
            "out_predictions",
            source=self.allsorts.out_predictions,
            output_folder="allsorts",
            output_name=StringFormatter(
                "{sample_name}_predictions", sample_name=self.sample_name
            ),
        )

        self.output(
            "out_probabilities",
            source=self.allsorts.out_probabilities,
            output_folder="allsorts",
            output_name=StringFormatter(
                "{sample_name}_probabilities", sample_name=self.sample_name
            ),
        )

        self.output(
            "out_distributions",
            source=self.allsorts.out_distributions,
            output_folder="allsorts",
            output_name=StringFormatter(
                "{sample_name}_distributions", sample_name=self.sample_name
            ),
        )

        self.output(
            "out_waterfalls",
            source=self.allsorts.out_waterfalls,
            output_folder="allsorts",
            output_name=StringFormatter(
                "{sample_name}_waterfalls", sample_name=self.sample_name
            ),
        )


if __name__ == "__main__":
    ALLSortsWorkflow_0_1_0.translate("cwl")

