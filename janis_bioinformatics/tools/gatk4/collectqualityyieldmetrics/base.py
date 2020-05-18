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


class GatkCollectQualityYieldMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectQualityYieldMetrics"

    def friendly_name(self) -> str:
        return "GATK4: CollectQualityYieldMetrics"

    def tool(self) -> str:
        return "Gatk4CollectQualityYieldMetrics"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-I) Input SAM or BAM file. Required."),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) File to write the output to. Required."
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
                tag="assume_sorted",
                input_type=Boolean(optional=True),
                prefix="--ASSUME_SORTED",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-AS) If true (default), then the sort order in the header file will be ignored. Default value: true. Possible values: {true, false} "
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
                tag="include_secondary_alignments",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_SECONDARY_ALIGNMENTS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If true, include bases from secondary alignments in metrics. Setting to true may cause double-counting of bases if there are secondary alignments in the input file.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="include_supplemental_alignments",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_SUPPLEMENTAL_ALIGNMENTS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If true, include bases from supplemental alignments in metrics. Setting to true may cause double-counting of bases if there are supplemental alignments in the input file.  Default value: false. Possible values: {true, false} "
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
                tag="stop_after",
                input_type=Boolean(optional=True),
                prefix="--STOP_AFTER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Stop after processing N reads, mainly for debugging. Default value: 0."
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
                tag="use_original_qualities",
                input_type=Boolean(optional=True),
                prefix="--USE_ORIGINAL_QUALITIES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OQ)  If available in the OQ tag, use the original quality scores as inputs instead of the quality scores in the QUAL field.  Default value: true. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:10:16.258928"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:10:16.258929"),
            documentation="b'USAGE: CollectQualityYieldMetrics [arguments]\nCollect metrics about reads that pass quality thresholds and Illumina-specific filters.  This tool evaluates the overall\nquality of reads within a bam file containing one read group. The output indicates the total numbers of bases within a\nread group that pass a minimum base quality score threshold and (in the case of Illumina data) pass Illumina quality\nfilters as described in the <a href='https://www.broadinstitute.org/gatk/guide/article?id=6329'>GATK Dictionary\nentry</a>. <br /><h4>Note on base quality score options</h4>If the quality score of read bases has been modified in a\nprevious data processing step such as <a href='https://www.broadinstitute.org/gatk/guide/article?id=44'>GATK Base\nRecalibration</a> and an OQ tag is available, this tool can be set to use the OQ value instead of the primary quality\nvalue for the evaluation. <br /><br />Note that the default behaviour of this program changed as of November 6th 2015 to\nno longer include secondary and supplemental alignments in the computation. <br /><h4>Usage Example:</h4><pre>java -jar\npicard.jar CollectQualityYieldMetrics \\<br />       I=input.bam \\<br />       O=quality_yield_metrics.txt \\<br\n/></pre>Please see <a\nhref='https://broadinstitute.github.io/picard/picard-metric-definitions.html#CollectQualityYieldMetrics.QualityYieldMetrics'>the\nQualityYieldMetrics documentation</a> for details and explanations of the output metrics.<hr />\nVersion:4.1.3.0\n",
        )
