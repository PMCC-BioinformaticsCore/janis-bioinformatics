from abc import ABC
from datetime import datetime

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool
from janis_core import (
    CommandTool,
    ToolInput,
    Array,
    File,
    Boolean,
    String,
    Filename,
    ToolMetadata,
    InputDocumentation,
    ToolOutput,
    InputSelector,
)
from janis_unix import TextFile


class FilterVepBase(BioinformaticsTool, ABC):
    def friendly_name(self) -> str:
        return "FilterVep"

    def tool_provider(self):
        return "Ensemble"

    def tool(self) -> str:
        return "FilterVep"

    def base_command(self):
        return ["filter_vep"]

    def inputs(self):
        return [
            ToolInput(
                tag="input_file",
                input_type=File(optional=True),
                prefix="--input_file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-i) Specify the input file (i.e. the VEP results file). If no input file is specified, the "
                    "script will attempt to read from STDIN. Input may be gzipped - to force the script to read "
                    "a file as gzipped, use --gz"
                ),
            ),
            ToolInput(
                tag="format",
                input_type=String(optional=True),
                prefix="--format",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="[vcf|tab] Specify input file format (tab for any tab-delimited format,"
                    " including default VEP output format)"
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(extension=".txt"),
                prefix="--output_file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-o) Specify the output file to write to. If no output file is specified, "
                    "the script will write to STDOUT"
                ),
            ),
            ToolInput(
                tag="force_overwrite",
                input_type=Boolean(optional=True),
                prefix="--force_overwrite",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Force the script to overwrite the output file if it already exists"
                ),
            ),
            ToolInput(
                tag="filter",
                input_type=Array(String, optional=True),
                prefix="--filter",
                separate_value_from_prefix=True,
                prefix_applies_to_all_elements=True,
                doc=InputDocumentation(
                    doc="(-f) Add filter. Multiple --filter flags may be used, and are "
                    "treated as logical ANDs, i.e. all filters must pass for a line to be printed"
                ),
            ),
            ToolInput(
                tag="list",
                input_type=Array(String, optional=True),
                prefix="--list",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-l) List allowed fields from the input file"
                ),
            ),
            ToolInput(
                tag="count",
                input_type=Boolean(optional=True),
                prefix="--count",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-c) Print only a count of matched lines"),
            ),
            ToolInput(
                tag="only_matched",
                input_type=Boolean(optional=True),
                prefix="--only_matched",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="In VCF files, the CSQ field that contains the consequence data will often "
                    "contain more than  one 'block' of consequence data, where each block corresponds "
                    "to a variant/feature overlap. Using  filters. By default, the script prints out the "
                    "entire VCF line if any of the blocks pass the filters."
                ),
            ),
            ToolInput(
                tag="vcf_info_field",
                input_type=String(optional=True),
                prefix="--vcf_info_field",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="With VCF input files, by default filter_vep expects to find VEP annotations encoded in the"
                    " CSQ INFO key; VEP itself can be configured to write to a different key (with the equivalent "
                    "--vcf_info_field flag). Use this flag to change the INFO key VEP expects to decode."
                ),
            ),
            ToolInput(
                tag="ontology",
                input_type=Boolean(optional=True),
                prefix="--ontology",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-y) Use Sequence Ontology to match consequence terms. Use with operator 'is' to match "
                    "against all child terms of your value. e.g. 'Consequence is coding_sequence_variant' "
                    "will match missense_variant, synonymous_variant etc. Requires database connection; "
                    "defaults to connecting to ensembldb.ensembl.org. Use --host, --port, --user, --version) "
                    "connection parameters."
                ),
            ),
            ToolInput(
                tag="help",
                input_type=Boolean(optional=True),
                prefix="--help",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="-h Print usage message and exit"),
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", TextFile, glob=InputSelector("outputFilename"))]

    def metadata(self):
        return ToolMetadata(
            contributors=[],
            dateCreated=datetime(2020, 5, 26),
            dateUpdated=datetime(2020, 5, 26),
            documentation="#------------#\n# filter_vep #\n#------------#\nhttp://www.ensembl.org/info/docs/tools/vep/script/vep_filter.html\n",
        )
