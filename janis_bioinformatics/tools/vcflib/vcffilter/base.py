from abc import ABC

from janis_core import (
    ToolInput,
    String,
    Int,
    ToolOutput,
    Float,
    Stdout,
    ToolMetadata,
    InputDocumentation,
    Boolean,
    Array,
)

from janis_bioinformatics.data_types import CompressedVcf, BedTabix
from janis_bioinformatics.data_types import Vcf
from janis_bioinformatics.tools.vcflib.vcflibtoolbase import VcfLibToolBase


class VcfFilterBase(VcfLibToolBase, ABC):
    def tool(self):
        return "vcffilter"

    def friendly_name(self):
        return "VcfLib: Vcf Filter"

    def base_command(self):
        return "vcffilter"

    def inputs(self):
        return [
            ToolInput("vcf", Vcf, position=1, doc="VCF to filter",),
            ToolInput(
                tag="info_filter",
                input_type=String(optional=True),
                prefix="--info-filter",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-f) specifies a filter to apply to the info fields of records, "
                    "removes alleles which do not pass the filter"
                ),
            ),
            ToolInput(
                tag="genotype_filter",
                input_type=String(optional=True),
                prefix="--genotype-filter",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-g) specifies a filter to apply to the genotype fields of records"
                ),
            ),
            ToolInput(
                tag="keep_info",
                input_type=Boolean(optional=True),
                prefix="--keep-info",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-k) used in conjunction with '-g', keeps variant info, but removes genotype"
                ),
            ),
            ToolInput(
                tag="filter_sites",
                input_type=Boolean(optional=True),
                prefix="--filter-sites",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-s) filter entire records, not just alleles"
                ),
            ),
            ToolInput(
                tag="tag_pass",
                input_type=String(optional=True),
                prefix="--tag-pass",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-t) tag vcf records as positively filtered with this tag, print all records"
                ),
            ),
            ToolInput(
                tag="tag_fail",
                input_type=String(optional=True),
                prefix="--tag-fail",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-F) tag vcf records as negatively filtered with this tag, print all records"
                ),
            ),
            ToolInput(
                tag="append_filter",
                input_type=Boolean(optional=True),
                prefix="--append-filter",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-A) append the existing filter tag, don't just replace it"
                ),
            ),
            ToolInput(
                tag="allele_tag",
                input_type=String(optional=True),
                prefix="--allele-tag",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-a) apply -t on a per-allele basis. adds or sets the corresponding INFO field tag"
                ),
            ),
            ToolInput(
                tag="invert",
                input_type=Boolean(optional=True),
                prefix="--invert",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-v) inverts the filter, e.g. grep -v"),
            ),
            ToolInput(
                tag="use_logical_or",
                input_type=Boolean(optional=True),
                prefix="--or",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-o) use logical OR instead of AND to combine filters"
                ),
            ),
            ToolInput(
                tag="region",
                input_type=Array(BedTabix, optional=True),
                prefix="--region",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-r) specify a region on which to target the filtering, requires a BGZF compressed file "
                    "which has been indexed with tabix.  any number of regions may be specified."
                ),
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", Stdout(Vcf), doc="Filtered VCF",)]

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=date(2020, 6, 4),
            dateUpdated=date(2020, 6, 4),
            institution=None,
            doi=None,
            citation=None,
            keywords=["vcflib", "filter"],
            documentationUrl="https://github.com/vcflib/vcflib",
            documentation="""\
Filter the specified vcf file using the set of filters.
Filters are specified in the form "<ID> <operator> <value>:
 -f "DP > 10"  # for info fields
 -g "GT = 1|1" # for genotype fields
 -f "CpG"  # for 'flag' fields

Operators can be any of: =, !, <, >, |, &

Any number of filters may be specified.  They are combined via logical AND
unless --or is specified on the command line.  Obtain logical negation through
the use of parentheses, e.g. "! ( DP = 10 )"

For convenience, you can specify "QUAL" to refer to the quality of the site, even
though it does not appear in the INFO fields.""",
        )
