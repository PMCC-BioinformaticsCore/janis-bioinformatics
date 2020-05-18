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


class GatkMarkIlluminaAdaptersBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "MarkIlluminaAdapters"

    def friendly_name(self) -> str:
        return "GATK4: MarkIlluminaAdapters"

    def tool(self) -> str:
        return "Gatk4MarkIlluminaAdapters"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-I) Undocumented option Required."),
            ),
            ToolInput(
                tag="metrics",
                input_type=File(optional=True),
                prefix="--METRICS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-M) Histogram showing counts of bases_clipped in how many reads Required."
                ),
            ),
            ToolInput(
                tag="adapter_truncation_length",
                input_type=Int(optional=True),
                prefix="--ADAPTER_TRUNCATION_LENGTH",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Adapters are truncated to this length to speed adapter matching.  Set to a large number to effectively disable truncation.  Default value: 30. "
                ),
            ),
            ToolInput(
                tag="adapters",
                input_type=Boolean(optional=True),
                prefix="--ADAPTERS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="This argument may be specified 0 or more times. Default value: [INDEXED, DUAL_INDEXED, PAIRED_END]. Possible values: {PAIRED_END, INDEXED, SINGLE_END, NEXTERA_V1, NEXTERA_V2, DUAL_INDEXED, FLUIDIGM, TRUSEQ_SMALLRNA, ALTERNATIVE_SINGLE_END} "
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
                tag="five_prime_adapter",
                input_type=String(optional=True),
                prefix="--FIVE_PRIME_ADAPTER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="For specifying adapters other than standard Illumina Default value: null."
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
                tag="max_error_rate_pe",
                input_type=Double(optional=True),
                prefix="--MAX_ERROR_RATE_PE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The maximum mismatch error rate to tolerate when clipping paired-end reads. Default value: 0.1. "
                ),
            ),
            ToolInput(
                tag="max_error_rate_se",
                input_type=Double(optional=True),
                prefix="--MAX_ERROR_RATE_SE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The maximum mismatch error rate to tolerate when clipping single-end reads. Default value: 0.1. "
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
                tag="min_match_bases_pe",
                input_type=Int(optional=True),
                prefix="--MIN_MATCH_BASES_PE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The minimum number of bases to match over (per-read) when clipping paired-end reads. Default value: 6. "
                ),
            ),
            ToolInput(
                tag="min_match_bases_se",
                input_type=Int(optional=True),
                prefix="--MIN_MATCH_BASES_SE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The minimum number of bases to match over when clipping single-end reads. Default value: 12. "
                ),
            ),
            ToolInput(
                tag="num_adapters_to_keep",
                input_type=String(optional=True),
                prefix="--NUM_ADAPTERS_TO_KEEP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(keep)  (plus any adapters that were tied with the adapters being kept).  Default value: 1. "
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) If output is not specified, just the metrics are generated Default value: null."
                ),
            ),
            ToolInput(
                tag="paired_run",
                input_type=Boolean(optional=True),
                prefix="--PAIRED_RUN",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PE) DEPRECATED. Whether this is a paired-end run. No longer used. Default value: null. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="prune_adapter_list_after_this_many_adapters_seen",
                input_type=Int(optional=True),
                prefix="--PRUNE_ADAPTER_LIST_AFTER_THIS_MANY_ADAPTERS_SEEN",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-APT)  If looking for multiple adapter sequences, then after having seen this many adapters, shorten the list of sequences. Keep the adapters that were found most frequently in the input so far. Set to -1 if the input has a heterogeneous mix of adapters so shortening is undesirable.  Default value: 100. "
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
                tag="three_prime_adapter",
                input_type=String(optional=True),
                prefix="--THREE_PRIME_ADAPTER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="For specifying adapters other than standard Illumina Default value: null."
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:04:47.335323"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:04:47.335325"),
            documentation="b'USAGE: MarkIlluminaAdapters [arguments]\nReads a SAM or BAM file and rewrites it with new adapter-trimming tags.  <p>This tool clears any existing\nadapter-trimming tags (XT:i:) in the optional tag region of a SAM file.  The SAM/BAM file must be sorted by query\nname.</p> <p>Outputs a metrics file histogram showing counts of bases_clipped per read.<h4>Usage example:</h4><pre>java\n-jar picard.jar MarkIlluminaAdapters \\<br /> INPUT=input.sam \\<br />METRICS=metrics.txt </pre><hr />\nVersion:4.1.3.0\n",
        )
