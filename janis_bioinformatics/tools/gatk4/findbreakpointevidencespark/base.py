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


class GatkFindBreakpointEvidenceSparkBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "FindBreakpointEvidenceSpark"

    def friendly_name(self) -> str:
        return "GATK4: FindBreakpointEvidenceSpark"

    def tool(self) -> str:
        return "Gatk4FindBreakpointEvidenceSpark"

    def inputs(self):
        return [
            ToolInput(
                tag="alignerIndexImage",
                input_type=String(optional=True),
                prefix="--aligner-index-image",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="bwa-mem index image file Required."),
            ),
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
                tag="kmersToIgnore",
                input_type=String(optional=True),
                prefix="--kmers-to-ignore",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="file containing ubiquitous kmer list. see FindBadGenomicKmersSpark to generate it. Required. "
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) sam file for aligned contigs Required."
                ),
            ),
            ToolInput(
                tag="adapterSequence",
                input_type=String(optional=True),
                prefix="--adapter-sequence",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Adapter sequence. Default value: null."),
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
                tag="allowedShortFragmentOverhang",
                input_type=Int(optional=True),
                prefix="--allowed-short-fragment-overhang",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Proper pairs have the positive strand read upstream of the negative strand read, but we allow this much slop for short fragments.  Default value: 10. "
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
                tag="assembledContigsOutputOrder",
                input_type=Boolean(optional=True),
                prefix="--assembled-contigs-output-order",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-sort)  sorting order to be used for the output assembly alignments SAM/BAM file (currently only coordinate or query name is supported)  Default value: coordinate. Possible values: {unsorted, queryname, coordinate, duplicate, unknown} "
                ),
            ),
            ToolInput(
                tag="assemblyToMappedSizeRatioGuess",
                input_type=Int(optional=True),
                prefix="--assembly-to-mapped-size-ratio-guess",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Guess at the ratio of reads in the final assembly to the number reads mapped to the interval.  Default value: 7. "
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
                tag="breakpointEvidenceDir",
                input_type=String(optional=True),
                prefix="--breakpoint-evidence-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" directory for evidence output  Default value: null. "
                ),
            ),
            ToolInput(
                tag="breakpointIntervals",
                input_type=Boolean(optional=True),
                prefix="--breakpoint-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: null."),
            ),
            ToolInput(
                tag="cleanerMaxCopyNumber",
                input_type=Int(optional=True),
                prefix="--cleaner-max-copy-number",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" KmerCleaner maximum copy number (not count, but copy number) for a kmer. Kmers observed too frequently are probably mismapped or ubiquitous.  Default value: 4. "
                ),
            ),
            ToolInput(
                tag="cleanerMaxIntervals",
                input_type=Int(optional=True),
                prefix="--cleaner-max-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" KmerCleaner maximum number of intervals for a localizing kmer. If a kmer occurs in too many intervals, it isn't sufficiently local.  Default value: 3. "
                ),
            ),
            ToolInput(
                tag="cleanerMinKmerCount",
                input_type=Int(optional=True),
                prefix="--cleaner-min-kmer-count",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" KmerCleaner minimum kmer count for a localizing kmer.  If we see it less often than this many times, we're guessing it's erroneous.  Default value: 4. "
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
                tag="crossContigsToIgnore",
                input_type=String(optional=True),
                prefix="--cross-contigs-to-ignore",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" file containing alt contig names that will be ignored when looking for inter-contig pairs  Default value: null. "
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
                tag="exclusionIntervalPadding",
                input_type=Int(optional=True),
                prefix="--exclusion-interval-padding",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Exclusion interval padding.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="exclusionIntervals",
                input_type=String(optional=True),
                prefix="--exclusion-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="file of reference intervals to exclude Default value: null."
                ),
            ),
            ToolInput(
                tag="externalEvidence",
                input_type=String(optional=True),
                prefix="--external-evidence",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="external evidence input file Default value: null."
                ),
            ),
            ToolInput(
                tag="externalEvidenceUncertainty",
                input_type=Int(optional=True),
                prefix="--external-evidence-uncertainty",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Uncertainty in location of external evidence.  Default value: 150. "
                ),
            ),
            ToolInput(
                tag="externalEvidenceWeight",
                input_type=Int(optional=True),
                prefix="--external-evidence-weight",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Weight to give external evidence.  Default value: 10. "
                ),
            ),
            ToolInput(
                tag="fastqDir",
                input_type=String(optional=True),
                prefix="--fastq-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="output dir for assembled fastqs Default value: null."
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
                tag="highCoverageIntervals",
                input_type=String(optional=True),
                prefix="--high-coverage-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" file for high-coverage intervals output  Default value: null. "
                ),
            ),
            ToolInput(
                tag="highDepthCoverageFactor",
                input_type=Int(optional=True),
                prefix="--high-depth-coverage-factor",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" We filter out contiguous regions of the genome that have coverage of at least high-depth-coverage-factor * avg-coverage and a peak coverage of high-depth-coverage-peak-factor * avg-coverage, because the reads mapped to those regions tend to be non-local and high depth prevents accurate assembly.  Default value: 3. "
                ),
            ),
            ToolInput(
                tag="highDepthCoveragePeakFactor",
                input_type=Int(optional=True),
                prefix="--high-depth-coverage-peak-factor",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" We filter out contiguous regions of the genome that have coverage of at least high-depth-coverage-factor * avg-coverage and a peak coverage of high-depth-coverage-peak-factor * avg-coverage, because the reads mapped to those regions tend to be non-local and high depth prevents accurate assembly.  Default value: 7. "
                ),
            ),
            ToolInput(
                tag="includeMappingLocation",
                input_type=Boolean(optional=True),
                prefix="--include-mapping-location",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Include read mapping location in FASTQ files.  Default value: true. Possible values: {true, false} "
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
                tag="intervalOnlyAssembly",
                input_type=Boolean(optional=True),
                prefix="--interval-only-assembly",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Don't look for extra reads mapped outside the interval.  Default value: false. Possible values: {true, false} "
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
                tag="kSize",
                input_type=Int(optional=True),
                prefix="--k-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Kmer size. Default value: 51."),
            ),
            ToolInput(
                tag="kmerIntervals",
                input_type=String(optional=True),
                prefix="--kmer-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="file for kmer intervals output Default value: null."
                ),
            ),
            ToolInput(
                tag="kmerMaxDustScore",
                input_type=Boolean(optional=True),
                prefix="--kmer-max-dust-score",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 49."),
            ),
            ToolInput(
                tag="maxFastqSize",
                input_type=Int(optional=True),
                prefix="--max-fastq-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Maximum total bases in FASTQs that can be assembled. Default value: 3000000."
                ),
            ),
            ToolInput(
                tag="maxTrackedFragmentLength",
                input_type=Int(optional=True),
                prefix="--max-tracked-fragment-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Largest fragment size that will be explicitly counted in determining fragment size statistics.  Default value: 2000. "
                ),
            ),
            ToolInput(
                tag="minCoherentEvidenceCoverageRatio",
                input_type=Double(optional=True),
                prefix="--min-coherent-evidence-coverage-ratio",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum weight of the evidence that shares a distal target locus to validate the evidence, as a ratio of the mean coverage in the BAM. The default value is coherent-count / mean coverage ~ 7 / 42.9 ~ 0.163  Default value: 0.1633408753260167. "
                ),
            ),
            ToolInput(
                tag="minEvidenceCoverageRatio",
                input_type=Double(optional=True),
                prefix="--min-evidence-coverage-ratio",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum weight of the corroborating read evidence to validate some single piece of evidence, as a ratio of the mean coverage in the BAM. The default value is overlap-count / mean coverage ~ 15 / 42.9 ~ 0.350  Default value: 0.35001616141289293. "
                ),
            ),
            ToolInput(
                tag="minEvidenceMapq",
                input_type=Int(optional=True),
                prefix="--min-evidence-mapq",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The minimum mapping quality for reads used to gather evidence of breakpoints. Default value: 20. "
                ),
            ),
            ToolInput(
                tag="minEvidenceMatchLength",
                input_type=Int(optional=True),
                prefix="--min-evidence-match-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The minimum length of the matched portion of an interesting alignment.  Reads that don't match at least this many reference bases won't be used in gathering evidence.  Default value: 45. "
                ),
            ),
            ToolInput(
                tag="minKmersPerInterval",
                input_type=Int(optional=True),
                prefix="--min-kmers-per-interval",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum number of localizing kmers in a valid interval.  Default value: 5. "
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
                tag="programName",
                input_type=String(optional=True),
                prefix="--program-name",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Name of the program running Default value: null."
                ),
            ),
            ToolInput(
                tag="qnameIntervalsForAssembly",
                input_type=String(optional=True),
                prefix="--qname-intervals-for-assembly",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" file for mapped qname intervals output  Default value: null. "
                ),
            ),
            ToolInput(
                tag="qnameIntervalsMapped",
                input_type=String(optional=True),
                prefix="--qname-intervals-mapped",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" file for mapped qname intervals output  Default value: null. "
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
                tag="readMetadata",
                input_type=String(optional=True),
                prefix="--read-metadata",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="output file for read metadata Default value: null."
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
                tag="runWithoutGapsAnnotation",
                input_type=Boolean(optional=True),
                prefix="--run-without-gaps-annotation",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Allow evidence filter to run without gaps annotation (assume no gaps).  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="runWithoutUmapS100Annotation",
                input_type=Boolean(optional=True),
                prefix="--run-without-umap-s100-annotation",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Allow evidence filter to run without annotation for single-read mappability of 100-mers (assume all mappable).  Default value: false. Possible values: {true, false} "
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
                tag="svEvidenceFilterModelFile",
                input_type=String(optional=True),
                prefix="--sv-evidence-filter-model-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Path to xgboost classifier model file for evidence filtering  Default value: null. "
                ),
            ),
            ToolInput(
                tag="svEvidenceFilterThresholdProbability",
                input_type=Double(optional=True),
                prefix="--sv-evidence-filter-threshold-probability",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum classified probability for a piece of evidence to pass xgboost evidence filter  Default value: 0.92. "
                ),
            ),
            ToolInput(
                tag="svEvidenceFilterType",
                input_type=Boolean(optional=True),
                prefix="--sv-evidence-filter-type",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Filter method for selecting evidence to group into Assembly Intervals  Default value: DENSITY. Possible values: {DENSITY, XGBOOST} "
                ),
            ),
            ToolInput(
                tag="svGenomeGapsFile",
                input_type=String(optional=True),
                prefix="--sv-genome-gaps-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Path to file enumerating gaps in the reference genome, used by classifier to score evidence for filtering. To use classifier without specifying gaps file, pass the flag"
                ),
            ),
            ToolInput(
                tag="runWithoutGapsAnnotation",
                input_type=Boolean(optional=True),
                prefix="--run-without-gaps-annotation",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: null."),
            ),
            ToolInput(
                tag="svGenomeUmapS100File",
                input_type=String(optional=True),
                prefix="--sv-genome-umap-s100-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Path to single read 100-mer mappability file in the reference genome, used by classifier to score evidence for filtering. To use classifier without specifying mappability file, pass the flag --run-without-umap-s100-annotation  Default value: null. "
                ),
            ),
            ToolInput(
                tag="targetLinkFile",
                input_type=String(optional=True),
                prefix="--target-link-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="output file for non-assembled breakpoints in bedpe format Default value: null."
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
                tag="unfilteredBreakpointEvidenceDir",
                input_type=String(optional=True),
                prefix="--unfiltered-breakpoint-evidence-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" directory for evidence output  Default value: null. "
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
                tag="writeGfas",
                input_type=Boolean(optional=True),
                prefix="--write-gfas",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Write GFA representation of assemblies in fastq-dir. Default value: false. Possible values: {true, false} "
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
                tag="expandAssemblyGraph",
                input_type=Boolean(optional=True),
                prefix="--expand-assembly-graph",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Traverse assembly graph and produce contigs for all paths.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="popVariantBubbles",
                input_type=Boolean(optional=True),
                prefix="--pop-variant-bubbles",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(ignoring) Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="removeShadowedContigs",
                input_type=Boolean(optional=True),
                prefix="--remove-shadowed-contigs",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Simplify local assemblies by removing contigs shadowed by similar contigs.  Default value: true. Possible values: {true, false} "
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
                tag="zDropoff",
                input_type=Int(optional=True),
                prefix="--z-dropoff",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="ZDropoff (see Bwa mem manual) for contig alignment. Default value: 20."
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:02:46.996823"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:02:46.996824"),
            documentation="**BETA FEATURE - WORK IN PROGRESS**\nUSAGE: FindBreakpointEvidenceSpark [arguments]\nThis tool is used in development and should not be of interest to most researchers.  It packages the identification of\ngenomic regions that might contain structural variation and the generation of local assemblies of these regions as a\nseparate tool, independent of the calling of structural variations from these assemblies Most researchers will run\nStructuralVariationDiscoveryPipelineSpark, which both generates local assemblies of interesting genomic regions, and\nthen calls structural variants from these assemblies. This tool identifies genomic regions that may harbor structural\nvariants by integrating evidence from split reads, discordant read pairs, template-length anomalies, and copy-number\nvariation.  It then prepares local assemblies of these regions for structural variant calling.  In addition to the reads\nthat align to these regions, reads sharing kmers (fixed-length subsequences) with the reads aligned in these regions are\nextracted to produce the local assemblies. The local assemblies are done with FermiLite, and the assembled contigs are\naligned to reference with BWA-MEM. The output is a file of aligned contigs from local assemblies to be used in calling\nstructural variants.\nVersion:4.1.3.0\n",
        )
