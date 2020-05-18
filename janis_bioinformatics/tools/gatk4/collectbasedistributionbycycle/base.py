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


class GatkCollectBaseDistributionByCycleBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectBaseDistributionByCycle"

    def friendly_name(self) -> str:
        return "GATK4: CollectBaseDistributionByCycle"

    def tool(self) -> str:
        return "Gatk4CollectBaseDistributionByCycle"

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
                doc=InputDocumentation(
                    doc="(-O) File to write the output to. Required."
                ),
            ),
            ToolInput(
                tag="aligned_reads_only",
                input_type=Boolean(optional=True),
                prefix="--ALIGNED_READS_ONLY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If set to true, calculate the base distribution over aligned reads only. Default value: false. Possible values: {true, false} "
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
                tag="max_records_in_ram",
                input_type=Int(optional=True),
                prefix="--MAX_RECORDS_IN_RAM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When writing files that need to be sorted, this will specify the number of records stored in RAM before spilling to disk. Increasing this number reduces the number of file handles needed to sort the file, and increases the amount of RAM needed.  Default value: 500000. "
                ),
            ),
            ToolInput(
                tag="pf_reads_only",
                input_type=Boolean(optional=True),
                prefix="--PF_READS_ONLY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If set to true, calculate the base distribution over PF reads only (Illumina specific). PF reads are reads that passed the internal quality filters applied by Illumina sequencers.  Default value: false. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:09:06.019656"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:09:06.019657"),
            documentation="b'USAGE: CollectBaseDistributionByCycle [arguments]\nChart the nucleotide distribution per cycle in a SAM or BAM fileThis tool produces a chart of the nucleotide\ndistribution per cycle in a SAM or BAM file in order to enable assessment of systematic errors at specific positions in\nthe reads.<br /><br /><h4>Interpretation notes</h4>Increased numbers of miscalled bases will be reflected in base\ndistribution changes and increases in the number of Ns.  In general, we expect that for any given cycle, or position\nwithin reads, the relative proportions of A, T, C and G should reflect the AT:GC content of the organism's genome. \nThus, for all four nucleotides, flattish lines would be expected.  Deviations from this expectation, for example a spike\nof A at a particular cycle (position within reads), would suggest a systematic sequencing error.<h4>Note on quality\ntrimming</h4>In the past, many sequencing data processing workflows included discarding the low-quality tails of reads\nby applying hard-clipping at some arbitrary base quality threshold value. This is no longer useful because most\nsophisticated analysis tools (such as the GATK variant discovery tools) are quality-aware, meaning that they are able to\ntake base quality into account when weighing evidence provided by sequencing reads. Unnecessary clipping may interfere\nwith other quality control evaluations and may lower the quality of analysis results. For example, trimming reduces the\neffectiveness of the Base Recalibration (BQSR) pre-processing step of the <a\nhref='https://www.broadinstitute.org/gatk/guide/best-practices'>GATK Best Practices for Variant Discovery</a>, which\naims to correct some types of systematic biases that affect the accuracy of base quality scores.<p>Note: Metrics labeled\nas percentages are actually expressed as fractions!</p><h4>Usage example:</h4><pre>java -jar picard.jar\nCollectBaseDistributionByCycle \\<br />      CHART=collect_base_dist_by_cycle.pdf \\<br />      I=input.bam \\<br />     \nO=output.txt</pre><hr />\nVersion:4.1.3.0\n",
        )
