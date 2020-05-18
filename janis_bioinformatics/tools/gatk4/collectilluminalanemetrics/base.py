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


class GatkCollectIlluminaLaneMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectIlluminaLaneMetrics"

    def friendly_name(self) -> str:
        return "GATK4: CollectIlluminaLaneMetrics"

    def tool(self) -> str:
        return "Gatk4CollectIlluminaLaneMetrics"

    def inputs(self):
        return [
            ToolInput(
                tag="output_directory",
                input_type=File(optional=True),
                prefix="--OUTPUT_DIRECTORY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The directory to which the output file will be written Required."
                ),
            ),
            ToolInput(
                tag="output_prefix",
                input_type=String(optional=True),
                prefix="--OUTPUT_PREFIX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The prefix to be prepended to the file name of the output file; an appropriate suffix will be applied  Required. "
                ),
            ),
            ToolInput(
                tag="run_directory",
                input_type=File(optional=True),
                prefix="--RUN_DIRECTORY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The Illumina run directory of the run for which the lane metrics are to be generated Required. "
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
                tag="file_extension",
                input_type=String(optional=True),
                prefix="--FILE_EXTENSION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-EXT) Append the given file extension to all metric file names (ex. OUTPUT.illumina_lane_metrics.EXT). None if null  Default value: null. "
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
                tag="is_novaseq",
                input_type=Boolean(optional=True),
                prefix="--IS_NOVASEQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Boolean the determines if this run is a NovaSeq run or not. (NovaSeq tile metrics files are in cycle 25 directory.  Default value: false. Possible values: {true, false} "
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
                tag="quiet",
                input_type=Boolean(optional=True),
                prefix="--QUIET",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to suppress job-summary info on System.err. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="read_structure",
                input_type=Boolean(optional=True),
                prefix="--READ_STRUCTURE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-RS)  A description of the logical structure of clusters in an Illumina Run, i.e. a description of the structure IlluminaBasecallsToSam assumes the  data to be in. It should consist of integer/character pairs describing the number of cycles and the type of those cycles (B for Sample Barcode, M for molecular barcode, T for Template, and S for skip).  E.g. If the input data consists of 80 base clusters and we provide a read structure of '28T8M8B8S28T' then the sequence may be split up into four reads: * read one with 28 cycles (bases) of template * read two with 8 cycles (bases) of molecular barcode (ex. unique molecular barcode) * read three with 8 cycles (bases) of sample barcode * 8 cycles (bases) skipped. * read four with 28 cycles (bases) of template The skipped cycles would NOT be included in an output SAM/BAM file or in read groups therein. If not given, will use the RunInfo.xml in the run directory.  Default value: null. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:04:20.458250"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:04:20.458252"),
            documentation="b'USAGE: CollectIlluminaLaneMetrics [arguments]\nCollects Illumina lane metrics for the given BaseCalling analysis directory.  This tool produces quality control metrics\non cluster density for each lane of an Illumina flowcell.  This tool takes Illumina TileMetrics data and places them\ninto directories containing lane- and phasing-level metrics.  In this context, phasing refers to the fraction of\nmolecules that fall behind or jump ahead (prephasing) during a read cycle.<h4>Usage example:</h4><pre>java -jar\npicard.jar CollectIlluminaLaneMetrics \\<br />      RUN_DIR=test_run \\<br />      OUTPUT_DIRECTORY=Lane_output_metrics\n\\<br />      OUTPUT_PREFIX=experiment1 \\<br />      READ_STRUCTURE=25T8B25T </pre><p>Please see the\nCollectIlluminaLaneMetrics <a\nhref='http://broadinstitute.github.io/picard/picard-metric-definitions.html#CollectIlluminaLaneMetrics'>definitions</a>\nfor a complete description of the metrics produced by this tool.</p><hr />\nVersion:4.1.3.0\n",
        )
