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
)

from janis_bioinformatics.data_types.bam import File
from janis_bioinformatics.tools.facets.facets_base import FacetsBase


class FacetsPlotBase(FacetsBase, ABC):
    @classmethod
    def facets_command(cls):
        return "Rscript /facets.R"

    def tool(self):
        return "FacetsPlot"

    def inputs(self):
        return [
            ToolInput("outputFilename", String(), position=3),
            ToolInput("pileup_file", File(), position=4),
            ToolInput("min_normal_depth", Int(), default=10, position=5),
            ToolInput("cval", Int(), default=150, position=6),
            ToolInput("maxiter", Int(), default=10, position=7),
            ToolInput("seed_initial", Int(), default=42, position=8),
            ToolInput("seed_iterations", Int(), default=10, position=9),
        ]

    def outputs(self):
        return [ToolOutput("out", File(), glob=InputSelector("outputFilename"))]

    def friendly_name(self):
        return "Facets: Make plot"

    def bind_metadata(self):
        self.metadata = ToolMetadata(
            contributors=["mumbler", "evanwehi"],
            dateCreated=date(2019, 12, 16),
            dateUpdated=date(2019, 12, 16),
            institution="Vanallen Lab",
            doi="https://doi.org/10.1093/nar/gkw520",
            citation="Ronglai Shen, Venkatraman E. Seshan; FACETS: allele-specific copy number and clonal heterogeneity analysis tool for high-throughput DNA sequencing, Nucleic Acids Research, Volume 44, Issue 16, 19 September 2016, Pages e131,",
            keywords=["facets", "snp-pileup"],
            documentationUrl="https://github.com/vanallenlab/facets",
            documentation="""
      """.strip(),
        )
        return self.metadata

    def arguments(self):
        return []

    additional_inputs = []