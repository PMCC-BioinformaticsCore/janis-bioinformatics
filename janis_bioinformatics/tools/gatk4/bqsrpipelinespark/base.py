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


class GatkBQSRPipelineSparkBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "BQSRPipelineSpark"

    def friendly_name(self) -> str:
        return "GATK4: BQSRPipelineSpark"

    def tool(self) -> str:
        return "Gatk4BQSRPipelineSpark"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=String(optional=True),
                prefix="--input",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) BAM/SAM/CRAM file containing reads This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="knownSites",
                input_type=String(optional=True),
                prefix="--known-sites",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="the known variants This argument must be specified at least once. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-O) the output bam Required."),
            ),
            ToolInput(
                tag="reference",
                input_type=String(optional=True),
                prefix="--reference",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-R) Reference sequence file Required."),
            ),
            ToolInput(
                tag="addOutputVcfCommandLine",
                input_type=Boolean(optional=True),
                prefix="--add-output-vcf-command-line",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-add-output-vcf-command-line)  If true, adds a command line header line to created VCF files.  Default value: true. Possible values: {true, false} "
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
                tag="bamPartitionSize",
                input_type=Boolean(optional=True),
                prefix="--bam-partition-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="maximum number of bytes to read from a file into each partition of reads. Setting this higher will result in fewer partitions. Note that this will not be equal to the size of the partition in memory. Defaults to 0, which uses the default split size (determined by the Hadoop input format, typically the size of one HDFS block).  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="binaryTagName",
                input_type=String(optional=True),
                prefix="--binary-tag-name",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="the binary tag covariate name if using it Default value: null."
                ),
            ),
            ToolInput(
                tag="bqsrBaqGapOpenPenalty",
                input_type=Double(optional=True),
                prefix="--bqsr-baq-gap-open-penalty",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" BQSR BAQ gap open penalty (Phred Scaled).  Default value is 40.  30 is perhaps better for whole genome call sets  Default value: 40.0. "
                ),
            ),
            ToolInput(
                tag="conf",
                input_type=String(optional=True),
                prefix="--conf",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Spark properties to set on the Spark context in the format <property>=<value> This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="createOutputBamIndex",
                input_type=Boolean(optional=True),
                prefix="--create-output-bam-index",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OBI)  If true, create a BAM index when writing a coordinate-sorted BAM file.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="createOutputBamSplittingIndex",
                input_type=Boolean(optional=True),
                prefix="--create-output-bam-splitting-index",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If true, create a BAM splitting index (SBI) when writing a coordinate-sorted BAM file.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="createOutputVariantIndex",
                input_type=Boolean(optional=True),
                prefix="--create-output-variant-index",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OVI)  If true, create a VCF index when writing a coordinate-sorted VCF file.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="defaultBaseQualities",
                input_type=Boolean(optional=True),
                prefix="--default-base-qualities",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: -1."),
            ),
            ToolInput(
                tag="deletionsDefaultQuality",
                input_type=Boolean(optional=True),
                prefix="--deletions-default-quality",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" default quality for the base deletions covariate  Default value: 45. "
                ),
            ),
            ToolInput(
                tag="disableReadFilter",
                input_type=String(optional=True),
                prefix="--disable-read-filter",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DF)  Read filters to be disabled before analysis  This argument may be specified 0 or more times. Default value: null. Possible Values: {WellformedReadFilter}"
                ),
            ),
            ToolInput(
                tag="disableSequenceDictionaryValidation",
                input_type=Boolean(optional=True),
                prefix="--disable-sequence-dictionary-validation",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-disable-sequence-dictionary-validation)  If specified, do not check the sequence dictionaries from our inputs for compatibility. Use at your own risk!  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="emitOriginalQuals",
                input_type=Boolean(optional=True),
                prefix="--emit-original-quals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="excludeIntervals",
                input_type=Boolean(optional=True),
                prefix="--exclude-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-XL) This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="gatkConfigFile",
                input_type=String(optional=True),
                prefix="--gatk-config-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="A configuration file to use with the GATK. Default value: null."
                ),
            ),
            ToolInput(
                tag="gcsMaxRetries",
                input_type=Int(optional=True),
                prefix="--gcs-max-retries",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-gcs-retries)  If the GCS bucket channel errors out, how many times it will attempt to re-initiate the connection  Default value: 20. "
                ),
            ),
            ToolInput(
                tag="gcsProjectForRequesterPays",
                input_type=String(optional=True),
                prefix="--gcs-project-for-requester-pays",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Project to bill when accessing 'requester pays' buckets. If unset, these buckets cannot be accessed.  Default value: . "
                ),
            ),
            ToolInput(
                tag="globalQscorePrior",
                input_type=Double(optional=True),
                prefix="--global-qscore-prior",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Global Qscore Bayesian prior to use for BQSR Default value: -1.0."
                ),
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
                tag="indelsContextSize",
                input_type=Int(optional=True),
                prefix="--indels-context-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ics)  Size of the k-mer context to be used for base insertions and deletions  Default value: 3. "
                ),
            ),
            ToolInput(
                tag="insertionsDefaultQuality",
                input_type=Boolean(optional=True),
                prefix="--insertions-default-quality",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" default quality for the base insertions covariate  Default value: 45. "
                ),
            ),
            ToolInput(
                tag="intervalExclusionPadding",
                input_type=Int(optional=True),
                prefix="--interval-exclusion-padding",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ixp)  Amount of padding (in bp) to add to each interval you are excluding.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="intervalMergingRule",
                input_type=Boolean(optional=True),
                prefix="--interval-merging-rule",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-imr)  Interval merging rule for abutting intervals  Default value: ALL. Possible values: {ALL, OVERLAPPING_ONLY} "
                ),
            ),
            ToolInput(
                tag="intervalPadding",
                input_type=Boolean(optional=True),
                prefix="--interval-padding",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-ip) Default value: 0."),
            ),
            ToolInput(
                tag="intervalSetRule",
                input_type=Boolean(optional=True),
                prefix="--interval-set-rule",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-isr)  Set merging approach to use for combining interval inputs  Default value: UNION. Possible values: {UNION, INTERSECTION} "
                ),
            ),
            ToolInput(
                tag="intervals",
                input_type=String(optional=True),
                prefix="--intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-L) One or more genomic intervals over which to operate This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="lowQualityTail",
                input_type=Boolean(optional=True),
                prefix="--low-quality-tail",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="minimum quality for the bases in the tail of the reads to be considered Default value: 2."
                ),
            ),
            ToolInput(
                tag="maximumCycleValue",
                input_type=Int(optional=True),
                prefix="--maximum-cycle-value",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-max-cycle)  The maximum cycle value permitted for the Cycle covariate  Default value: 500. "
                ),
            ),
            ToolInput(
                tag="mismatchesContextSize",
                input_type=Int(optional=True),
                prefix="--mismatches-context-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-mcs)  Size of the k-mer context to be used for base mismatches  Default value: 2. "
                ),
            ),
            ToolInput(
                tag="mismatchesDefaultQuality",
                input_type=Boolean(optional=True),
                prefix="--mismatches-default-quality",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" default quality for the base mismatches covariate  Default value: -1. "
                ),
            ),
            ToolInput(
                tag="numReducers",
                input_type=Int(optional=True),
                prefix="--num-reducers",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="For tools that shuffle data or write an output, sets the number of reducers. Defaults to 0, which gives one partition per 10MB of input.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="outputShardTmpDir",
                input_type=Boolean(optional=True),
                prefix="--output-shard-tmp-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(in)  intermediate output shards, if not specified .parts/ will be used  Default value: null.  Cannot be used in conjuction with argument(s) shardedOutput"
                ),
            ),
            ToolInput(
                tag="preserveQscoresLessThan",
                input_type=Int(optional=True),
                prefix="--preserve-qscores-less-than",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Don't recalibrate bases with quality scores less than this threshold (with -bqsr)  Default value: 6. "
                ),
            ),
            ToolInput(
                tag="programName",
                input_type=String(optional=True),
                prefix="--program-name",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Name of the program running Default value: null."
                ),
            ),
            ToolInput(
                tag="quantizeQuals",
                input_type=Int(optional=True),
                prefix="--quantize-quals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Quantize quality scores to a given number of levels Default value: 0. Cannot be used in conjuction with argument(s) staticQuantizationQuals roundDown"
                ),
            ),
            ToolInput(
                tag="quantizingLevels",
                input_type=Int(optional=True),
                prefix="--quantizing-levels",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="number of distinct quality scores in the quantized output Default value: 16."
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
                tag="readFilter",
                input_type=String(optional=True),
                prefix="--read-filter",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-RF) Read filters to be applied before analysis This argument may be specified 0 or more times. Default value: null. Possible Values: {AlignmentAgreesWithHeaderReadFilter, AllowAllReadsReadFilter, AmbiguousBaseReadFilter, CigarContainsNoNOperator, FirstOfPairReadFilter, FragmentLengthReadFilter, GoodCigarReadFilter, HasReadGroupReadFilter, IntervalOverlapReadFilter, LibraryReadFilter, MappedReadFilter, MappingQualityAvailableReadFilter, MappingQualityNotZeroReadFilter, MappingQualityReadFilter, MatchingBasesAndQualsReadFilter, MateDifferentStrandReadFilter, MateOnSameContigOrNoMappedMateReadFilter, MateUnmappedAndUnmappedReadFilter, MetricsReadFilter, NonChimericOriginalAlignmentReadFilter, NonZeroFragmentLengthReadFilter, NonZeroReferenceLengthAlignmentReadFilter, NotDuplicateReadFilter, NotOpticalDuplicateReadFilter, NotSecondaryAlignmentReadFilter, NotSupplementaryAlignmentReadFilter, OverclippedReadFilter, PairedReadFilter, PassesVendorQualityCheckReadFilter, PlatformReadFilter, PlatformUnitReadFilter, PrimaryLineReadFilter, ProperlyPairedReadFilter, ReadGroupBlackListReadFilter, ReadGroupReadFilter, ReadLengthEqualsCigarLengthReadFilter, ReadLengthReadFilter, ReadNameReadFilter, ReadStrandFilter, SampleReadFilter, SecondOfPairReadFilter, SeqIsStoredReadFilter, SoftClippedReadFilter, ValidAlignmentEndReadFilter, ValidAlignmentStartReadFilter, WellformedReadFilter}"
                ),
            ),
            ToolInput(
                tag="readIndex",
                input_type=String(optional=True),
                prefix="--read-index",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-read-index)  Indices to use for the read inputs. If specified, an index must be provided for every read input and in the same order as the read inputs. If this argument is not specified, the path to the index for each input will be inferred automatically.  This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="readValidationStringency",
                input_type=Boolean(optional=True),
                prefix="--read-validation-stringency",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-VS)  Validation stringency for all SAM/BAM/CRAM/SRA files read by this program.  The default stringency value SILENT can improve performance when processing a BAM file in which variable-length data (read, qualities, tags) do not otherwise need to be decoded.  Default value: SILENT. Possible values: {STRICT, LENIENT, SILENT} "
                ),
            ),
            ToolInput(
                tag="shardedOutput",
                input_type=Boolean(optional=True),
                prefix="--sharded-output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="For tools that write an output, write the output in multiple pieces (shards) Default value: false. Possible values: {true, false}  Cannot be used in conjuction with argument(s) shardedPartsDir"
                ),
            ),
            ToolInput(
                tag="sparkMaster",
                input_type=String(optional=True),
                prefix="--spark-master",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="URL of the Spark Master to submit jobs to when using the Spark pipeline runner. Default value: local[*]. "
                ),
            ),
            ToolInput(
                tag="sparkVerbosity",
                input_type=String(optional=True),
                prefix="--spark-verbosity",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Spark verbosity. Overrides --verbosity for Spark-generated logs only. Possible values: {ALL, DEBUG, INFO, WARN, ERROR, FATAL, OFF, TRACE}  Default value: null. "
                ),
            ),
            ToolInput(
                tag="tmpDir",
                input_type=Boolean(optional=True),
                prefix="--tmp-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Temp directory to use. Default value: null."
                ),
            ),
            ToolInput(
                tag="useJdkDeflater",
                input_type=Boolean(optional=True),
                prefix="--use-jdk-deflater",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-jdk-deflater)  Whether to use the JdkDeflater (as opposed to IntelDeflater)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="useJdkInflater",
                input_type=Boolean(optional=True),
                prefix="--use-jdk-inflater",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-jdk-inflater)  Whether to use the JdkInflater (as opposed to IntelInflater)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="useNio",
                input_type=Boolean(optional=True),
                prefix="--use-nio",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to use NIO or the Hadoop filesystem (default) for reading files. (Note that the Hadoop filesystem is always used for writing files.)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="useOriginalQualities",
                input_type=Boolean(optional=True),
                prefix="--use-original-qualities",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OQ)  Use the base quality scores from the OQ tag  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="verbosity",
                input_type=Boolean(optional=True),
                prefix="--verbosity",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-verbosity)  Control verbosity of logging.  Default value: INFO. Possible values: {ERROR, WARNING, INFO, DEBUG} "
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
                tag="disableToolDefaultReadFilters",
                input_type=Boolean(optional=True),
                prefix="--disable-tool-default-read-filters",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-disable-tool-default-read-filters)  Disable all tool default read filters (WARNING: many tools will not function correctly without their default read filters on)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="roundDownQuantized",
                input_type=String(optional=True),
                prefix="--round-down-quantized",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Default value: false. Possible values: {true, false}  Cannot be used in conjuction with argument(s) quantizationLevels"
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
            ToolInput(
                tag="staticQuantizedQuals",
                input_type=Int(optional=True),
                prefix="--static-quantized-quals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Use static quantized quality scores to a given number of levels (with -bqsr)  This argument may be specified 0 or more times. Default value: null.  Cannot be used in conjuction with argument(s) quantizationLevels"
                ),
            ),
            ToolInput(
                tag="ambigFilterBases",
                input_type=Int(optional=True),
                prefix="--ambig-filter-bases",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Threshold number of ambiguous bases. If null, uses threshold fraction; otherwise, overrides threshold fraction.  Default value: null.  Cannot be used in conjuction with argument(s) maxAmbiguousBaseFraction"
                ),
            ),
            ToolInput(
                tag="ambigFilterFrac",
                input_type=Double(optional=True),
                prefix="--ambig-filter-frac",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Threshold fraction of ambiguous bases Default value: 0.05. Cannot be used in conjuction with argument(s) maxAmbiguousBases"
                ),
            ),
            ToolInput(
                tag="maxFragmentLength",
                input_type=Boolean(optional=True),
                prefix="--max-fragment-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 1000000."),
            ),
            ToolInput(
                tag="minFragmentLength",
                input_type=Boolean(optional=True),
                prefix="--min-fragment-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 0."),
            ),
            ToolInput(
                tag="keepIntervals",
                input_type=String(optional=True),
                prefix="--keep-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="One or more genomic intervals to keep This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="library",
                input_type=String(optional=True),
                prefix="--library",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-library) Name of the library to keep This argument must be specified at least once. Required."
                ),
            ),
            ToolInput(
                tag="maximumMappingQuality",
                input_type=Int(optional=True),
                prefix="--maximum-mapping-quality",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum mapping quality to keep (inclusive)  Default value: null. "
                ),
            ),
            ToolInput(
                tag="minimumMappingQuality",
                input_type=Int(optional=True),
                prefix="--minimum-mapping-quality",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum mapping quality to keep (inclusive)  Default value: 10. "
                ),
            ),
            ToolInput(
                tag="dontRequireSoftClipsBothEnds",
                input_type=Boolean(optional=True),
                prefix="--dont-require-soft-clips-both-ends",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Allow a read to be filtered out based on having only 1 soft-clipped block. By default, both ends must have a soft-clipped block, setting this flag requires only 1 soft-clipped block  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="filterTooShort",
                input_type=Int(optional=True),
                prefix="--filter-too-short",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Minimum number of aligned bases Default value: 30."
                ),
            ),
            ToolInput(
                tag="platformFilterName",
                input_type=Boolean(optional=True),
                prefix="--platform-filter-name",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="This argument must be specified at least once. Required."
                ),
            ),
            ToolInput(
                tag="blackListedLanes",
                input_type=String(optional=True),
                prefix="--black-listed-lanes",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Platform unit (PU) to filter out This argument must be specified at least once. Required."
                ),
            ),
            ToolInput(
                tag="readGroupBlackList",
                input_type=Boolean(optional=True),
                prefix="--read-group-black-list",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="keepReadGroup",
                input_type=String(optional=True),
                prefix="--keep-read-group",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The name of the read group to keep Required."
                ),
            ),
            ToolInput(
                tag="maxReadLength",
                input_type=Int(optional=True),
                prefix="--max-read-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Keep only reads with length at most equal to the specified value Required."
                ),
            ),
            ToolInput(
                tag="minReadLength",
                input_type=Int(optional=True),
                prefix="--min-read-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Keep only reads with length at least equal to the specified value Default value: 1."
                ),
            ),
            ToolInput(
                tag="readName",
                input_type=String(optional=True),
                prefix="--read-name",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Keep only reads with this read name Required."
                ),
            ),
            ToolInput(
                tag="keepReverseStrandOnly",
                input_type=Boolean(optional=True),
                prefix="--keep-reverse-strand-only",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Keep only reads on the reverse strand  Required. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="sample",
                input_type=String(optional=True),
                prefix="--sample",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-sample) The name of the sample(s) to keep, filtering out all others This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="invertSoftClipRatioFilter",
                input_type=Boolean(optional=True),
                prefix="--invert-soft-clip-ratio-filter",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Inverts the results from this filter, causing all variants that would pass to fail and visa-versa.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="softClippedLeadingTrailingRatio",
                input_type=Double(optional=True),
                prefix="--soft-clipped-leading-trailing-ratio",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Threshold ratio of soft clipped bases (leading / trailing the cigar string) to total bases in read for read to be filtered.  Default value: null.  Cannot be used in conjuction with argument(s) minimumSoftClippedRatio"
                ),
            ),
            ToolInput(
                tag="softClippedRatioThreshold",
                input_type=Double(optional=True),
                prefix="--soft-clipped-ratio-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Threshold ratio of soft clipped bases (anywhere in the cigar string) to total bases in read for read to be filtered.  Default value: null.  Cannot be used in conjuction with argument(s) minimumLeadingTrailingSoftClippedRatio"
                ),
            ),
        ]

    def outputs(self):
        return []

    def metadata(self):
        return ToolMetadata(
            contributors=[],
            dateCreated=datetime.fromisoformat("2020-05-18T14:55:47.477401"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:55:47.477402"),
            documentation="**BETA FEATURE - WORK IN PROGRESS**\nUSAGE: BQSRPipelineSpark [arguments]\nThis tools performs 2 steps of BQSR - creation of recalibration tables and rewriting of the bam, without writing the\ntables to disk. \nVersion:4.1.3.0\n",
        )
