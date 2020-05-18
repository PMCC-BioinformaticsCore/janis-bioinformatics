from abc import ABC
from datetime import datetime
from janis_bioinformatics.tools.gatk4.gatk4toolbase import Gatk4ToolBase

from janis_core import (
    CommandTool,
    ToolInput,
    ToolOutput,
    File,
    Boolean,
    String,
    Int,
    Double,
    Float,
    InputSelector,
    Filename,
    ToolMetadata,
    InputDocumentation,
)


class GatkFilterIntervalsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "FilterIntervals"

    def friendly_name(self) -> str:
        return "GATK4: FilterIntervals"

    def tool(self) -> str:
        return "Gatk4FilterIntervals"

    def inputs(self):
        return [
            ToolInput(
                tag="intervals",
                input_type=String(optional=True),
                prefix="--intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-L) One or more genomic intervals over which to operate This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Output Picard interval-list file containing the filtered intervals. Required."
                ),
            ),
            ToolInput(
                tag="annotatedIntervals",
                input_type=File(optional=True),
                prefix="--annotated-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Input file containing annotations for genomic intervals (output of AnnotateIntervals). Must be provided if no counts files are provided.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="arguments_file",
                input_type=File(optional=True),
                prefix="--arguments_file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="read one or more arguments files and add them to the command line This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="excludeIntervals",
                input_type=Boolean(optional=True),
                prefix="--exclude-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-XL) This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="extremeCountFilterMaximumPercentile",
                input_type=Double(optional=True),
                prefix="--extreme-count-filter-maximum-percentile",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum-percentile parameter for the extreme-count filter.  Intervals with a count that has a percentile strictly greater than this in a percentage of samples strictly greater than extreme-count-filter-percentage-of-samples will be filtered out.  (This is the second count-based filter applied.)  Default value: 99.0. "
                ),
            ),
            ToolInput(
                tag="extremeCountFilterMinimumPercentile",
                input_type=Double(optional=True),
                prefix="--extreme-count-filter-minimum-percentile",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum-percentile parameter for the extreme-count filter.  Intervals with a count that has a percentile strictly less than this in a percentage of samples strictly greater than extreme-count-filter-percentage-of-samples will be filtered out.  (This is the second count-based filter applied.)  Default value: 1.0. "
                ),
            ),
            ToolInput(
                tag="extremeCountFilterPercentageOfSamples",
                input_type=Double(optional=True),
                prefix="--extreme-count-filter-percentage-of-samples",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Percentage-of-samples parameter for the extreme-count filter.  Intervals with a count that has a percentile outside of [extreme-count-filter-minimum-percentile, extreme-count-filter-maximum-percentile] in a percentage of samples strictly greater than this will be filtered out.  (This is the second count-based filter applied.)  Default value: 90.0. "
                ),
            ),
            ToolInput(
                tag="gatkConfigFile",
                input_type=String(optional=True),
                prefix="--gatk-config-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="A configuration file to use with the GATK. Default value: null."
                ),
            ),
            ToolInput(
                tag="gcsMaxRetries",
                input_type=Int(optional=True),
                prefix="--gcs-max-retries",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-gcs-retries)  If the GCS bucket channel errors out, how many times it will attempt to re-initiate the connection  Default value: 20. "
                ),
            ),
            ToolInput(
                tag="gcsProjectForRequesterPays",
                input_type=String(optional=True),
                prefix="--gcs-project-for-requester-pays",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Project to bill when accessing 'requester pays' buckets. If unset, these buckets cannot be accessed.  Default value: . "
                ),
            ),
            ToolInput(
                tag="help",
                input_type=Boolean(optional=True),
                prefix="--help",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-h) display the help message Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--input",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input TSV or HDF5 files containing integer read counts in genomic intervals (output of CollectReadCounts).  Must be provided if no annotated-intervals file is provided.  This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="intervalExclusionPadding",
                input_type=Int(optional=True),
                prefix="--interval-exclusion-padding",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ixp)  Amount of padding (in bp) to add to each interval you are excluding.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="intervalMergingRule",
                input_type=Boolean(optional=True),
                prefix="--interval-merging-rule",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-imr)  Interval merging rule for abutting intervals  Default value: ALL. Possible values: {ALL, OVERLAPPING_ONLY} "
                ),
            ),
            ToolInput(
                tag="intervalPadding",
                input_type=Boolean(optional=True),
                prefix="--interval-padding",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-ip) Default value: 0."),
            ),
            ToolInput(
                tag="intervalSetRule",
                input_type=Boolean(optional=True),
                prefix="--interval-set-rule",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-isr)  Set merging approach to use for combining interval inputs  Default value: UNION. Possible values: {UNION, INTERSECTION} "
                ),
            ),
            ToolInput(
                tag="lowCountFilterCountThreshold",
                input_type=Int(optional=True),
                prefix="--low-count-filter-count-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Count-threshold parameter for the low-count filter.  Intervals with a count strictly less than this threshold in a percentage of samples strictly greater than low-count-filter-percentage-of-samples will be filtered out.  (This is the first count-based filter applied.)  Default value: 5. "
                ),
            ),
            ToolInput(
                tag="lowCountFilterPercentageOfSamples",
                input_type=Double(optional=True),
                prefix="--low-count-filter-percentage-of-samples",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Percentage-of-samples parameter for the low-count filter.  Intervals with a count strictly less than low-count-filter-count-threshold in a percentage of samples strictly greater than this will be filtered out.  (This is the first count-based filter applied.)  Default value: 90.0. "
                ),
            ),
            ToolInput(
                tag="maximumGcContent",
                input_type=Double(optional=True),
                prefix="--maximum-gc-content",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Maximum allowed value for GC-content annotation (inclusive). Default value: 0.9."
                ),
            ),
            ToolInput(
                tag="maximumMappability",
                input_type=Double(optional=True),
                prefix="--maximum-mappability",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Maximum allowed value for mappability annotation (inclusive). Default value: 1.0."
                ),
            ),
            ToolInput(
                tag="maximumSegmentalDuplicationContent",
                input_type=Double(optional=True),
                prefix="--maximum-segmental-duplication-content",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum allowed value for segmental-duplication-content annotation (inclusive).  Default value: 0.5. "
                ),
            ),
            ToolInput(
                tag="minimumGcContent",
                input_type=Double(optional=True),
                prefix="--minimum-gc-content",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Minimum allowed value for GC-content annotation (inclusive). Default value: 0.1."
                ),
            ),
            ToolInput(
                tag="minimumMappability",
                input_type=Double(optional=True),
                prefix="--minimum-mappability",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Minimum allowed value for mappability annotation (inclusive). Default value: 0.9."
                ),
            ),
            ToolInput(
                tag="minimumSegmentalDuplicationContent",
                input_type=Double(optional=True),
                prefix="--minimum-segmental-duplication-content",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum allowed value for segmental-duplication-content annotation (inclusive).  Default value: 0.0. "
                ),
            ),
            ToolInput(
                tag="quiet",
                input_type=Boolean(optional=True),
                prefix="--QUIET",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to suppress job-summary info on System.err. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="tmpDir",
                input_type=Boolean(optional=True),
                prefix="--tmp-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Temp directory to use. Default value: null."
                ),
            ),
            ToolInput(
                tag="useJdkDeflater",
                input_type=Boolean(optional=True),
                prefix="--use-jdk-deflater",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-jdk-deflater)  Whether to use the JdkDeflater (as opposed to IntelDeflater)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="useJdkInflater",
                input_type=Boolean(optional=True),
                prefix="--use-jdk-inflater",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-jdk-inflater)  Whether to use the JdkInflater (as opposed to IntelInflater)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="verbosity",
                input_type=Boolean(optional=True),
                prefix="--verbosity",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-verbosity)  Control verbosity of logging.  Default value: INFO. Possible values: {ERROR, WARNING, INFO, DEBUG} "
                ),
            ),
            ToolInput(
                tag="version",
                input_type=Boolean(optional=True),
                prefix="--version",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="display the version number for this tool Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="showhidden",
                input_type=Boolean(optional=True),
                prefix="--showHidden",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-showHidden)  display hidden arguments  Default value: false. Possible values: {true, false} "
                ),
            ),
        ]

    def outputs(self):
        return []

    def metadata(self):
        return ToolMetadata(
            contributors=[],
            dateCreated=datetime.fromisoformat("2020-05-18T14:05:32.041630"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:05:32.041631"),
            documentation="USAGE: FilterIntervals [arguments]\nFilters intervals based on annotations and/or count statistics\nVersion:4.1.3.0\n",
        )
