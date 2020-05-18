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


class GatkCollectGcBiasMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectGcBiasMetrics"

    def friendly_name(self) -> str:
        return "GATK4: CollectGcBiasMetrics"

    def tool(self) -> str:
        return "Gatk4CollectGcBiasMetrics"

    def inputs(self):
        return [
            ToolInput(
                tag="chart_output",
                input_type=File(optional=True),
                prefix="--CHART_OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CHART) The PDF file to render the chart to. Required."
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
                doc=InputDocumentation(
                    doc="(-O) File to write the output to. Required."
                ),
            ),
            ToolInput(
                tag="summary_output",
                input_type=File(optional=True),
                prefix="--SUMMARY_OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-S) The text file to write summary metrics to. Required."
                ),
            ),
            ToolInput(
                tag="also_ignore_duplicates",
                input_type=Boolean(optional=True),
                prefix="--ALSO_IGNORE_DUPLICATES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ALSO_IGNORE_DUPLICATES)  Use to get additional results without duplicates. This option allows to gain two plots per level at the same time: one is the usual one and the other excludes duplicates.  Default value: false. Possible values: {true, false} "
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
                tag="is_bisulfite_sequenced",
                input_type=Boolean(optional=True),
                prefix="--IS_BISULFITE_SEQUENCED",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-BS)  Whether the SAM or BAM file consists of bisulfite sequenced reads.  Default value: false. Possible values: {true, false} "
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
                tag="minimum_genome_fraction",
                input_type=Double(optional=True),
                prefix="--MINIMUM_GENOME_FRACTION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MGF)  For summary metrics, exclude GC windows that include less than this fraction of the genome.  Default value: 1.0E-5. "
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
                tag="scan_window_size",
                input_type=Int(optional=True),
                prefix="--SCAN_WINDOW_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-WINDOW_SIZE)  The size of the scanning windows on the reference genome that are used to bin reads.  Default value: 100. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:09:17.681327"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:09:17.681328"),
            documentation="b'USAGE: CollectGcBiasMetrics [arguments]\nCollect metrics regarding GC bias. This tool collects information about the relative proportions of guanine (G) and\ncytosine (C) nucleotides in a sample.  Regions of high and low G + C content have been shown to interfere with\nmapping/aligning, ultimately leading to fragmented genome assemblies and poor coverage in a phenomenon known as 'GC\nbias'.  Detailed information on the effects of GC bias on the collection and analysis of sequencing data can be found at\nDOI: 10.1371/journal.pone.0062856/.<br /><br /><p>The GC bias statistics are always output in a detailed long-form\nversion, but a summary can also be produced. Both the detailed metrics and the summary metrics are output as tables\n'.txt' files) and an accompanying chart that plots the data ('.pdf' file). </p> <h4>Detailed metrics</h4>The table of\ndetailed metrics includes GC percentages for each bin (GC), the percentage of WINDOWS corresponding to each GC bin of\nthe reference sequence, the numbers of reads that start within a particular %GC content bin (READ_STARTS), and the mean\nbase quality of the reads that correspond to a specific GC content distribution window (MEAN_BASE_QUALITY). \nNORMALIZED_COVERAGE is a relative measure of sequence coverage by the reads at a particular GC content.For each run, the\ncorresponding reference sequence is divided into bins or windows based on the percentage of G + C content ranging from 0\n- 100%.  The percentages of G + C are determined from a defined length of sequence; the default value is set at 100\nbases. The mean of the distribution will vary among organisms; human DNA has a mean GC content of 40%, suggesting a\nslight preponderance of AT-rich regions.  <br /><br /><h4>Summary metrics</h4>The table of summary metrics captures\nrun-specific bias information including WINDOW_SIZE, ALIGNED_READS, TOTAL_CLUSTERS, AT_DROPOUT, and GC_DROPOUT.  While\nWINDOW_SIZE refers to the numbers of bases used for the distribution (see above), the ALIGNED_READS and TOTAL_CLUSTERS\nare the total number of aligned reads and the total number of reads (after filtering) produced in a run. In addition,\nthe tool produces both AT_DROPOUT and GC_DROPOUT metrics, which indicate the percentage of misaligned reads that\ncorrelate with low (%-GC is &lt; 50%) or high (%-GC is &gt; 50%) GC content respectively.  <br /><br />The percentage of\n'coverage' or depth in a GC bin is calculated by dividing the number of reads of a particular GC content by the mean\nnumber of reads of all GC bins.  A number of 1 represents mean coverage, a number less than 1 represents lower than mean\ncoverage (e.g. 0.5 means half as much coverage as average) while a number greater than 1 represents higher than mean\ncoverage (e.g. 3.1 means this GC bin has 3.1 times more reads per window than average).  This tool also tracks mean\nbase-quality scores of the reads within each GC content bin, enabling the user to determine how base quality scores vary\nwith GC content.  <br /> <br />The chart output associated with this data table plots the NORMALIZED_COVERAGE, the\ndistribution of WINDOWs corresponding to GC percentages, and base qualities corresponding to each %GC bin.<p>Note:\nMetrics labeled as percentages are actually expressed as fractions!</p><h4>Usage Example:</h4><pre>java -jar picard.jar\nCollectGcBiasMetrics \\<br />      I=input.bam \\<br />      O=gc_bias_metrics.txt \\<br />      CHART=gc_bias_metrics.pdf\n\\<br />      S=summary_metrics.txt \\<br />      R=reference_sequence.fasta</pre>Please see <a\nhref='https://broadinstitute.github.io/picard/picard-metric-definitions.html#GcBiasMetrics'>the GcBiasMetrics\ndocumentation</a> for further explanations of each metric.<hr />\nVersion:4.1.3.0\n",
        )
