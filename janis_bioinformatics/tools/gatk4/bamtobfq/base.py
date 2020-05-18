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


class GatkBamToBfqBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "BamToBfq"

    def friendly_name(self) -> str:
        return "GATK4: BamToBfq"

    def tool(self) -> str:
        return "Gatk4BamToBfq"

    def inputs(self):
        return [
            ToolInput(
                tag="analysis_dir",
                input_type=File(optional=True),
                prefix="--ANALYSIS_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The analysis directory for the binary output file. Required."
                ),
            ),
            ToolInput(
                tag="flowcell_barcode",
                input_type=String(optional=True),
                prefix="--FLOWCELL_BARCODE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-F) Flowcell barcode (e.g. 30PYMAAXX). Required. Cannot be used in conjuction with argument(s) OUTPUT_FILE_PREFIX"
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-I) The BAM file to parse. Required."),
            ),
            ToolInput(
                tag="output_file_prefix",
                input_type=String(optional=True),
                prefix="--OUTPUT_FILE_PREFIX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Prefix for all output files Required. Cannot be used in conjuction with argument(s) FLOWCELL_BARCODE (F) LANE (L)"
                ),
            ),
            ToolInput(
                tag="paired_run",
                input_type=Boolean(optional=True),
                prefix="--PAIRED_RUN",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PE) Whether this is a paired-end run. Required. Possible values: {true, false}"
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
                tag="bases_to_write",
                input_type=Int(optional=True),
                prefix="--BASES_TO_WRITE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The number of bases from each read to write to the bfq file. If this is non-null, then only the first BASES_TO_WRITE bases from each read will be written.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="clip_adapters",
                input_type=Boolean(optional=True),
                prefix="--CLIP_ADAPTERS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to clip adapters from the reads Default value: true. Possible values: {true, false} "
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
                tag="include_non_pf_reads",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_NON_PF_READS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-NONPF)  Whether to include non-PF reads  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="lane",
                input_type=Int(optional=True),
                prefix="--LANE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-L) Lane number. Default value: null. Cannot be used in conjuction with argument(s) OUTPUT_FILE_PREFIX"
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
                tag="read_chunk_size",
                input_type=Int(optional=True),
                prefix="--READ_CHUNK_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CHUNK)  Number of reads to break into individual groups for alignment  Default value: 2000000. "
                ),
            ),
            ToolInput(
                tag="read_name_prefix",
                input_type=String(optional=True),
                prefix="--READ_NAME_PREFIX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Prefix to be stripped off the beginning of all read names (to make them short enough to run in Maq)  Default value: null. "
                ),
            ),
            ToolInput(
                tag="reads_to_align",
                input_type=Boolean(optional=True),
                prefix="--READS_TO_ALIGN",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-NUM) Default value: null."),
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
                tag="run_barcode",
                input_type=String(optional=True),
                prefix="--RUN_BARCODE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-RB) Deprecated option; use READ_NAME_PREFIX instead Default value: null. Cannot be used in conjuction with argument(s) READ_NAME_PREFIX"
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:55:54.266012"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:55:54.266013"),
            documentation="b'USAGE: BamToBfq [arguments]\n<p>Converts a BAM file into a BFQ (binary fastq formatted) file.</p><p>The BFQ format is the input format to some tools\nlike Maq aligner.</p><h3>Input</h3><p>A single BAM file to convert</p><h3>Output</h3><p>One or two FASTQ files depending\non whether the BAM file contains single- or paired-end sequencing data. You must indicate the output directory that will\ncontain these files (<code>ANALYSIS_DIR</code>) and the output file name prefix\n(<code>OUTPUT_FILE_PREFIX</code>).</p><h3>Usage example:</h3><pre>java -jar picard.jar BamToBfq \\\nI=input.bam \\\nANALYSIS_DIR=output_dir \\\nOUTPUT_FILE_PREFIX=output_name \\\nPAIRED_RUN=false</pre><hr />\nVersion:4.1.3.0\n",
        )
