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


class GatkCollectSamErrorMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectSamErrorMetrics"

    def friendly_name(self) -> str:
        return "GATK4: CollectSamErrorMetrics"

    def tool(self) -> str:
        return "Gatk4CollectSamErrorMetrics"

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
                    doc="(-O) Base name for output files. Actual file names will be generated from the basename and suffixes from the ERROR and STRATIFIER by adding a '.' and then error_by_stratifier[_and_stratifier]* where 'error' is ERROR's extension, and 'stratifier' is STRATIFIER's suffix. For example, an ERROR_METRIC of ERROR:BASE_QUALITY:GC_CONTENT will produce an extension '.error_by_base_quality_and_gc'. The suffixes can be found in the documentation for ERROR_VALUE and SUFFIX_VALUE.  Required. "
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
                tag="vcf",
                input_type=File(optional=True),
                prefix="--VCF",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-V) VCF of known variation for sample. program will skip over polymorphic sites in this VCF and avoid collecting data on these loci.  Required. "
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
                tag="error_metrics",
                input_type=String(optional=True),
                prefix="--ERROR_METRICS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Errors to collect in the form of 'ERROR(:STRATIFIER)*'. To see the values available for ERROR and STRATIFIER look at the documentation for the arguments ERROR_VALUE and STRATIFIER_VALUE.  This argument may be specified 0 or more times. Default value: [ERROR, ERROR:BASE_QUALITY, ERROR:INSERT_LENGTH, ERROR:GC_CONTENT, ERROR:READ_DIRECTION, ERROR:PAIR_ORIENTATION, ERROR:HOMOPOLYMER, ERROR:BINNED_HOMOPOLYMER, ERROR:CYCLE, ERROR:READ_ORDINALITY, ERROR:READ_ORDINALITY:CYCLE, ERROR:READ_ORDINALITY:HOMOPOLYMER, ERROR:READ_ORDINALITY:GC_CONTENT, ERROR:READ_ORDINALITY:PRE_DINUC, ERROR:MAPPING_QUALITY, ERROR:READ_GROUP, ERROR:MISMATCHES_IN_READ, ERROR:ONE_BASE_PADDED_CONTEXT, OVERLAPPING_ERROR, OVERLAPPING_ERROR:BASE_QUALITY, OVERLAPPING_ERROR:INSERT_LENGTH, OVERLAPPING_ERROR:READ_ORDINALITY, OVERLAPPING_ERROR:READ_ORDINALITY:CYCLE, OVERLAPPING_ERROR:READ_ORDINALITY:HOMOPOLYMER, OVERLAPPING_ERROR:READ_ORDINALITY:GC_CONTENT]. "
                ),
            ),
            ToolInput(
                tag="error_value",
                input_type=Boolean(optional=True),
                prefix="--ERROR_VALUE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="A fake argument used to show the options of ERROR (in ERROR_METRICS). Default value: null. Possible values: { ERROR (Collects the average error at the bases provided. Suffix is: 'error'.) OVERLAPPING_ERROR (Only considers bases from the overlapping parts of reads from the same template. For those bases, it calculates the error that can be attributable to pre-sequencing, versus during-sequencing. Suffix is: 'overlapping_error'.) } "
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
                tag="intervals",
                input_type=File(optional=True),
                prefix="--INTERVALS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-L) Region(s) to limit analysis to. Supported formats are VCF or interval_list. Will intersect inputs if multiple are given.   This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="long_homopolymer",
                input_type=String(optional=True),
                prefix="--LONG_HOMOPOLYMER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-LH) Used by the BINNED_HOMOPOLYMER stratifier. Default value: 6. "
                ),
            ),
            ToolInput(
                tag="max_loci",
                input_type=Boolean(optional=True),
                prefix="--MAX_LOCI",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MAX) Maximum number of loci to process (or unlimited if 0). Default value: 0."
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
                tag="min_base_q",
                input_type=Int(optional=True),
                prefix="--MIN_BASE_Q",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-BQ) Minimum base quality to include base. Default value: 20."
                ),
            ),
            ToolInput(
                tag="min_mapping_q",
                input_type=Int(optional=True),
                prefix="--MIN_MAPPING_Q",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MQ) Minimum mapping quality to include read. Default value: 20."
                ),
            ),
            ToolInput(
                tag="prior_q",
                input_type=Int(optional=True),
                prefix="--PRIOR_Q",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PE) The prior error, in phred-scale (used for calculating empirical error rates). Default value: 30. "
                ),
            ),
            ToolInput(
                tag="probability",
                input_type=Double(optional=True),
                prefix="--PROBABILITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-P) The probability of selecting a locus for analysis (for downsampling). Default value: 1.0."
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
                tag="stratifier_value",
                input_type=Boolean(optional=True),
                prefix="--STRATIFIER_VALUE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Default value: null. Possible values: { ALL (Puts all bases in the same stratum. Suffix is 'all'.) GC_CONTENT (The GC-content of the read. Suffix is 'gc'.) READ_ORDINALITY (The read ordinality (i.e. first or second). Suffix is 'read_ordinality'.) READ_BASE (the base in the original reading direction. Suffix is 'read_base'.) READ_DIRECTION (The alignment direction of the read (encoded as + or -). Suffix is 'read_direction'.) PAIR_ORIENTATION (The read-pair's orientation (encoded as '[FR]1[FR]2'). Suffix is 'pair_orientation'.) PAIR_PROPERNESS (The properness of the read-pair's alignment. Looks for indications of chimerism. Suffix is 'pair_proper'.) REFERENCE_BASE (The reference base in the read's direction. Suffix is 'ref_base'.) PRE_DINUC (The read base at the previous cycle, and the current reference base. Suffix is 'pre_dinuc'.) POST_DINUC (The read base at the subsequent cycle, and the current reference base. Suffix is 'post_dinuc'.) HOMOPOLYMER_LENGTH (The length of homopolymer the base is part of (only accounts for bases that were read prior to the current base). Suffix is 'homopolymer_length'.) HOMOPOLYMER (The length of homopolymer, the base that the homopolymer is comprised of, and the reference base. Suffix is 'homopolymer_and_following_ref_base'.) BINNED_HOMOPOLYMER (The scale of homopolymer (long or short), the base that the homopolymer is comprised of, and the reference base. Suffix is 'binned_length_homopolymer_and_following_ref_base'.) FLOWCELL_TILE (The flowcell and tile where the base was read (taken from the read name). Suffix is 'tile'.) READ_GROUP (The read-group id of the read. Suffix is 'read_group'.) CYCLE (The machine cycle during which the base was read. Suffix is 'cycle'.) BINNED_CYCLE (The binned machine cycle. Similar to CYCLE, but binned into 5 evenly spaced ranges across the size of the read.  This stratifier may produce confusing results when used on datasets with variable sized reads. Suffix is 'binned_cycle'.) SOFT_CLIPS (The number of softclipped bases the read has. Suffix is 'softclipped_bases'.) INSERT_LENGTH (The insert-size they came from (taken from the TLEN field.) Suffix is 'insert_length'.) BASE_QUALITY (The base quality. Suffix is 'base_quality'.) MAPPING_QUALITY (The read's mapping quality. Suffix is 'mapping_quality'.) MISMATCHES_IN_READ (The number of bases in the read that mismatch the reference, excluding the current base.  This stratifier requires the NM tag. Suffix is 'mismatches_in_read'.) ONE_BASE_PADDED_CONTEXT (The current reference base and a one base padded region from the read resulting in a 3-base context. Suffix is 'one_base_padded_context'.) TWO_BASE_PADDED_CONTEXT (The current reference base and a two base padded region from the read resulting in a 5-base context. Suffix is 'two_base_padded_context'.) CONSENSUS (Whether or not duplicate reads were used to form a consensus read.  This stratifier makes use of the aD, bD, and cD tags for duplex consensus reads.  If the reads are single index consensus, only the cD tags are used. Suffix is 'consensus'.) NS_IN_READ (The number of Ns in the read. Suffix is 'ns_in_read'.) } "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:10:48.160098"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:10:48.160099"),
            documentation="b'USAGE: CollectSamErrorMetrics [arguments]\nProgram to collect error metrics on bases stratified in various ways.\n<p>Sequencing errors come in different 'flavors'. For example, some occur during sequencing while others happen during\nlibrary construction, prior to the sequencing. They may be correlated with various aspect of the sequencing experiment:\nposition in the read, base context, length of insert and so on.\n<p>This program collects two different kinds of error metrics (one which attempts to distinguish between pre- and post-\nsequencer errors, and on which doesn't) and a collation of 'stratifiers' each of which assigns bases into various bins.\nThe stratifiers can be used together to generate a composite stratification. <p>For example:<p>The BASE_QUALITY\nstratifier will place bases in bins according to their declared base quality. The READ_ORDINALITY stratifier will place\nbases in one of two bins depending on whether their read is 'first' or 'second'. One could generate a composite\nstratifier BASE_QUALITY:READ_ORDINALITY which will do both stratifications as the same time. \n<p>The resulting metric file will be named according to a provided prefix and a suffix which is generated  automatically\naccording to the error metric. The tool can collect multiple metrics in a single pass and there should be hardly any\nperformance loss when specifying multiple metrics at the same time; the default includes a large collection of metrics. \n<p>To estimate the error rate the tool assumes that all differences from the reference are errors. For this to be a\nreasonable assumption the tool needs to know the sites at which the sample is actually polymorphic and a confidence\ninterval where the user is relatively certain that the polymorphic sites are known and accurate. These two inputs are\nprovided as a VCF and INTERVALS. The program will only process sites that are in the intersection of the interval lists\nin the INTERVALS argument as long as they are not polymorphic in the VCF.\nVersion:4.1.3.0\n",
        )
