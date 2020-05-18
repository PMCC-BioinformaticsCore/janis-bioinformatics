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


class GatkCallCopyRatioSegmentsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CallCopyRatioSegments"

    def friendly_name(self) -> str:
        return "GATK4: CallCopyRatioSegments"

    def tool(self) -> str:
        return "Gatk4CallCopyRatioSegments"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--input",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input file containing copy-ratio segments (.cr.seg output of ModelSegments). Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Output file for called copy-ratio segments. Required."
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
                tag="callingCopyRatioZScoreThreshold",
                input_type=Double(optional=True),
                prefix="--calling-copy-ratio-z-score-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Threshold on z-score of non-log2 copy ratio used for calling segments.  Default value: 2.0. "
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
                tag="neutralSegmentCopyRatioLowerBound",
                input_type=Double(optional=True),
                prefix="--neutral-segment-copy-ratio-lower-bound",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Lower bound on non-log2 copy ratio used for determining copy-neutral segments.  Default value: 0.9. "
                ),
            ),
            ToolInput(
                tag="neutralSegmentCopyRatioUpperBound",
                input_type=Double(optional=True),
                prefix="--neutral-segment-copy-ratio-upper-bound",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Upper bound on non-log2 copy ratio used for determining copy-neutral segments.  Default value: 1.1. "
                ),
            ),
            ToolInput(
                tag="outlierNeutralSegmentCopyRatioZScoreThreshold",
                input_type=Double(optional=True),
                prefix="--outlier-neutral-segment-copy-ratio-z-score-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Threshold on z-score of non-log2 copy ratio used for determining outlier copy-neutral segments.  If non-log2 copy ratio z-score is above this threshold for a copy-neutral segment, it is considered an outlier and not used in the calculation of the length-weighted mean and standard deviation used for calling.  Default value: 2.0. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:05:00.419837"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:05:00.419838"),
            documentation="USAGE: CallCopyRatioSegments [arguments]\nCalls copy-ratio segments as amplified, deleted, or copy-number neutral\nVersion:4.1.3.0\n",
        )
