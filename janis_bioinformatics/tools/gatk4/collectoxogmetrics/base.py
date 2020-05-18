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


class GatkCollectOxoGMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectOxoGMetrics"

    def friendly_name(self) -> str:
        return "GATK4: CollectOxoGMetrics"

    def tool(self) -> str:
        return "Gatk4CollectOxoGMetrics"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input BAM file for analysis. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Location of output metrics file to write. Required."
                ),
            ),
            ToolInput(
                tag="reference_sequence",
                input_type=File(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-R) Reference sequence file. Required."),
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
                tag="context_size",
                input_type=Int(optional=True),
                prefix="--CONTEXT_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The number of context bases to include on each side of the assayed G/C base. Default value: 1. "
                ),
            ),
            ToolInput(
                tag="contexts",
                input_type=String(optional=True),
                prefix="--CONTEXTS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The optional set of sequence contexts to restrict analysis to. If not supplied all contexts are analyzed.  This argument may be specified 0 or more times. Default value: null. "
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
                tag="db_snp",
                input_type=File(optional=True),
                prefix="--DB_SNP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="VCF format dbSNP file, used to exclude regions around known polymorphisms from analysis. Default value: null. "
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
                tag="include_non_pf_reads",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_NON_PF_READS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-NON_PF)  Whether or not to include non-PF reads.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="intervals",
                input_type=File(optional=True),
                prefix="--INTERVALS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="An optional list of intervals to restrict analysis to. Default value: null."
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
                tag="maximum_insert_size",
                input_type=Int(optional=True),
                prefix="--MAXIMUM_INSERT_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MAX_INS)  The maximum insert size for a read to be included in analysis. Set of 0 to allow unpaired reads.  Default value: 600. "
                ),
            ),
            ToolInput(
                tag="minimum_insert_size",
                input_type=Int(optional=True),
                prefix="--MINIMUM_INSERT_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MIN_INS)  The minimum insert size for a read to be included in analysis. Set of 0 to allow unpaired reads.  Default value: 60. "
                ),
            ),
            ToolInput(
                tag="minimum_mapping_quality",
                input_type=Int(optional=True),
                prefix="--MINIMUM_MAPPING_QUALITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MQ)  The minimum mapping quality score for a base to be included in analysis.  Default value: 30. "
                ),
            ),
            ToolInput(
                tag="minimum_quality_score",
                input_type=Int(optional=True),
                prefix="--MINIMUM_QUALITY_SCORE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-Q)  The minimum base quality score for a base to be included in analysis.  Default value: 20. "
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
                tag="stop_after",
                input_type=Int(optional=True),
                prefix="--STOP_AFTER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="For debugging purposes: stop after visiting this many sites with at least 1X coverage. Default value: 2147483647. "
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
                tag="use_oq",
                input_type=Boolean(optional=True),
                prefix="--USE_OQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When available, use original quality scores for filtering. Default value: true. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:10:09.676391"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:10:09.676394"),
            documentation="b'USAGE: CollectOxoGMetrics [arguments]\nCollect metrics to assess oxidative artifacts.This tool collects metrics quantifying the error rate resulting from\noxidative artifacts. For a brief primer on oxidative artifacts, see <a\nhref='http://gatkforums.broadinstitute.org/discussion/6328/oxog-oxidative-artifacts'>the GATK Dictionary</a>.<br /><br\n/>This tool calculates the Phred-scaled probability that an alternate base call results from an oxidation artifact. This\nprobability score is based on base context, sequencing read orientation, and the characteristic low allelic frequency. \nPlease see the following reference for an in-depth <a\nhref='http://nar.oxfordjournals.org/content/early/2013/01/08/nar.gks1443'>discussion</a> of the OxoG error rate. \n<p>Lower probability values implicate artifacts resulting from 8-oxoguanine, while higher probability values suggest\nthat an alternate base call is due to either some other type of artifact or is a real variant.</p><h4>Usage\nexample:</h4><pre>java -jar picard.jar CollectOxoGMetrics \\<br />      I=input.bam \\<br />      O=oxoG_metrics.txt \\<br\n/>      R=reference_sequence.fasta</pre><hr />\nVersion:4.1.3.0\n",
        )
