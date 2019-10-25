from datetime import datetime

from janis_core import (
    ToolInput,
    Array,
    File,
    Boolean,
    Directory,
    String,
    Int,
    Filename,
    ToolMetadata,
)

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class MultiqcBase(BioinformaticsTool):
    def friendly_name(self) -> str:
        return "Multiqc"

    @staticmethod
    def tool_provider():
        return "MultiQC"

    @staticmethod
    def tool() -> str:
        return "MultiQC"

    @staticmethod
    def base_command():
        return ["multiqc"]

    def inputs(self):
        return [
            ToolInput(
                "directory",
                Directory,
                position=1,
                doc="searches a given directory for analysis logs and compiles a HTML report",
            ),
            ToolInput(
                tag="force",
                input_type=Boolean(optional=True),
                prefix="--force",
                separate_value_from_prefix=True,
                doc="(-f) Overwrite any existing reports",
            ),
            ToolInput(
                tag="dirs",
                input_type=String(optional=True),
                prefix="--dirs",
                separate_value_from_prefix=True,
                doc="(-d) Prepend directory to sample names",
            ),
            ToolInput(
                tag="dirsDepth",
                input_type=Int(optional=True),
                prefix="--dirs-depth",
                separate_value_from_prefix=True,
                doc="(-dd) Prepend [INT] directories to sample names. Negative number to take from start of path.",
            ),
            ToolInput(
                tag="fullnames",
                input_type=Boolean(optional=True),
                prefix="--fullnames",
                separate_value_from_prefix=True,
                doc="(-s) Do not clean the sample names (leave as full file name)",
            ),
            ToolInput(
                tag="title",
                input_type=String(optional=True),
                prefix="--title",
                separate_value_from_prefix=True,
                doc="(-i) Report title. Printed as page header, used for filename if not otherwise specified.",
            ),
            ToolInput(
                tag="comment",
                input_type=String(optional=True),
                prefix="--comment",
                separate_value_from_prefix=True,
                doc="(-b) Custom comment, will be printed at the top of the report.",
            ),
            ToolInput(
                tag="filename",
                input_type=Filename(),
                prefix="--filename",
                separate_value_from_prefix=True,
                doc="(-n) Report filename. Use 'stdout' to print to standard out.",
            ),
            ToolInput(
                tag="outdir",
                input_type=Filename(),
                prefix="--outdir",
                separate_value_from_prefix=True,
                doc="(-o) Create report in the specified output directory.",
            ),
            ToolInput(
                tag="template",
                input_type=String(optional=True),
                prefix="--template",
                separate_value_from_prefix=True,
                doc="(-t)  Report template to use.",
            ),
            ToolInput(
                tag="tag",
                input_type=String(optional=True),
                prefix="--tag",
                separate_value_from_prefix=True,
                doc="Use only modules which tagged with this keyword, eg. RNA",
            ),
            ToolInput(
                tag="view_tags",
                input_type=Boolean(optional=True),
                prefix="--view_tags",
                separate_value_from_prefix=True,
                doc="(--view-tags) View the available tags and which modules they load",
            ),
            ToolInput(
                tag="ignore",
                input_type=Boolean(optional=True),
                prefix="--ignore",
                separate_value_from_prefix=True,
                doc="(-x) Ignore analysis files (glob expression)",
            ),
            ToolInput(
                tag="ignoreSamples",
                input_type=Boolean(optional=True),
                prefix="--ignore-samples",
                separate_value_from_prefix=True,
                doc="Ignore sample names (glob expression)",
            ),
            ToolInput(
                tag="ignoreSymlinks",
                input_type=Boolean(optional=True),
                prefix="--ignore-symlinks",
                separate_value_from_prefix=True,
                doc="Ignore symlinked directories and files",
            ),
            ToolInput(
                tag="sampleNames",
                input_type=File(optional=True),
                prefix="--sample-names",
                separate_value_from_prefix=True,
                doc="File containing alternative sample names",
            ),
            # mfranklin: Containers don't bind in any extra files except for the ones you specify,
            #               so a file that lists extra files doesn't do anything
            # ToolInput(
            #     tag="fileList",
            #     input_type=String(optional=True),
            #     prefix="--file-list",
            #     separate_value_from_prefix=True,
            #     doc="(-l) Supply a file containing a list of file paths to be searched, one per row",
            # ),
            ToolInput(
                tag="exclude",
                input_type=Array(String, optional=True),
                prefix="--exclude",
                separate_value_from_prefix=True,
                prefix_applies_to_all_elements=True,
                doc="(-e) Do not use this module. Can specify multiple times.",
            ),
            ToolInput(
                tag="module",
                input_type=Array(String, optional=True),
                prefix="--module",
                separate_value_from_prefix=True,
                prefix_applies_to_all_elements=True,
                doc="(-m) Use only this module. Can specify multiple times.",
            ),
            ToolInput(
                tag="dataDir",
                input_type=Boolean(optional=True),
                prefix="--data-dir",
                separate_value_from_prefix=True,
                doc="Force the parsed data directory to be created.",
            ),
            ToolInput(
                tag="noDataDir",
                input_type=Boolean(optional=True),
                prefix="--no-data-dir",
                separate_value_from_prefix=True,
                doc="Prevent the parsed data directory from being created.",
            ),
            ToolInput(
                tag="dataFormat",
                input_type=String(optional=True),
                prefix="--data-format",
                separate_value_from_prefix=True,
                doc="(-k)  Output parsed data in a different format. Default: tsv",
            ),
            # ToolInput(
            #     tag="zipDataDir",
            #     input_type=Boolean(optional=True),
            #     prefix="--zip-data-dir",
            #     separate_value_from_prefix=True,
            #     doc="(-z) Compress the data directory.",
            # ),
            ToolInput(
                tag="export",
                input_type=Boolean(optional=True),
                prefix="--export",
                separate_value_from_prefix=True,
                doc="(-p) Export plots as static images in addition to the report",
            ),
            ToolInput(
                tag="flat",
                input_type=Boolean(optional=True),
                prefix="--flat",
                separate_value_from_prefix=True,
                doc="(-fp) Use only flat plots (static images)",
            ),
            ToolInput(
                tag="interactive",
                input_type=Boolean(optional=True),
                prefix="--interactive",
                separate_value_from_prefix=True,
                doc="(-ip) Use only interactive plots (HighCharts Javascript)",
            ),
            ToolInput(
                tag="lint",
                input_type=Boolean(optional=True),
                prefix="--lint",
                separate_value_from_prefix=True,
                doc="Use strict linting (validation) to help code development",
            ),
            ToolInput(
                tag="pdf",
                input_type=Boolean(optional=True),
                prefix="--pdf",
                separate_value_from_prefix=True,
                doc="Creates PDF report with 'simple' template. Requires Pandoc to be installed.",
            ),
            ToolInput(
                tag="noMegaqcUpload",
                input_type=Boolean(optional=True),
                prefix="--no-megaqc-upload",
                separate_value_from_prefix=True,
                doc="Don't upload generated report to MegaQC, even if MegaQC options are found",
            ),
            ToolInput(
                tag="config",
                input_type=File(optional=True),
                prefix="--config",
                separate_value_from_prefix=True,
                doc="(-c) Specific config file to load, after those in MultiQC dir / home dir / working dir.",
            ),
            ToolInput(
                tag="cl_config",
                input_type=File(optional=True),
                prefix="--cl_config",
                separate_value_from_prefix=True,
                doc="(--cl-config) Specify MultiQC config YAML on the command line",
            ),
            ToolInput(
                tag="verbose",
                input_type=Boolean(optional=True),
                prefix="--verbose",
                separate_value_from_prefix=True,
                doc="(-v) Increase output verbosity.",
            ),
            ToolInput(
                tag="quiet",
                input_type=Boolean(optional=True),
                prefix="--quiet",
                separate_value_from_prefix=True,
                doc="(-q) Only show log warnings",
            ),
            # ToolInput(
            #     tag="version",
            #     input_type=String(optional=True),
            #     prefix="--version",
            #     separate_value_from_prefix=True,
            #     doc="Show the version and exit.",
            # ),
            # ToolInput(
            #     tag="help",
            #     input_type=String(optional=True),
            #     prefix="--help",
            #     separate_value_from_prefix=True,
            #     doc="(-h) Show this message and exit.",
            # ),
        ]

    def outputs(self):
        return []

    def metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=datetime.fromisoformat("2019-10-24T12:59:09.125482"),
            dateUpdated=datetime.fromisoformat("2019-10-24T12:59:09.125491"),
            documentationUrl="http://multiqc.info",
            documentation="""Usage: multiqc [OPTIONS] <analysis directory>
MultiQC aggregates results from bioinformatics analyses across many samples into a single report.
It searches a given directory for analysis logs and compiles a HTML report. It's a general use tool, 
perfect for summarising the output from numerous bioinformatics tools.
To run, supply with one or more directory to scan for analysis results. To run here, use 'multiqc .'

Author: Phil Ewels (http://phil.ewels.co.uk)
""",
        )
