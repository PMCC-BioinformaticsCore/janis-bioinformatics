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
    FacetsSnpPileup_2_0_8,
    RunFacets_2_0_8,
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
        self.input("pseudo_snps", Int(optional=True))
        self.input("max_depth", Int(optional=True))
        self.input("everything", Boolean(optional=True))
        self.input("genome", String(optional=True))
        self.input("cval", Int(optional=True))
        self.input("purity_cval", Int(optional=True))
        self.input("normal_depth", Int(optional=True))

        self.add_snp_pileup()
        self.add_run_facets()

    def add_snp_pileup(self):
        self.step(
            "snp_pileup",
            FacetsSnpPileup_2_0_8(
                normal_bam=self.normal_bam,
                tumor_bam=self.tumour_bam,
                output_prefix=StringFormatter(
                    "{tumour}--{normal}",
                    tumour=self.tumour_id,
                    normal=self.normal_id,
                ),
                vcf_file=self.common_snp_vcf,
                pseudo_snps=self.pseudo_snps,
                max_depth=self.max_depth,
            ),
        )

    def add_run_facets(self):
        self.step(
            "run_facets",
            RunFacets_2_0_8(
                counts_file=self.snp_pileup.out,
                outputPrefix=StringFormatter(
                    "{tumour}--{normal}", tumour=self.tumour_id, normal=self.normal_id
                ),
                directory=".",
                everything=self.everything,
                genome=self.genome,
                cval=self.cval,
                purity_cval=self.purity_cval,
                normal_depth=self.normal_depth,
            ),
        )

        self.output(
            "out_summary",
            source=self.run_facets.out_summary,
            output_folder="facets",
            output_name=StringFormatter(
                "{tumour}--{normal}.txt", tumour=self.tumour_id, normal=self.normal_id
            ),
        )
        self.output(
            "out_purity_png",
            source=self.run_facets.out_purity_png,
            output_folder="facets",
            output_name=StringFormatter(
                "{tumour}--{normal}_purity.png",
                tumour=self.tumour_id,
                normal=self.normal_id,
            ),
        ),
        self.output(
            "out_purity_seg",
            source=self.run_facets.out_purity_seg,
            output_folder="facets",
            output_name=StringFormatter(
                "{tumour}--{normal}_purity.seg",
                tumour=self.tumour_id,
                normal=self.normal_id,
            ),
        ),
        self.output(
            "out_purity_rds",
            source=self.run_facets.out_purity_rds,
            output_folder="facets",
            output_name=StringFormatter(
                "{tumour}--{normal}_purity.rds",
                tumour=self.tumour_id,
                normal=self.normal_id,
            ),
        ),
        self.output(
            "out_hisens_png",
            source=self.run_facets.out_hisens_png,
            output_folder="facets",
            output_name=StringFormatter(
                "{tumour}--{normal}_hisens.png",
                tumour=self.tumour_id,
                normal=self.normal_id,
            ),
        ),
        self.output(
            "out_hisens_seg",
            source=self.run_facets.out_hisens_seg,
            output_folder="facets",
            output_name=StringFormatter(
                "{tumour}--{normal}_hisens.seg",
                tumour=self.tumour_id,
                normal=self.normal_id,
            ),
        ),
        self.output(
            "out_hisens_rds",
            source=self.run_facets.out_hisens_rds,
            output_folder="facets",
            output_name=StringFormatter(
                "{tumour}--{normal}_hisens.rds",
                tumour=self.tumour_id,
                normal=self.normal_id,
            ),
        ),
        self.output(
            "out_arm_level",
            source=self.run_facets.out_arm_level,
            output_folder="facets",
            output_name=StringFormatter(
                "{tumour}--{normal}.arm_level.txt",
                tumour=self.tumour_id,
                normal=self.normal_id,
            ),
        ),
        self.output(
            "out_gene_level",
            source=self.run_facets.out_gene_level,
            output_folder="facets",
            output_name=StringFormatter(
                "{tumour}--{normal}.gene_level.txt",
                tumour=self.tumour_id,
                normal=self.normal_id,
            ),
        ),
        self.output(
            "out_qc",
            source=self.run_facets.out_qc,
            output_folder="facets",
            output_name=StringFormatter(
                "{tumour}--{normal}.qc.txt",
                tumour=self.tumour_id,
                normal=self.normal_id,
            ),
        ),


if __name__ == "__main__":
    FacestWorkflow().translate("wdl")
