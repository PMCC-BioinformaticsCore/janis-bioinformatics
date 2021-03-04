from abc import ABC
from datetime import date

from janis_core import (
    ToolInput,
    ToolOutput,
    Int,
    String,
    Boolean,
    Filename,
    InputSelector,
    ToolMetadata,
    Array,
    File,
)

from janis_bioinformatics.data_types.bam import BamBai
from janis_bioinformatics.tools.facets.facets_base import FacetsBase


class FacetsSnpPileupBase(FacetsBase, ABC):
    @classmethod
    def facets_command(cls):
        return "snp-pileup-wrapper.R"

    def tool(self):
        return "FacetsSnpPileup"

    def inputs(self):
        return [
            ToolInput(
                "vcf_file",
                File(),
                prefix="--vcf-file",
                doc="Path to VCF file containing SNP positions",
            ),
            ToolInput(
                "normal_bam",
                BamBai(),
                prefix="--normal-bam",
                doc="Path to normal sample BAM file",
            ),
            ToolInput(
                "tumor_bam",
                BamBai(),
                prefix="--tumor-bam",
                doc="Path to tumor sample BAM file",
            ),
            ToolInput(
                "output_prefix",
                Filename(),
                prefix="--output-prefix",
                doc="Path to VCF file containing SNP positions",
            ),
            ToolInput(
                "pseudo_snps",
                Int(optional=True),
                prefix="--pseudo-snps",
                doc="Do pileup at every p:th position [default %(default)s]",
            ),
            ToolInput(
                "max_depth",
                Int(optional=True),
                prefix="--max-depth",
                doc="Maximum read depth [default %(default)s]",
            )
            # ToolInput(
            #     "snp-pileup-path", String(optional=True), prefix="--snp-pileup-path"
            # ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out", File(), glob=InputSelector("output_prefix") + ".snp_pileup.gz"
            )
        ]

    def friendly_name(self):
        return "Facets: snp-pileup"

    def bind_metadata(self):
        self.metadata = ToolMetadata(
            contributors=["mumbler", "evanwehi", "Jiaan Yu"],
            dateCreated=date(2019, 12, 16),
            dateUpdated=date(2021, 3, 4),
            institution="Memorial Sloan Kettering Cancer Center",
            doi="https://doi.org/10.1093/nar/gkw520",
            citation="Ronglai Shen, Venkatraman E. Seshan; FACETS: allele-specific copy number and clonal heterogeneity analysis tool for high-throughput DNA sequencing, Nucleic Acids Research, Volume 44, Issue 16, 19 September 2016, Pages e131,",
            keywords=["facets", "snp-pileup"],
            documentationUrl="https://github.com/mskcc/facets-suite",
            documentation="""
      """.strip(),
        )
        return self.metadata

    def arguments(self):
        return []

    additional_inputs = []
