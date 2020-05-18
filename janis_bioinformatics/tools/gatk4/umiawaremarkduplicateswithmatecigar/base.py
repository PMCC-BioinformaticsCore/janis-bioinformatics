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


class GatkUmiAwareMarkDuplicatesWithMateCigarBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "UmiAwareMarkDuplicatesWithMateCigar"

    def friendly_name(self) -> str:
        return "GATK4: UmiAwareMarkDuplicatesWithMateCigar"

    def tool(self) -> str:
        return "Gatk4UmiAwareMarkDuplicatesWithMateCigar"

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
                tag="umi_metrics_file",
                input_type=File(optional=True),
                prefix="--UMI_METRICS_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-UMI_METRICS)  UMI Metrics  Required. "),
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
                tag="allow_missing_umis",
                input_type=Boolean(optional=True),
                prefix="--ALLOW_MISSING_UMIS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="FOR TESTING ONLY: allow for missing UMIs if data doesn't have UMIs. This option is intended to be used ONLY for testing the code. Use MarkDuplicatesWithMateCigar if data has no UMIs. Mixed data (where some reads have UMIs and others do not) is not supported.  Default value: false. Possible values: {true, false} "
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
                tag="barcode_tag",
                input_type=String(optional=True),
                prefix="--BARCODE_TAG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Barcode SAM tag (ex. BC for 10X Genomics) Default value: null."
                ),
            ),
            ToolInput(
                tag="clear_dt",
                input_type=Boolean(optional=True),
                prefix="--CLEAR_DT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Clear DT tag from input SAM records. Should be set to false if input SAM doesn't have this tag.  Default true  Default value: true. Possible values: {true, false} "
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
                tag="duplex_umi",
                input_type=Boolean(optional=True),
                prefix="--DUPLEX_UMI",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Treat UMIs as being duplex stranded. This option requires that the UMI consist of two equal length strings that are separated by a hyphen (e.g. 'ATC-GTC'). Reads are considered duplicates if, in addition to standard definition, have identical normalized UMIs.  A UMI from the 'bottom' strand is normalized by swapping its content around the hyphen (eg. ATC-GTC becomes GTC-ATC).  A UMI from the 'top' strand is already normalized as it is. Both reads from a read pair considered top strand if the read 1 unclipped 5' coordinate is less than the read 2 unclipped 5' coordinate. All chimeric reads and read fragments are treated as having come from the top strand. With this option is it required that the BARCODE_TAG hold non-normalized UMIs. Default false.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="duplicate_scoring_strategy",
                input_type=Boolean(optional=True),
                prefix="--DUPLICATE_SCORING_STRATEGY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DS)  The scoring strategy for choosing the non-duplicate among candidates.  Default value: SUM_OF_BASE_QUALITIES. Possible values: {SUM_OF_BASE_QUALITIES, TOTAL_MAPPED_REFERENCE_LENGTH, RANDOM} "
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
                tag="max_edit_distance_to_join",
                input_type=Int(optional=True),
                prefix="--MAX_EDIT_DISTANCE_TO_JOIN",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MAX_EDIT_DISTANCE_TO_JOIN)  Largest edit distance that UMIs must have in order to be considered as coming from distinct source molecules.  Default value: 1. "
                ),
            ),
            ToolInput(
                tag="max_file_handles_for_read_ends_map",
                input_type=Int(optional=True),
                prefix="--MAX_FILE_HANDLES_FOR_READ_ENDS_MAP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MAX_FILE_HANDLES)  Maximum number of file handles to keep open when spilling read ends to disk. Set this number a little lower than the per-process maximum number of file that may be open. This number can be found by executing the 'ulimit -n' command on a Unix system.  Default value: 8000. "
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
                tag="max_sequences_for_disk_read_ends_map",
                input_type=Int(optional=True),
                prefix="--MAX_SEQUENCES_FOR_DISK_READ_ENDS_MAP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MAX_SEQS)  This option is obsolete. ReadEnds will always be spilled to disk.  Default value: 50000. "
                ),
            ),
            ToolInput(
                tag="molecular_identifier_tag",
                input_type=String(optional=True),
                prefix="--MOLECULAR_IDENTIFIER_TAG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" SAM tag to uniquely identify the molecule from which a read was derived.  Use of this option requires that the BARCODE_TAG option be set to a non null value.  Default null.  Default value: null. "
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
                    doc="(-PG_NAME)  Value of PN tag of PG record to be created.  Default value: UmiAwareMarkDuplicatesWithMateCigar. "
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
                tag="remove_duplicates",
                input_type=Boolean(optional=True),
                prefix="--REMOVE_DUPLICATES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true do not write duplicates to the output file instead of writing them with appropriate flags set.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="remove_sequencing_duplicates",
                input_type=Boolean(optional=True),
                prefix="--REMOVE_SEQUENCING_DUPLICATES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If true remove 'optical' duplicates and other duplicates that appear to have arisen from the sequencing process instead of the library preparation process, even if REMOVE_DUPLICATES is false. If REMOVE_DUPLICATES is true, all duplicates are removed and this option is ignored.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="sorting_collection_size_ratio",
                input_type=Double(optional=True),
                prefix="--SORTING_COLLECTION_SIZE_RATIO",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" This number, plus the maximum RAM available to the JVM, determine the memory footprint used by some of the sorting collections.  If you are running out of memory, try reducing this number.  Default value: 0.25. "
                ),
            ),
            ToolInput(
                tag="tag_duplicate_set_members",
                input_type=Boolean(optional=True),
                prefix="--TAG_DUPLICATE_SET_MEMBERS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If a read appears in a duplicate set, add two tags. The first tag, DUPLICATE_SET_SIZE_TAG (DS), indicates the size of the duplicate set. The smallest possible DS value is 2 which occurs when two reads map to the same portion of the reference only one of which is marked as duplicate. The second tag, DUPLICATE_SET_INDEX_TAG (DI), represents a unique identifier for the duplicate set to which the record belongs. This identifier is the index-in-file of the representative read that was selected out of the duplicate set.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="tagging_policy",
                input_type=Boolean(optional=True),
                prefix="--TAGGING_POLICY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Determines how duplicate types are recorded in the DT optional attribute.  Default value: DontTag. Possible values: {DontTag, OpticalOnly, All} "
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
                tag="umi_tag_name",
                input_type=String(optional=True),
                prefix="--UMI_TAG_NAME",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-UMI_TAG_NAME)  Tag name to use for UMI  Default value: RX. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:00:16.989398"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:00:16.989399"),
            documentation="b'\n**EXPERIMENTAL FEATURE - USE AT YOUR OWN RISK**\nUSAGE: UmiAwareMarkDuplicatesWithMateCigar [arguments]\nIdentifies duplicate reads using information from read positions and UMIs. <p>This tool locates and tags duplicate reads\nin a BAM or SAM file, where duplicate reads aredefined as originating from a single fragment of DNA. It is based on the\n{@link MarkDuplicatesWithMateCigar} tool, with added logicto leverage Unique Molecular Identifier (UMI)\ninformation.</p><p>It makes use of the fact that duplicate sets with UMIs can be broken up into subsets based\noninformation contained in the UMI.  In addition to assuming that all members of a duplicate set must have the same\nstart and end position, it imposes thatthey must also have sufficiently similar UMIs. In this context, 'sufficiently\nsimilar' is parameterized by the command lineargument MAX_EDIT_DISTANCE_TO_JOIN, which sets the edit distance between\nUMIs that will be considered to be part of the sameoriginal molecule. This logic allows for sequencing errors in\nUMIs.</p><p> If UMIs contain dashes, the dashes will be ignored. If UMIs contain Ns, these UMIs will not contribute to\nUMI metricsassociated with each record. If the MAX_EDIT_DISTANCE_TO_JOIN allows, UMIs with Ns will be included in the\nduplicate set andthe UMI metrics associated with each duplicate set. Ns are counted as an edit distance from other bases\n{ATCG}, but are notconsidered different from each other.</p><p>This tool is NOT intended to be used on data without\nUMIs; for marking duplicates in non-UMI data, see {@link MarkDuplicates} or{@link MarkDuplicatesWithMateCigar}. Mixed\ndata (where some reads have UMIs and others do not) is not supported.</p><p>Note also that this tool will not work with\nalignments that have large gaps or deletions, such as those from RNA-seq data.This is due to the need to buffer small\ngenomic windows to ensure integrity of the duplicate marking, while large skips(ex. skipping introns) in the alignment\nrecords would force making that window very large, thus exhausting memory. </p><p>Note: Metrics labeled as percentages\nare actually expressed as fractions!</p><h4>Usage example:</h4><pre>java -jar picard.jar\nUmiAwareMarkDuplicatesWithMateCigar <br />      I=input.bam <br />      O=output.bam <br />     \nM=output_duplicate_metrics.txt <br />      UMI_METRICS=output_umi_metrics.txt</pre><hr />\nVersion:4.1.3.0\n",
        )
