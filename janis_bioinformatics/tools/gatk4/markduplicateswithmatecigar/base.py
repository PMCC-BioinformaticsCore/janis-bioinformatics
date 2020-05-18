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


class GatkMarkDuplicatesWithMateCigarBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "MarkDuplicatesWithMateCigar"

    def friendly_name(self) -> str:
        return "GATK4: MarkDuplicatesWithMateCigar"

    def tool(self) -> str:
        return "Gatk4MarkDuplicatesWithMateCigar"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=String(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) One or more input SAM or BAM files to analyze. Must be coordinate sorted. This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="metrics_file",
                input_type=File(optional=True),
                prefix="--METRICS_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-M) File to write duplication metrics to Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output file to write marked records to Required."
                ),
            ),
            ToolInput(
                tag="add_pg_tag_to_reads",
                input_type=Boolean(optional=True),
                prefix="--ADD_PG_TAG_TO_READS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Default value: true. Possible values: {true, false} "
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
                tag="assume_sort_order",
                input_type=Boolean(optional=True),
                prefix="--ASSUME_SORT_ORDER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ASO)  If not null, assume that the input file has this order even if the header says otherwise.  Default value: null. Possible values: {unsorted, queryname, coordinate, duplicate, unknown}  Cannot be used in conjuction with argument(s) ASSUME_SORTED (AS)"
                ),
            ),
            ToolInput(
                tag="assume_sorted",
                input_type=Boolean(optional=True),
                prefix="--ASSUME_SORTED",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-AS) If true, assume that the input file is coordinate sorted even if the header says otherwise. Deprecated, used ASSUME_SORT_ORDER=coordinate instead.  Default value: false. Possible values: {true, false}  Cannot be used in conjuction with argument(s) ASSUME_SORT_ORDER (ASO) ASSUME_SORT_ORDER (ASO)"
                ),
            ),
            ToolInput(
                tag="block_size",
                input_type=Int(optional=True),
                prefix="--BLOCK_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The block size for use in the coordinate-sorted record buffer. Default value: 100000."
                ),
            ),
            ToolInput(
                tag="comment",
                input_type=String(optional=True),
                prefix="--COMMENT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CO) Comment(s) to include in the output file's header. This argument may be specified 0 or more times. Default value: null. "
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
                tag="duplicate_scoring_strategy",
                input_type=Boolean(optional=True),
                prefix="--DUPLICATE_SCORING_STRATEGY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DS)  The scoring strategy for choosing the non-duplicate among candidates.  Default value: TOTAL_MAPPED_REFERENCE_LENGTH. Possible values: {SUM_OF_BASE_QUALITIES, TOTAL_MAPPED_REFERENCE_LENGTH, RANDOM} "
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
                tag="max_optical_duplicate_set_size",
                input_type=Boolean(optional=True),
                prefix="--MAX_OPTICAL_DUPLICATE_SET_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" This number is the maximum size of a set of duplicate reads for which we will attempt to determine which are optical duplicates.  Please be aware that if you raise this value too high and do encounter a very large set of duplicate reads, it will severely affect the runtime of this tool.  To completely disable this check, set the value to -1.  Default value: 300000. "
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
                tag="minimum_distance",
                input_type=Int(optional=True),
                prefix="--MINIMUM_DISTANCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The minimum distance to buffer records to account for clipping on the 5' end of the records. For a given alignment, this parameter controls the width of the window to search for duplicates of that alignment. Due to 5' read clipping, duplicates do not necessarily have the same 5' alignment coordinates, so the algorithm needs to search around the neighborhood. For single end sequencing data, the neighborhood is only determined by the amount of clipping (assuming no split reads), thus setting MINIMUM_DISTANCE to twice the sequencing read length should be sufficient. For paired end sequencing, the neighborhood is also determined by the fragment insert size, so you may want to set MINIMUM_DISTANCE to something like twice the 99.5% percentile of the fragment insert size distribution (see CollectInsertSizeMetrics). Or you can set this number to -1 to use either a) twice the first read's read length, or b) 100, whichever is smaller. Note that the larger the window, the greater the RAM requirements, so you could run into performance limitations if you use a value that is unnecessarily large.  Default value: -1. "
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
                tag="program_group_command_line",
                input_type=String(optional=True),
                prefix="--PROGRAM_GROUP_COMMAND_LINE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PG_COMMAND)  Value of CL tag of PG record to be created. If not supplied the command line will be detected automatically.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="program_group_name",
                input_type=String(optional=True),
                prefix="--PROGRAM_GROUP_NAME",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PG_NAME)  Value of PN tag of PG record to be created.  Default value: MarkDuplicatesWithMateCigar. "
                ),
            ),
            ToolInput(
                tag="program_group_version",
                input_type=String(optional=True),
                prefix="--PROGRAM_GROUP_VERSION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PG_VERSION)  Value of VN tag of PG record to be created. If not specified, the version will be detected automatically.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="program_record_id",
                input_type=Boolean(optional=True),
                prefix="--PROGRAM_RECORD_ID",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PG)  disable PG record creation.  This string may have a suffix appended to avoid collision with other program record IDs.  Default value: MarkDuplicates. "
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
                tag="reference_sequence",
                input_type=File(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R) Reference sequence file. Default value: null."
                ),
            ),
            ToolInput(
                tag="remove_duplicates",
                input_type=Boolean(optional=True),
                prefix="--REMOVE_DUPLICATES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true do not write duplicates to the output file instead of writing them with appropriate flags set.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="skip_pairs_with_no_mate_cigar",
                input_type=Boolean(optional=True),
                prefix="--SKIP_PAIRS_WITH_NO_MATE_CIGAR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Skip record pairs with no mate cigar and include them in the output.  Default value: true. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:57:41.983077"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:57:41.983078"),
            documentation="b'USAGE: MarkDuplicatesWithMateCigar [arguments]\nIdentifies duplicate reads, accounting for mate CIGAR.  This tool locates and tags duplicate reads (both PCR and\noptical) in a BAM or SAM file, where duplicate reads are defined as originating from the same original fragment of DNA,\ntaking into account the CIGAR string of read mates. <br /><br />It is intended as an improvement upon the original\nMarkDuplicates algorithm, from which it differs in several ways, includingdifferences in how it breaks ties. It may be\nthe most effective duplicate marking program available, as it handles all cases including clipped and gapped alignments\nand locates duplicate molecules using mate cigar information. However, please note that it is not yet used in the\nBroad's production pipeline, so use it at your own risk. <br /><br />Note also that this tool will not work with\nalignments that have large gaps or deletions, such as those from RNA-seq data.  This is due to the need to buffer small\ngenomic windows to ensure integrity of the duplicate marking, while large skips (ex. skipping introns) in the alignment\nrecords would force making that window very large, thus exhausting memory. <br /><p>Note: Metrics labeled as percentages\nare actually expressed as fractions!</p><h4>Usage example:</h4><pre>java -jar picard.jar MarkDuplicatesWithMateCigar\n\\<br />      I=input.bam \\<br />      O=mark_dups_w_mate_cig.bam \\<br />     \nM=mark_dups_w_mate_cig_metrics.txt</pre><hr />\nVersion:4.1.3.0\n",
        )
