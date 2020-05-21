from abc import ABC
from typing import Dict, Any

from janis_bioinformatics.data_types import BamBai, Bed, FastaWithDict, VcfTabix
from janis_core import (
    Array,
    Boolean,
    CaptureType,
    CpuSelector,
    Double,
    File,
    Filename,
    Float,
    InputSelector,
    Int,
    String,
    ToolInput,
    ToolMetadata,
    ToolOutput,
    get_value_for_hints_and_ordered_resource_tuple,
)
from janis_unix import TarFileGz, TextFile

from ..gatk4toolbase import Gatk4ToolBase

CORES_TUPLE = [
    # (CaptureType.key(), {
    #     CaptureType.CHROMOSOME: 2,
    #     CaptureType.EXOME: 2,
    #     CaptureType.THIRTYX: 2,
    #     CaptureType.NINETYX: 2,
    #     CaptureType.THREEHUNDREDX: 2
    # })
]

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 32,
            CaptureType.CHROMOSOME: 64,
            CaptureType.EXOME: 64,
            CaptureType.THIRTYX: 64,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class Gatk4Mutect2Base_4_1(Gatk4ToolBase, ABC):
    def friendly_name(self) -> str:
        return "GatkMutect2"

    def tool(self) -> str:
        return "Gatk4Mutect2"

    @classmethod
    def gatk_command(cls):
        return "Mutect2"

    def inputs(self):
        return [
            ToolInput(
                tag="tumorBams",
                input_type=Array(BamBai),
                prefix="-I",
                prefix_applies_to_all_elements=True,
                doc="(--input) BAM/SAM/CRAM file containing reads This argument must be specified at least once. Required. ",
            ),
            ToolInput(
                tag="normalBams",
                input_type=Array(BamBai),
                prefix="-I",
                prefix_applies_to_all_elements=True,
                doc="(--input) Extra BAM/SAM/CRAM file containing reads This argument must be specified at least once. Required. ",
            ),
            ToolInput(
                tag="normalSample",
                input_type=String,
                prefix="--normal-sample",
                doc="(--normal-sample, if) May be URL-encoded as output by GetSampleName with",
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf.gz"),
                position=20,
                prefix="-O",
            ),
            ToolInput(
                tag="reference",
                input_type=FastaWithDict(),
                prefix="--reference",
                doc="(-R) Reference sequence file Required.",
            ),
            ToolInput(
                tag="activityProfileOut",
                input_type=String(optional=True),
                prefix="--activity-profile-out",
                doc="Default value: null.",
            ),
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
                tag="afOfAllelesNotInResource",
                input_type=String(optional=True),
                prefix="--af-of-alleles-not-in-resource",
                doc="(-default-af)  Population allele fraction assigned to alleles not found in germline resource.  Please see docs/mutect/mutect2.pdf fora derivation of the default value.  Default value: -1.0. ",
            ),
            ToolInput(
                tag="alleles",
                input_type=String(optional=True),
                prefix="--alleles",
                doc="The set of alleles for which to force genotyping regardless of evidence Default value: null. ",
            ),
            ToolInput(
                tag="annotation",
                input_type=String(optional=True),
                prefix="--annotation",
                doc="(-A) One or more specific annotations to add to variant calls This argument may be specified 0 or more times. Default value: null. Possible Values: {AlleleFraction, AS_BaseQualityRankSumTest, AS_FisherStrand, AS_InbreedingCoeff, AS_MappingQualityRankSumTest, AS_QualByDepth, AS_ReadPosRankSumTest, AS_RMSMappingQuality, AS_StrandOddsRatio, BaseQuality, BaseQualityRankSumTest, ChromosomeCounts, ClippingRankSumTest, CountNs, Coverage, DepthPerAlleleBySample, DepthPerSampleHC, ExcessHet, FisherStrand, FragmentLength, GenotypeSummaries, InbreedingCoeff, LikelihoodRankSumTest, MappingQuality, MappingQualityRankSumTest, MappingQualityZero, OrientationBiasReadCounts, OriginalAlignment, PossibleDeNovo, QualByDepth, ReadPosition, ReadPosRankSumTest, ReferenceBases, RMSMappingQuality, SampleList, StrandBiasBySample, StrandOddsRatio, TandemRepeat, UniqueAltReadCount}",
            ),
            ToolInput(
                tag="annotationGroup",
                input_type=String(optional=True),
                prefix="--annotation-group",
                doc="(-G) One or more groups of annotations to apply to variant calls This argument may be specified 0 or more times. Default value: null. Possible Values: {AS_StandardAnnotation, ReducibleAnnotation, StandardAnnotation, StandardHCAnnotation, StandardMutectAnnotation}",
            ),
            ToolInput(
                tag="annotationsToExclude",
                input_type=String(optional=True),
                prefix="--annotations-to-exclude",
                doc="(-AX)  One or more specific annotations to exclude from variant calls  This argument may be specified 0 or more times. Default value: null. Possible Values: {BaseQuality, Coverage, DepthPerAlleleBySample, DepthPerSampleHC, FragmentLength, MappingQuality, OrientationBiasReadCounts, ReadPosition, StrandBiasBySample, TandemRepeat}",
            ),
            ToolInput(
                tag="arguments_file",
                input_type=File(optional=True),
                prefix="--arguments_file",
                doc="read one or more arguments files and add them to the command line This argument may be specified 0 or more times. Default value: null. ",
            ),
            ToolInput(
                tag="assemblyRegionOut",
                input_type=String(optional=True),
                prefix="--assembly-region-out",
                doc="Output the assembly region to this IGV formatted file Default value: null.",
            ),
            ToolInput(
                tag="baseQualityScoreThreshold",
                input_type=Int(optional=True),
                prefix="--base-quality-score-threshold",
                doc=" Base qualities below this threshold will be reduced to the minimum (6)  Default value: 18.",
            ),
            ToolInput(
                tag="callableDepth",
                input_type=Int(optional=True),
                prefix="--callable-depth",
                doc="Minimum depth to be considered callable for Mutect stats. Does not affect genotyping. Default value: 10. ",
            ),
            ToolInput(
                tag="cloudIndexPrefetchBuffer",
                input_type=Int(optional=True),
                prefix="--cloud-index-prefetch-buffer",
                doc="(-CIPB)  Size of the cloud-only prefetch buffer (in MB; 0 to disable). Defaults to cloudPrefetchBuffer if unset.  Default value: -1. ",
            ),
            ToolInput(
                tag="cloudPrefetchBuffer",
                input_type=Int(optional=True),
                prefix="--cloud-prefetch-buffer",
                doc="(-CPB)  Size of the cloud-only prefetch buffer (in MB; 0 to disable).  Default value: 40. ",
            ),
            ToolInput(
                tag="createOutputBamIndex",
                input_type=Boolean(optional=True),
                prefix="--create-output-bam-index",
                doc="(-OBI)  If true, create a BAM/CRAM index when writing a coordinate-sorted BAM/CRAM file.  Default value: true. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="createOutputBamMd5",
                input_type=Boolean(optional=True),
                prefix="--create-output-bam-md5",
                doc="(-OBM)  If true, create a MD5 digest for any BAM/SAM/CRAM file created  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="createOutputVariantIndex",
                input_type=Boolean(optional=True),
                prefix="--create-output-variant-index",
                doc="(-OVI)  If true, create a VCF index when writing a coordinate-sorted VCF file.  Default value: true. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="createOutputVariantMd5",
                input_type=Boolean(optional=True),
                prefix="--create-output-variant-md5",
                doc="(-OVM)  If true, create a a MD5 digest any VCF file created.  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="disableBamIndexCaching",
                input_type=Boolean(optional=True),
                prefix="--disable-bam-index-caching",
                doc="(-DBIC)  If true, don't cache bam indexes, this will reduce memory requirements but may harm performance if many intervals are specified.  Caching is automatically disabled if there are no intervals specified.  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="disableReadFilter",
                input_type=Boolean(optional=True),
                prefix="--disable-read-filter",
                doc="(-DF)  Read filters to be disabled before analysis  This argument may be specified 0 or more times. Default value: null. Possible Values: {GoodCigarReadFilter, MappedReadFilter, MappingQualityAvailableReadFilter, MappingQualityNotZeroReadFilter, MappingQualityReadFilter, NonChimericOriginalAlignmentReadFilter, NonZeroReferenceLengthAlignmentReadFilter, NotDuplicateReadFilter, NotSecondaryAlignmentReadFilter, PassesVendorQualityCheckReadFilter, ReadLengthReadFilter, WellformedReadFilter}",
            ),
            ToolInput(
                tag="disableSequenceDictionaryValidation",
                input_type=Boolean(optional=True),
                prefix="-disable-sequence-dictionary-validation",
                doc="(--disable-sequence-dictionary-validation)  If specified, do not check the sequence dictionaries from our inputs for compatibility. Use at your own risk!  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="downsamplingStride",
                input_type=Int(optional=True),
                prefix="--downsampling-stride",
                doc="(-stride)  Downsample a pool of reads starting within a range of one or more bases.  Default value: 1. ",
            ),
            ToolInput(
                tag="excludeIntervals",
                input_type=Boolean(optional=True),
                prefix="--exclude-intervals",
                doc="(-XLOne) This argument may be specified 0 or more times. Default value: null. ",
            ),
            ToolInput(
                tag="f1r2MaxDepth",
                input_type=Int(optional=True),
                prefix="--f1r2-max-depth",
                doc="sites with depth higher than this value will be grouped Default value: 200.",
            ),
            ToolInput(
                tag="f1r2MedianMq",
                input_type=Int(optional=True),
                prefix="--f1r2-median-mq",
                doc="skip sites with median mapping quality below this value Default value: 50.",
            ),
            ToolInput(
                tag="f1r2MinBq",
                input_type=Int(optional=True),
                prefix="--f1r2-min-bq",
                doc="exclude bases below this quality from pileup Default value: 20.",
            ),
            ToolInput(
                tag="f1r2TarGz_outputFilename",
                input_type=Filename(extension=".tar.gz"),
                prefix="--f1r2-tar-gz",
                doc="If specified, collect F1R2 counts and output files into this tar.gz file Default value: null. ",
            ),
            ToolInput(
                tag="founderId",
                input_type=String(optional=True),
                prefix="-founder-id",
                doc="(--founder-id)  Samples representing the population founders This argument may be specified 0 or more times. Default value: null. ",
            ),
            ToolInput(
                tag="gatkConfigFile",
                input_type=String(optional=True),
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
                doc=" Project to bill when accessing requester pays buckets. If unset, these buckets cannot be accessed.  Default value: . ",
            ),
            ToolInput(
                tag="genotypeGermlineSites",
                input_type=Boolean(optional=True),
                prefix="--genotype-germline-sites",
                doc=" (EXPERIMENTAL) Call all apparent germline site even though they will ultimately be filtered.  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="genotypePonSites",
                input_type=Boolean(optional=True),
                prefix="--genotype-pon-sites",
                doc="Call sites in the PoN even though they will ultimately be filtered. Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="germlineResource",
                input_type=VcfTabix(optional=True),
                prefix="--germline-resource",
                doc=" Population vcf of germline sequencing containing allele fractions.  Default value: null. ",
            ),
            ToolInput(
                tag="graph",
                input_type=String(optional=True),
                prefix="-graph",
                doc="(--graph-output) Write debug assembly graph information to this file Default value: null.",
            ),
            ToolInput(
                tag="help",
                input_type=Boolean(optional=True),
                prefix="-h",
                doc="(--help) display the help message Default value: false. Possible values: {true, false}",
            ),
            ToolInput(
                tag="ignoreItrArtifacts",
                input_type=String(optional=True),
                prefix="--ignore-itr-artifactsTurn",
                doc=" inverted tandem repeats.  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="initialTumorLod",
                input_type=String(optional=True),
                prefix="--initial-tumor-lod",
                doc="(-init-lod)  Log 10 odds threshold to consider pileup active.  Default value: 2.0. ",
            ),
            ToolInput(
                tag="intervalExclusionPadding",
                input_type=String(optional=True),
                prefix="--interval-exclusion-padding",
                doc="(-ixp)  Amount of padding (in bp) to add to each interval you are excluding.  Default value: 0. ",
            ),
            ToolInput(
                tag="imr",
                input_type=String(optional=True),
                prefix="--interval-merging-rule",
                doc="(--interval-merging-rule)  Interval merging rule for abutting intervals  Default value: ALL. Possible values: {ALL, OVERLAPPING_ONLY} ",
            ),
            ToolInput(
                tag="ip",
                input_type=String(optional=True),
                prefix="-ipAmount",
                doc="(--interval-padding) Default value: 0.",
            ),
            ToolInput(
                tag="isr",
                input_type=String(optional=True),
                prefix="--interval-set-rule",
                doc="(--interval-set-rule)  Set merging approach to use for combining interval inputs  Default value: UNION. Possible values: {UNION, INTERSECTION} ",
            ),
            ToolInput(
                tag="intervals",
                input_type=Bed(optional=True),
                prefix="--intervals",
                doc="(-L) One or more genomic intervals over which to operate This argument may be specified 0 or more times. Default value: null. ",
            ),
            ToolInput(
                tag="le",
                input_type=Boolean(optional=True),
                prefix="-LE",
                doc="(--lenient) Lenient processing of VCF files Default value: false. Possible values: {true, false}",
            ),
            ToolInput(
                tag="maxPopulationAf",
                input_type=String(optional=True),
                prefix="--max-population-af",
                doc="(-max-af)  Maximum population allele frequency in tumor-only mode.  Default value: 0.01. ",
            ),
            ToolInput(
                tag="maxReadsPerAlignmentStart",
                input_type=Int(optional=True),
                prefix="--max-reads-per-alignment-start",
                doc=" Maximum number of reads to retain per alignment start position. Reads above this threshold will be downsampled. Set to 0 to disable.  Default value: 50. ",
            ),
            ToolInput(
                tag="minBaseQualityScore",
                input_type=String(optional=True),
                prefix="--min-base-quality-score",
                doc="(-mbq:Byte)  Minimum base quality required to consider a base for calling  Default value: 10. ",
            ),
            ToolInput(
                tag="mitochondriaMode",
                input_type=Boolean(optional=True),
                prefix="--mitochondria-mode",
                doc="Mitochondria mode sets emission and initial LODs to 0. Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="nativePairHmmThreads",
                input_type=Int(optional=True),
                prefix="--native-pair-hmm-threads",
                default=CpuSelector(),
                doc=" How many threads should a native pairHMM implementation use  Default value: 4. ",
            ),
            ToolInput(
                tag="nativePairHmmUseDoublePrecision",
                input_type=Boolean(optional=True),
                prefix="--native-pair-hmm-use-double-precision",
                doc=" use double precision in the native pairHmm. This is slower but matches the java implementation better  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="normalLod",
                input_type=Double(optional=True),
                prefix="--normal-lod",
                doc="Log 10 odds threshold for calling normal variant non-germline. Default value: 2.2.",
            ),
            ToolInput(
                tag="encode",
                input_type=String(optional=True),
                prefix="-encode",
                doc="This argument may be specified 0 or more times. Default value: null.",
            ),
            ToolInput(
                tag="panelOfNormals",
                input_type=VcfTabix(optional=True),
                prefix="--panel-of-normals",
                doc="(--panel-of-normals)  VCF file of sites observed in normal.  Default value: null. ",
            ),
            ToolInput(
                tag="pcrIndelQual",
                input_type=Int(optional=True),
                prefix="--pcr-indel-qual",
                doc="Phred-scaled PCR SNV qual for overlapping fragments Default value: 40.",
            ),
            ToolInput(
                tag="pcrSnvQual",
                input_type=Int(optional=True),
                prefix="--pcr-snv-qual",
                doc="Phred-scaled PCR SNV qual for overlapping fragments Default value: 40.",
            ),
            ToolInput(
                tag="pedigree",
                input_type=String(optional=True),
                prefix="--pedigree",
                doc="(-ped) Pedigree file for determining the population founders. Default value: null.",
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
                doc="(-RF) Read filters to be applied before analysis This argument may be specified 0 or more times. Default value: null. Possible Values: {AlignmentAgreesWithHeaderReadFilter, AllowAllReadsReadFilter, AmbiguousBaseReadFilter, CigarContainsNoNOperator, FirstOfPairReadFilter, FragmentLengthReadFilter, GoodCigarReadFilter, HasReadGroupReadFilter, IntervalOverlapReadFilter, LibraryReadFilter, MappedReadFilter, MappingQualityAvailableReadFilter, MappingQualityNotZeroReadFilter, MappingQualityReadFilter, MatchingBasesAndQualsReadFilter, MateDifferentStrandReadFilter, MateOnSameContigOrNoMappedMateReadFilter, MateUnmappedAndUnmappedReadFilter, MetricsReadFilter, NonChimericOriginalAlignmentReadFilter, NonZeroFragmentLengthReadFilter, NonZeroReferenceLengthAlignmentReadFilter, NotDuplicateReadFilter, NotOpticalDuplicateReadFilter, NotSecondaryAlignmentReadFilter, NotSupplementaryAlignmentReadFilter, OverclippedReadFilter, PairedReadFilter, PassesVendorQualityCheckReadFilter, PlatformReadFilter, PlatformUnitReadFilter, PrimaryLineReadFilter, ProperlyPairedReadFilter, ReadGroupBlackListReadFilter, ReadGroupReadFilter, ReadLengthEqualsCigarLengthReadFilter, ReadLengthReadFilter, ReadNameReadFilter, ReadStrandFilter, SampleReadFilter, SecondOfPairReadFilter, SeqIsStoredReadFilter, ValidAlignmentEndReadFilter, ValidAlignmentStartReadFilter, WellformedReadFilter}",
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
                doc="(-VS:ValidationStringency)  Validation stringency for all SAM/BAM/CRAM/SRA files read by this program.  The default stringency value SILENT can improve performance when processing a BAM file in which variable-length data (read, qualities, tags) do not otherwise need to be decoded.  Default value: SILENT. Possible values: {STRICT, LENIENT, SILENT} ",
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
                prefix="--sites-only-vcf-output",
                doc=" If true, don't emit genotype fields when writing vcf file output.  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="tmpDir",
                input_type=String(optional=True),
                prefix="--tmp-dir",
                doc="Temp directory to use. Default value: null.",
            ),
            ToolInput(
                tag="tumorLodToEmit",
                input_type=String(optional=True),
                prefix="--tumor-lod-to-emit",
                doc="(-emit-lod)  Log 10 odds threshold to emit variant to VCF.  Default value: 3.0. ",
            ),
            ToolInput(
                tag="tumor",
                input_type=String(optional=True),
                prefix="-tumor",
                doc="(--tumor-sample) BAM sample name of tumor. May be URL-encoded as output by GetSampleName with -encode argument.  Default value: null. ",
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
                prefix="-verbosity",
                doc="(--verbosity)  Control verbosity of logging.  Default value: INFO. Possible values: {ERROR, WARNING, INFO, DEBUG} ",
            ),
            ToolInput(
                tag="version",
                input_type=Boolean(optional=True),
                prefix="--version",
                doc="display the version number for this tool Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="activeProbabilityThreshold",
                input_type=Double(optional=True),
                prefix="--active-probability-threshold",
                doc=" Minimum probability for a locus to be considered active.  Default value: 0.002. ",
            ),
            ToolInput(
                tag="adaptivePruningInitialErrorRate",
                input_type=Double(optional=True),
                prefix="--adaptive-pruning-initial-error-rate",
                doc=" Initial base error rate estimate for adaptive pruning  Default value: 0.001. ",
            ),
            ToolInput(
                tag="allowNonUniqueKmersInRef",
                input_type=Boolean(optional=True),
                prefix="--allow-non-unique-kmers-in-ref",
                doc=" Allow graphs that have non-unique kmers in the reference  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="assemblyRegionPadding",
                input_type=Int(optional=True),
                prefix="--assembly-region-padding",
                doc=" Number of additional bases of context to include around each assembly region  Default value: 100. ",
            ),
            ToolInput(
                tag="bamout",
                input_type=String(optional=True),
                prefix="-bamout",
                doc="(--bam-output) File to which assembled haplotypes should be written Default value: null.",
            ),
            ToolInput(
                tag="bamWriterType",
                input_type=String(optional=True),
                prefix="--bam-writer-type",
                doc="Which haplotypes should be written to the BAM Default value: CALLED_HAPLOTYPES. Possible values: {ALL_POSSIBLE_HAPLOTYPES, CALLED_HAPLOTYPES} ",
            ),
            ToolInput(
                tag="debugAssembly",
                input_type=String(optional=True),
                prefix="--debug-assembly",
                doc="(-debug)  Print out verbose debug information about each assembly region  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="disableAdaptivePruning",
                input_type=Boolean(optional=True),
                prefix="--disable-adaptive-pruning",
                doc=" Disable the adaptive algorithm for pruning paths in the graph  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="disableToolDefaultAnnotations",
                input_type=Boolean(optional=True),
                prefix="-disable-tool-default-annotations",
                doc="(--disable-tool-default-annotations)  Disable all tool default annotations  Default value: false. Possible values: {true, false}",
            ),
            ToolInput(
                tag="disableToolDefaultReadFilters",
                input_type=Boolean(optional=True),
                prefix="-disable-tool-default-read-filters",
                doc="(--disable-tool-default-read-filters)  Disable all tool default read filters (WARNING: many tools will not function correctly without their default read filters on)  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="dontIncreaseKmerSizesForCycles",
                input_type=Boolean(optional=True),
                prefix="--dont-increase-kmer-sizes-for-cycles",
                doc=" Disable iterating over kmer sizes when graph cycles are detected  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="dontTrimActiveRegions",
                input_type=Boolean(optional=True),
                prefix="--dont-trim-active-regions",
                doc=" If specified, we will not trim down the active region from the full region (active + extension) to just the active interval for genotyping  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="dontUseSoftClippedBases",
                input_type=Boolean(optional=True),
                prefix="--dont-use-soft-clipped-bases",
                doc=" Do not analyze soft clipped bases in the reads  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="erc",
                input_type=String(optional=True),
                prefix="-ERC",
                doc="(--emit-ref-confidence)  (BETA feature) Mode for emitting reference confidence scores  Default value: NONE. Possible values: {NONE, BP_RESOLUTION, GVCF} ",
            ),
            ToolInput(
                tag="enableAllAnnotations",
                input_type=Boolean(optional=True),
                prefix="--enable-all-annotations",
                doc=" Use all possible annotations (not for the faint of heart)  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="forceActive",
                input_type=Boolean(optional=True),
                prefix="--force-active",
                doc="If provided, all regions will be marked as active Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="genotypeFilteredAlleles",
                input_type=Boolean(optional=True),
                prefix="--genotype-filtered-alleles",
                doc=" Whether to force genotype even filtered alleles  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="gvcfLodBand",
                input_type=String(optional=True),
                prefix="--gvcf-lod-band",
                doc="(-LODB) Exclusive upper bounds for reference confidence LOD bands (must be specified in increasing order)  This argument may be specified 0 or more times. Default value: [-2.5, -2.0, -1.5,",
            ),
            ToolInput(
                tag="kmerSize",
                input_type=Int(optional=True),
                prefix="--kmer-size",
                doc="Kmer size to use in the read threading assembler This argument may be specified 0 or more times. Default value: [10, 25]. ",
            ),
            ToolInput(
                tag="maxAssemblyRegionSize",
                input_type=Int(optional=True),
                prefix="--max-assembly-region-size",
                doc=" Maximum size of an assembly region  Default value: 300. ",
            ),
            ToolInput(
                tag="mnpDist",
                input_type=Int(optional=True),
                prefix="-mnp-dist",
                doc="(--max-mnp-distance)  Two or more phased substitutions separated by this distance or less are merged into MNPs.  Default value: 1. ",
            ),
            ToolInput(
                tag="maxNumHaplotypesInPopulation",
                input_type=Int(optional=True),
                prefix="--max-num-haplotypes-in-population",
                doc=" Maximum number of haplotypes to consider for your population  Default value: 128. ",
            ),
            ToolInput(
                tag="maxProbPropagationDistance",
                input_type=Int(optional=True),
                prefix="--max-prob-propagation-distance",
                doc=" Upper limit on how many bases away probability mass can be moved around when calculating the boundaries between active and inactive assembly regions  Default value: 50. ",
            ),
            ToolInput(
                tag="maxSuspiciousReadsPerAlignmentStart",
                input_type=Int(optional=True),
                prefix="--max-suspicious-reads-per-alignment-start",
                doc=" Maximum number of suspicious reads (mediocre mapping quality or too many substitutions) allowed in a downsampling stride.  Set to 0 to disable.  Default value: 0. ",
            ),
            ToolInput(
                tag="maxUnprunedVariants",
                input_type=Int(optional=True),
                prefix="--max-unpruned-variants",
                doc=" Maximum number of variants in graph the adaptive pruner will allow  Default value: 100. ",
            ),
            ToolInput(
                tag="minAssemblyRegionSize",
                input_type=Int(optional=True),
                prefix="--min-assembly-region-size",
                doc=" Minimum size of an assembly region  Default value: 50. ",
            ),
            ToolInput(
                tag="minDanglingBranchLength",
                input_type=Int(optional=True),
                prefix="--min-dangling-branch-length",
                doc=" Minimum length of a dangling branch to attempt recovery  Default value: 4. ",
            ),
            ToolInput(
                tag="minPruning",
                input_type=Int(optional=True),
                prefix="--min-pruning",
                doc="Minimum support to not prune paths in the graph Default value: 2.",
            ),
            ToolInput(
                tag="minimumAlleleFraction",
                input_type=Float(optional=True),
                prefix="--minimum-allele-fraction",
                doc="(-min-AF)  Lower bound of variant allele fractions to consider when calculating variant LOD  Default value: 0.0. ",
            ),
            ToolInput(
                tag="numPruningSamples",
                input_type=Int(optional=True),
                prefix="--num-pruning-samples",
                doc="Default value: 1.",
            ),
            ToolInput(
                tag="pairHmmGapContinuationPenalty",
                input_type=Int(optional=True),
                prefix="--pair-hmm-gap-continuation-penalty",
                doc=" Flat gap continuation penalty for use in the Pair HMM  Default value: 10. ",
            ),
            ToolInput(
                tag="pairhmm",
                input_type=String(optional=True),
                prefix="-pairHMM",
                doc="(--pair-hmm-implementation)  The PairHMM implementation to use for genotype likelihood calculations  Default value: FASTEST_AVAILABLE. Possible values: {EXACT, ORIGINAL, LOGLESS_CACHING, AVX_LOGLESS_CACHING, AVX_LOGLESS_CACHING_OMP, EXPERIMENTAL_FPGA_LOGLESS_CACHING, FASTEST_AVAILABLE} ",
            ),
            ToolInput(
                tag="pcrIndelModel",
                input_type=String(optional=True),
                prefix="--pcr-indel-model",
                doc=" The PCR indel model to use  Default value: CONSERVATIVE. Possible values: {NONE, HOSTILE, AGGRESSIVE, CONSERVATIVE} ",
            ),
            ToolInput(
                tag="phredScaledGlobalReadMismappingRate",
                input_type=Int(optional=True),
                prefix="--phred-scaled-global-read-mismapping-rate",
                doc=" The global assumed mismapping rate for reads  Default value: 45. ",
            ),
            ToolInput(
                tag="pruningLodThreshold",
                input_type=Float(optional=True),
                prefix="--pruning-lod-thresholdLn",
                doc="Default value: 2.302585092994046. ",
            ),
            ToolInput(
                tag="recoverAllDanglingBranches",
                input_type=Boolean(optional=True),
                prefix="--recover-all-dangling-branches",
                doc=" Recover all dangling branches  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="showhidden",
                input_type=Boolean(optional=True),
                prefix="-showHidden",
                doc="(--showHidden)  display hidden arguments  Default value: false. Possible values: {true, false} ",
            ),
            ToolInput(
                tag="smithWaterman",
                input_type=String(optional=True),
                prefix="--smith-waterman",
                doc=" Which Smith-Waterman implementation to use, generally FASTEST_AVAILABLE is the right choice  Default value: JAVA. Possible values: {FASTEST_AVAILABLE, AVX_ENABLED, JAVA} ",
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
                doc="One or more genomic intervals to keep This argument must be specified at least once. Required. ",
            ),
            ToolInput(
                tag="library",
                input_type=String(optional=True),
                prefix="-library",
                doc="(--library) Name of the library to keep This argument must be specified at least once. Required.",
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
                doc=" Minimum mapping quality to keep (inclusive)  Default value: 20. ",
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
                prefix="--platform-filter-name",
                doc="This argument must be specified at least once. Required.",
            ),
            ToolInput(
                tag="blackListedLanes",
                input_type=String(optional=True),
                prefix="--black-listed-lanes",
                doc="Platform unit (PU) to filter out This argument must be specified at least once. Required.",
            ),
            ToolInput(
                tag="readGroupBlackList",
                input_type=String(optional=True),
                prefix="--read-group-black-listThe",
                doc="This argument must be specified at least once. Required. ",
            ),
            ToolInput(
                tag="keepReadGroup",
                input_type=String(optional=True),
                prefix="--keep-read-group",
                doc="The name of the read group to keep Required.",
            ),
            ToolInput(
                tag="maxReadLength",
                input_type=Int(optional=True),
                prefix="--max-read-length",
                doc="Keep only reads with length at most equal to the specified value Default value: 2147483647. ",
            ),
            ToolInput(
                tag="minReadLength",
                input_type=Int(optional=True),
                prefix="--min-read-length",
                doc="Keep only reads with length at least equal to the specified value Default value: 30.",
            ),
            ToolInput(
                tag="readName",
                input_type=String(optional=True),
                prefix="--read-name",
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
                prefix="-sample",
                doc="(--sample) The name of the sample(s) to keep, filtering out all others This argument must be specified at least once. Required. ",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                VcfTabix,
                glob=InputSelector("outputFilename"),
                doc="To determine type",
            ),
            ToolOutput(
                "stats",
                TextFile(extension=".stats"),
                glob=InputSelector("outputFilename") + ".stats",
                doc="To determine type",
            ),
            ToolOutput(
                "f1f2r_out",
                TarFileGz,
                glob=InputSelector("f1r2TarGz_outputFilename"),
                doc="To determine type",
            ),
        ]

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 4

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 16

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=date(2018, 12, 24),
            dateUpdated=date(2019, 1, 24),
            institution="Broad Institute",
            doi=None,
            citation="See https://software.broadinstitute.org/gatk/documentation/article?id=11027 for more information",
            keywords=["gatk", "gatk4", "broad", "mutect2"],
            documentationUrl="https://software.broadinstitute.org/gatk/documentation/tooldocs/4.0.10.0/org_broadinstitute_hellbender_tools_walkers_mutect_Mutect2.php",
            documentation="USAGE: Mutect2 [arguments]\nCall somatic SNVs and indels via local assembly of haplotypes\nVersion:4.1.2.0\n",
        )
