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


class GatkAnalyzeCovariatesBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "AnalyzeCovariates"

    def friendly_name(self) -> str:
        return "GATK4: AnalyzeCovariates"

    def tool(self) -> str:
        return "Gatk4AnalyzeCovariates"

    def inputs(self):
        return [
            ToolInput(
                tag="afterReportFile",
                input_type=File(optional=True),
                prefix="--after-report-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-after)  file containing the BQSR second-pass report file  Default value: null. "
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
                tag="beforeReportFile",
                input_type=File(optional=True),
                prefix="--before-report-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-before)  file containing the BQSR first-pass report file  Default value: null. "
                ),
            ),
            ToolInput(
                tag="bqsrRecalFile",
                input_type=File(optional=True),
                prefix="--bqsr-recal-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-bqsr) Input covariates table file for on-the-fly base quality score recalibration Default value: null. "
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
                tag="ignoreLastModificationTimes",
                input_type=Boolean(optional=True),
                prefix="--ignore-last-modification-times",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" do not emit warning messages related to suspicious last modification time order of inputs  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="intermediateCsvFile",
                input_type=File(optional=True),
                prefix="--intermediate-csv-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-csv)  location of the csv intermediate file  Default value: null. "
                ),
            ),
            ToolInput(
                tag="plotsReportFile",
                input_type=File(optional=True),
                prefix="--plots-report-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-plots)  location of the output report  Default value: null. "
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
            dateCreated=datetime.fromisoformat("2020-05-19T08:37:02.658448"),
            dateUpdated=datetime.fromisoformat("2020-05-19T08:37:02.658449"),
            documentation="USAGE: AnalyzeCovariates [arguments]\nEvaluate and compare base quality score recalibration (BQSR) tables\nVersion:4.1.3.0\n",
        )
