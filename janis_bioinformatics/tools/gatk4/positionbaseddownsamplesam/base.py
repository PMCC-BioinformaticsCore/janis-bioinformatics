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


class GatkPositionBasedDownsampleSamBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "PositionBasedDownsampleSam"

    def friendly_name(self) -> str:
        return "GATK4: PositionBasedDownsampleSam"

    def tool(self) -> str:
        return "Gatk4PositionBasedDownsampleSam"

    def inputs(self):
        return [
            ToolInput(
                tag="fraction",
                input_type=Double(optional=True),
                prefix="--FRACTION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-F) The (approximate) fraction of reads to be kept, between 0 and 1. Required."
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) The input SAM or BAM file to downsample. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output, downsampled, SAM or BAM file. Required."
                ),
            ),
            ToolInput(
                tag="allow_multiple_downsampling_despite_warnings",
                input_type=Boolean(optional=True),
                prefix="--ALLOW_MULTIPLE_DOWNSAMPLING_DESPITE_WARNINGS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Allow downsampling again despite this being a bad idea with possibly unexpected results.  Default value: false. Possible values: {true, false} "
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
                tag="quiet",
                input_type=Boolean(optional=True),
                prefix="--QUIET",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to suppress job-summary info on System.err. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="read_name_regex",
                input_type=String(optional=True),
                prefix="--READ_NAME_REGEX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Use these regular expressions to parse read names in the input SAM file. Read names are parsed to extract three variables: tile/region, x coordinate and y coordinate. The x and y coordinates are used to determine the downsample decision. Set this option to null to disable optical duplicate detection, e.g. for RNA-seq The regular expression should contain three capture groups for the three variables, in order. It must match the entire read name. Note that if the default regex is specified, a regex match is not actually done, but instead the read name is split on colons (:). For 5 element names, the 3rd, 4th and 5th elements are assumed to be tile, x and y values. For 7 element names (CASAVA 1.8), the 5th, 6th, and 7th elements are assumed to be tile, x and y values.  Default value: <optimized capture of last three ':' separated fields as numeric values>. "
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
                tag="remove_duplicate_information",
                input_type=Boolean(optional=True),
                prefix="--REMOVE_DUPLICATE_INFORMATION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Determines whether the duplicate tag should be reset since the downsampling requires re-marking duplicates.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="stop_after",
                input_type=Boolean(optional=True),
                prefix="--STOP_AFTER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Stop after processing N reads, mainly for debugging. Default value: null."
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:58:04.085370"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:58:04.085373"),
            documentation="b'USAGE: PositionBasedDownsampleSam [arguments]\n<h3>Summary</h3>\nClass to downsample a SAM/BAM file based on the position of the read in a flowcell. As with DownsampleSam, all the reads\nwith the same queryname are either kept or dropped as a unit.\n<h3>Details</h3>\nThe downsampling is _not_ random (and there is no random seed). It is deterministically determined by the position of\neach read within its tile. Specifically, it draws an ellipse that covers a FRACTION of the total tile's area and of all\nthe edges of the tile. It uses this area to determine whether to keep or drop the record. Since reads with the same name\nhave the same position (mates, secondary and supplemental alignments), the decision will be the same for all of them.\nThe main concern of this downsampling method is that due to 'optical duplicates' downsampling randomly can create a\nresult that has a different optical duplicate rate, and therefore a different estimated library size (when running\nMarkDuplicates). This method keeps (physically) close read together, so that (except for reads near the boundary of the\ncircle) optical duplicates are kept or dropped as a group. By default the program expects the read names to have 5 or 7\nfields separated by colons (:) and it takes the last two to indicate the x and y coordinates of the reads within the\ntile whence it was sequenced. See DEFAULT_READ_NAME_REGEX for more detail. The program traverses the INPUT twice: first\nto find out the size of each of the tiles, and next to perform the downsampling. Downsampling invalidates the duplicate\nflag because duplicate reads before downsampling may not all remain duplicated after downsampling. Thus, the default\nsetting also removes the duplicate information. \nExample\njava -jar picard.jar PositionBasedDownsampleSam \\\nI=input.bam \\\nO=downsampled.bam \\\nFRACTION=0.1\nCaveats\nNote 1: This method is <b>technology and read-name dependent</b>. If the read-names do not have coordinate information\nembedded in them, or if your BAM contains reads from multiple technologies (flowcell versions, sequencing machines) this\nwill not work properly. It has been designed to work with Illumina technology and reads-names. Consider modifying {@link\n#READ_NAME_REGEX} in other cases. \nNote 2: The code has been designed to simulate, as accurately as possible, sequencing less, <b>not</b> for getting an\nexact downsampled fraction (Use {@link DownsampleSam} for that.) In particular, since the reads may be distributed\nnon-evenly within the lanes/tiles, the resulting downsampling percentage will not be accurately determined by the input\nargument FRACTION. \nNote 3:Consider running {@link MarkDuplicates} after downsampling in order to 'expose' the duplicates whose\nrepresentative has been downsampled away.\nNote 4:The downsampling assumes a uniform distribution of reads in the flowcell. Input already downsampled with\nPositionBasedDownsampleSam violates this assumption. To guard against such input, PositionBasedDownsampleSam always\nplaces a PG record in the header of its output, and aborts whenever it finds such a PG record in its input.\nVersion:4.1.3.0\n",
        )
