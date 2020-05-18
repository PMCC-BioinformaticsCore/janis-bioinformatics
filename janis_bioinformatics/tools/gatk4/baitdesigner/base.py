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


class GatkBaitDesignerBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "BaitDesigner"

    def friendly_name(self) -> str:
        return "GATK4: BaitDesigner"

    def tool(self) -> str:
        return "Gatk4BaitDesigner"

    def inputs(self):
        return [
            ToolInput(
                tag="design_name",
                input_type=String(optional=True),
                prefix="--DESIGN_NAME",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="The name of the bait design Required."),
            ),
            ToolInput(
                tag="reference_sequence",
                input_type=File(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-R) Reference sequence file. Required."),
            ),
            ToolInput(
                tag="targets",
                input_type=File(optional=True),
                prefix="--TARGETS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-T) The file with design parameters and targets Required."
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
                tag="bait_offset",
                input_type=Int(optional=True),
                prefix="--BAIT_OFFSET",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The desired offset between the start of one bait and the start of another bait for the same target.  Default value: 80. "
                ),
            ),
            ToolInput(
                tag="bait_size",
                input_type=Int(optional=True),
                prefix="--BAIT_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The length of each individual bait to design Default value: 120."
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
                tag="design_on_target_strand",
                input_type=Boolean(optional=True),
                prefix="--DESIGN_ON_TARGET_STRAND",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If true design baits on the strand of the target feature, if false always design on the + strand of the genome.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="design_strategy",
                input_type=Boolean(optional=True),
                prefix="--DESIGN_STRATEGY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The design strategy to use to layout baits across each target  Default value: FixedOffset. Possible values: {CenteredConstrained, FixedOffset, Simple} "
                ),
            ),
            ToolInput(
                tag="fill_pools",
                input_type=Boolean(optional=True),
                prefix="--FILL_POOLS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true, fill up the pools with alternating fwd and rc copies of all baits. Equal copies of all baits will always be maintained  Default value: true. Possible values: {true, false} "
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
                tag="left_primer",
                input_type=String(optional=True),
                prefix="--LEFT_PRIMER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The left amplification primer to prepend to all baits for synthesis Default value: ATCGCACCAGCGTGT. "
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
                tag="merge_nearby_targets",
                input_type=String(optional=True),
                prefix="--MERGE_NEARBY_TARGETS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" be more efficient.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="minimum_baits_per_target",
                input_type=Int(optional=True),
                prefix="--MINIMUM_BAITS_PER_TARGET",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The minimum number of baits to design per target.  Default value: 2. "
                ),
            ),
            ToolInput(
                tag="output_agilent_files",
                input_type=Boolean(optional=True),
                prefix="--OUTPUT_AGILENT_FILES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="output_directory",
                input_type=File(optional=True),
                prefix="--OUTPUT_DIRECTORY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output directory. If not provided then the DESIGN_NAME will be used as the output directory  Default value: null. "
                ),
            ),
            ToolInput(
                tag="padding",
                input_type=Int(optional=True),
                prefix="--PADDING",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Pad the input targets by this amount when designing baits. Padding is applied on both sides in this amount.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="pool_size",
                input_type=Int(optional=True),
                prefix="--POOL_SIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The size of pools or arrays for synthesis. If no pool files are desired, can be set to 0. Default value: 55000. "
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
                tag="repeat_tolerance",
                input_type=Int(optional=True),
                prefix="--REPEAT_TOLERANCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Baits that have more than REPEAT_TOLERANCE soft or hard masked bases will not be allowed Default value: 50. "
                ),
            ),
            ToolInput(
                tag="right_primer",
                input_type=String(optional=True),
                prefix="--RIGHT_PRIMER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The right amplification primer to prepend to all baits for synthesis Default value: CACTGCGGCTCCTCA. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:00:30.093269"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:00:30.093270"),
            documentation="b'USAGE: BaitDesigner [arguments]\nDesigns oligonucleotide baits for hybrid selection reactions.<p>This tool is used to design custom bait sets for hybrid\nselection experiments. The following files are input into BaitDesigner: a (TARGET) interval list indicating the\nsequences of interest, e.g. exons with their respective coordinates, a reference sequence, and a unique identifier\nstring (DESIGN_NAME). </p><p>The tool will output interval_list files of both bait and target sequences as well as the\nactual bait sequences in FastA format. At least two baits are output for each target sequence, with greater numbers for\nlarger intervals. Although the default values for both bait size  (120 bases) nd offsets (80 bases) are suitable for\nmost applications, these values can be customized. Offsets represent the distance between sequential baits on a\ncontiguous stretch of target DNA sequence. </p><p>The tool will also output a pooled set of 55,000 (default)\noligonucleotides representing all of the baits redundantly. This redundancy achieves a uniform concentration of\noligonucleotides for synthesis by a vendor as well as equal numbersof each bait to prevent bias during the hybrid\nselection reaction. </p><h4>Usage example:</h4><pre>java -jar picard.jar BaitDesigner \\<br />     \nTARGET=targets.interval_list \\<br />      DESIGN_NAME=new_baits \\<br />      R=reference_sequence.fasta </pre> <hr />\nVersion:4.1.3.0\n",
        )
