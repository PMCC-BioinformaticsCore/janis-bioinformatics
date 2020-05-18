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


class GatkCollectHiSeqXPfFailMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectHiSeqXPfFailMetrics"

    def friendly_name(self) -> str:
        return "GATK4: CollectHiSeqXPfFailMetrics"

    def tool(self) -> str:
        return "Gatk4CollectHiSeqXPfFailMetrics"

    def inputs(self):
        return [
            ToolInput(
                tag="basecalls_dir",
                input_type=File(optional=True),
                prefix="--BASECALLS_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-B) The Illumina basecalls directory. Required."
                ),
            ),
            ToolInput(
                tag="lane",
                input_type=Int(optional=True),
                prefix="--LANE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-L) Lane number. Required."),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Basename for metrics file. Resulting file will be <OUTPUT>.pffail_summary_metrics Required. "
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
                tag="max_records_in_ram",
                input_type=Int(optional=True),
                prefix="--MAX_RECORDS_IN_RAM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When writing files that need to be sorted, this will specify the number of records stored in RAM before spilling to disk. Increasing this number reduces the number of file handles needed to sort the file, and increases the amount of RAM needed.  Default value: 500000. "
                ),
            ),
            ToolInput(
                tag="n_cycles",
                input_type=Int(optional=True),
                prefix="--N_CYCLES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Number of cycles to look at. At time of writing PF status gets determined at cycle 24 so numbers greater than this will yield strange results. In addition, PF status is currently determined at cycle 24, so running this with any other value is neither tested nor recommended.  Default value: 24. "
                ),
            ),
            ToolInput(
                tag="num_processors",
                input_type=Int(optional=True),
                prefix="--NUM_PROCESSORS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-NP) Run this many PerTileBarcodeExtractors in parallel. If NUM_PROCESSORS = 0, number of cores is automatically set to the number of cores available on the machine. If NUM_PROCESSORS < 0 then the number of cores used will be the number available on the machine less NUM_PROCESSORS.  Default value: 1. "
                ),
            ),
            ToolInput(
                tag="prob_explicit_reads",
                input_type=Double(optional=True),
                prefix="--PROB_EXPLICIT_READS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-P)  The fraction of (non-PF) reads for which to output explicit classification. Output file will be <OUTPUT>.pffail_detailed_metrics (if PROB_EXPLICIT_READS != 0)  Default value: 0.0. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:09:24.415756"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:09:24.415757"),
            documentation="b'USAGE: CollectHiSeqXPfFailMetrics [arguments]\nClassify PF-Failing reads in a HiSeqX Illumina Basecalling directory into various categories.<p>This tool categorizes\nthe reads that did not pass filter (PF-Failing) into four groups.  These groups are based on a heuristic that was\nderived by looking at a few titration experiments. </p><p>After examining the called bases from the first 24 cycles of\neach read, the PF-Failed reads are grouped into the following four categories: <ul><li>MISALIGNED - The first 24\nbasecalls of a read are uncalled (numNs~24).   These types of reads appear to be flow cell artifacts because reads were\nonly found near tile boundaries and were concentration (library) independent</li> <li>EMPTY - All 24 bases are called\n(numNs~0) but the number of bases with quality scores greater than two is less than or equal to eight (numQGtTwo<=8). \nThese reads were location independent within the tiles and were inversely proportional to the library\nconcentration</li><li>POLYCLONAL - All 24 bases were called and numQGtTwo>=12, were independent of their location with\nthe tiles, and were directly proportional to the library concentration.  These reads are likely the result of PCR\nartifacts </li><li>UNKNOWN - The remaining reads that are PF-Failing but did not fit into any of the groups listed\nabove</li></ul></p>  <p>The tool defaults to the SUMMARY output which indicates the number of PF-Failed reads per tile\nand groups them into the categories described above accordingly.</p> <p>A DETAILED metrics option is also available that\nsubdivides the SUMMARY outputs by the x- y- position of these reads within each tile.  To obtain the DETAILED metric\ntable, you must add the PROB_EXPLICIT_READS option to your command line and set the value between 0 and 1.  This value\nrepresents the fractional probability of PF-Failed reads to send to output.  For example, if PROB_EXPLICIT_READS=0, then\nno metrics will be output.  If PROB_EXPLICIT_READS=1, then it will provide detailed metrics for all (100%) of the reads.\nIt follows that setting the PROB_EXPLICIT_READS=0.5, will provide detailed metrics for half of the PF-Failed reads.</p>\n<p>Note: Metrics labeled as percentages are actually expressed as fractions!</p><h4>Usage example: (SUMMARY\nMetrics)</h4> <pre>java -jar picard.jar CollectHiSeqXPfFailMetrics \\<br />      BASECALLS_DIR=/BaseCalls/ \\<br />     \nOUTPUT=/metrics/ \\<br />      LANE=001</pre><h4>Usage example: (DETAILED Metrics)</h4><pre>java -jar picard.jar\nCollectHiSeqXPfFailMetrics \\<br />      BASECALLS_DIR=/BaseCalls/ \\<br />      OUTPUT=/Detail_metrics/ \\<br />     \nLANE=001 \\<br />      PROB_EXPLICIT_READS=1</pre>Please see our documentation on the <a\nhref='https://broadinstitute.github.io/picard/picard-metric-definitions.html#CollectHiSeqXPfFailMetrics.PFFailSummaryMetric'>SUMMARY</a>\nand <a\nhref='https://broadinstitute.github.io/picard/picard-metric-definitions.html#CollectHiSeqXPfFailMetrics.PFFailDetailedMetric'>DETAILED</a>\nmetrics for comprehensive explanations of the outputs produced by this tool.<hr />\nVersion:4.1.3.0\n",
        )
