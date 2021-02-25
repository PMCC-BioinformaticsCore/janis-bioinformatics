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

from janis_bioinformatics.data_types import CompressedVcf
from janis_bioinformatics.data_types.bam import File, BamBai
from janis_bioinformatics.tools.facets.facets_base import FacetsBase


class FacetsSnpPileupBase(FacetsBase, ABC):
    @classmethod
    def facets_command(cls):
        return "LD_LIBRARY_PATH=/opt/conda/lib /snp-pileup"

    def tool(self):
        return "FacetsSnpPileup"

    def inputs(self):
        return [
            ToolInput(
                "count_orphans",
                Boolean(optional=True),
                prefix="--count-orphans",
                position=2,
                doc="Do not discard anomalous read pairs",
            ),
            ToolInput(
                "ignore_overlaps",
                Boolean(optional=True),
                prefix="--ignore-overlaps",
                position=4,
                doc="Disable read-pair overlap detection.",
            ),
            ToolInput(
                "max_depth",
                Int(optional=True),
                prefix="--maxdepth=",
                position=6,
                separate_value_from_prefix=False,
                doc="Sets the maximum depth. Default is 4000.",
            ),
            ToolInput(
                "min_map_quality",
                Int(optional=True),
                prefix="--min-map-quality=",
                position=8,
                separate_value_from_prefix=False,
                doc="Sets the minimum threshold for mapping quality. Default is 0.",
            ),
            ToolInput(
                "min_base_quality",
                Int(optional=True),
                prefix="--min-base-quality=",
                position=10,
                separate_value_from_prefix=False,
                doc="Sets the minimum threshold for base quality. Default is 0.",
            ),
            ToolInput(
                "min_read_counts",
                Array(Int(), optional=True),
                separator=",",
                prefix="--min-read-counts=",
                separator=",",
                position=12,
                separate_value_from_prefix=False,
                doc="Comma separated list of minimum read counts for a position to be output. Default is 0.",
            ),
            ToolInput(
                "gzip",
                Boolean(optional=True),
                prefix="--gzip",
                position=14,
                doc="Compresses the output file with BGZF.",
            ),
            ToolInput(
                "pseudo_snps",
                String(optional=True),
                prefix="--pseudo-snps=",
                position=16,
                separate_value_from_prefix=False,
                doc="Every MULTIPLE positions, if there is no SNP,"
                "insert a blank record with the total count at the"
                "position.",
            ),
            ToolInput("vcf_file", CompressedVcf(), position=18),
            ToolInput("output_filename", Filename(extension=".csv.gz"), position=19),
            ToolInput("normal", BamBai(), position=20),
            ToolInput("tumour", BamBai(), position=21),
        ]

    def outputs(self):
        return [ToolOutput("out", File(), glob=InputSelector("output_filename"))]

    def friendly_name(self):
        return "Facets: snp-pileup"

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
