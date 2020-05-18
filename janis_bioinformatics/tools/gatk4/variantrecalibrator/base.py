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


class GatkVariantRecalibratorBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "VariantRecalibrator"

    def friendly_name(self) -> str:
        return "GATK4: VariantRecalibrator"

    def tool(self) -> str:
        return "Gatk4VariantRecalibrator"

    def inputs(self):
        return [
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output recal file used by ApplyRecalibration Required."
                ),
            ),
            ToolInput(
                tag="resource",
                input_type=Boolean(optional=True),
                prefix="--resource",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-resource)  A list of sites for which to apply a prior probability of being correct but which aren't used by the algorithm (training and truth sets are required to run)  This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="tranchesFile",
                input_type=String(optional=True),
                prefix="--tranches-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The output tranches file used by ApplyRecalibration Required."
                ),
            ),
            ToolInput(
                tag="useAnnotation",
                input_type=String(optional=True),
                prefix="--use-annotation",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-an) The names of the annotations which should used for calculations This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="variant",
                input_type=String(optional=True),
                prefix="--variant",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-V) One or more VCF files containing variants This argument must be specified at least once. Required. "
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
                tag="aggregate",
                input_type=Boolean(optional=True),
                prefix="--aggregate",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-aggregate)  Additional raw input variants to be used in building the model  This argument may be specified 0 or more times. Default value: null. "
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
                tag="cloudIndexPrefetchBuffer",
                input_type=Int(optional=True),
                prefix="--cloud-index-prefetch-buffer",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CIPB)  Size of the cloud-only prefetch buffer (in MB; 0 to disable). Defaults to cloudPrefetchBuffer if unset.  Default value: -1. "
                ),
            ),
            ToolInput(
                tag="cloudPrefetchBuffer",
                input_type=Int(optional=True),
                prefix="--cloud-prefetch-buffer",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CPB)  Size of the cloud-only prefetch buffer (in MB; 0 to disable).  Default value: 40. "
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
                tag="help",
                input_type=Boolean(optional=True),
                prefix="--help",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-h) display the help message Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="ignoreAllFilters",
                input_type=Boolean(optional=True),
                prefix="--ignore-all-filters",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If specified, the variant recalibrator will ignore all input filters. Useful to rerun the VQSR from a filtered output file.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="ignoreFilter",
                input_type=String(optional=True),
                prefix="--ignore-filter",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If specified, the variant recalibrator will also use variants marked as filtered by the specified filter name in the input VCF file  This argument may be specified 0 or more times. Default value: null. "
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
                tag="inputModel",
                input_type=String(optional=True),
                prefix="--input-model",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If specified, the variant recalibrator will read the VQSR model from this file path. Default value: null. "
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
                tag="mode",
                input_type=Boolean(optional=True),
                prefix="--mode",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-mode) Recalibration mode to employ Default value: SNP. Possible values: {SNP, INDEL, BOTH}"
                ),
            ),
            ToolInput(
                tag="outputModel",
                input_type=String(optional=True),
                prefix="--output-model",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If specified, the variant recalibrator will output the VQSR model to this file path. Default value: null. "
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
                tag="rscriptFile",
                input_type=String(optional=True),
                prefix="--rscript-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The output rscript file generated by the VQSR to aid in visualization of the input data and learned model  Default value: null. "
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
                tag="targetTitv",
                input_type=Double(optional=True),
                prefix="--target-titv",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-titv) The expected novel Ti/Tv ratio to use when calculating FDR tranches and for display on the optimization curve output figures. (approx 2.15 for whole genome experiments). ONLY USED FOR PLOTTING PURPOSES!  Default value: 2.15. "
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
                tag="truthSensitivityTranche",
                input_type=Double(optional=True),
                prefix="--truth-sensitivity-tranche",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-tranche)  The levels of truth sensitivity at which to slice the data. (in percent, that is 1.0 for 1 percent)  This argument may be specified 0 or more times. Default value: [100.0, 99.9, 99.0, 90.0]. "
                ),
            ),
            ToolInput(
                tag="useAlleleSpecificAnnotations",
                input_type=Boolean(optional=True),
                prefix="--use-allele-specific-annotations",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-AS)  If specified, the variant recalibrator will attempt to use the allele-specific versions of the specified annotations.  Default value: false. Possible values: {true, false} "
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
                tag="badLodScoreCutoff",
                input_type=Double(optional=True),
                prefix="--bad-lod-score-cutoff",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-bad-lod-cutoff)  LOD score cutoff for selecting bad variants  Default value: -5.0. "
                ),
            ),
            ToolInput(
                tag="dirichlet",
                input_type=Double(optional=True),
                prefix="--dirichlet",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The dirichlet parameter in the variational Bayes algorithm. Default value: 0.001."
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
                tag="kMeansIterations",
                input_type=Int(optional=True),
                prefix="--k-means-iterations",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Number of k-means iterations Default value: 100."
                ),
            ),
            ToolInput(
                tag="maxAttempts",
                input_type=Int(optional=True),
                prefix="--max-attempts",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Number of attempts to build a model before failing Default value: 1."
                ),
            ),
            ToolInput(
                tag="maxGaussians",
                input_type=Int(optional=True),
                prefix="--max-gaussians",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Max number of Gaussians for the positive model Default value: 8."
                ),
            ),
            ToolInput(
                tag="maxIterations",
                input_type=Int(optional=True),
                prefix="--max-iterations",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Maximum number of VBEM iterations Default value: 150."
                ),
            ),
            ToolInput(
                tag="maxNegativeGaussians",
                input_type=Int(optional=True),
                prefix="--max-negative-gaussians",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Max number of Gaussians for the negative model  Default value: 2. "
                ),
            ),
            ToolInput(
                tag="maximumTrainingVariants",
                input_type=Int(optional=True),
                prefix="--maximum-training-variants",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum number of training data  Default value: 2500000. "
                ),
            ),
            ToolInput(
                tag="minimumBadVariants",
                input_type=Boolean(optional=True),
                prefix="--minimum-bad-variants",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 1000."),
            ),
            ToolInput(
                tag="mqCapForLogitJitterTransform",
                input_type=Int(optional=True),
                prefix="--mq-cap-for-logit-jitter-transform",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-mq-cap)  Apply logit transform and jitter to MQ values  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="priorCounts",
                input_type=Double(optional=True),
                prefix="--prior-counts",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The number of prior counts to use in the variational Bayes algorithm. Default value: 20.0. "
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
                tag="shrinkage",
                input_type=Double(optional=True),
                prefix="--shrinkage",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The shrinkage parameter in the variational Bayes algorithm. Default value: 1.0."
                ),
            ),
            ToolInput(
                tag="standardDeviationThreshold",
                input_type=Double(optional=True),
                prefix="--standard-deviation-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-std)  Annotation value divergence threshold (number of standard deviations from the means)   Default value: 10.0. "
                ),
            ),
            ToolInput(
                tag="trustAllPolymorphic",
                input_type=Boolean(optional=True),
                prefix="--trust-all-polymorphic",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Trust that all the input training sets' unfiltered records contain only polymorphic sites to drastically speed up the computation.  Default value: false. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:06:44.437462"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:06:44.437463"),
            documentation="USAGE: VariantRecalibrator [arguments]\nBuild a recalibration model to score variant quality for filtering purposes\nVersion:4.1.3.0\n",
        )
