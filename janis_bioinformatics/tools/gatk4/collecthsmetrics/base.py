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


class GatkCollectHsMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectHsMetrics"

    def friendly_name(self) -> str:
        return "GATK4: CollectHsMetrics"

    def tool(self) -> str:
        return "Gatk4CollectHsMetrics"

    def inputs(self):
        return [
            ToolInput(
                tag="bait_intervals",
                input_type=File(optional=True),
                prefix="--BAIT_INTERVALS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-BI) An interval list file that contains the locations of the baits used. This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) An aligned SAM or BAM file. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output file to write the metrics to. Required."
                ),
            ),
            ToolInput(
                tag="target_intervals",
                input_type=File(optional=True),
                prefix="--TARGET_INTERVALS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-TI) An interval list file that contains the locations of the targets. This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="allele_fraction",
                input_type=Double(optional=True),
                prefix="--ALLELE_FRACTION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Allele fraction for which to calculate theoretical sensitivity. This argument may be specified 0 or more times. Default value: [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5]. "
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
                tag="bait_set_name",
                input_type=String(optional=True),
                prefix="--BAIT_SET_NAME",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-N) Bait set name. If not provided it is inferred from the filename of the bait intervals. Default value: null. "
                ),
            ),
            ToolInput(
                tag="clip_overlapping_reads",
                input_type=Boolean(optional=True),
                prefix="--CLIP_OVERLAPPING_READS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" True if we are to clip overlapping reads, false otherwise.  Default value: true. Possible values: {true, false} "
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
                tag="coverage_cap",
                input_type=Boolean(optional=True),
                prefix="--COVERAGE_CAP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-covMax)  200.  Default value: 200. "),
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
                tag="include_indels",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_INDELS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true count inserted bases as on target and deleted bases as covered by a read. Default value: false. Possible values: {true, false} "
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
                tag="metric_accumulation_level",
                input_type=Boolean(optional=True),
                prefix="--METRIC_ACCUMULATION_LEVEL",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-LEVEL)  The level(s) at which to accumulate metrics.  This argument may be specified 0 or more times. Default value: [ALL_READS]. Possible values: {ALL_READS, SAMPLE, LIBRARY, READ_GROUP} "
                ),
            ),
            ToolInput(
                tag="minimum_base_quality",
                input_type=Int(optional=True),
                prefix="--MINIMUM_BASE_QUALITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-Q)  Minimum base quality for a base to contribute coverage.  Default value: 20. "
                ),
            ),
            ToolInput(
                tag="minimum_mapping_quality",
                input_type=Int(optional=True),
                prefix="--MINIMUM_MAPPING_QUALITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MQ)  Minimum mapping quality for a read to contribute coverage.  Default value: 20. "
                ),
            ),
            ToolInput(
                tag="near_distance",
                input_type=Int(optional=True),
                prefix="--NEAR_DISTANCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The maximum distance between a read and the nearest probe/bait/amplicon for the read to be considered 'near probe' and included in percent selected.  Default value: 250. "
                ),
            ),
            ToolInput(
                tag="per_base_coverage",
                input_type=File(optional=True),
                prefix="--PER_BASE_COVERAGE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="An optional file to output per base coverage information to. The per-base file contains one line per target base and can grow very large. It is not recommended for use with large target sets.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="per_target_coverage",
                input_type=File(optional=True),
                prefix="--PER_TARGET_COVERAGE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="An optional file to output per target coverage information to. Default value: null."
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
                tag="reference_sequence",
                input_type=File(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R) Reference sequence file. Default value: null."
                ),
            ),
            ToolInput(
                tag="sample_size",
                input_type=Int(optional=True),
                prefix="--SAMPLE_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Sample Size used for Theoretical Het Sensitivity sampling. Default is 10000. Default value: 10000. "
                ),
            ),
            ToolInput(
                tag="theoretical_sensitivity_output",
                input_type=File(optional=True),
                prefix="--THEORETICAL_SENSITIVITY_OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Output for Theoretical Sensitivity metrics where the allele fractions are provided by the ALLELE_FRACTION argument.  Default value: null. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:09:30.826855"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:09:30.826856"),
            documentation="b'USAGE: CollectHsMetrics [arguments]\nCollects hybrid-selection (HS) metrics for a SAM or BAM file.  <p>This tool takes a SAM/BAM file input and collects\nmetrics that are specific for sequence datasets generated through hybrid-selection. Hybrid-selection (HS) is the most\ncommonly used technique to capture exon-specific sequences for targeted sequencing experiments such as exome sequencing;\nfor more information, please see the corresponding <a\nhref='http://www.broadinstitute.org/gatk/guide/article?id=6331'>GATK Dictionary entry</a>. </p> <p>This tool requires an\naligned SAM or BAM file as well as bait and target interval files in Picard interval_list format. You should use the\nbait and interval files that correspond to the capture kit that was used to generate the capture libraries for\nsequencing, which can generally be obtained from the kit manufacturer. If the baits and target intervals are provided in\nBED format, you can convert them to the Picard interval_list format using Picard's <a\nhref='http://broadinstitute.github.io/picard/command-line-overview.html#BedToIntervalList'>BedToInterval</a> tool.\n</p><p>If a reference sequence is provided, this program will calculate both AT_DROPOUT and GC_DROPOUT metrics. Dropout\nmetrics are an attempt to measure the reduced representation of reads, in regions that deviate from 50% G/C content.\nThis reduction in the number of aligned reads is due to the increased numbers of errors associated with sequencing\nregions with excessive or deficient numbers of G/C bases, ultimately leading to poor mapping efficiencies and\nlowcoverage in the affected regions. </p><p>If you are interested in getting G/C content and mean sequence depth\ninformation for every target interval, use the PER_TARGET_COVERAGE option. </p><p>Note: Metrics labeled as percentages\nare actually expressed as fractions!</p>  <h4>Usage Example:</h4><pre>java -jar picard.jar CollectHsMetrics \\<br />     \nI=input_reads.bam \\<br />      O=output_hs_metrics.txt \\<br />      R=reference.fasta \\<br />     \nBAIT_INTERVALS=bait.interval_list \\<br />      TARGET_INTERVALS=target.interval_list</pre> <p>Please see <a\nhref='http://broadinstitute.github.io/picard/picard-metric-definitions.html#HsMetrics'>CollectHsMetrics</a> for detailed\ndescriptions of the output metrics produced by this tool.</p><hr />\nVersion:4.1.3.0\n",
        )
