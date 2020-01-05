from datetime import datetime

from janis_core import (
    CommandTool,
    ToolInput,
    File,
    Boolean,
    String,
    Int,
    ToolMetadata,
    Double,
    Filename,
    ToolOutput,
    InputSelector,
)
from janis_bioinformatics.tools.gatk4.gatk4toolbase import Gatk4ToolBase

from janis_bioinformatics.data_types import FastaWithDict, Bed, BamBai


class Gatk4SplitReadsBase(Gatk4ToolBase):
    def friendly_name(self) -> str:
        return "GATK4: SplitReads"

    def tool(self) -> str:
        return "Gatk4SplitReads"

    @classmethod
    def gatk_command(cls):
        return "SplitReads"

    def inputs(self):
        return [
            ToolInput(
                "outputFilename",
                String,
                prefix="--output",
                default=".",
                doc="The directory to output SAM/BAM/CRAM files. Default value: '.' ",
            ),
            ToolInput(
                "bam",
                BamBai,
                prefix="--input",
                position=1,
                secondaries_present_as={".bai": "^.bai"},
                doc="(-I:String) BAM/SAM/CRAM file containing reads  This argument must be specified at least once.",
            ),
            ToolInput(
                tag="intervals",
                input_type=Bed(optional=True),
                prefix="--intervals",
                doc="(-L:String) One or more genomic intervals over which to operate This argument may be specified 0 or more times. Default value: null. ",
            ),
            *Gatk4SplitReadsBase.additional_args,
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                BamBai,
                glob=InputSelector("bam", use_basename=True),
                doc="Bam",
                secondaries_present_as={".bai": "^.bai"},
            )
        ]

    def metadata(self):
        return ToolMetadata(
            dateCreated=datetime.fromisoformat("2019-09-16T15:53:15.813130"),
            dateUpdated=datetime.fromisoformat("2019-09-16T15:53:15.813131"),
            documentation="USAGE: SplitReads [arguments]\nOutputs reads from a SAM/BAM/CRAM by read group, sample and library name\nVersion:4.1.3.0",
        )

    additional_args = [
        ToolInput(
            tag="addOutputSamProgramRecord",
            input_type=Boolean(optional=True),
            prefix="-add-output-sam-program-record",
            doc="(--add-output-sam-program-record)  If true, adds a PG tag to created SAM/BAM/CRAM files.  Default value: true. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="addOutputVcfCommandLine",
            input_type=Boolean(optional=True),
            prefix="-add-output-vcf-command-line",
            doc="(--add-output-vcf-command-line)  If true, adds a command line header line to created VCF files.  Default value: true. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="arguments_file",
            input_type=File(optional=True),
            prefix="--arguments_file:File",
            doc="read one or more arguments files and add them to the command line This argument may be specified 0 or more times. Default value: null. ",
        ),
        ToolInput(
            tag="cloudIndexPrefetchBuffer",
            input_type=String(optional=True),
            prefix="--cloud-index-prefetch-buffer",
            doc="(-CIPB:Integer)  Size of the cloud-only prefetch buffer (in MB; 0 to disable). Defaults to cloudPrefetchBuffer if unset.  Default value: -1. ",
        ),
        ToolInput(
            tag="cloudPrefetchBuffer",
            input_type=String(optional=True),
            prefix="--cloud-prefetch-buffer",
            doc="(-CPB:Integer)  Size of the cloud-only prefetch buffer (in MB; 0 to disable).  Default value: 40. ",
        ),
        ToolInput(
            tag="createOutputBamIndex",
            input_type=String(optional=True),
            prefix="--create-output-bam-index",
            doc="(-OBI:Boolean)  If true, create a BAM/CRAM index when writing a coordinate-sorted BAM/CRAM file.  Default value: true. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="createOutputBamMd5",
            input_type=String(optional=True),
            prefix="--create-output-bam-md5",
            doc="(-OBM:Boolean)  If true, create a MD5 digest for any BAM/SAM/CRAM file created  Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="createOutputVariantIndex",
            input_type=String(optional=True),
            prefix="--create-output-variant-index",
            doc="(-OVI:Boolean)  If true, create a VCF index when writing a coordinate-sorted VCF file.  Default value: true. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="createOutputVariantMd5",
            input_type=String(optional=True),
            prefix="--create-output-variant-md5",
            doc="(-OVM:Boolean)  If true, create a a MD5 digest any VCF file created.  Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="disableBamIndexCaching",
            input_type=String(optional=True),
            prefix="--disable-bam-index-caching",
            doc="(-DBIC:Boolean)  If true, don't cache bam indexes, this will reduce memory requirements but may harm performance if many intervals are specified.  Caching is automatically disabled if there are no intervals specified.  Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="disableReadFilter",
            input_type=String(optional=True),
            prefix="--disable-read-filter",
            doc="(-DF:String)  Read filters to be disabled before analysis  This argument may be specified 0 or more times. Default value: null. Possible Values: {WellformedReadFilter}",
        ),
        ToolInput(
            tag="disableSequenceDictionaryValidation",
            input_type=Boolean(optional=True),
            prefix="-disable-sequence-dictionary-validation",
            doc="(--disable-sequence-dictionary-validation)  If specified, do not check the sequence dictionaries from our inputs for compatibility. Use at your own risk!  Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="excludeIntervals",
            input_type=String(optional=True),
            prefix="--exclude-intervals",
            doc="(-XL:StringOne) This argument may be specified 0 or more times. Default value: null. ",
        ),
        ToolInput(
            tag="gatkConfigFile",
            input_type=File(optional=True),
            prefix="--gatk-config-file",
            doc="A configuration file to use with the GATK. Default value: null.",
        ),
        ToolInput(
            tag="gcsRetries",
            input_type=Int(optional=True),
            prefix="-gcs-retries",
            doc="(--gcs-max-retries)  If the GCS bucket channel errors out, how many times it will attempt to re-initiate the connection  Default value: 20. ",
        ),
        ToolInput(
            tag="gcsProjectForRequesterPays",
            input_type=String(optional=True),
            prefix="--gcs-project-for-requester-pays",
            doc=" Project to bill when accessing requester pays  buckets. If unset, these buckets cannot be accessed.  Default value: . ",
        ),
        ToolInput(
            tag="intervalExclusionPadding",
            input_type=Int(optional=True),
            prefix="--interval-exclusion-padding",
            doc="(-ixp:Integer)  Amount of padding (in bp) to add to each interval you are excluding.  Default value: 0. ",
        ),
        ToolInput(
            tag="imr",
            input_type=String(optional=True),
            prefix="-imr:IntervalMergingRule",
            doc="(--interval-merging-rule)  Interval merging rule for abutting intervals  Default value: ALL. Possible values: {ALL, OVERLAPPING_ONLY} ",
        ),
        ToolInput(
            tag="ip",
            input_type=Int(optional=True),
            prefix="-ip",
            doc="(--interval-padding) Default value: 0.",
        ),
        ToolInput(
            tag="isr",
            input_type=String(optional=True),
            prefix="-isr:IntervalSetRule",
            doc="(--interval-set-rule)  Set merging approach to use for combining interval inputs  Default value: UNION. Possible values: {UNION, INTERSECTION} ",
        ),
        ToolInput(
            tag="le",
            input_type=Boolean(optional=True),
            prefix="--lenient",
            doc="(-LE) Lenient processing of VCF files Default value: false. Possible values: {true, false}",
        ),
        ToolInput(
            tag="quiet",
            input_type=Boolean(optional=True),
            prefix="--QUIET",
            doc="Whether to suppress job-summary info on System.err. Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="readFilter",
            input_type=String(optional=True),
            prefix="--read-filter",
            doc="(-RF:String) Read filters to be applied before analysis This argument may be specified 0 or more times. Default value: null. Possible Values: {AlignmentAgreesWithHeaderReadFilter, AllowAllReadsReadFilter, AmbiguousBaseReadFilter, CigarContainsNoNOperator, FirstOfPairReadFilter, FragmentLengthReadFilter, GoodCigarReadFilter, HasReadGroupReadFilter, IntervalOverlapReadFilter, LibraryReadFilter, MappedReadFilter, MappingQualityAvailableReadFilter, MappingQualityNotZeroReadFilter, MappingQualityReadFilter, MatchingBasesAndQualsReadFilter, MateDifferentStrandReadFilter, MateOnSameContigOrNoMappedMateReadFilter, MateUnmappedAndUnmappedReadFilter, MetricsReadFilter, NonChimericOriginalAlignmentReadFilter, NonZeroFragmentLengthReadFilter, NonZeroReferenceLengthAlignmentReadFilter, NotDuplicateReadFilter, NotOpticalDuplicateReadFilter, NotSecondaryAlignmentReadFilter, NotSupplementaryAlignmentReadFilter, OverclippedReadFilter, PairedReadFilter, PassesVendorQualityCheckReadFilter, PlatformReadFilter, PlatformUnitReadFilter, PrimaryLineReadFilter, ProperlyPairedReadFilter, ReadGroupBlackListReadFilter, ReadGroupReadFilter, ReadLengthEqualsCigarLengthReadFilter, ReadLengthReadFilter, ReadNameReadFilter, ReadStrandFilter, SampleReadFilter, SecondOfPairReadFilter, SeqIsStoredReadFilter, SoftClippedReadFilter, ValidAlignmentEndReadFilter, ValidAlignmentStartReadFilter, WellformedReadFilter}",
        ),
        ToolInput(
            tag="readIndex",
            input_type=String(optional=True),
            prefix="-read-index",
            doc="(--read-index)  Indices to use for the read inputs. If specified, an index must be provided for every read input and in the same order as the read inputs. If this argument is not specified, the path to the index for each input will be inferred automatically.  This argument may be specified 0 or more times. Default value: null. ",
        ),
        ToolInput(
            tag="readValidationStringency",
            input_type=String(optional=True),
            prefix="--read-validation-stringency",
            doc="(-VS:ValidationStringency)  Validation stringency for all SAM/BAM/CRAM/SRA files read by this program.  The default stringency value SILENT can improve performance when processing a BAM file in which variable-length data (read, qualities, tags) do not otherwise need to be decoded.  Default value: SITool returned: 0 LENT. Possible values: {STRICT, LENIENT, SILENT} ",
        ),
        ToolInput(
            tag="reference",
            input_type=FastaWithDict(optional=True),
            prefix="--reference",
            doc="(-R:String) Reference sequence Default value: null.",
        ),
        ToolInput(
            tag="secondsBetweenProgressUpdates",
            input_type=Double(optional=True),
            prefix="-seconds-between-progress-updates",
            doc="(--seconds-between-progress-updates)  Output traversal statistics every time this many seconds elapse  Default value: 10.0. ",
        ),
        ToolInput(
            tag="sequenceDictionary",
            input_type=String(optional=True),
            prefix="-sequence-dictionary",
            doc="(--sequence-dictionary)  Use the given sequence dictionary as the master/canonical sequence dictionary.  Must be a .dict file.  Default value: null. ",
        ),
        ToolInput(
            tag="sitesOnlyVcfOutput",
            input_type=Boolean(optional=True),
            prefix="--sites-only-vcf-output:Boolean",
            doc=" If true, don't emit genotype fields when writing vcf file output.  Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="splitLibraryName",
            input_type=String(optional=True),
            prefix="--split-library-name",
            doc="(-LB)  Split file by library.  Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="rg",
            input_type=String(optional=True),
            prefix="--split-read-group",
            doc="(-RG:BooleanSplit) Default value: false. Possible values: {true, false}",
        ),
        ToolInput(
            tag="splitSample",
            input_type=String(optional=True),
            prefix="--split-sample",
            doc="(-SM:Boolean) Split file by sample. Default value: false. Possible values: {true, false}",
        ),
        ToolInput(
            tag="tmpDir",
            input_type=String(optional=True),
            prefix="--tmp-dir:GATKPathSpecifier",
            doc="Temp directory to use. Default value: null.",
        ),
        ToolInput(
            tag="jdkDeflater",
            input_type=Boolean(optional=True),
            prefix="-jdk-deflater",
            doc="(--use-jdk-deflater)  Whether to use the JdkDeflater (as opposed to IntelDeflater)  Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="jdkInflater",
            input_type=Boolean(optional=True),
            prefix="-jdk-inflater",
            doc="(--use-jdk-inflater)  Whether to use the JdkInflater (as opposed to IntelInflater)  Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="verbosity",
            input_type=String(optional=True),
            prefix="-verbosity:LogLevel",
            doc="(--verbosity)  Control verbosity of logging.  Default value: INFO. Possible values: {ERROR, WARNING, INFO, DEBUG} ",
        ),
        ToolInput(
            tag="disableToolDefaultReadFilters",
            input_type=Boolean(optional=True),
            prefix="-disable-tool-default-read-filters",
            doc="(--disable-tool-default-read-filters)  Disable all tool default read filters (WARNING: many tools will not function correctly without their default read filters on)  Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="ambigFilterBases",
            input_type=Int(optional=True),
            prefix="--ambig-filter-bases",
            doc="Threshold number of ambiguous bases. If null, uses threshold fraction; otherwise, overrides threshold fraction.  Default value: null.  Cannot be used in conjuction with argument(s) maxAmbiguousBaseFraction",
        ),
        ToolInput(
            tag="ambigFilterFrac",
            input_type=Double(optional=True),
            prefix="--ambig-filter-frac",
            doc="Threshold fraction of ambiguous bases Default value: 0.05. Cannot be used in conjuction with argument(s) maxAmbiguousBases",
        ),
        ToolInput(
            tag="maxFragmentLength",
            input_type=Int(optional=True),
            prefix="--max-fragment-length",
            doc="Default value: 1000000.",
        ),
        ToolInput(
            tag="minFragmentLength",
            input_type=Int(optional=True),
            prefix="--min-fragment-length",
            doc="Default value: 0.",
        ),
        ToolInput(
            tag="keepIntervals",
            input_type=String(optional=True),
            prefix="--keep-intervals",
            doc='Valid only if "IntervalOverlapReadFilter" is specified: One or more genomic intervals to keep This argument must be specified at least once. Required. ',
        ),
        ToolInput(
            tag="library",
            input_type=String(optional=True),
            prefix="-library",
            doc='(--library) Valid only if "LibraryReadFilter" is specified: Name of the library to keep This argument must be specified at least once. Required.',
        ),
        ToolInput(
            tag="maximumMappingQuality",
            input_type=Int(optional=True),
            prefix="--maximum-mapping-quality",
            doc=" Maximum mapping quality to keep (inclusive)  Default value: null. ",
        ),
        ToolInput(
            tag="minimumMappingQuality",
            input_type=Int(optional=True),
            prefix="--minimum-mapping-quality",
            doc=" Minimum mapping quality to keep (inclusive)  Default value: 10. ",
        ),
        ToolInput(
            tag="dontRequireSoftClipsBothEnds",
            input_type=Boolean(optional=True),
            prefix="--dont-require-soft-clips-both-ends",
            doc=" Allow a read to be filtered out based on having only 1 soft-clipped block. By default, both ends must have a soft-clipped block, setting this flag requires only 1 soft-clipped block  Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="filterTooShort",
            input_type=Int(optional=True),
            prefix="--filter-too-short",
            doc="Minimum number of aligned bases Default value: 30.",
        ),
        ToolInput(
            tag="platformFilterName",
            input_type=String(optional=True),
            prefix="--platform-filter-name:String",
            doc="This argument must be specified at least once. Required.",
        ),
        ToolInput(
            tag="blackListedLanes",
            input_type=String(optional=True),
            prefix="--black-listed-lanes:String",
            doc="Platform unit (PU) to filter out This argument must be specified at least once. Required.",
        ),
        ToolInput(
            tag="readGroupBlackList",
            input_type=String(optional=True),
            prefix="--read-group-black-list:StringThe",
            doc="This argument must be specified at least once. Required. ",
        ),
        ToolInput(
            tag="keepReadGroup",
            input_type=String(optional=True),
            prefix="--keep-read-group:String",
            doc="The name of the read group to keep Required.",
        ),
        ToolInput(
            tag="maxReadLength",
            input_type=Int(optional=True),
            prefix="--max-read-length",
            doc="Keep only reads with length at most equal to the specified value Required.",
        ),
        ToolInput(
            tag="minReadLength",
            input_type=Int(optional=True),
            prefix="--min-read-length",
            doc="Keep only reads with length at least equal to the specified value Default value: 1.",
        ),
        ToolInput(
            tag="readName",
            input_type=String(optional=True),
            prefix="--read-name:String",
            doc="Keep only reads with this read name Required.",
        ),
        ToolInput(
            tag="keepReverseStrandOnly",
            input_type=Boolean(optional=True),
            prefix="--keep-reverse-strand-only",
            doc=" Keep only reads on the reverse strand  Required. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="sample",
            input_type=String(optional=True),
            prefix="-sample:String",
            doc="(--sample) The name of the sample(s) to keep, filtering out all others This argument must be specified at least once. Required. ",
        ),
        ToolInput(
            tag="invertSoftClipRatioFilter",
            input_type=Boolean(optional=True),
            prefix="--invert-soft-clip-ratio-filter",
            doc=" Inverts the results from this filter, causing all variants that would pass to fail and visa-versa.  Default value: false. Possible values: {true, false} ",
        ),
        ToolInput(
            tag="softClippedLeadingTrailingRatio",
            input_type=Double(optional=True),
            prefix="--soft-clipped-leading-trailing-ratio",
            doc=" Threshold ratio of soft clipped bases (leading / trailing the cigar string) to total bases in read for read to be filtered.  Default value: null.  Cannot be used in conjuction with argument(s) minimumSoftClippedRatio",
        ),
        ToolInput(
            tag="softClippedRatioThreshold",
            input_type=Double(optional=True),
            prefix="--soft-clipped-ratio-threshold",
            doc=" Threshold ratio of soft clipped bases (anywhere in the cigar string) to total bases in read for read to be filtered.  Default value: null.  Cannot be used in conjuction with argument(s) minimumLeadingTrailingSoftClippedRatio",
        ),
    ]
