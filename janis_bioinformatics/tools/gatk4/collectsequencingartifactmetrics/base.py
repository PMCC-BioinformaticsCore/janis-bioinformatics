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


class GatkCollectSequencingArtifactMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectSequencingArtifactMetrics"

    def friendly_name(self) -> str:
        return "GATK4: CollectSequencingArtifactMetrics"

    def tool(self) -> str:
        return "Gatk4CollectSequencingArtifactMetrics"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-I) Input SAM or BAM file. Required."),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) File to write the output to. Required."
                ),
            ),
            ToolInput(
                tag="reference_sequence",
                input_type=File(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-R) Reference sequence file. Required."),
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
                tag="assume_sorted",
                input_type=Boolean(optional=True),
                prefix="--ASSUME_SORTED",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-AS) If true (default), then the sort order in the header file will be ignored. Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="compression_level",
                input_type=Int(optional=True),
                prefix="--COMPRESSION_LEVEL",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Compression level for all compressed files created (e.g. BAM and VCF). Default value: 2."
                ),
            ),
            ToolInput(
                tag="context_size",
                input_type=Int(optional=True),
                prefix="--CONTEXT_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The number of context bases to include on each side of the assayed base. Default value: 1. "
                ),
            ),
            ToolInput(
                tag="contexts_to_print",
                input_type=String(optional=True),
                prefix="--CONTEXTS_TO_PRINT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If specified, only print results for these contexts in the detail metrics output. However, the summary metrics output will still take all contexts into consideration.  This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="create_index",
                input_type=Boolean(optional=True),
                prefix="--CREATE_INDEX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to create a BAM index when writing a coordinate-sorted BAM file. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="create_md5_file",
                input_type=Boolean(optional=True),
                prefix="--CREATE_MD5_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to create an MD5 digest for any BAM or FASTQ files created. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="db_snp",
                input_type=File(optional=True),
                prefix="--DB_SNP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="VCF format dbSNP file, used to exclude regions around known polymorphisms from analysis. Default value: null. "
                ),
            ),
            ToolInput(
                tag="file_extension",
                input_type=String(optional=True),
                prefix="--FILE_EXTENSION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-EXT) Append the given file extension to all metric file names (ex. OUTPUT.pre_adapter_summary_metrics.EXT). None if null  Default value: null. "
                ),
            ),
            ToolInput(
                tag="ga4gh_client_secrets",
                input_type=Boolean(optional=True),
                prefix="--GA4GH_CLIENT_SECRETS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: client_secrets.json."),
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
                tag="include_duplicates",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_DUPLICATES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DUPES)  Include duplicate reads. If set to true then all reads flagged as duplicates will be included as well.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="include_non_pf_reads",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_NON_PF_READS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-NON_PF)  Whether or not to include non-PF reads.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="include_unpaired",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_UNPAIRED",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-UNPAIRED)  Include unpaired reads. If set to true then all paired reads will be included as well - MINIMUM_INSERT_SIZE and MAXIMUM_INSERT_SIZE will be ignored.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="intervals",
                input_type=File(optional=True),
                prefix="--INTERVALS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="An optional list of intervals to restrict analysis to. Default value: null."
                ),
            ),
            ToolInput(
                tag="max_records_in_ram",
                input_type=Int(optional=True),
                prefix="--MAX_RECORDS_IN_RAM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When writing files that need to be sorted, this will specify the number of records stored in RAM before spilling to disk. Increasing this number reduces the number of file handles needed to sort the file, and increases the amount of RAM needed.  Default value: 500000. "
                ),
            ),
            ToolInput(
                tag="maximum_insert_size",
                input_type=Int(optional=True),
                prefix="--MAXIMUM_INSERT_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MAX_INS)  The maximum insert size for a read to be included in analysis. Set to 0 to have no maximum.  Default value: 600. "
                ),
            ),
            ToolInput(
                tag="minimum_insert_size",
                input_type=Int(optional=True),
                prefix="--MINIMUM_INSERT_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MIN_INS)  The minimum insert size for a read to be included in analysis.  Default value: 60. "
                ),
            ),
            ToolInput(
                tag="minimum_mapping_quality",
                input_type=Int(optional=True),
                prefix="--MINIMUM_MAPPING_QUALITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MQ)  The minimum mapping quality score for a base to be included in analysis.  Default value: 30. "
                ),
            ),
            ToolInput(
                tag="minimum_quality_score",
                input_type=Int(optional=True),
                prefix="--MINIMUM_QUALITY_SCORE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-Q)  The minimum base quality score for a base to be included in analysis.  Default value: 20. "
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
                tag="stop_after",
                input_type=Boolean(optional=True),
                prefix="--STOP_AFTER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Stop after processing N reads, mainly for debugging. Default value: 0."
                ),
            ),
            ToolInput(
                tag="tandem_reads",
                input_type=String(optional=True),
                prefix="--TANDEM_READS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-TANDEM, i.e.)  to face the same direction.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="tmp_dir",
                input_type=File(optional=True),
                prefix="--TMP_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="One or more directories with space available to be used by this program for temporary storage of working files  This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="use_jdk_deflater",
                input_type=Boolean(optional=True),
                prefix="--USE_JDK_DEFLATER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-use_jdk_deflater)  Use the JDK Deflater instead of the Intel Deflater for writing compressed output  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="use_jdk_inflater",
                input_type=Boolean(optional=True),
                prefix="--USE_JDK_INFLATER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-use_jdk_inflater)  Use the JDK Inflater instead of the Intel Inflater for reading compressed input  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="use_oq",
                input_type=Boolean(optional=True),
                prefix="--USE_OQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When available, use original quality scores for filtering. Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="validation_stringency",
                input_type=Boolean(optional=True),
                prefix="--VALIDATION_STRINGENCY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Validation stringency for all SAM files read by this program.  Setting stringency to SILENT can improve performance when processing a BAM file in which variable-length data (read, qualities, tags) do not otherwise need to be decoded.  Default value: STRICT. Possible values: {STRICT, LENIENT, SILENT} "
                ),
            ),
            ToolInput(
                tag="verbosity",
                input_type=Boolean(optional=True),
                prefix="--VERBOSITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Control verbosity of logging. Default value: INFO. Possible values: {ERROR, WARNING, INFO, DEBUG} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:10:54.349778"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:10:54.349780"),
            documentation="b'USAGE: CollectSequencingArtifactMetrics [arguments]\nCollect metrics to quantify single-base sequencing artifacts.  <p>This tool examines two sources of sequencing errors\nassociated with hybrid selection protocols.  These errors are divided into two broad categories, pre-adapter and\nbait-bias.  Pre-adapter errors can arise from laboratory manipulations of a nucleic acid sample e.g. shearing and occur\nprior to the ligation of adapters for PCR amplification (hence the name pre-adapter).  </p><p>Bait-bias artifacts occur\nduring or after the target selection step, and correlate with substitution rates that are 'biased', or higher for sites\nhaving one base on the reference/positive strand relative to sites having the complementary base on that strand.  For\nexample, during the target selection step, a (G>T) artifact might result in a higher substitution rate at sites with a G\non the positive strand (and C on the negative), relative to sites with the flip (C positive)/(G negative).  This is\nknown as the 'G-Ref' artifact. </p><p>For additional information on these types of artifacts, please see the\ncorresponding GATK dictionary entries on <a\nhref='https://www.broadinstitute.org/gatk/guide/article?id=6333'>bait-bias</a> and <a\nhref='https://www.broadinstitute.org/gatk/guide/article?id=6332'>pre-adapter artifacts</a>.</p><p>This tool produces\nfour files; summary and detail metrics files for both pre-adapter and bait-bias artifacts. The detailed metrics show the\nerror rates for each type of base substitution within every possible triplet base configuration.  Error rates associated\nwith these substitutions are Phred-scaled and provided as quality scores, the lower the value, the more likely it is\nthat an alternate base call is due to an artifact. The summary metrics provide likelihood information on the\n'worst-case' errors. </p><h4>Usage example:</h4><pre>java -jar picard.jar CollectSequencingArtifactMetrics \\<br />    \nI=input.bam \\<br />     O=artifact_metrics.txt \\<br />     R=reference_sequence.fasta</pre>Please see the metrics at the\nfollowing links <a\nhref='http://broadinstitute.github.io/picard/picard-metric-definitions.html#SequencingArtifactMetrics.PreAdapterDetailMetrics'>PreAdapterDetailMetrics</a>,\n<a\nhref='http://broadinstitute.github.io/picard/picard-metric-definitions.html#SequencingArtifactMetrics.PreAdapterSummaryMetrics'>PreAdapterSummaryMetrics</a>,\n<a\nhref='http://broadinstitute.github.io/picard/picard-metric-definitions.html#SequencingArtifactMetrics.BaitBiasDetailMetrics'>BaitBiasDetailMetrics</a>,\nand <a\nhref='http://broadinstitute.github.io/picard/picard-metric-definitions.html#SequencingArtifactMetrics.BaitBiasSummaryMetrics'>BaitBiasSummaryMetrics</a>\nfor complete descriptions of the output metrics produced by this tool. <hr />\nVersion:4.1.3.0\n",
        )
