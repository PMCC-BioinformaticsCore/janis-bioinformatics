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


class GatkCollectIndependentReplicateMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectIndependentReplicateMetrics"

    def friendly_name(self) -> str:
        return "GATK4: CollectIndependentReplicateMetrics"

    def tool(self) -> str:
        return "Gatk4CollectIndependentReplicateMetrics"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-I) Input (indexed) BAM file. Required."),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-O) Write metrics to this file Required."),
            ),
            ToolInput(
                tag="vcf",
                input_type=File(optional=True),
                prefix="--VCF",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-V) Input VCF file Required."),
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
                tag="barcode_bq",
                input_type=String(optional=True),
                prefix="--BARCODE_BQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Barcode Quality SAM tag. Default value: QX."
                ),
            ),
            ToolInput(
                tag="barcode_tag",
                input_type=String(optional=True),
                prefix="--BARCODE_TAG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Barcode SAM tag. Default value: RX."),
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
                tag="matrix_output",
                input_type=File(optional=True),
                prefix="--MATRIX_OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MO) Write the confusion matrix (of UMIs) to this file Default value: null."
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
                tag="minimum_barcode_bq",
                input_type=Int(optional=True),
                prefix="--MINIMUM_BARCODE_BQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MBQ)  minimal value for the base quality of all the bases in a molecular barcode, for it to be used.  Default value: 30. "
                ),
            ),
            ToolInput(
                tag="minimum_bq",
                input_type=Int(optional=True),
                prefix="--MINIMUM_BQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-BQ) minimal value for the base quality of a base to be used in the estimation. Default value: 17. "
                ),
            ),
            ToolInput(
                tag="minimum_gq",
                input_type=Int(optional=True),
                prefix="--MINIMUM_GQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-GQ) minimal value for the GQ field in the VCF to use variant site. Default value: 90."
                ),
            ),
            ToolInput(
                tag="minimum_mq",
                input_type=Int(optional=True),
                prefix="--MINIMUM_MQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MQ) minimal value for the mapping quality of the reads to be used in the estimation. Default value: 40. "
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
                tag="sample",
                input_type=String(optional=True),
                prefix="--SAMPLE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ALIAS) Name of sample to look at in VCF. Can be omitted if VCF contains only one sample. Default value: null. "
                ),
            ),
            ToolInput(
                tag="stop_after",
                input_type=Int(optional=True),
                prefix="--STOP_AFTER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Number of sets to examine before stopping. Default value: 0."
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:09:36.969096"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:09:36.969097"),
            documentation="b'\n**EXPERIMENTAL FEATURE - USE AT YOUR OWN RISK**\nUSAGE: CollectIndependentReplicateMetrics [arguments]\nEstimates the rate of independent replication rate of reads within a bam. \nThat is, it estimates the fraction of the reads which would be marked as duplicates but are actually biological\nreplicates, independent observations of the data. \nVersion:4.1.3.0\n",
        )
