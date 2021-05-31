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
    StringFormatter,
    File,
    Double,
    CaptureType,
    get_value_for_hints_and_ordered_resource_tuple,
)
from typing import List, Dict, Any
from janis_bioinformatics.tools.facets.facets_base import FacetsBase

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.CHROMOSOME: 16,
            CaptureType.EXOME: 16,
            CaptureType.THIRTYX: 16,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class RunFacetsBase(FacetsBase, ABC):
    @classmethod
    def facets_command(cls):
        return "run-facets-wrapper.R"

    def tool(self):
        return "RunFacets"

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 64

    def inputs(self):
        return [
            ToolInput(
                "counts_file",
                File(),
                prefix="--counts-file",
                doc="Merged, gzipped tumor-normal output from snp-pileup",
            ),
            ToolInput(
                "outputPrefix",
                Filename(),
                prefix="--sample-id",
                doc="Sample ID, preferrable Tumor_Normal to keep track of the normal used",
            ),
            ToolInput(
                "directory",
                String(),
                prefix="--directory",
                default=".",
                doc="Output directory to which all output files are written",
            ),
            ToolInput(
                "everything",
                Boolean(optional=True),
                prefix="--everything",
                doc="Run full suite [default False]",
            ),
            ToolInput(
                "genome",
                String(optional=True),
                prefix="--genome",
                doc="Reference genome [default hg19]",
            ),
            ToolInput(
                "cval",
                Int(optional=True),
                prefix="--cval",
                doc="Segmentation parameter (cval) [default 50]",
            ),
            ToolInput(
                "purity_cval",
                Int(optional=True),
                prefix="--purity-cval",
                doc="If two pass, purity segmentation parameter (cval)",
            ),
            ToolInput(
                "min_nhet",
                Int(optional=True),
                prefix="--min-nhet",
                doc="Min. number of heterozygous SNPs required for clustering [default 15]",
            ),
            ToolInput(
                "purity_min_nhet",
                Int(optional=True),
                prefix="--purity-min-nhet",
                doc="If two pass, purity min. number of heterozygous SNPs (cval) [default 15]",
            ),
            ToolInput(
                "snp_window_size",
                Int(optional=True),
                prefix="--snp-window-size",
                doc="Window size for heterozygous SNPs [default 250]",
            ),
            ToolInput(
                "normal_depth",
                Int(optional=True),
                prefix="--normal-depth",
                doc="Min. depth in normal to keep SNPs [default 35]",
            ),
            ToolInput(
                "dipLogR",
                Double(optional=True),
                prefix="--dipLogR",
                doc="Manual dipLogR",
            ),
            ToolInput(
                "seed",
                Int(optional=True),
                prefix="--seed",
                doc="Manual seed value [default 100]",
            ),
            ToolInput(
                "legacy_output",
                Boolean(optional=True),
                prefix="--legacy-output",
                doc="create legacy output files (.RData and .cncf.txt) [default False]",
            ),
            ToolInput(
                "facets_lib_path",
                String(),
                prefix="--facets-lib-path",
                default="/usr/local/lib/R/site-library",
                doc="path to the facets library. if none provided, uses version available to library(facets)",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out_summary",
                File(),
                glob=InputSelector("outputPrefix") + ".txt",
            ),
            ToolOutput(
                "out_purity_png",
                File(),
                glob=InputSelector("outputPrefix") + "_purity.png",
            ),
            ToolOutput(
                "out_purity_seg",
                File(),
                glob=InputSelector("outputPrefix") + "_purity.seg",
            ),
            ToolOutput(
                "out_purity_rds",
                File(),
                glob=InputSelector("outputPrefix") + "_purity.rds",
            ),
            ToolOutput(
                "out_hisens_png",
                File(),
                glob=InputSelector("outputPrefix") + "_hisens.png",
            ),
            ToolOutput(
                "out_hisens_seg",
                File(),
                glob=InputSelector("outputPrefix") + "_hisens.seg",
            ),
            ToolOutput(
                "out_hisens_rds",
                File(),
                glob=InputSelector("outputPrefix") + "_hisens.rds",
            ),
            ToolOutput(
                "out_arm_level",
                File(optional=True),
                glob=InputSelector("outputPrefix") + ".arm_level.txt",
            ),
            ToolOutput(
                "out_gene_level",
                File(optional=True),
                glob=InputSelector("outputPrefix") + ".gene_level.txt",
            ),
            ToolOutput(
                "out_qc",
                File(optional=True),
                glob=InputSelector("outputPrefix") + ".qc.txt",
            ),
        ]

    def friendly_name(self):
        return "Facets: Make plot"

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
