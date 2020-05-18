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


class GatkIlluminaBasecallsToSamBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "IlluminaBasecallsToSam"

    def friendly_name(self) -> str:
        return "GATK4: IlluminaBasecallsToSam"

    def tool(self) -> str:
        return "Gatk4IlluminaBasecallsToSam"

    def inputs(self):
        return [
            ToolInput(
                tag="barcode_params",
                input_type=File(optional=True),
                prefix="--BARCODE_PARAMS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Deprecated (use LIBRARY_PARAMS). Tab-separated file for creating all output BAMs for barcoded run with single IlluminaBasecallsToSam invocation.  Columns are BARCODE, OUTPUT, SAMPLE_ALIAS, and LIBRARY_NAME.  Row with BARCODE=N is used to specify a file for no barcode match  Required.  Cannot be used in conjuction with argument(s) OUTPUT (O) SAMPLE_ALIAS (ALIAS) LIBRARY_NAME (LIB) LIBRARY_PARAMS"
                ),
            ),
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
                tag="library_params",
                input_type=File(optional=True),
                prefix="--LIBRARY_PARAMS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Tab-separated file for creating all output BAMs for a lane with single IlluminaBasecallsToSam invocation.  The columns are OUTPUT, SAMPLE_ALIAS, and LIBRARY_NAME, BARCODE_1, BARCODE_2 ... BARCODE_X where X = number of barcodes per cluster (optional).  Row with BARCODE_1 set to 'N' is used to specify a file for no barcode match. You may also provide any 2 letter RG header attributes (excluding PU, CN, PL, and DT)  as columns in this file and the values for those columns will be inserted into the RG tag for the BAM file created for a given row.  Required.  Cannot be used in conjuction with argument(s) OUTPUT (O) SAMPLE_ALIAS (ALIAS) LIBRARY_NAME (LIB) BARCODE_PARAMS"
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Deprecated (use LIBRARY_PARAMS). The output SAM or BAM file. Format is determined by extension.  Required.  Cannot be used in conjuction with argument(s) BARCODE_PARAMS LIBRARY_PARAMS"
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
                tag="sample_alias",
                input_type=String(optional=True),
                prefix="--SAMPLE_ALIAS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ALIAS) Deprecated (use LIBRARY_PARAMS). The name of the sequenced sample Required. Cannot be used in conjuction with argument(s) BARCODE_PARAMS LIBRARY_PARAMS"
                ),
            ),
            ToolInput(
                tag="sequencing_center",
                input_type=String(optional=True),
                prefix="--SEQUENCING_CENTER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The name of the sequencing center that produced the reads. Used to set the @RG->CN header tag.  Required. "
                ),
            ),
            ToolInput(
                tag="adapters_to_check",
                input_type=Boolean(optional=True),
                prefix="--ADAPTERS_TO_CHECK",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Which adapters to look for in the read.  This argument may be specified 0 or more times. Default value: [INDEXED, DUAL_INDEXED, NEXTERA_V2, FLUIDIGM]. Possible values: {PAIRED_END, INDEXED, SINGLE_END, NEXTERA_V1, NEXTERA_V2, DUAL_INDEXED, FLUIDIGM, TRUSEQ_SMALLRNA, ALTERNATIVE_SINGLE_END} "
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
                tag="barcode_population_strategy",
                input_type=Boolean(optional=True),
                prefix="--BARCODE_POPULATION_STRATEGY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" When should the sample barcode (as read by the sequencer) be placed on the reads in the BC tag?  Default value: ORPHANS_ONLY. Possible values: { ORPHANS_ONLY (Put barcodes only into the records that were not assigned to any declared barcode.) INEXACT_MATCH (Put barcodes into records for which an exact match with a declared barcode was not found.) ALWAYS (Put barcodes into all the records.) } "
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
                    doc="If set, this is the first tile to be processed (used for debugging). Note that tiles are not processed in numerical order.  Default value: null.  Cannot be used in conjuction with argument(s) PROCESS_SINGLE_TILE"
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
                    doc="(-IGNORE_UNEXPECTED)  Whether to ignore reads whose barcodes are not found in LIBRARY_PARAMS.  Useful when outputting BAMs for only a subset of the barcodes in a lane.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="include_barcode_quality",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_BARCODE_QUALITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Should the barcode quality be included when the sample barcode is included?  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="include_bc_in_rg_tag",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_BC_IN_RG_TAG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" until included in the SAM spec.  Default value: false. Possible values: {true, false} "
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
                tag="library_name",
                input_type=String(optional=True),
                prefix="--LIBRARY_NAME",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-LIB) Deprecated (use LIBRARY_PARAMS). The name of the sequenced library Default value: null. Cannot be used in conjuction with argument(s) BARCODE_PARAMS LIBRARY_PARAMS"
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
                tag="molecular_index_base_quality_tag",
                input_type=String(optional=True),
                prefix="--MOLECULAR_INDEX_BASE_QUALITY_TAG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The tag to use to store any molecular index base qualities.  If more than one molecular index is found, their qualities will be concatenated and stored here (.i.e. the number of 'M' operators in the READ_STRUCTURE)  Default value: QX. "
                ),
            ),
            ToolInput(
                tag="molecular_index_tag",
                input_type=String(optional=True),
                prefix="--MOLECULAR_INDEX_TAG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The tag to use to store any molecular indexes. If more than one molecular index is found, they will be concatenated and stored here.  Default value: RX. "
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
                tag="platform",
                input_type=String(optional=True),
                prefix="--PLATFORM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The name of the sequencing technology that produced the read. Default value: ILLUMINA."
                ),
            ),
            ToolInput(
                tag="process_single_tile",
                input_type=Boolean(optional=True),
                prefix="--PROCESS_SINGLE_TILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(process)  name.  Default value: null.  Cannot be used in conjuction with argument(s) FIRST_TILE"
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
                tag="read_group_id",
                input_type=String(optional=True),
                prefix="--READ_GROUP_ID",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-RG) ID used to link RG header record with RG tag in SAM record. If these are unique in SAM files that get merged, merge performance is better.  If not specified, READ_GROUP_ID will be set to <first 5 chars of RUN_BARCODE>.<LANE> .  Default value: null. "
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
                tag="run_start_date",
                input_type=Boolean(optional=True),
                prefix="--RUN_START_DATE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The start date of the run. Default value: null."
                ),
            ),
            ToolInput(
                tag="tag_per_molecular_index",
                input_type=String(optional=True),
                prefix="--TAG_PER_MOLECULAR_INDEX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The list of tags to store each molecular index.  The number of tags should match the number of molecular indexes.  This argument may be specified 0 or more times. Default value: null. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:04:40.570178"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:04:40.570180"),
            documentation="b'USAGE: IlluminaBasecallsToSam [arguments]\nTransforms raw Illumina sequencing data into an unmapped SAM or BAM file.<p>The IlluminaBaseCallsToSam program collects,\ndemultiplexes, and sorts reads across all of the tiles of a lane via barcode to produce an unmapped SAM/BAM file.  An\nunmapped BAM file is often referred to as a uBAM.  All barcode, sample, and library data is provided in the\nLIBRARY_PARAMS file.  Note, this LIBRARY_PARAMS file should be formatted according to the specifications indicated\nbelow.  The following is an example of a properly formatted LIBRARY_PARAMS\nfile:</p>BARCODE_1\tOUTPUT\tSAMPLE_ALIAS\tLIBRARY_NAME\nAAAAAAAA\tSA_AAAAAAAA.bam\tSA_AAAAAAAA\tLN_AAAAAAAA\nAAAAGAAG\tSA_AAAAGAAG.bam\tSA_AAAAGAAG\tLN_AAAAGAAG\nAACAATGG\tSA_AACAATGG.bam\tSA_AACAATGG\tLN_AACAATGG\nN\tSA_non_indexed.bam\tSA_non_indexed\tLN_NNNNNNNN\n<p>The BARCODES_DIR file is produced by the <a\nhref='http://broadinstitute.github.io/picard/command-line-overview.html#ExtractIlluminaBarcodes'>ExtractIlluminaBarcodes</a>\ntool for each lane of a flow cell.</p>  <h4>Usage example:</h4><pre>java -jar picard.jar IlluminaBasecallsToSam \\<br /> \nBASECALLS_DIR=/BaseCalls/ \\<br />      LANE=001 \\<br />      READ_STRUCTURE=25T8B25T \\<br />      RUN_BARCODE=run15 \\<br\n/>      IGNORE_UNEXPECTED_BARCODES=true \\<br />      LIBRARY_PARAMS=library.params </pre><hr />\nVersion:4.1.3.0\n",
        )
