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


class GatkIlluminaBasecallsToFastqBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "IlluminaBasecallsToFastq"

    def friendly_name(self) -> str:
        return "GATK4: IlluminaBasecallsToFastq"

    def tool(self) -> str:
        return "Gatk4IlluminaBasecallsToFastq"

    def inputs(self):
        return [
            ToolInput(
                tag="basecalls_dir",
                input_type=File(optional=True),
                prefix="--BASECALLS_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-B) The basecalls directory. Required."),
            ),
            ToolInput(
                tag="lane",
                input_type=Int(optional=True),
                prefix="--LANE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-L) Lane number. Required."),
            ),
            ToolInput(
                tag="multiplex_params",
                input_type=File(optional=True),
                prefix="--MULTIPLEX_PARAMS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Tab-separated file for creating all output FASTQs demultiplexed by barcode for a lane with single IlluminaBasecallsToFastq invocation.  The columns are OUTPUT_PREFIX, and BARCODE_1, BARCODE_2 ... BARCODE_X where X = number of barcodes per cluster (optional).  Row with BARCODE_1 set to 'N' is used to specify an output_prefix for no barcode match.  Required.  Cannot be used in conjuction with argument(s) OUTPUT_PREFIX (O)"
                ),
            ),
            ToolInput(
                tag="output_prefix",
                input_type=File(optional=True),
                prefix="--OUTPUT_PREFIX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The prefix for output FASTQs. Extensions as described above are appended. Use this option for a non-barcoded run, or for a barcoded run in which it is not desired to demultiplex reads into separate files by barcode.  Required.  Cannot be used in conjuction with argument(s) MULTIPLEX_PARAMS"
                ),
            ),
            ToolInput(
                tag="read_structure",
                input_type=String(optional=True),
                prefix="--READ_STRUCTURE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-RS) A description of the logical structure of clusters in an Illumina Run, i.e. a description of the structure IlluminaBasecallsToSam assumes the  data to be in. It should consist of integer/character pairs describing the number of cycles and the type of those cycles (B for Sample Barcode, M for molecular barcode, T for Template, and S for skip).  E.g. If the input data consists of 80 base clusters and we provide a read structure of '28T8M8B8S28T' then the sequence may be split up into four reads: * read one with 28 cycles (bases) of template * read two with 8 cycles (bases) of molecular barcode (ex. unique molecular barcode) * read three with 8 cycles (bases) of sample barcode * 8 cycles (bases) skipped. * read four with 28 cycles (bases) of template The skipped cycles would NOT be included in an output SAM/BAM file or in read groups therein.  Required. "
                ),
            ),
            ToolInput(
                tag="run_barcode",
                input_type=String(optional=True),
                prefix="--RUN_BARCODE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The barcode of the run. Prefixed to read names. Required."
                ),
            ),
            ToolInput(
                tag="adapters_to_check",
                input_type=Boolean(optional=True),
                prefix="--ADAPTERS_TO_CHECK",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Deprecated (No longer used). Which adapters to look for in the read.  This argument may be specified 0 or more times. Default value: null. Possible values: {PAIRED_END, INDEXED, SINGLE_END, NEXTERA_V1, NEXTERA_V2, DUAL_INDEXED, FLUIDIGM, TRUSEQ_SMALLRNA, ALTERNATIVE_SINGLE_END} "
                ),
            ),
            ToolInput(
                tag="apply_eamss_filter",
                input_type=Boolean(optional=True),
                prefix="--APPLY_EAMSS_FILTER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Apply EAMSS filtering to identify inappropriately quality scored bases towards the ends of reads and convert their quality scores to Q2.  Default value: true. Possible values: {true, false} "
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
                tag="barcodes_dir",
                input_type=File(optional=True),
                prefix="--BARCODES_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-BCD) The barcodes directory with _barcode.txt files (generated by ExtractIlluminaBarcodes). If not set, use BASECALLS_DIR.   Default value: null. "
                ),
            ),
            ToolInput(
                tag="compress_outputs",
                input_type=Boolean(optional=True),
                prefix="--COMPRESS_OUTPUTS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-GZIP)  Compress output FASTQ files using gzip and append a .gz extension to the file names.  Default value: false. Possible values: {true, false} "
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
                tag="first_tile",
                input_type=Int(optional=True),
                prefix="--FIRST_TILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If set, this is the first tile to be processed (used for debugging). Note that tiles are not processed in numerical order.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="flowcell_barcode",
                input_type=String(optional=True),
                prefix="--FLOWCELL_BARCODE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The barcode of the flowcell that was sequenced; required if emitting Casava1.8-style read name headers  Default value: null. "
                ),
            ),
            ToolInput(
                tag="force_gc",
                input_type=Boolean(optional=True),
                prefix="--FORCE_GC",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true, call System.gc() periodically. This is useful in cases in which the -Xmx value passed is larger than the available memory.  Default value: true. Possible values: {true, false} "
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
                tag="ignore_unexpected_barcodes",
                input_type=Boolean(optional=True),
                prefix="--IGNORE_UNEXPECTED_BARCODES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-INGORE_UNEXPECTED)  Whether to ignore reads whose barcodes are not found in MULTIPLEX_PARAMS.  Useful when outputting FASTQs for only a subset of the barcodes in a lane.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="include_non_pf_reads",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_NON_PF_READS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-NONPF)  Whether to include non-PF reads  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="machine_name",
                input_type=String(optional=True),
                prefix="--MACHINE_NAME",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The name of the machine on which the run was sequenced; required if emitting Casava1.8-style read name headers  Default value: null. "
                ),
            ),
            ToolInput(
                tag="max_reads_in_ram_per_tile",
                input_type=Int(optional=True),
                prefix="--MAX_READS_IN_RAM_PER_TILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Configure SortingCollections to store this many records before spilling to disk. For an indexed run, each SortingCollection gets this value/number of indices.  Default value: 1200000. "
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
                tag="minimum_quality",
                input_type=Int(optional=True),
                prefix="--MINIMUM_QUALITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The minimum quality (after transforming 0s to 1s) expected from reads. If qualities are lower than this value, an error is thrown.The default of 2 is what the Illumina's spec describes as the minimum, but in practice the value has been observed lower.  Default value: 2. "
                ),
            ),
            ToolInput(
                tag="num_processors",
                input_type=Int(optional=True),
                prefix="--NUM_PROCESSORS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The number of threads to run in parallel. If NUM_PROCESSORS = 0, number of cores is automatically set to the number of cores available on the machine. If NUM_PROCESSORS < 0, then the number of cores used will be the number available on the machine less NUM_PROCESSORS.  Default value: 0. "
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
                tag="read_name_format",
                input_type=Boolean(optional=True),
                prefix="--READ_NAME_FORMAT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The read name header formatting to emit.  Casava1.8 formatting has additional information beyond Illumina, including: the passing-filter flag value for the read, the flowcell name, and the sequencer name.  Default value: CASAVA_1_8. Possible values: {CASAVA_1_8, ILLUMINA} "
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
                tag="tile_limit",
                input_type=Int(optional=True),
                prefix="--TILE_LIMIT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If set, process no more than this many tiles (used for debugging). Default value: null."
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:04:34.070771"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:04:34.070773"),
            documentation="b'USAGE: IlluminaBasecallsToFastq [arguments]\nGenerate FASTQ file(s) from Illumina basecall read data.  <p>This tool generates FASTQ files from data in an Illumina\nBaseCalls output directory.  Separate FASTQ files are created for each template, barcode, and index (molecular barcode)\nread.  Briefly, the template reads are the target sequence of your experiment, the barcode sequence reads facilitate\nsample demultiplexing, and the index reads help mitigate instrument phasing errors.  For additional information on the\nread types, please see the following reference <a\nhref'=http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3245947/'>here</a>.</p><p>In the absence of sample pooling\n(multiplexing) and/or barcodes, then an OUTPUT_PREFIX (file directory) must be provided as the sample identifier.  For\nmultiplexed samples, a MULTIPLEX_PARAMS file must be specified.  The MULTIPLEX_PARAMS file contains the list of sample\nbarcodes used to sort template, barcode, and index reads.  It is essentially the same as the BARCODE_FILE used in the<a\nhref='http://broadinstitute.github.io/picard/command-line-overview.html#ExtractIlluminaBarcodes'>ExtractIlluminaBarcodes</a>\ntool.</p>     <p>Files from this tool use the following naming format: {prefix}.{type}_{number}.fastq with the {prefix}\nindicating the sample barcode, the {type} indicating the types of reads e.g. index, barcode, or blank (if it contains a\ntemplate read).  The {number} indicates the read number, either first (1) or second (2) for paired-end sequencing. </p>\n<h4>Usage examples:</h4><pre>Example 1: Sample(s) with either no barcode or barcoded without multiplexing <br />java\n-jar picard.jar IlluminaBasecallsToFastq \\<br />      READ_STRUCTURE=25T8B25T \\<br />     \nBASECALLS_DIR=basecallDirectory \\<br />      LANE=001 \\<br />      OUTPUT_PREFIX=noBarcode.1 \\<br />     \nRUN_BARCODE=run15 \\<br />      FLOWCELL_BARCODE=abcdeACXX <br /><br />Example 2: Multiplexed samples <br />java -jar\npicard.jar IlluminaBasecallsToFastq \\<br />      READ_STRUCTURE=25T8B25T \\<br />      BASECALLS_DIR=basecallDirectory\n\\<br />      LANE=001 \\<br />      MULTIPLEX_PARAMS=demultiplexed_output.txt \\<br />      RUN_BARCODE=run15 \\<br />     \nFLOWCELL_BARCODE=abcdeACXX <br /></pre><p>The FLOWCELL_BARCODE is required if emitting Casava 1.8-style read name\nheaders.</p><hr />\nVersion:4.1.3.0\n",
        )
