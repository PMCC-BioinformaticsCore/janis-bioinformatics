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


class GatkDenoiseReadCountsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "DenoiseReadCounts"

    def friendly_name(self) -> str:
        return "GATK4: DenoiseReadCounts"

    def tool(self) -> str:
        return "Gatk4DenoiseReadCounts"

    def inputs(self):
        return [
            ToolInput(
                tag="denoisedCopyRatios",
                input_type=File(optional=True),
                prefix="--denoised-copy-ratios",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Output file for denoised copy ratios. Required."
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--input",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input TSV or HDF5 file containing integer read counts in genomic intervals for a single case sample (output of CollectReadCounts).  Required. "
                ),
            ),
            ToolInput(
                tag="standardizedCopyRatios",
                input_type=File(optional=True),
                prefix="--standardized-copy-ratios",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Output file for standardized copy ratios.  GC-bias correction will be performed if annotations for GC content are provided.  Required. "
                ),
            ),
            ToolInput(
                tag="annotatedIntervals",
                input_type=File(optional=True),
                prefix="--annotated-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Input file containing annotations for GC content in genomic intervals (output of AnnotateIntervals).  Intervals must be identical to and in the same order as those in the input read-counts file.  If a panel of normals is provided, this input will be ignored.  Default value: null. "
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
                tag="countPanelOfNormals",
                input_type=Boolean(optional=True),
                prefix="--count-panel-of-normals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc=" Default value: null. "),
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
                tag="numberOfEigensamples",
                input_type=Int(optional=True),
                prefix="--number-of-eigensamples",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Number of eigensamples to use for denoising.  If not specified or if the number of eigensamples available in the panel of normals is smaller than this, all eigensamples will be used.  Default value: null. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:05:19.404299"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:05:19.404300"),
            documentation="USAGE: DenoiseReadCounts [arguments]\nDenoises read counts to produce denoised copy ratios\nVersion:4.1.3.0\n",
        )
