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


class GatkExtractIlluminaBarcodesBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "ExtractIlluminaBarcodes"

    def friendly_name(self) -> str:
        return "GATK4: ExtractIlluminaBarcodes"

    def tool(self) -> str:
        return "Gatk4ExtractIlluminaBarcodes"

    def inputs(self):
        return [
            ToolInput(
                tag="barcode",
                input_type=String(optional=True),
                prefix="--BARCODE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Barcode sequence. These must be unique, and all the same length. This cannot be used with reads that have more than one barcode; use BARCODE_FILE in that case.   This argument must be specified at least once. Required.  Cannot be used in conjuction with argument(s) BARCODE_FILE"
                ),
            ),
            ToolInput(
                tag="barcode_file",
                input_type=File(optional=True),
                prefix="--BARCODE_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Tab-delimited file of barcode sequences, barcode name and, optionally, library name. Barcodes must be unique and all the same length.  Column headers must be 'barcode_sequence' (or 'barcode_sequence_1'), 'barcode_sequence_2' (optional), 'barcode_name', and 'library_name'.  Required.  Cannot be used in conjuction with argument(s) BARCODE"
                ),
            ),
            ToolInput(
                tag="basecalls_dir",
                input_type=File(optional=True),
                prefix="--BASECALLS_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-B) The Illumina basecalls directory. Required."
                ),
            ),
            ToolInput(
                tag="lane",
                input_type=Int(optional=True),
                prefix="--LANE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-L) Lane number. Required."),
            ),
            ToolInput(
                tag="metrics_file",
                input_type=File(optional=True),
                prefix="--METRICS_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-M) Per-barcode and per-lane metrics written to this file. Required."
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
                tag="arguments_file",
                input_type=File(optional=True),
                prefix="--arguments_file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="read one or more arguments files and add them to the command line This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="compress_outputs",
                input_type=Boolean(optional=True),
                prefix="--COMPRESS_OUTPUTS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-GZIP)  Compress output s_l_t_barcode.txt files using gzip and append a .gz extension to the file names.  Default value: false. Possible values: {true, false} "
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
                tag="max_mismatches",
                input_type=Int(optional=True),
                prefix="--MAX_MISMATCHES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Maximum mismatches for a barcode to be considered a match. Default value: 1."
                ),
            ),
            ToolInput(
                tag="max_no_calls",
                input_type=Int(optional=True),
                prefix="--MAX_NO_CALLS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Maximum allowable number of no-calls in a barcode read before it is considered unmatchable.  Default value: 2. "
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
                tag="min_mismatch_delta",
                input_type=Int(optional=True),
                prefix="--MIN_MISMATCH_DELTA",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Minimum difference between number of mismatches in the best and second best barcodes for a barcode to be considered a match.  Default value: 1. "
                ),
            ),
            ToolInput(
                tag="minimum_base_quality",
                input_type=Int(optional=True),
                prefix="--MINIMUM_BASE_QUALITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-Q)  Minimum base quality. Any barcode bases falling below this quality will be considered a mismatch even in the bases match.  Default value: 0. "
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
                    doc="Run this many PerTileBarcodeExtractors in parallel. If NUM_PROCESSORS = 0, number of cores is automatically set to the number of cores available on the machine. If NUM_PROCESSORS < 0 then the number of cores used will be the number available on the machine less NUM_PROCESSORS.  Default value: 1. "
                ),
            ),
            ToolInput(
                tag="output_dir",
                input_type=File(optional=True),
                prefix="--OUTPUT_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Where to write _barcode.txt files. By default, these are written to BASECALLS_DIR. Default value: null. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:04:27.095792"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:04:27.095793"),
            documentation="b'USAGE: ExtractIlluminaBarcodes [arguments]\nTool determines the barcode for each read in an Illumina lane.  <p>This tool determines the numbers of reads containing\nbarcode-matching sequences and provides statistics on the quality of these barcode matches.</p> <p>Illumina sequences\ncan contain at least two types of barcodes, sample and molecular (index).  Sample barcodes (B in the read structure) are\nused to demultiplex pooled samples while index barcodes (M in the read structure) are used to differentiate multiple\nreads of a template when carrying out paired-end sequencing.  Note that this tool only extracts sample (B) and not\nmolecular barcodes (M).</p><p>Barcodes can be provided in the form of a list (BARCODE_FILE) or a string representing the\nbarcode (BARCODE).  The BARCODE_FILE contains multiple fields including 'barcode_sequence' (or 'barcode_sequence_1'),\n'barcode_sequence_2' (optional), 'barcode_name', and 'library_name'. In contrast, the BARCODE argument is used for runs\nwith reads containing a single barcode (nonmultiplexed) and can be added directly as a string of text e.g.\nBARCODE=CAATAGCG.</p><p>Data is output per lane/tile within the BaseCalls directory with the file name format of\n's_{lane}_{tile}_barcode.txt'.  These files contain the following tab-separated columns:<ul> <li>Read subsequence at\nbarcode position</li><li>Y or N indicating if there was a barcode match</li><li>Matched barcode sequence (empty if read\ndid not match one of the barcodes)</li>  <li>The number of mismatches if there was a barcode match</li>  <li>The number\nof mismatches to the second best barcode if there was a barcode match</li>  </ul>If there is no match but we're close to\nthe threshold of calling it a match, we output the barcode that would have been matched but in lower case.  Threshold\nvalues can be adjusted to accommodate barcode sequence mismatches from the reads.  The metrics file produced by the\nExtractIlluminaBarcodes program indicates the number of matches (and mismatches) between the barcode reads and the\nactual barcodes.  These metrics are provided both per-barcode and per lane and can be found in the BaseCalls\ndirectory.</p><p>For poorly matching barcodes, the order of specification of barcodes can cause arbitrary output\ndifferences.</p><h4>Usage example:</h4> <pre>java -jar picard.jar ExtractIlluminaBarcodes \\<br />             \nBASECALLS_DIR=/BaseCalls/ \\<br />              LANE=1 \\<br />          READ_STRUCTURE=25T8B25T \\<br />             \nBARCODE_FILE=barcodes.txt \\<br />              METRICS_FILE=metrics_output.txt </pre>Please see the\nExtractIlluminaBarcodes.BarcodeMetric <a\nhref='http://broadinstitute.github.io/picard/picard-metric-definitions.html#ExtractIlluminaBarcodes.BarcodeMetric'>definitions</a>\nfor a complete description of the metrics produced by this tool.</p><hr />\nVersion:4.1.3.0\n",
        )
