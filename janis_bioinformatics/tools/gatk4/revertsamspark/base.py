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


class GatkRevertSamSparkBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "RevertSamSpark"

    def friendly_name(self) -> str:
        return "GATK4: RevertSamSpark"

    def tool(self) -> str:
        return "Gatk4RevertSamSpark"

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
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output SAM/BAM file to create, or an output directory if '--output-by-readgroup' is set.  Required.  Cannot be used in conjuction with argument(s) outputMap"
                ),
            ),
            ToolInput(
                tag="outputMap",
                input_type=String(optional=True),
                prefix="--output-map",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Tab separated file with two columns, OUTPUT_MAP_READ_GROUP_FIELD_NAME and OUTPUT_MAP_OUTPUT_FILE_FIELD_NAME, providing file mapping only used if '--output-by-readgroup' is set.  Required.  Cannot be used in conjuction with argument(s) output (O)"
                ),
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
                tag="attributesToClear",
                input_type=String(optional=True),
                prefix="--attributes-to-clear",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When removing alignment information, the set of optional tags to remove. This argument may be specified 0 or more times. Default value: null. "
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
                tag="disableReadFilter",
                input_type=String(optional=True),
                prefix="--disable-read-filter",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DF)  Read filters to be disabled before analysis  This argument may be specified 0 or more times. Default value: null. Possible Values: {AllowAllReadsReadFilter}"
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
                tag="dontRestoreOriginalQualities",
                input_type=Boolean(optional=True),
                prefix="--dont-restore-original-qualities",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Set to prevent the tool from setting the OQ field to the QUAL where available.  Default value: false. Possible values: {true, false} "
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
                tag="help",
                input_type=Boolean(optional=True),
                prefix="--help",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-h) display the help message Default value: false. Possible values: {true, false}"
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
                tag="keepAlignmentInformation",
                input_type=Boolean(optional=True),
                prefix="--keep-alignment-information",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Don't remove any of the alignment information from the file.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="keepFirstDuplicate",
                input_type=Boolean(optional=True),
                prefix="--keep-first-duplicate",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" R1/R2/unpaired reads respectively. For paired end reads, keeps only the first R1 and R2 found respectively, and discards all unpaired reads. Duplicates do not refer to the duplicate flag in the FLAG field, but instead reads with the same name.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="libraryName",
                input_type=String(optional=True),
                prefix="--library-name",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The library name to use in the reverted output file. This will override the existing sample alias in the file and is used only if all the read groups in the input file have the same library name.  Default value: null. "
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
                tag="outputByReadgroup",
                input_type=Boolean(optional=True),
                prefix="--output-by-readgroup",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(outputs) Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="outputByReadgroupFileFormat",
                input_type=Boolean(optional=True),
                prefix="--output-by-readgroup-file-format",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" When using --output-by-readgroup, the output file format can be set to a certain format.  Default value: dynamic. Possible values: { sam (Generate SAM files.) bam (Generate BAM files.) cram (Generate CRAM files.) dynamic (Generate files based on the extention of input.) } "
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
                tag="programName",
                input_type=String(optional=True),
                prefix="--program-name",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Name of the program running Default value: null."
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
                tag="reference",
                input_type=String(optional=True),
                prefix="--reference",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R) Reference sequence Default value: null."
                ),
            ),
            ToolInput(
                tag="removeDefaultAttributesToClear",
                input_type=Boolean(optional=True),
                prefix="--remove-default-attributes-to-clear",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" When removing alignment information, the set of optional tags to remove.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="removeDuplicateInformation",
                input_type=Boolean(optional=True),
                prefix="--remove-duplicate-information",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" By default we remove duplicate read flags from all reads.  Note that if this is true,  the output may have the unusual but sometimes desirable trait of having unmapped reads that are marked as duplicates.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="sampleAlias",
                input_type=String(optional=True),
                prefix="--sample-alias",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ALIAS) The sample alias to use in the reverted output file. This will override the existing sample alias in the file and is used only if all the read groups in the input file have the same sample alias.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="sanitize",
                input_type=Boolean(optional=True),
                prefix="--sanitize",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="WARNING: This option is potentially destructive. If enabled will discard reads in order to produce a consistent output BAM. Reads discarded include (but are not limited to) paired reads with missing mates, duplicated records, records with mismatches in length of bases and qualities. This option should only be enabled if the output sort order is queryname and will always cause sorting to occur.  Default value: false. Possible values: {true, false} "
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
                tag="sortOrder",
                input_type=Boolean(optional=True),
                prefix="--sort-order",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-SO) The sort order to create the reverted output file with, defaults to whatever is specified in the current file  Default value: queryname. Possible values: {unsorted, queryname, coordinate, duplicate, unknown} "
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
                tag="showhidden",
                input_type=Boolean(optional=True),
                prefix="--showHidden",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-showHidden)  display hidden arguments  Default value: false. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:58:57.253971"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:58:57.253972"),
            documentation="**BETA FEATURE - WORK IN PROGRESS**\nUSAGE: RevertSamSpark [arguments]\nThis tool removes or restores certain properties of the SAM records, including alignment information, which can be used\nto produce an unmapped BAM (uBAM) from a previously aligned BAM. It is also capable of restoring the original quality\nscores of a BAM file that has already undergone base quality score recalibration (BQSR) if theoriginal qualities were\nretained.\n<h3>Examples</h3>\n<h4>Example with single output:</h4>\ngatk RevertSamSpark \\n-I input.bam \\n-O reverted.bam\n<h4>Example outputting by read group with output map:</h4>\ngatk RevertSamSpark \\n-I input.bam \\n--output-by-readgroup \\n--output-map reverted_bam_paths.tsv\nWill output a BAM/SAM file per read group.\n<h4>Example outputting by read group without output map:</h4>\ngatk RevertSamSpark \\n-I input.bam \\n--output-by-readgroup \\n-O /write/reverted/read/group/bams/in/this/dir\nWill output a BAM file per read group. Output format can be overridden with the outputByReadgroupFileFormat option.\nNote: If the program fails due to a SAM validation error, consider setting the VALIDATION_STRINGENCY option to LENIENT\nor SILENT if the failures are expected to be obviated by the reversion process (e.g. invalid alignment information will\nbe obviated when the keep-alignment-information option is used).\nVersion:4.1.3.0\n",
        )
