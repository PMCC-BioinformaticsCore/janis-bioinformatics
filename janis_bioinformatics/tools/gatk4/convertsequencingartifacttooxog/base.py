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


class GatkConvertSequencingArtifactToOxoGBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "ConvertSequencingArtifactToOxoG"

    def friendly_name(self) -> str:
        return "GATK4: ConvertSequencingArtifactToOxoG"

    def tool(self) -> str:
        return "Gatk4ConvertSequencingArtifactToOxoG"

    def inputs(self):
        return [
            ToolInput(
                tag="input_base",
                input_type=File(optional=True),
                prefix="--INPUT_BASE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Basename of the input artifact metrics file (output by CollectSequencingArtifactMetrics) Required. "
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
                tag="compression_level",
                input_type=Int(optional=True),
                prefix="--COMPRESSION_LEVEL",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Compression level for all compressed files created (e.g. BAM and VCF). Default value: 2."
                ),
            ),
            ToolInput(
                tag="create_index",
                input_type=Boolean(optional=True),
                prefix="--CREATE_INDEX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to create a BAM index when writing a coordinate-sorted BAM file. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="create_md5_file",
                input_type=Boolean(optional=True),
                prefix="--CREATE_MD5_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to create an MD5 digest for any BAM or FASTQ files created. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="ga4gh_client_secrets",
                input_type=Boolean(optional=True),
                prefix="--GA4GH_CLIENT_SECRETS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: client_secrets.json."),
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
                tag="max_records_in_ram",
                input_type=Int(optional=True),
                prefix="--MAX_RECORDS_IN_RAM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When writing files that need to be sorted, this will specify the number of records stored in RAM before spilling to disk. Increasing this number reduces the number of file handles needed to sort the file, and increases the amount of RAM needed.  Default value: 500000. "
                ),
            ),
            ToolInput(
                tag="output_base",
                input_type=File(optional=True),
                prefix="--OUTPUT_BASE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Basename for output OxoG metrics. Defaults to same basename as input metrics Default value: null. "
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
                tag="reference_sequence",
                input_type=File(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R) Reference sequence file. Default value: null."
                ),
            ),
            ToolInput(
                tag="tmp_dir",
                input_type=File(optional=True),
                prefix="--TMP_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="One or more directories with space available to be used by this program for temporary storage of working files  This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="use_jdk_deflater",
                input_type=Boolean(optional=True),
                prefix="--USE_JDK_DEFLATER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-use_jdk_deflater)  Use the JDK Deflater instead of the Intel Deflater for writing compressed output  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="use_jdk_inflater",
                input_type=Boolean(optional=True),
                prefix="--USE_JDK_INFLATER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-use_jdk_inflater)  Use the JDK Inflater instead of the Intel Inflater for reading compressed input  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="validation_stringency",
                input_type=Boolean(optional=True),
                prefix="--VALIDATION_STRINGENCY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Validation stringency for all SAM files read by this program.  Setting stringency to SILENT can improve performance when processing a BAM file in which variable-length data (read, qualities, tags) do not otherwise need to be decoded.  Default value: STRICT. Possible values: {STRICT, LENIENT, SILENT} "
                ),
            ),
            ToolInput(
                tag="verbosity",
                input_type=Boolean(optional=True),
                prefix="--VERBOSITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Control verbosity of logging. Default value: INFO. Possible values: {ERROR, WARNING, INFO, DEBUG} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:11:48.768027"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:11:48.768028"),
            documentation="b'USAGE: ConvertSequencingArtifactToOxoG [arguments]\nExtract OxoG metrics from generalized artifacts metrics.  <p>This tool extracts 8-oxoguanine (OxoG) artifact metrics\nfrom the output of CollectSequencingArtifactsMetrics (a tool that provides detailed information on a variety of\nartifacts found in sequencing libraries) and converts them to the CollectOxoGMetrics tool's output format. This\nconveniently eliminates the need to run CollectOxoGMetrics if we already ran CollectSequencingArtifactsMetrics in our\npipeline. See the documentation for <a\nhref='http://broadinstitute.github.io/picard/command-line-overview.html#CollectSequencingArtifactsMetrics'>CollectSequencingArtifactsMetrics</a>\nand <a\nhref='http://broadinstitute.github.io/picard/command-line-overview.html#CollectOxoGMetrics'>CollectOxoGMetrics</a> for\nadditional information on these tools.</p>.<p>Note that only the base of the CollectSequencingArtifactsMetrics output\nfile name is required for the (INPUT_BASE) parameter. For example, if the file name is\nartifact_metrics.txt.bait_bias_detail_metrics or artifact_metrics.txt.pre_adapter_detail_metrics, only the file name\nbase 'artifact_metrics' is required on the command line for this parameter.  An output file called\n'artifact_metrics.oxog_metrics' will be generated automatically.  Finally, to run this tool successfully, the\nREFERENCE_SEQUENCE must be provided.</p><h4>Usage example:</h4><pre>java -jar picard.jar ConvertSequencingArtifactToOxoG\n\\<br />     I=artifact_metrics \\<br />     R=reference.fasta</pre>Please see the metrics definitions page at <a\nhref='http://broadinstitute.github.io/picard/picard-metric-definitions.html#CollectOxoGMetrics.CpcgMetrics'>ConvertSequencingArtifactToOxoG</a>\nfor detailed descriptions of the output metrics produced by this tool.<hr />\nVersion:4.1.3.0\n",
        )
