from datetime import date

from janis_core import (
    ToolInput,
    Int,
    Float,
    Boolean,
    String,
    ToolOutput,
    Filename,
    File,
    InputSelector,
    ToolArgument,
    CaptureType,
    CpuSelector,
    Array,
    StringFormatter,
    ToolMetadata,
    WorkflowMetadata,
)

# data types
from janis_bioinformatics.data_types import BamBai, Bed
from janis_bioinformatics.tools import BioinformaticsWorkflow

from janis_bioinformatics.tools.facets import (
    FacetsSnpPileup_0_5_14_2,
    FacetsPlot_0_5_14_2,
)


class FacestWorkflow(BioinformaticsWorkflow):
    def id(self) -> str:
        return "FacetsWorkflow"

    def friendly_name(self):
        return "Facets workflow"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def bind_metadata(self):
        return WorkflowMetadata(
            version="v0.1.0",
            contributors=["Jiaan Yu"],
            dateCreated=date(2021, 2, 25),
            dateUpdated=date(2021, 2, 25),
        )

    def constructor(self):
        self.input("normal_bam", BamBai)
        self.input("tumour_bam", BamBai)
        self.input("normal_id", String)
        self.input("tumour_id", String)
        self.input("common_snp_vcf", File)

        # optional
        self.input("gzip", Boolean, default=True)
        self.input("min_map_quality", Int, default=30)
        self.input("min_base_quality", Int, default=30)
        self.input("min_read_counts", Array(Int), default=[10, 0])
        self.input("min_normal_depth", Int, default=10)
        self.input("cval", Int, default=150)
        self.input("maxiter", Int, default=10)
        self.input("seed_initial", Int, default=42)
        self.input("seed_iterations", Int, default=10)

        self.add_snp_pileup()
        self.add_plot()

    def add_snp_pileup(self):
        self.step(
            "snp_pileup",
            FacetsSnpPileup_0_5_14_2(
                normal=self.normal_bam,
                tumour=self.tumour_bam,
                output_filename=StringFormatter(
                    "{tumour}--{normal}_coverage.csv.gz", tumour=self.tumour_id, normal=self.normal_id
                ),
                vcf_file=self.common_snp_vcf,
                gzip=self.gzip,
                min_map_quality=self.min_map_quality,
                min_base_quality=self.min_base_quality,
                min_read_counts=self.min_read_counts,
            ),
        )

    def add_plot(self):
        self.step(
            "facets_plot",
            FacetsPlot_0_5_14_2(
                outputPrefix=StringFormatter(
                    "{tumour}--{normal}", tumour=self.tumour_id, normal=self.normal_id
                ),
                pileup_file=self.snp_pileup.out,
                min_normal_depth=self.min_normal_depth,
                cval=self.cval,
                maxiter=self.maxiter,
                seed_initial=self.seed_initial,
                seed_iterations=self.seed_iterations,
            ),
        )
        # self.output(
        #     "genome_segments_plot",
        #     source=self.facets_plot.out_genome_segments,
        #     output_folder="facets",
        #     output_name=StringFormatter(
        #         "{tumour}--{normal}.genome_segments.pdf",
        #         tumour=self.tumour_id,
        #         normal=self.normal_id,
        #     ),
        # )

        # self.output(
        #     "diagnostic_plot",
        #     source=self.facets_plot.out_diagnostic_plot,
        #     output_folder="facets",
        #     output_name=StringFormatter(
        #         "{tumour}--{normal}.diagnostic_plot.pdf",
        #         tumour=self.tumour_id,
        #         normal=self.normal_id,
        #     ),
        # )


if __name__ == "__main__":
    FacestWorkflow().translate("wdl")

