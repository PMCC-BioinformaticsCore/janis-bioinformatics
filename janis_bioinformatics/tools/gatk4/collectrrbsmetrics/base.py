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


class GatkCollectRrbsMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectRrbsMetrics"

    def friendly_name(self) -> str:
        return "GATK4: CollectRrbsMetrics"

    def tool(self) -> str:
        return "Gatk4CollectRrbsMetrics"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) The BAM or SAM file containing aligned reads. Must be coordinate sorted Required."
                ),
            ),
            ToolInput(
                tag="metrics_file_prefix",
                input_type=String(optional=True),
                prefix="--METRICS_FILE_PREFIX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-M)  Base name for output files  Required. "
                ),
            ),
            ToolInput(
                tag="reference",
                input_type=File(optional=True),
                prefix="--REFERENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R) The reference sequence fasta file Required."
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
                    doc="(-AS) If true, assume that the input file is coordinate sorted even if the header says otherwise.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="c_quality_threshold",
                input_type=Boolean(optional=True),
                prefix="--C_QUALITY_THRESHOLD",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 20."),
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
                tag="max_mismatch_rate",
                input_type=Double(optional=True),
                prefix="--MAX_MISMATCH_RATE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Maximum percentage of mismatches in a read for it to be considered, with a range of 0-1 Default value: 0.1. "
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
                    doc="(-LEVEL)  The level(s) at which to accumulate metrics.    This argument may be specified 0 or more times. Default value: [ALL_READS]. Possible values: {ALL_READS, SAMPLE, LIBRARY, READ_GROUP} "
                ),
            ),
            ToolInput(
                tag="minimum_read_length",
                input_type=Boolean(optional=True),
                prefix="--MINIMUM_READ_LENGTH",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 5."),
            ),
            ToolInput(
                tag="next_base_quality_threshold",
                input_type=Int(optional=True),
                prefix="--NEXT_BASE_QUALITY_THRESHOLD",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Threshold for quality of a base next to a C before the C base is considered  Default value: 10. "
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
                tag="sequence_names",
                input_type=String(optional=True),
                prefix="--SEQUENCE_NAMES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Set of sequence names to consider, if not specified all sequences will be used This argument may be specified 0 or more times. Default value: null. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:10:41.911001"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:10:41.911002"),
            documentation="b'USAGE: CollectRrbsMetrics [arguments]\n<b>Collects metrics from reduced representation bisulfite sequencing (Rrbs) data.</b>  <p>This tool uses reduced\nrepresentation bisulfite sequencing (Rrbs) data to determine cytosine methylation status across all reads of a genomic\nDNA sequence.  For a primer on bisulfite sequencing and cytosine methylation, please see the corresponding <a\nhref='https://www.broadinstitute.org/gatk/guide/article?id=6330'>GATK Dictionary entry</a>. </p><p>Briefly, bisulfite\nreduction converts un-methylated cytosine (C) to uracil (U) bases.  Methylated sites are not converted because they are\nresistant to bisulfite reduction.  Subsequent to PCR amplification of the reaction products, bisulfite reduction\nmanifests as [C -> T (+ strand) or G -> A (- strand)] base conversions.  Thus, conversion rates can be calculated from\nthe reads as follows: [CR = converted/(converted + unconverted)]. Since methylated cytosines are protected against\nRrbs-mediated conversion, the methylation rate (MR) is as follows:[MR = unconverted/(converted + unconverted) = (1 -\nCR)].</p><p>The CpG CollectRrbsMetrics tool outputs three files including summary and detail metrics tables as well as a\nPDF file containing four graphs. These graphs are derived from the summary table and include a comparison of conversion\nrates for both CpG and non-CpG sites, the distribution of total numbers of CpG sites as a function of the CpG conversion\nrates, the distribution of CpG sites by the level of read coverage (depth), and the numbers of reads discarded resulting\nfrom either exceeding the mismatch rate or size (too short).  The detailed metrics table includes the coordinates of all\nof the CpG sites for the experiment as well as the conversion rates observed for each site.</p><h4>Usage\nexample:</h4><pre>java -jar picard.jar CollectRrbsMetrics \\<br />      R=reference_sequence.fasta \\<br />     \nI=input.bam \\<br />      M=basename_for_metrics_files</pre><p>Please see the CollectRrbsMetrics <a\nhref='https://broadinstitute.github.io/picard/picard-metric-definitions.html#RrbsCpgDetailMetrics'>definitions</a> for a\ncomplete description of both the detail and summary metrics produced by this tool.</p><hr />\nVersion:4.1.3.0\n",
        )
