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


class GatkCollectWgsMetricsWithNonZeroCoverageBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectWgsMetricsWithNonZeroCoverage"

    def friendly_name(self) -> str:
        return "GATK4: CollectWgsMetricsWithNonZeroCoverage"

    def tool(self) -> str:
        return "Gatk4CollectWgsMetricsWithNonZeroCoverage"

    def inputs(self):
        return [
            ToolInput(
                tag="chart_output",
                input_type=File(optional=True),
                prefix="--CHART_OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CHART) A file (with .pdf extension) to write the chart to. Required."
                ),
            ),
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
                doc=InputDocumentation(doc="(-O) Output metrics file. Required."),
            ),
            ToolInput(
                tag="reference_sequence",
                input_type=File(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-R) Reference sequence file. Required."),
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
                tag="compression_level",
                input_type=Int(optional=True),
                prefix="--COMPRESSION_LEVEL",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Compression level for all compressed files created (e.g. BAM and VCF). Default value: 2."
                ),
            ),
            ToolInput(
                tag="count_unpaired",
                input_type=Boolean(optional=True),
                prefix="--COUNT_UNPAIRED",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true, count unpaired reads, and paired reads with one end unmapped Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="coverage_cap",
                input_type=Int(optional=True),
                prefix="--COVERAGE_CAP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CAP) Treat positions with coverage exceeding this value as if they had coverage at this value (but calculate the difference for PCT_EXC_CAPPED).  Default value: 250. "
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
                tag="include_bq_histogram",
                input_type=String(optional=True),
                prefix="--INCLUDE_BQ_HISTOGRAM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="intervals",
                input_type=File(optional=True),
                prefix="--INTERVALS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="An interval list file that contains the positions to restrict the assessment. Please note that all bases of reads that overlap these intervals will be considered, even if some of those bases extend beyond the boundaries of the interval. The ideal use case for this argument is to use it to restrict the calculation to a subset of (whole) contigs.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="locus_accumulation_cap",
                input_type=Int(optional=True),
                prefix="--LOCUS_ACCUMULATION_CAP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" At positions with coverage exceeding this value, completely ignore reads that accumulate beyond this value (so that they will not be considered for PCT_EXC_CAPPED).  Used to keep memory consumption in check, but could create bias if set too low  Default value: 100000. "
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
                tag="minimum_base_quality",
                input_type=Int(optional=True),
                prefix="--MINIMUM_BASE_QUALITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-Q)  Minimum base quality for a base to contribute coverage. N bases will be treated as having a base quality of negative infinity and will therefore be excluded from coverage regardless of the value of this parameter.  Default value: 20. "
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
                tag="quiet",
                input_type=Boolean(optional=True),
                prefix="--QUIET",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to suppress job-summary info on System.err. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="read_length",
                input_type=Int(optional=True),
                prefix="--READ_LENGTH",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Average read length in the file. Default is 150. Default value: 150."
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
                tag="stop_after",
                input_type=Boolean(optional=True),
                prefix="--STOP_AFTER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="For debugging purposes, stop after processing this many genomic bases. Default value: -1."
                ),
            ),
            ToolInput(
                tag="theoretical_sensitivity_output",
                input_type=File(optional=True),
                prefix="--THEORETICAL_SENSITIVITY_OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Output for Theoretical Sensitivity metrics.  Default value: null. "
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
                tag="use_fast_algorithm",
                input_type=Boolean(optional=True),
                prefix="--USE_FAST_ALGORITHM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true, fast algorithm is used. Default value: false. Possible values: {true, false}"
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:11:19.112569"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:11:19.112570"),
            documentation="b'\n**EXPERIMENTAL FEATURE - USE AT YOUR OWN RISK**\nUSAGE: CollectWgsMetricsWithNonZeroCoverage [arguments]\nCollect metrics about coverage and performance of whole genome sequencing (WGS) experiments.  This tool collects metrics\nabout the percentages of reads that pass base- and mapping- quality filters as well as coverage (read-depth) levels.\nBoth minimum base- and mapping-quality values as well as the maximum read depths (coverage cap) are user defined.  This\nextends CollectWgsMetrics by including metrics related only to siteswith non-zero (>0) coverage.<p>Note: Metrics labeled\nas percentages are actually expressed as fractions!</p><h4>Usage Example:</h4><pre>java -jar picard.jar\nCollectWgsMetricsWithNonZeroCoverage \\<br />       I=input.bam \\<br />       O=collect_wgs_metrics.txt \\<br />      \nCHART=collect_wgs_metrics.pdf  \\<br />       R=reference_sequence.fasta </pre>Please see the <a\nhref='https://broadinstitute.github.io/picard/picard-metric-definitions.html#CollectWgsMetricsWithNonZeroCoverage.WgsMetricsWithNonZeroCoverage'>WgsMetricsWithNonZeroCoverage</a>\ndocumentation for detailed explanations of the output metrics.<hr />\nVersion:4.1.3.0\n",
        )
