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


class GatkLiftOverIntervalListBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "LiftOverIntervalList"

    def friendly_name(self) -> str:
        return "GATK4: LiftOverIntervalList"

    def tool(self) -> str:
        return "Gatk4LiftOverIntervalList"

    def inputs(self):
        return [
            ToolInput(
                tag="chain",
                input_type=File(optional=True),
                prefix="--CHAIN",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Chain file that guides the LiftOver process. Required."
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) The input interval list to be lifted over. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output interval list file. Required."
                ),
            ),
            ToolInput(
                tag="sequence_dictionary",
                input_type=String(optional=True),
                prefix="--SEQUENCE_DICTIONARY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-SD)  of the target reference.)  Required. "
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
                tag="min_liftover_pct",
                input_type=Double(optional=True),
                prefix="--MIN_LIFTOVER_PCT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Minimum percentage of bases in each input interval that must map to output interval for liftover of that interval to occur. If the program fails to find a good target for an interval, a warning will be emitted and the interval will be dropped from the output.   Default value: 0.95. "
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
                tag="reject",
                input_type=File(optional=True),
                prefix="--REJECT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Interval List file for intervals that were rejected Default value: null."
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:53:44.659571"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:53:44.659572"),
            documentation="b'USAGE: LiftOverIntervalList [arguments]\nLifts over an interval list from one reference build to another. This tool adjusts the coordinates in an interval list\non one reference to its homologous interval list on another reference, based on a chain file that describes the\ncorrespondence between the two references. It is based on the UCSC LiftOver tool (see:\nhttp://genome.ucsc.edu/cgi-bin/hgLiftOver) and uses a UCSC chain file to guide its operation. It accepts both Picard\ninterval_list files or VCF files as interval inputs.\n<h3>Usage example:</h3>java -jar picard.jar LiftOverIntervalList \\\nI=input.interval_list \\\nO=output.interval_list \\\nSD=reference_sequence.dict \\\nCHAIN=build.chain</pre>\n<h3>Return codes</h3>\nIf all the intervals lifted over successfully, program will return 0. It will return 1 otherwise.\n<h3>Caveats</h3>\nAn interval is 'lifted' in its entirety, but it might intersect (a 'hit') with multiple chain-blocks. Instead of placing\nthe interval in multiple hits, it is lifted over using the first hit that passes the threshold of MIN_LIFTOVER_PCT. For\nlarge enough MIN_LIFTOVER_PCT this is non-ambiguous, but if one uses small values of MIN_LIFTOVER_PCT (perhaps in order\nto increase the rate of successful hits...) the liftover could end up going to the smaller of two good hits. On the\nother hand, if none of the hits pass the threshold a warning will be emitted and the interval will not be lifted.\nVersion:4.1.3.0\n",
        )
