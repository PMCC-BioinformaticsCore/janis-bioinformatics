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


class GatkEstimateLibraryComplexityBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "EstimateLibraryComplexity"

    def friendly_name(self) -> str:
        return "GATK4: EstimateLibraryComplexity"

    def tool(self) -> str:
        return "Gatk4EstimateLibraryComplexity"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) One or more files to combine and estimate library complexity from. Reads can be mapped or unmapped.  This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Output file to writes per-library metrics to. Required."
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
                tag="barcode_tag",
                input_type=String(optional=True),
                prefix="--BARCODE_TAG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Barcode SAM tag (ex. BC for 10X Genomics) Default value: null."
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
                tag="max_diff_rate",
                input_type=Double(optional=True),
                prefix="--MAX_DIFF_RATE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The maximum rate of differences between two reads to call them identical. Default value: 0.03. "
                ),
            ),
            ToolInput(
                tag="max_group_ratio",
                input_type=Int(optional=True),
                prefix="--MAX_GROUP_RATIO",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Do not process self-similar groups that are this many times over the mean expected group size. I.e. if the input contains 10m read pairs and MIN_IDENTICAL_BASES is set to 5, then the mean expected group size would be approximately 10 reads.  Default value: 500. "
                ),
            ),
            ToolInput(
                tag="max_optical_duplicate_set_size",
                input_type=Boolean(optional=True),
                prefix="--MAX_OPTICAL_DUPLICATE_SET_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" This number is the maximum size of a set of duplicate reads for which we will attempt to determine which are optical duplicates.  Please be aware that if you raise this value too high and do encounter a very large set of duplicate reads, it will severely affect the runtime of this tool.  To completely disable this check, set the value to -1.  Default value: 300000. "
                ),
            ),
            ToolInput(
                tag="max_read_length",
                input_type=Int(optional=True),
                prefix="--MAX_READ_LENGTH",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The maximum number of bases to consider when comparing reads (0 means no maximum). Default value: 0. "
                ),
            ),
            ToolInput(
                tag="max_records_in_ram",
                input_type=Int(optional=True),
                prefix="--MAX_RECORDS_IN_RAM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When writing files that need to be sorted, this will specify the number of records stored in RAM before spilling to disk. Increasing this number reduces the number of file handles needed to sort the file, and increases the amount of RAM needed.  Default value: 1971367. "
                ),
            ),
            ToolInput(
                tag="min_group_count",
                input_type=Int(optional=True),
                prefix="--MIN_GROUP_COUNT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Minimum number group count. On a per-library basis, we count the number of groups of duplicates that have a particular size.  Omit from consideration any count that is less than this value.  For example, if we see only one group of duplicates with size 500, we omit it from the metric calculations if MIN_GROUP_COUNT is set to two.  Setting this to two may help remove technical artifacts from the library size calculation, for example, adapter dimers.  Default value: 2. "
                ),
            ),
            ToolInput(
                tag="min_identical_bases",
                input_type=String(optional=True),
                prefix="--MIN_IDENTICAL_BASES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" grouped together for duplicate detection.  In effect total_reads / 4^max_id_bases reads will be compared at a time, so lower numbers will produce more accurate results but consume exponentially more memory and CPU.  Default value: 5. "
                ),
            ),
            ToolInput(
                tag="min_mean_quality",
                input_type=Int(optional=True),
                prefix="--MIN_MEAN_QUALITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The minimum mean quality of the bases in a read pair for the read to be analyzed. Reads with lower average quality are filtered out and not considered in any calculations.  Default value: 20. "
                ),
            ),
            ToolInput(
                tag="optical_duplicate_pixel_distance",
                input_type=Int(optional=True),
                prefix="--OPTICAL_DUPLICATE_PIXEL_DISTANCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The maximum offset between two duplicate clusters in order to consider them optical duplicates. The default is appropriate for unpatterned versions of the Illumina platform. For the patterned flowcell models, 2500 is moreappropriate. For other platforms and models, users should experiment to find what works best.  Default value: 100. "
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
                tag="read_name_regex",
                input_type=String(optional=True),
                prefix="--READ_NAME_REGEX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="MarkDuplicates can use the tile and cluster positions to estimate the rate of optical duplication in addition to the dominant source of duplication, PCR, to provide a more accurate estimation of library size. By default (with no READ_NAME_REGEX specified), MarkDuplicates will attempt to extract coordinates using a split on ':' (see Note below).  Set READ_NAME_REGEX to 'null' to disable optical duplicate detection. Note that without optical duplicate counts, library size estimation will be less accurate. If the read name does not follow a standard Illumina colon-separation convention, but does contain tile and x,y coordinates, a regular expression can be specified to extract three variables: tile/region, x coordinate and y coordinate from a read name. The regular expression must contain three capture groups for the three variables, in order. It must match the entire read name.   e.g. if field names were separated by semi-colon (';') this example regex could be specified      (?:.*;)?([0-9]+)[^;]*;([0-9]+)[^;]*;([0-9]+)[^;]*$ Note that if no READ_NAME_REGEX is specified, the read name is split on ':'.   For 5 element names, the 3rd, 4th and 5th elements are assumed to be tile, x and y values.   For 7 element names (CASAVA 1.8), the 5th, 6th, and 7th elements are assumed to be tile, x and y values.  Default value: <optimized capture of last three ':' separated fields as numeric values>. "
                ),
            ),
            ToolInput(
                tag="read_one_barcode_tag",
                input_type=Boolean(optional=True),
                prefix="--READ_ONE_BARCODE_TAG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: null."),
            ),
            ToolInput(
                tag="read_two_barcode_tag",
                input_type=Boolean(optional=True),
                prefix="--READ_TWO_BARCODE_TAG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: null."),
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:12:08.327701"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:12:08.327702"),
            documentation="b'USAGE: EstimateLibraryComplexity [arguments]\nEstimates the numbers of unique molecules in a sequencing library.  <p>This tool outputs quality metrics for a\nsequencing library preparation.Library complexity refers to the number of unique DNA fragments present in a given\nlibrary.  Reductions in complexity resulting from PCR amplification during library preparation will ultimately\ncompromise downstream analyses via an elevation in the number of duplicate reads.  PCR-associated duplication artifacts\ncan result from: inadequate amounts of starting material (genomic DNA, cDNA, etc.), losses during cleanups, and size\nselection issues.  Duplicate reads can also arise from optical duplicates resulting from sequencing-machine optical\nsensor artifacts.</p>  <p>This tool attempts to estimate library complexity from sequence of read pairs alone.  Reads\nare sorted by the first N bases (5 by default) of the first read and then the first N bases of the second read of a\npair.   Read pairs are considered to be duplicates if they match each other with no gaps and an overall mismatch rate\nless than or equal to MAX_DIFF_RATE (0.03 by default).  Reads of poor quality are filtered out to provide a more\naccurate estimate.  The filtering removes reads with any poor quality bases as defined by a read's MIN_MEAN_QUALITY (20\nis the default value) across either the first or second read.  Unpaired reads are ignored in this computation.</p>\n<p>The algorithm attempts to detect optical duplicates separately from PCR duplicates and excludes these in the\ncalculation of library size.  Also, since there is no alignment information used in this algorithm, an additional filter\nis applied to the data as follows.  After examining all reads, a histogram is built in which the number of reads in a\nduplicate set is compared with the number of of duplicate sets.   All bins that contain exactly one duplicate set are\nthen removed from the histogram as outliers prior to the library size estimation.  </p><h4>Usage example:</h4><pre>java\n-jar picard.jar EstimateLibraryComplexity \\<br />     I=input.bam \\<br />     O=est_lib_complex_metrics.txt</pre>Please\nsee the documentation for the companion <a\nhref='https://broadinstitute.github.io/picard/command-line-overview.html#MarkDuplicates'>MarkDuplicates</a> tool.<hr />\nVersion:4.1.3.0\n",
        )
