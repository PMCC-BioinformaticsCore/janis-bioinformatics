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


class GatkVariantEvalBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "VariantEval"

    def friendly_name(self) -> str:
        return "GATK4: VariantEval"

    def tool(self) -> str:
        return "Gatk4VariantEval"

    def inputs(self):
        return [
            ToolInput(
                tag="eval",
                input_type=Boolean(optional=True),
                prefix="--eval",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-eval) Input evaluation file(s) This argument must be specified at least once. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) File to which variants should be written Required."
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
                tag="ancestralAlignments",
                input_type=File(optional=True),
                prefix="--ancestral-alignments",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-aa)  Fasta file with ancestral alleles  Default value: null. "
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
                tag="comp",
                input_type=Boolean(optional=True),
                prefix="--comp",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-comp) Input comparison file(s) This argument may be specified 0 or more times. Default value: null. "
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
                tag="dbsnp",
                input_type=Boolean(optional=True),
                prefix="--dbsnp",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-D) dbSNP file Default value: null."),
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
                tag="disableSequenceDictionaryValidation",
                input_type=Boolean(optional=True),
                prefix="--disable-sequence-dictionary-validation",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-disable-sequence-dictionary-validation)  If specified, do not check the sequence dictionaries from our inputs for compatibility. Use at your own risk!  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="doNotUseAllStandardModules",
                input_type=Boolean(optional=True),
                prefix="--do-not-use-all-standard-modules",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-no-ev)  Do not use the standard modules by default (instead, only those that are specified with the -EV option)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="doNotUseAllStandardStratifications",
                input_type=Boolean(optional=True),
                prefix="--do-not-use-all-standard-stratifications",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-no-st)  Do not use the standard stratification modules by default (instead, only those that are specified with the -S option)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="evalModule",
                input_type=String(optional=True),
                prefix="--eval-module",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-EV) One or more specific eval modules to apply to the eval track(s) (in addition to the standard modules, unless -noEV is specified)  This argument may be specified 0 or more times. Default value: null. "
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
                tag="goldStandard",
                input_type=Boolean(optional=True),
                prefix="--gold-standard",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-gold)  Evaluations that count calls at sites of true variation (e.g., indel calls) will use this argument as their gold standard for comparison  Default value: null. "
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
                tag="keepAc0",
                input_type=Boolean(optional=True),
                prefix="--keep-ac0",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-keep-ac0) If provided, modules that track polymorphic sites will not require that a site have AC > 0 when the input eval has genotypes  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="knownCnvs",
                input_type=Boolean(optional=True),
                prefix="--known-cnvs",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-known-cnvs)  File containing tribble-readable features describing a known list of copy number variants  Default value: null. "
                ),
            ),
            ToolInput(
                tag="known_names",
                input_type=String(optional=True),
                prefix="--KNOWN_NAMES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-known-name)  Name of feature bindings containing variant sites that should be treated as known when splitting eval features into known and novel subsets  This argument may be specified 0 or more times. Default value: null. "
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
                tag="list",
                input_type=Boolean(optional=True),
                prefix="--list",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ls) List the available eval modules and exit Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="mendelianViolationQualThreshold",
                input_type=Double(optional=True),
                prefix="--mendelian-violation-qual-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-mvq)  Minimum genotype QUAL score for each trio member required to accept a site as a violation. Default is 50.  Default value: 50.0. "
                ),
            ),
            ToolInput(
                tag="mergeEvals",
                input_type=Boolean(optional=True),
                prefix="--merge-evals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-merge-evals)  If provided, all -eval tracks will be merged into a single eval track  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="minPhaseQuality",
                input_type=Double(optional=True),
                prefix="--min-phase-quality",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-mpq)  Minimum phasing quality  Default value: 10.0. "
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
                tag="quiet",
                input_type=Boolean(optional=True),
                prefix="--QUIET",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to suppress job-summary info on System.err. Default value: false. Possible values: {true, false} "
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
                tag="requireStrictAlleleMatch",
                input_type=Boolean(optional=True),
                prefix="--require-strict-allele-match",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-strict)  If provided only comp and eval tracks with exactly matching reference and alternate alleles will be counted as overlapping  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="sample",
                input_type=String(optional=True),
                prefix="--sample",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-sn) Derive eval and comp contexts using only these sample genotypes, when genotypes are available in the original context  This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="samplePloidy",
                input_type=Int(optional=True),
                prefix="--sample-ploidy",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ploidy)  Per-sample ploidy (number of chromosomes per sample)  Default value: 2. "
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
                tag="select_exps",
                input_type=String(optional=True),
                prefix="--SELECT_EXPS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-select) One or more stratifications to use when evaluating the data This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="select_names",
                input_type=String(optional=True),
                prefix="--SELECT_NAMES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-select-name)  Names to use for the list of stratifications (must be a 1-to-1 mapping)  This argument may be specified 0 or more times. Default value: null. "
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
                tag="stratIntervals",
                input_type=Boolean(optional=True),
                prefix="--strat-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-strat-intervals)  File containing tribble-readable features for the IntervalStratificiation  Default value: null. "
                ),
            ),
            ToolInput(
                tag="stratificationModule",
                input_type=String(optional=True),
                prefix="--stratification-module",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ST)  One or more specific stratification modules to apply to the eval track(s) (in addition to the standard stratifications, unless -noS is specified)  This argument may be specified 0 or more times. Default value: null. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:05:24.736910"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:05:24.736911"),
            documentation="log4j:WARN No appenders could be found for logger (org.reflections.Reflections).\nlog4j:WARN Please initialize the log4j system properly.\nlog4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.\n**BETA FEATURE - WORK IN PROGRESS**\nUSAGE: VariantEval [arguments]\nGiven a variant callset, it is common to calculate various quality control metrics. These metrics include the number of\nraw or filtered SNP counts; ratio of transition mutations to transversions; concordance of a particular sample's calls\nto a genotyping chip; number of singletons per sample; etc. Furthermore, it is often useful to stratify these metrics by\nvarious criteria like functional class (missense, nonsense, silent), whether the site is CpG site, the amino acid\ndegeneracy of the site, etc. VariantEval facilitates these calculations in two ways: by providing several built-in\nevaluation and stratification modules, and by providing a framework that permits the easy development of new evaluation\nand stratification modules.\nVersion:4.1.3.0\n",
        )
