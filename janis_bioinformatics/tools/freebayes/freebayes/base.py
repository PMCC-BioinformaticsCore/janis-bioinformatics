from abc import ABC
from typing import Dict, Any

from janis_core import (
    ToolInput,
    Filename,
    ToolOutput,
    String,
    Float,
    InputSelector,
    CaptureType,
    ToolArgument,
    MemorySelector,
    Array,
    Int,
    Boolean,
    File,
    Double,
    CpuSelector,
    get_value_for_hints_and_ordered_resource_tuple,
    ToolMetadata,
)
from janis_unix import TarFileGz, TextFile

from janis_bioinformatics.data_types import (
    BamBai,
    Bed,
    FastaWithDict,
    VcfIdx,
    Vcf,
    VcfTabix,
    CompressedVcf,
)


CORES_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 2,
            CaptureType.CHROMOSOME: 4,
            CaptureType.EXOME: 4,
            CaptureType.THIRTYX: 4,
            CaptureType.NINETYX: 4,
            CaptureType.THREEHUNDREDX: 4,
        },
    )
]

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 4,
            CaptureType.CHROMOSOME: 16,
            CaptureType.EXOME: 32,
            CaptureType.THIRTYX: 64,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]

class freebayesBase(BioinformaticsTool, ABC):
    def friendly_name(self) -> str:
        return "freebayes"

    @staticmethod
    def tools_provider():
        return "freebayes"

    @staticmethod
    def tool():
        return "freebayes"

    @staticmethod
    def base_command():
        return "freebayes"

    def cpus(self, hints: Dict[str, Any]):
        val=get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return4

    def memory(self, hints: Dict[str, Any]):
        val=get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 8

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput(
                tag="bams",
                input_type=Array(BamBai),
                prefix="-b",
                prefix_applies_to_all_elements=True,
                doc="Add FILE to the set of BAM files to be analyzed.",
            ),
            ToolInput(
                tag="bamList",
                input_type=TextFile(optional=True)
                prefix="-L",
                doc="A file containing a list of BAM files to be analyzed.",
            ),
            ToolInput(
                tag="stdin",
                prefix="-c",
                doc="Read BAM input on stdin.",
            ),
            ToolInput(
                tag="reference",
                input_type=FastaWithDict(),
                prefix="-f",
                doc=" Use FILE as the reference sequence for analysis. An index file (FILE.fai) will be created if none exists. If neither --targets nor --region are specified, FreeBayes will analyze every position in this reference.",
                ),
            ToolInput(
                tag="targetsFile",
            	prefix="-t",
                input_type=BedFile(optional=True),
                doc=" Limit analysis to targets listed in the BED-format FILE.",
            ),
            ToolInput(
                tag="region",
            	prefix="-r",
                input_type=String(optional=True)
                doc="<chrom>:<start_position>-<end_position> Limit analysis to the specified region, 0-base coordinates, end_position not included (same as BED format). Either '-' or '..' maybe used as a separator.",
            ),
            ToolInput(
                tag="samplesFile",
            	prefix="-s",
                input_type=TextFile(optional=True),
                doc="FILE  Limit analysis to samples listed (one per line) in the FILE. By default FreeBayes will analyze all samples in its input BAM files.",
            ),
            ToolInput(
                tag="popFile",
            	prefix="--populations",
                input_type=TextFile(optional=True),
                doc="FILE Each line of FILE should list a sample and a population which it is part of. The population-based bayesian inference model will then be partitioned on the basis of the populations.",
            ),
            ToolInput(
                tag="cnvFile",
            	prefix="-A",
                input_type=TextFile(optional=True),
                doc="FILE Read a copy number map from the BED file FILE, which has either a sample-level ploidy: sample name, copy number or a region-specific format: reference sequence, start, end, sample name, copy number ... for each region in each sample which does not have the default copy number as set by --ploidy.",
            ),
            ToolInput(
                tag="outputFilename",
            	prefix="-v",
                input_type=Vcf(),
                doc="FILE Output VCF-format results to FILE. (default: stdout)",
            ),
            ToolInput(
                tag="gvcfFlag",
            	prefix="--gvcf",
                input_type=Boolean(optional=True),
                default=False,
                doc="Write gVCF output, which indicates coverage in uncalled regions.",
            ),
            ToolInput(
                tag="gvcfChunkSize",
            	prefix="--gvcf-chunk",
                input_type=Int(optional=True)
                doc=" When writing gVCF output emit a record for every NUM bases.",
            ),
            ToolInput(
                tag="candidateVcf",
            	prefix="-@",
                input_type=File(optional=True),
                doc=" Use variants reported in VCF file as input to the algorithm. Variants in this file will included in the output even if there is not enough support in the data to pass input filters.",
            ),
            ToolInput(
                tag="restrictSitesFlag",
            	prefix="-l",
                input_type=Boolean(optional=True),
                doc="Only provide variant calls and genotype likelihoods for sites and alleles which are provided in the VCF input, and provide output in the VCF for all input alleles, not just those which have support in the data.",
            ),
            ToolInput(
                tag="candidateHaploVcf",
            	prefix="--haplotype-basis-alleles",
                input_type=File(optional=True),
                doc="When specified, only variant alleles provided in this input VCF will be used for the construction of complex or haplotype alleles.",
            ),
            ToolInput(
                tag="reportHapAllelesFlag",
            	prefix="--report-all-haplotype-alleles",
                input_type=Boolean(optional=True),
                doc="At sites where genotypes are made over haplotype alleles, provide information about all alleles in output, not only those which are called.",
            ),
            ToolInput(
                tag="monomorphicFlag",
            	prefix="--report-monomorphic",
                input_type=Boolean(optional=True),
                doc=" Report even loci which appear to be monomorphic, and report all considered alleles, even those which are not in called genotypes. Loci which do not have any potential alternates have '.' for ALT.",
            ),
            ToolInput(
                tag="polyMoprhProbFlag",
            	prefix="-P",
                input_type=Float(optional=True),
                default=0.0,
                doc="Report sites if the probability that there is a polymorphism at the site is greater than N. default: 0.0. Note that post-filtering is generally recommended over the use of this parameter.",
            ),
            ToolInput(
                tag="strictFlag",
            	prefix="--strict-vcf",
                input_type=Boolean(optional=True),
                doc="Generate strict VCF format (FORMAT/GQ will be an int)",
            ),
            ToolInput(
                tag="theta",
            	prefix="-T",
                input_type=Float(),
                default=0.001,
                doc="The expected mutation rate or pairwise nucleotide diversity among the population under analysis. This serves as the single parameter to the Ewens Sampling Formula prior model default: 0.001",
            ),
            ToolInput(
                tag="ploidy",
            	prefix="-p",
                input_type=Int(),
                default=2,
                doc="Sets the default ploidy for the analysis to N. default: 2",
            ),
            ToolInput(
                tag="pooledDiscreteFlag",
            	prefix="-J",
                input_type=Boolean(optional=True),
                doc="Assume that samples result from pooled sequencing. Model pooled samples using discrete genotypes across pools. When using this flag, set --ploidy to the number of alleles in each sample or use the --cnv-map to define per-sample ploidy.",
            ),
            ToolInput(
                tag="pooledContinousFlag",
            	prefix="-K",
                input_type=Boolean(optional=True),
                doc="Output all alleles which pass input filters, regardles of genotyping outcome or model.",
            ),
            ToolInput(
                tag="addRefFlag",
            	prefix="-Z",
                input_type=Boolean(optional=True),
                doc="This flag includes the reference allele in the analysis as if it is another sample from the same population.",
            ),
            ToolInput(
                tag="refQual",
            	prefix="--reference-quality",
                input_type=String(),
                default="100,60",
                doc="--reference-quality MQ,BQ  Assign mapping quality of MQ to the reference allele at each site and base quality of BQ. default: 100,60",
            ),
            ToolInput(
                tag="ignoreSNPsFlag",
            	prefix="-I",
                input_type=Boolean(optional=True),
                doc="Ignore SNP alleles.",
            ),
            ToolInput(
                tag="ignoreINDELsFlag",
            	prefix="-i",
                input_type=Boolean(optional=True),
                doc="Ignore insertion and deletion alleles.",
            ),
            ToolInput(
                tag="ignoreMNPsFlag",
            	prefix="-X",
                input_type=Boolean(optional=True),
                doc="Ignore multi-nuceotide polymorphisms, MNPs.",
            ),
            ToolInput(
                tag='ignoreComplexVarsFlag',
            	prefix="-u",
                input_type=Boolean(optional=True),
                doc="Ignore complex events (composites of other classes).",
            ),
            ToolInput(
                tag="maxNumOfAlleles",
            	prefix="-n",
                input_type=Int(),
                default=0,
                doc="Evaluate only the best N SNP alleles, ranked by sum of supporting quality scores. (Set to 0 to use all; default: all)",
            ),
            ToolInput(
                tag="maxNumOfComplexVars",
            	prefix="-E",
                input_type=Int(optional=True),
                doc="",
            ),
            ToolInput(
                tag="haplotypeLength",
            	prefix="--haplotype-length",
                input_type=Int(),
                default=3,
                doc="Allow haplotype calls with contiguous embedded matches of up to this length. Set N=-1 to disable clumping. (default: 3)",
            ),
            ToolInput(
                tag="minRepSize",
            	prefix="--min-repeat-size",
                input_type=Int(),
                default=5,
                doc="When assembling observations across repeats, require the total repeat length at least this many bp. (default: 5)",
            ),
            ToolInput(
                tag="minRepEntropy",
            	prefix="--min-repeat-entropy",
                input_type=Int(),
                default=1,
                doc="To detect interrupted repeats, build across sequence until it has  entropy > N bits per bp. Set to 0 to turn off. (default: 1)",
            ),
            ToolInput(
                tag="noPartObsFlag",
            	prefix="--no-partial-observations",
                input_type=Boolean(optional=True),
                doc="Exclude observations which do not fully span the dynamically-determined detection window. (default, use all observations, dividing partial support across matching haplotypes when generating haplotypes.)",
            ),
            ToolInput(
                tag="noNormaliseFlag",
            	prefix="-O",
                input_type=Boolean(optional=True),
                doc="Turn off left-alignment of indels, which is enabled by default.",
            ),
            ToolInput(
                tag="useDupFlag",
            	prefix="-4",
                input_type=Boolean(),
                default=False,
                doc="Include duplicate-marked alignments in the analysis. default: exclude duplicates marked as such in alignments",
            ),
            ToolInput(
                tag="minMappingQual",
            	prefix="-m",
                input_type=Int(),
                default=1,
                doc=" Exclude alignments from analysis if they have a mapping quality less than Q. default: 1",
            ),
            ToolInput(
                tag="minBaseQual",
            	prefix="-q",
                input_type=Int(),
                default=0,
            	doc=" -q --min-base-quality Q Exclude alleles from analysis if their supporting base quality is less than Q. default: 0",
            ),
            ToolInput(
                tag="minSupQsum",
            	prefix="-R",
                input_type=Int(),
                default=0,
            	doc=" -R --min-supporting-allele-qsum Q Consider any allele in which the sum of qualities of supporting observations is at least Q. default: 0",
            ),
            ToolInput(
                tag="minSupMQsum",
            	prefix="-Y",
                input_type=Int(),
                default=0,
            	doc=" -Y --min-supporting-mapping-qsum Q Consider any allele in which and the sum of mapping qualities of supporting reads is at least Q. default: 0",
            ),
            ToolInput(
                tag="minSupBQthres",
            	prefix="-Q",
                input_type=Int(),
                default=10,
            	doc=" -Q --mismatch-base-quality-threshold Q Count mismatches toward --read-mismatch-limit if the base quality of the mismatch is >= Q. default: 10",
            ),
            ToolInput(
                tag="readMisMatchLim",
            	prefix="-U",
                input_type=Int(optional=True),
            	doc=" -U --read-mismatch-limit N Exclude reads with more than N mismatches where each mismatch has base quality >= mismatch-base-quality-threshold. default: ~unbounded",
            ),
            ToolInput(
                tag="maxMisMatchFrac",
            	prefix="-z",
                input_type=Float(),
                default=1.0,
            	doc=" -z --read-max-mismatch-fraction N Exclude reads with more than N [0,1] fraction of mismatches where each mismatch has base quality >= mismatch-base-quality-threshold default: 1.0",
            ),
            ToolInput(
                tag="readSNPLim",
            	prefix="-$",
                input_type=Int(optional=True),
            	doc=" -$ --read-snp-limit N Exclude reads with more than N base mismatches, ignoring gaps with quality >= mismatch-base-quality-threshold. default: ~unbounded",
            ),
            ToolInput(
                tag="readINDELLim",
            	prefix="-e",
                input_type=Int(optional=True),
            	doc=" -e --read-indel-limit N Exclude reads with more than N separate gaps. default: ~unbounded",
            ),
            ToolInput(
                tag="standardFilterFlag",
            	prefix="-0",
                input_type=Boolean(optional=True),
            	doc=" -0 --standard-filters Use stringent input base and mapping quality filters Equivalent to -m 30 -q 20 -R 0 -S 0",
            ),
            ToolInput(
                tag="minAltFrac",
            	prefix="-F",
                input_type=Float(),
                default=0.05,
            	doc=" -F --min-alternate-fraction N Require at least this fraction of observations supporting an alternate allele within a single individual in the in order to evaluate the position. default: 0.05",
            ),
            ToolInput(
                tag="minAltCount",
            	prefix="-C",
                input_type=Int(),
                default=2,
            	doc=" -C --min-alternate-count N Require at least this count of observations supporting an alternate allele within a single individual in order to evaluate the position. default: 2",
            ),
            ToolInput(
                tag="minAltQSum",
            	prefix="-3",
                input_type=Int(),
                default=0,
            	doc=" -3 --min-alternate-qsum N Require at least this sum of quality of observations supporting an alternate allele within a single individual in order to evaluate the position. default: 0",
            ),
            ToolInput(
                tag="minAltTotal",
            	prefix="-G",
                input_type=Int(),
                default=1,
            	doc=" -G --min-alternate-total N Require at least this count of observations supporting an alternate allele within the total population in order to use the allele in analysis. default: 1",
            ),
            ToolInput(
                tag="minCov",
            	prefix="--min-coverage",
                input_type=Int(),
                default=0,
            	doc=" --min-coverage N Require at least this coverage to process a site. default: 0",
            ),
            ToolInput(
                tag="maxCov",
            	prefix="--max-coverage",
                input_type=Int(optional=True),
            	doc=" --max-coverage N Do not process sites with greater than this coverage. default: no limit",
            ),
            ToolInput(
                tag="noPopPriorsFlag",
            	prefix="-k",
                input_type=Boolean(optional=True),
            	doc=" -k --no-population-priors Equivalent to --pooled-discrete --hwe-priors-off and removal of Ewens Sampling Formula component of priors.",
            ),
            ToolInput(
                tag="noHWEPriorsFlag",
            	prefix="-w",
                input_type=Boolean(optional=True),
            	doc=" -w --hwe-priors-off Disable estimation of the probability of the combination arising under HWE given the allele frequency as estimated by observation frequency.",
            ),
            ToolInput(
                tag="noBinOBSPriorsFlag",
            	prefix="-V",
                input_type=Boolean(optional=True),
            	doc=" -V --binomial-obs-priors-off Disable incorporation of prior expectations about observations. Uses read placement probability, strand balance probability, and read position (5'-3') probability.",
            ),
            ToolInput(
                tag="noABPriorsFlag",
            	prefix="-a",
                input_type=Boolean(optional=True),
            	doc=" -a --allele-balance-priors-off Disable use of aggregate probability of observation balance between alleles as a component of the priors.",
            ),
            ToolInput(
                tag="obsBiasFile",
            	prefix="--observation-bias",
                input_type=TextFile(optional=True),
            	doc=" --observation-bias FILE Read length-dependent allele observation biases from FILE. The format is [length] [alignment efficiency relative to reference] where the efficiency is 1 if there is no relative observation bias.",
            ),
            ToolInput(
                tag="baseQualCap",
            	prefix="--base-quality-cap",
                input_type=Int(optional=True),
            	doc=" --base-quality-cap Q Limit estimated observation quality by capping base quality at Q.",
            ),
            ToolInput(
                tag="probContamin",
            	prefix="--prob-contamination",
                input_type=Float(),
                default=0.000000001,
            	doc=" --prob-contamination F An estimate of contamination to use for all samples. default: 10e-9",
            ),
            ToolInput(
                tag="legGLScalc",
            	prefix="--legacy-gls",
                input_type=Boolean(optional=True),
            	doc=" --legacy-gls Use legacy (polybayes equivalent) genotype likelihood calculations",
            ),
            ToolInput(
                tag="contaminEst",
            	prefix="--contamination-estimates",
                input_type=TextFile(optional=True),
            	doc=" --contamination-estimates FILE A file containing per-sample estimates of contamination, such as those generated by VerifyBamID. The format should be: sample p(read=R|genotype=AR) p(read=A|genotype=AA) Sample '*' can be used to set default contamination estimates.",
            ),
            ToolInput(
                tag="repoprtMaxGLFlag",
            	prefix="--report-genotype-likelihood-max",
                input_type=Boolean(optional=True),
            	doc=" --report-genotype-likelihood-max Report genotypes using the maximum-likelihood estimate provided from genotype likelihoods.",
            ),
            ToolInput(
                tag="genotypingMaxIter",
            	prefix="-B",
                input_type=Int(),
                default=1000,
            	doc=" -B --genotyping-max-iterations N Iterate no more than N times during genotyping step. default: 1000.",
            ),
            ToolInput(
                tag="genotypingMaxBDepth",
            	prefix="--genotyping-max-banddepth",
                input_type=Int(),
                default=6,
            	doc=" --genotyping-max-banddepth N Integrate no deeper than the Nth best genotype by likelihood when genotyping. default: 6.",
            ),
            ToolInput(
                tag="postIntegrationLim",
            	prefix="-W",
                input_type=String(),
                default="1,3",
            	doc=" -W --posterior-integration-limits N,M Integrate all genotype combinations in our posterior space which include no more than N samples with their Mth best data likelihood. default: 1,3.",
            ),
            ToolInput(
                tag="excludeUnObsGT",
            	prefix="-N",
                input_type=Boolean(optional=True),
            	doc=" -N --exclude-unobserved-genotypes Skip sample genotypings for which the sample has no supporting reads.",
            ),
            ToolInput(
                tag="gtVarThres",
            	prefix="-S",
                input_type=Int(optional=True),
            	doc=" -S --genotype-variant-threshold N Limit posterior integration to samples where the second-best genotype likelihood is no more than log(N) from the highest genotype likelihood for the sample. default: ~unbounded",
            ),
            ToolInput(
                tag="useMQFlag",
            	prefix="-j",
                input_type=Boolean(optional=True),
            	doc=" -j --use-mapping-quality Use mapping quality of alleles when calculating data likelihoods.",
            ),
            ToolInput(
                tag="harmIndelQualFlag",
            	prefix="-H",
                input_type=Boolean(optional=True),
            	doc=" -H --harmonic-indel-quality Use a weighted sum of base qualities around an indel, scaled by the distance from the indel. By default use a minimum BQ in flanking sequence.",
            ),
            ToolInput(
                tag="readDepFact",
            	prefix="-D",
                input_type=Float(),
                default=0.9,
            	doc=" -D --read-dependence-factor N Incorporate non-independence of reads by scaling successive observations by this factor during data likelihood calculations. default: 0.9",
            ),
            ToolInput(
                tag="gtQuals",
            	prefix="-=",
                input_type=Boolean(optional=True),
            	doc=" -= --genotype-qualities Calculate the marginal probability of genotypes and report as GQ in each sample field in the VCF output.",
            ),
        ]

        def outputs(self):
            return [
                ToolOutput(
                    "out",
                    Vcf,
                    glob=InputSelector("outputFilename"),
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
                creator="Sebastian Hollizeck",
                maintainer="Sebastian Hollizeck",
                maintainerEmail="sebastian.hollizeck@petermac.org",
                dateCreated=date(2019, 10, 08),
                dateUpdated=date(2019, 10, 08),
                institution=None,
                doi=None,
                citation="Garrison E, Marth G. Haplotype-based variant detection from short-read sequencing. arXiv preprint arXiv:1207.3907 [q-bio.GN] 2012",
                keywords=["freebayes", "bayesian"],
                documentationUrl="https://github.com/ekg/freebayes",
                documentation="usage: freebayes [OPTION] ... [BAM FILE] ...\nBayesian haplotype-based polymorphism discovery.\nVersion:1.2.0\n",
            )
