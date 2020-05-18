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


class GatkReadsPipelineSparkBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "ReadsPipelineSpark"

    def friendly_name(self) -> str:
        return "GATK4: ReadsPipelineSpark"

    def tool(self) -> str:
        return "Gatk4ReadsPipelineSpark"

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
                doc=InputDocumentation(doc="(-O) the output vcf Required."),
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
                tag="align",
                input_type=Boolean(optional=True),
                prefix="--align",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="whether to perform alignment using BWA-MEM Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="alleles",
                input_type=Boolean(optional=True),
                prefix="--alleles",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The set of alleles at which to genotype when --genotyping-mode is GENOTYPE_GIVEN_ALLELES Default value: null. "
                ),
            ),
            ToolInput(
                tag="annotateWithNumDiscoveredAlleles",
                input_type=Boolean(optional=True),
                prefix="--annotate-with-num-discovered-alleles",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If provided, we will annotate records with the number of alternate alleles that were discovered (but not necessarily genotyped) at a given site  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="annotation",
                input_type=String(optional=True),
                prefix="--annotation",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-A) One or more specific annotations to add to variant calls This argument may be specified 0 or more times. Default value: null. Possible Values: {AlleleFraction, AS_BaseQualityRankSumTest, AS_FisherStrand, AS_InbreedingCoeff, AS_MappingQualityRankSumTest, AS_QualByDepth, AS_ReadPosRankSumTest, AS_RMSMappingQuality, AS_StrandOddsRatio, BaseQuality, BaseQualityHistogram, BaseQualityRankSumTest, ChromosomeCounts, ClippingRankSumTest, CountNs, Coverage, DepthPerAlleleBySample, DepthPerSampleHC, ExcessHet, FisherStrand, FragmentLength, GenotypeSummaries, InbreedingCoeff, LikelihoodRankSumTest, MappingQuality, MappingQualityRankSumTest, MappingQualityZero, OrientationBiasReadCounts, OriginalAlignment, PossibleDeNovo, QualByDepth, ReadPosition, ReadPosRankSumTest, ReferenceBases, RMSMappingQuality, SampleList, StrandBiasBySample, StrandOddsRatio, TandemRepeat, UniqueAltReadCount}"
                ),
            ),
            ToolInput(
                tag="annotationGroup",
                input_type=String(optional=True),
                prefix="--annotation-group",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-G) One or more groups of annotations to apply to variant calls This argument may be specified 0 or more times. Default value: null. Possible Values: {AlleleSpecificAnnotation, AS_StandardAnnotation, ReducibleAnnotation, StandardAnnotation, StandardHCAnnotation, StandardMutectAnnotation}"
                ),
            ),
            ToolInput(
                tag="annotationsToExclude",
                input_type=String(optional=True),
                prefix="--annotations-to-exclude",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-AX)  One or more specific annotations to exclude from variant calls  This argument may be specified 0 or more times. Default value: null. Possible Values: {BaseQualityRankSumTest, ChromosomeCounts, Coverage, DepthPerAlleleBySample, DepthPerSampleHC, ExcessHet, FisherStrand, InbreedingCoeff, MappingQualityRankSumTest, QualByDepth, ReadPosRankSumTest, RMSMappingQuality, StrandOddsRatio}"
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
                tag="assemblyRegionPadding",
                input_type=Int(optional=True),
                prefix="--assembly-region-padding",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Number of additional bases of context to include around each assembly region  Default value: 100. "
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
                tag="baseQualityScoreThreshold",
                input_type=Boolean(optional=True),
                prefix="--base-quality-score-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Base qualities below this threshold will be reduced to the minimum (6)  Default value: 18."
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
                tag="bwaMemIndexImage",
                input_type=String(optional=True),
                prefix="--bwa-mem-index-image",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-image)  The BWA-MEM index image file name that you've distributed to each executor  Default value: null. "
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
                tag="contaminationFractionToFilter",
                input_type=Double(optional=True),
                prefix="--contamination-fraction-to-filter",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-contamination)  Fraction of contamination in sequencing data (for all samples) to aggressively remove  Default value: 0.0. "
                ),
            ),
            ToolInput(
                tag="correctOverlappingQuality",
                input_type=Boolean(optional=True),
                prefix="--correct-overlapping-quality",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Undocumented option  Default value: false. Possible values: {true, false} "
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
                tag="dbsnp",
                input_type=Boolean(optional=True),
                prefix="--dbsnp",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-D) dbSNP file Default value: null."),
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
                tag="doNotMarkUnmappedMates",
                input_type=Boolean(optional=True),
                prefix="--do-not-mark-unmapped-mates",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Enabling this option will mean unmapped mates of duplicate marked reads will not be marked as duplicates.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="duplicateScoringStrategy",
                input_type=Boolean(optional=True),
                prefix="--duplicate-scoring-strategy",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DS)  The scoring strategy for choosing the non-duplicate among candidates.  Default value: SUM_OF_BASE_QUALITIES. Possible values: {SUM_OF_BASE_QUALITIES, TOTAL_MAPPED_REFERENCE_LENGTH} "
                ),
            ),
            ToolInput(
                tag="duplicateTaggingPolicy",
                input_type=Boolean(optional=True),
                prefix="--duplicate-tagging-policy",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Determines how duplicate types are recorded in the DT optional attribute.  Default value: DontTag. Possible values: {DontTag, OpticalOnly, All}  Cannot be used in conjuction with argument(s) removeAllDuplicates removeSequencingDuplicates"
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
                tag="founderId",
                input_type=String(optional=True),
                prefix="--founder-id",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-founder-id)  Samples representing the population 'founders'  This argument may be specified 0 or more times. Default value: null. "
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
                tag="genotypingMode",
                input_type=Boolean(optional=True),
                prefix="--genotyping-mode",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Specifies how to determine the alternate alleles to use for genotyping  Default value: DISCOVERY. Possible values: {DISCOVERY, GENOTYPE_GIVEN_ALLELES} "
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
                tag="graphOutput",
                input_type=String(optional=True),
                prefix="--graph-output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-graph) Write debug assembly graph information to this file Default value: null."
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
                tag="heterozygosity",
                input_type=Double(optional=True),
                prefix="--heterozygosity",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Heterozygosity value used to compute prior likelihoods for any locus. See the GATKDocs for full details on the meaning of this population genetics concept  Default value: 0.001."
                ),
            ),
            ToolInput(
                tag="heterozygosityStdev",
                input_type=Boolean(optional=True),
                prefix="--heterozygosity-stdev",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 0.01."),
            ),
            ToolInput(
                tag="indelHeterozygosity",
                input_type=Boolean(optional=True),
                prefix="--indel-heterozygosity",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="See the GATKDocs for heterozygosity for full details on the meaning of this population genetics concept  Default value: 1.25E-4. "
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
                tag="maxAssemblyRegionSize",
                input_type=Int(optional=True),
                prefix="--max-assembly-region-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum size of an assembly region  Default value: 300. "
                ),
            ),
            ToolInput(
                tag="maxReadsPerAlignmentStart",
                input_type=Int(optional=True),
                prefix="--max-reads-per-alignment-start",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum number of reads to retain per alignment start position. Reads above this threshold will be downsampled. Set to 0 to disable.  Default value: 50. "
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
                tag="minAssemblyRegionSize",
                input_type=Int(optional=True),
                prefix="--min-assembly-region-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum size of an assembly region  Default value: 50. "
                ),
            ),
            ToolInput(
                tag="minBaseQualityScore",
                input_type=Boolean(optional=True),
                prefix="--min-base-quality-score",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-mbq)  Minimum base quality required to consider a base for calling  Default value: 10. "
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
                tag="nativePairHmmThreads",
                input_type=Int(optional=True),
                prefix="--native-pair-hmm-threads",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" How many threads should a native pairHMM implementation use  Default value: 4. "
                ),
            ),
            ToolInput(
                tag="nativePairHmmUseDoublePrecision",
                input_type=Boolean(optional=True),
                prefix="--native-pair-hmm-use-double-precision",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" use double precision in the native pairHmm. This is slower but matches the java implementation better  Default value: false. Possible values: {true, false} "
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
                tag="numReferenceSamplesIfNoCall",
                input_type=Int(optional=True),
                prefix="--num-reference-samples-if-no-call",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Number of hom-ref genotypes to infer at sites not present in a panel  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="outputBam",
                input_type=String(optional=True),
                prefix="--output-bam",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="the output bam Default value: null."),
            ),
            ToolInput(
                tag="outputMode",
                input_type=Boolean(optional=True),
                prefix="--output-mode",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Specifies which type of calls we should output Default value: EMIT_VARIANTS_ONLY. Possible values: {EMIT_VARIANTS_ONLY, EMIT_ALL_CONFIDENT_SITES, EMIT_ALL_SITES} "
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
                tag="pedigree",
                input_type=File(optional=True),
                prefix="--pedigree",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ped) Pedigree file for determining the population 'founders' Default value: null."
                ),
            ),
            ToolInput(
                tag="populationCallset",
                input_type=Boolean(optional=True),
                prefix="--population-callset",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-population)  Callset to use in calculating genotype priors  Default value: null. "
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
                tag="readShardPadding",
                input_type=Int(optional=True),
                prefix="--read-shard-padding",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-read-shard-padding)  Each read shard has this many bases of extra context on each side. Read shards must have as much or more padding than assembly regions.  Default value: 100. "
                ),
            ),
            ToolInput(
                tag="readShardSize",
                input_type=Int(optional=True),
                prefix="--read-shard-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-read-shard-size)  Maximum size of each read shard, in bases. For good performance, this should be much larger than the maximum assembly region size.  Default value: 5000. "
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
                tag="recoverDanglingHeads",
                input_type=Boolean(optional=True),
                prefix="--recover-dangling-heads",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" This argument is deprecated since version 3.3  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="removeAllDuplicates",
                input_type=Boolean(optional=True),
                prefix="--remove-all-duplicates",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If true do not write duplicates to the output file instead of writing them with appropriate flags set.  Default value: false. Possible values: {true, false}  Cannot be used in conjuction with argument(s) taggingPolicy removeSequencingDuplicates"
                ),
            ),
            ToolInput(
                tag="removeSequencingDuplicates",
                input_type=Boolean(optional=True),
                prefix="--remove-sequencing-duplicates",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If true do not write optical/sequencing duplicates to the output file instead of writing them with appropriate flags set.  Default value: false. Possible values: {true, false}  Cannot be used in conjuction with argument(s) taggingPolicy removeAllDuplicates"
                ),
            ),
            ToolInput(
                tag="sampleName",
                input_type=String(optional=True),
                prefix="--sample-name",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ALIAS) Name of single sample to use from a multi-sample bam Default value: null."
                ),
            ),
            ToolInput(
                tag="samplePloidy",
                input_type=Int(optional=True),
                prefix="--sample-ploidy",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ploidy)  Ploidy (number of chromosomes) per sample. For pooled data, set to (Number of samples in each pool * Sample Ploidy).  Default value: 2. "
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
                tag="singleEndAlignment",
                input_type=Boolean(optional=True),
                prefix="--single-end-alignment",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-se)  Run single-end instead of paired-end alignment  Default value: false. Possible values: {true, false} "
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
                tag="standardMinConfidenceThresholdForCalling",
                input_type=Double(optional=True),
                prefix="--standard-min-confidence-threshold-for-calling",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-stand-call-conf)  The minimum phred-scaled confidence threshold at which variants should be called  Default value: 30.0. "
                ),
            ),
            ToolInput(
                tag="strict",
                input_type=Boolean(optional=True),
                prefix="--strict",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="whether to use the strict implementation or not (defaults to the faster implementation that doesn't strictly match the walker version)  Default value: false. Possible values: {true, false} "
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
                tag="useNewQualCalculator",
                input_type=Boolean(optional=True),
                prefix="--use-new-qual-calculator",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-new-qual)  Use the new AF model instead of the so-called exact model  Default value: true. Possible values: {true, false} "
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
                tag="useOldQualCalculator",
                input_type=Boolean(optional=True),
                prefix="--use-old-qual-calculator",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-old-qual)  Use the old AF model  Default value: false. Possible values: {true, false} "
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
                tag="activeProbabilityThreshold",
                input_type=Double(optional=True),
                prefix="--active-probability-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum probability for a locus to be considered active.  Default value: 0.002. "
                ),
            ),
            ToolInput(
                tag="adaptivePruning",
                input_type=Boolean(optional=True),
                prefix="--adaptive-pruning",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Use Mutect2's adaptive graph pruning algorithm Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="adaptivePruningInitialErrorRate",
                input_type=Double(optional=True),
                prefix="--adaptive-pruning-initial-error-rate",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Initial base error rate estimate for adaptive pruning  Default value: 0.001. "
                ),
            ),
            ToolInput(
                tag="allSitePls",
                input_type=Boolean(optional=True),
                prefix="--all-site-pls",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Annotate all sites with PLs Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="allowNonUniqueKmersInRef",
                input_type=Boolean(optional=True),
                prefix="--allow-non-unique-kmers-in-ref",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Allow graphs that have non-unique kmers in the reference  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="bamOutput",
                input_type=String(optional=True),
                prefix="--bam-output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-bamout) File to which assembled haplotypes should be written Default value: null."
                ),
            ),
            ToolInput(
                tag="bamWriterType",
                input_type=Boolean(optional=True),
                prefix="--bam-writer-type",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Which haplotypes should be written to the BAM Default value: CALLED_HAPLOTYPES. Possible values: {ALL_POSSIBLE_HAPLOTYPES, CALLED_HAPLOTYPES} "
                ),
            ),
            ToolInput(
                tag="comp",
                input_type=Boolean(optional=True),
                prefix="--comp",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-comp) Comparison VCF file(s) This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="consensus",
                input_type=Boolean(optional=True),
                prefix="--consensus",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="1000G consensus mode Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="contaminationFractionPerSampleFile",
                input_type=File(optional=True),
                prefix="--contamination-fraction-per-sample-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-contamination-file)  Tab-separated File containing fraction of contamination in sequencing data (per sample) to aggressively remove. Format should be '<SampleID><TAB><Contamination>' (Contamination is double) per line; No header.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="debugAssembly",
                input_type=Boolean(optional=True),
                prefix="--debug-assembly",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-debug)  Print out verbose debug information about each assembly region  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="disableOptimizations",
                input_type=Boolean(optional=True),
                prefix="--disable-optimizations",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Don't skip calculations in ActiveRegions with no variants  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="disableToolDefaultAnnotations",
                input_type=Boolean(optional=True),
                prefix="--disable-tool-default-annotations",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-disable-tool-default-annotations)  Disable all tool default annotations  Default value: false. Possible values: {true, false}"
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
                tag="doNotRunPhysicalPhasing",
                input_type=Boolean(optional=True),
                prefix="--do-not-run-physical-phasing",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Disable physical phasing  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="dontIncreaseKmerSizesForCycles",
                input_type=Boolean(optional=True),
                prefix="--dont-increase-kmer-sizes-for-cycles",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Disable iterating over kmer sizes when graph cycles are detected  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="dontTrimActiveRegions",
                input_type=Boolean(optional=True),
                prefix="--dont-trim-active-regions",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If specified, we will not trim down the active region from the full region (active + extension) to just the active interval for genotyping  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="dontUseSoftClippedBases",
                input_type=Boolean(optional=True),
                prefix="--dont-use-soft-clipped-bases",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Do not analyze soft clipped bases in the reads  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="emitRefConfidence",
                input_type=Boolean(optional=True),
                prefix="--emit-ref-confidence",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ERC)  Mode for emitting reference confidence scores (For Mutect2, this is a BETA feature)  Default value: NONE. Possible values: {NONE, BP_RESOLUTION, GVCF} "
                ),
            ),
            ToolInput(
                tag="enableAllAnnotations",
                input_type=Boolean(optional=True),
                prefix="--enable-all-annotations",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Use all possible annotations (not for the faint of heart)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="floorBlocks",
                input_type=Boolean(optional=True),
                prefix="--floor-blocks",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Output the band lower bound for each GQ block regardless of the data it represents Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="genotypeFilteredAlleles",
                input_type=Boolean(optional=True),
                prefix="--genotype-filtered-alleles",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Whether to genotype all given alleles, even filtered ones, --genotyping-mode is GENOTYPE_GIVEN_ALLELES  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="gvcfGqBands",
                input_type=Int(optional=True),
                prefix="--gvcf-gq-bands",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-GQB) Exclusive upper bounds for reference confidence GQ bands (must be in [1, 100] and specified in increasing order)  This argument may be specified 0 or more times. Default value: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 70, 80, 90, 99]. "
                ),
            ),
            ToolInput(
                tag="indelSizeToEliminateInRefModel",
                input_type=Int(optional=True),
                prefix="--indel-size-to-eliminate-in-ref-model",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The size of an indel to check for in the reference model  Default value: 10. "
                ),
            ),
            ToolInput(
                tag="inputPrior",
                input_type=Double(optional=True),
                prefix="--input-prior",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Input prior for calls This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="kmerSize",
                input_type=Int(optional=True),
                prefix="--kmer-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Kmer size to use in the read threading assembler This argument may be specified 0 or more times. Default value: [10, 25]. "
                ),
            ),
            ToolInput(
                tag="maxAlternateAlleles",
                input_type=Int(optional=True),
                prefix="--max-alternate-alleles",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum number of alternate alleles to genotype  Default value: 6. "
                ),
            ),
            ToolInput(
                tag="maxGenotypeCount",
                input_type=Int(optional=True),
                prefix="--max-genotype-count",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Maximum number of genotypes to consider at any site Default value: 1024."
                ),
            ),
            ToolInput(
                tag="maxMnpDistance",
                input_type=Int(optional=True),
                prefix="--max-mnp-distance",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-mnp-dist)  Two or more phased substitutions separated by this distance or less are merged into MNPs.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="maxNumHaplotypesInPopulation",
                input_type=Int(optional=True),
                prefix="--max-num-haplotypes-in-population",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum number of haplotypes to consider for your population  Default value: 128. "
                ),
            ),
            ToolInput(
                tag="maxProbPropagationDistance",
                input_type=Int(optional=True),
                prefix="--max-prob-propagation-distance",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Upper limit on how many bases away probability mass can be moved around when calculating the boundaries between active and inactive assembly regions  Default value: 50. "
                ),
            ),
            ToolInput(
                tag="maxUnprunedVariants",
                input_type=Int(optional=True),
                prefix="--max-unpruned-variants",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum number of variants in graph the adaptive pruner will allow  Default value: 100. "
                ),
            ),
            ToolInput(
                tag="minDanglingBranchLength",
                input_type=Int(optional=True),
                prefix="--min-dangling-branch-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum length of a dangling branch to attempt recovery  Default value: 4. "
                ),
            ),
            ToolInput(
                tag="minPruning",
                input_type=Int(optional=True),
                prefix="--min-pruning",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Minimum support to not prune paths in the graph Default value: 2."
                ),
            ),
            ToolInput(
                tag="numPruningSamples",
                input_type=String(optional=True),
                prefix="--num-pruning-samples",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 1."),
            ),
            ToolInput(
                tag="pairHmmGapContinuationPenalty",
                input_type=Int(optional=True),
                prefix="--pair-hmm-gap-continuation-penalty",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Flat gap continuation penalty for use in the Pair HMM  Default value: 10. "
                ),
            ),
            ToolInput(
                tag="pairHmmImplementation",
                input_type=Boolean(optional=True),
                prefix="--pair-hmm-implementation",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-pairHMM)  The PairHMM implementation to use for genotype likelihood calculations  Default value: FASTEST_AVAILABLE. Possible values: {EXACT, ORIGINAL, LOGLESS_CACHING, AVX_LOGLESS_CACHING, AVX_LOGLESS_CACHING_OMP, EXPERIMENTAL_FPGA_LOGLESS_CACHING, FASTEST_AVAILABLE} "
                ),
            ),
            ToolInput(
                tag="pcrIndelModel",
                input_type=Boolean(optional=True),
                prefix="--pcr-indel-model",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The PCR indel model to use  Default value: CONSERVATIVE. Possible values: {NONE, HOSTILE, AGGRESSIVE, CONSERVATIVE} "
                ),
            ),
            ToolInput(
                tag="phredScaledGlobalReadMismappingRate",
                input_type=Int(optional=True),
                prefix="--phred-scaled-global-read-mismapping-rate",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The global assumed mismapping rate for reads  Default value: 45. "
                ),
            ),
            ToolInput(
                tag="pruningLodThreshold",
                input_type=Boolean(optional=True),
                prefix="--pruning-lod-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 2.302585092994046. "),
            ),
            ToolInput(
                tag="recoverAllDanglingBranches",
                input_type=Boolean(optional=True),
                prefix="--recover-all-dangling-branches",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Recover all dangling branches  Default value: false. Possible values: {true, false} "
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
                tag="smithWaterman",
                input_type=Boolean(optional=True),
                prefix="--smith-waterman",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Which Smith-Waterman implementation to use, generally FASTEST_AVAILABLE is the right choice  Default value: JAVA. Possible values: {FASTEST_AVAILABLE, AVX_ENABLED, JAVA} "
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
                tag="useAllelesTrigger",
                input_type=Boolean(optional=True),
                prefix="--use-alleles-trigger",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="useFilteredReadsForAnnotations",
                input_type=Boolean(optional=True),
                prefix="--use-filtered-reads-for-annotations",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Use the contamination-filtered read maps for the purposes of annotating variants  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="allowOldRmsMappingQualityAnnotationData",
                input_type=Boolean(optional=True),
                prefix="--allow-old-rms-mapping-quality-annotation-data",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Override to allow old RMSMappingQuality annotated VCFs to function  Default value: false. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:02:16.092000"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:02:16.092001"),
            documentation="**BETA FEATURE - WORK IN PROGRESS**\nUSAGE: ReadsPipelineSpark [arguments]\nTakes unaligned or aligned reads and runs BWA (if specified), MarkDuplicates, BQSR, and HaplotypeCaller. The final\nresult is analysis-ready variants.\nVersion:4.1.3.0\n",
        )
