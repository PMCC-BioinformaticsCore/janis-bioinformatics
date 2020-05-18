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


class GatkGenomicsDBImportBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "GenomicsDBImport"

    def friendly_name(self) -> str:
        return "GATK4: GenomicsDBImport"

    def tool(self) -> str:
        return "Gatk4GenomicsDBImport"

    def inputs(self):
        return [
            ToolInput(
                tag="genomicsdbUpdateWorkspacePath",
                input_type=String(optional=True),
                prefix="--genomicsdb-update-workspace-path",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Workspace when updating GenomicsDB. Must be a POSIX file system path, but can be a relative path. Use this argument when adding new samples to an existing GenomicsDB workspace or when using the output-interval-list-to-file option. Either this or genomicsdb-workspace-path must be specified. Must point to an existing workspace.  Required.  Cannot be used in conjuction with argument(s) workspace"
                ),
            ),
            ToolInput(
                tag="genomicsdbWorkspacePath",
                input_type=String(optional=True),
                prefix="--genomicsdb-workspace-path",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Workspace for GenomicsDB. Must be a POSIX file system path, but can be a relative path. Use this argument when creating a new GenomicsDB workspace. Either this or genomicsdb-update-workspace-path must be specified. Must be an empty or non-existent directory.  Required.  Cannot be used in conjuction with argument(s) incrementalImportWorkspace intervalListOutputPathString (output-interval-list-to-file)"
                ),
            ),
            ToolInput(
                tag="addOutputSamProgramRecord",
                input_type=Boolean(optional=True),
                prefix="--add-output-sam-program-record",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-add-output-sam-program-record)  If true, adds a PG tag to created SAM/BAM/CRAM files.  Default value: true. Possible values: {true, false} "
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
                tag="batchSize",
                input_type=Int(optional=True),
                prefix="--batch-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Batch size controls the number of samples for which readers are open at once and therefore provides a way to minimize memory consumption. However, it can take longer to complete. Use the consolidate flag if more than a hundred batches were used. This will improve feature read time. batchSize=0 means no batching (i.e. readers for all samples will be opened at once) Defaults to 0  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="cloudIndexPrefetchBuffer",
                input_type=Int(optional=True),
                prefix="--cloud-index-prefetch-buffer",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CIPB)  Size of the cloud-only prefetch buffer (in MB; 0 to disable). Defaults to cloudPrefetchBuffer if unset.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="cloudPrefetchBuffer",
                input_type=Int(optional=True),
                prefix="--cloud-prefetch-buffer",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CPB)  Size of the cloud-only prefetch buffer (in MB; 0 to disable).  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="consolidate",
                input_type=Boolean(optional=True),
                prefix="--consolidate",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-consolidate)  Boolean flag to enable consolidation. If importing data in batches, a new fragment is created for each batch. In case thousands of fragments are created, GenomicsDB feature readers will try to open ~20x as many files. Also, internally GenomicsDB would consume more memory to maintain bookkeeping data from all fragments. Use this flag to merge all fragments into one. Merging can potentially improve read performance, however overall benefit might not be noticeable as the top Java layers have significantly higher overheads. This flag has no effect if only one batch is used. Defaults to false  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="createOutputBamIndex",
                input_type=Boolean(optional=True),
                prefix="--create-output-bam-index",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OBI)  If true, create a BAM/CRAM index when writing a coordinate-sorted BAM/CRAM file.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="createOutputBamMd5",
                input_type=Boolean(optional=True),
                prefix="--create-output-bam-md5",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OBM)  If true, create a MD5 digest for any BAM/SAM/CRAM file created  Default value: false. Possible values: {true, false} "
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
                tag="createOutputVariantMd5",
                input_type=Boolean(optional=True),
                prefix="--create-output-variant-md5",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OVM)  If true, create a a MD5 digest any VCF file created.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="disableBamIndexCaching",
                input_type=Boolean(optional=True),
                prefix="--disable-bam-index-caching",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DBIC)  If true, don't cache bam indexes, this will reduce memory requirements but may harm performance if many intervals are specified.  Caching is automatically disabled if there are no intervals specified.  Default value: false. Possible values: {true, false} "
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
                tag="genomicsdbSegmentSize",
                input_type=Boolean(optional=True),
                prefix="--genomicsdb-segment-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" enough to hold data from one site.  Defaults to 1048576  Default value: 1048576. "
                ),
            ),
            ToolInput(
                tag="genomicsdbVcfBufferSize",
                input_type=Boolean(optional=True),
                prefix="--genomicsdb-vcf-buffer-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-genomicsdb-vcf-buffer-size)  Buffer size in bytes to store variant contexts. Larger values are better as smaller values cause frequent disk writes. Defaults to 16384 which was empirically determined to work well for many inputs.  Default value: 16384. "
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
                tag="inp",
                input_type=String(optional=True),
                prefix="--input",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) BAM/SAM/CRAM file containing reads This argument may be specified 0 or more times. Default value: null. "
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
                tag="lenient",
                input_type=Boolean(optional=True),
                prefix="--lenient",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-LE) Lenient processing of VCF files Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="mergeInputIntervals",
                input_type=Boolean(optional=True),
                prefix="--merge-input-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-merge-input-intervals)  Boolean flag to import all data in between intervals.  Improves performance using large lists of intervals, as in exome sequencing, especially if GVCF data only exists for specified intervals.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="outputIntervalListToFile",
                input_type=String(optional=True),
                prefix="--output-interval-list-to-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-output-interval-list-to-file)  Path to output file where intervals from existing workspace should be written.If this option is specified, the tools outputs the interval_list of the workspace pointed to by genomicsdb-update-workspace-path at the path specified here in a Picard-style interval_list with a sequence dictionary header  Default value: null.  Cannot be used in conjuction with argument(s) workspace"
                ),
            ),
            ToolInput(
                tag="overwriteExistingGenomicsdbWorkspace",
                input_type=Boolean(optional=True),
                prefix="--overwrite-existing-genomicsdb-workspace",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Will overwrite given workspace if it exists. Otherwise a new workspace is created. Cannot be set to true if genomicsdb-update-workspace-path is also set. Defaults to false  Default value: false. Possible values: {true, false} "
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
                tag="secondsBetweenProgressUpdates",
                input_type=Double(optional=True),
                prefix="--seconds-between-progress-updates",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-seconds-between-progress-updates)  Output traversal statistics every time this many seconds elapse  Default value: 10.0. "
                ),
            ),
            ToolInput(
                tag="sequenceDictionary",
                input_type=String(optional=True),
                prefix="--sequence-dictionary",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-sequence-dictionary)  Use the given sequence dictionary as the master/canonical sequence dictionary.  Must be a .dict file.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="sitesOnlyVcfOutput",
                input_type=Boolean(optional=True),
                prefix="--sites-only-vcf-output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If true, don't emit genotype fields when writing vcf file output.  Default value: false. Possible values: {true, false} "
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
                tag="validateSampleNameMap",
                input_type=Boolean(optional=True),
                prefix="--validate-sample-name-map",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-validate-sample-name-map)  Boolean flag to enable checks on the sampleNameMap file. If true, tool checks whetherfeature readers are valid and shows a warning if sample names do not match with the headers. Defaults to false  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="variant",
                input_type=String(optional=True),
                prefix="--variant",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-V) GVCF files to be imported to GenomicsDB. Each file must containdata for only a single sample. Either this or sample-name-map must be specified.  This argument may be specified 0 or more times. Default value: null.  Cannot be used in conjuction with argument(s) sampleNameMapFile"
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
                tag="maxNumIntervalsToImportInParallel",
                input_type=Int(optional=True),
                prefix="--max-num-intervals-to-import-in-parallel",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-max-num-intervals-to-import-in-parallel)  Max number of intervals to import in parallel; higher values may improve performance, but require more memory and a higher number of file descriptors open at the same time  Default value: 1. "
                ),
            ),
            ToolInput(
                tag="readerThreads",
                input_type=Int(optional=True),
                prefix="--reader-threads",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-reader-threads)  How many simultaneous threads to use when opening VCFs in batches; higher values may improve performance when network latency is an issue. Multiple reader threads are not supported when running with multiple intervals.  Default value: 1. "
                ),
            ),
            ToolInput(
                tag="sampleNameMap",
                input_type=String(optional=True),
                prefix="--sample-name-map",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Path to file containing a mapping of sample name to file uri in tab delimited format. If this is specified then the header from the first sample will be treated as the merged header rather than merging the headers, and the sample names will be taken from this file. This may be used to rename input samples. This is a performance optimization that relaxes the normal checks for consistent headers.  Using vcfs with incompatible headers may result in silent data corruption.  Default value: null.  Cannot be used in conjuction with argument(s) variantPaths (V)"
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:01:43.438585"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:01:43.438587"),
            documentation="USAGE: GenomicsDBImport [arguments]\nImport VCFs to GenomicsDB\nVersion:4.1.3.0\n",
        )
