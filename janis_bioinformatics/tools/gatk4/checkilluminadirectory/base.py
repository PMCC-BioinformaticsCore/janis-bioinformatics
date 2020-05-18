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


class GatkCheckIlluminaDirectoryBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CheckIlluminaDirectory"

    def friendly_name(self) -> str:
        return "GATK4: CheckIlluminaDirectory"

    def tool(self) -> str:
        return "Gatk4CheckIlluminaDirectory"

    def inputs(self):
        return [
            ToolInput(
                tag="basecalls_dir",
                input_type=File(optional=True),
                prefix="--BASECALLS_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-B) The basecalls output directory. Required."
                ),
            ),
            ToolInput(
                tag="lanes",
                input_type=Int(optional=True),
                prefix="--LANES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-L) The number of the lane(s) to check. This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="read_structure",
                input_type=String(optional=True),
                prefix="--READ_STRUCTURE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-RS) A description of the logical structure of clusters in an Illumina Run, i.e. a description of the structure IlluminaBasecallsToSam assumes the  data to be in. It should consist of integer/character pairs describing the number of cycles and the type of those cycles (B for Sample Barcode, M for molecular barcode, T for Template, and S for skip).  E.g. If the input data consists of 80 base clusters and we provide a read structure of '28T8M8B8S28T' then the sequence may be split up into four reads: * read one with 28 cycles (bases) of template * read two with 8 cycles (bases) of molecular barcode (ex. unique molecular barcode) * read three with 8 cycles (bases) of sample barcode * 8 cycles (bases) skipped. * read four with 28 cycles (bases) of template The skipped cycles would NOT be included in an output SAM/BAM file or in read groups therein. Note:  If you want to check whether or not a future IlluminaBasecallsToSam or ExtractIlluminaBarcodes run will fail then be sure to use the exact same READ_STRUCTURE that you would pass to these programs for this run.  Required. "
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
                tag="data_types",
                input_type=Boolean(optional=True),
                prefix="--DATA_TYPES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DT)  The data types that should be checked for each tile/cycle.  If no values are provided then the data types checked are those required by IlluminaBaseCallsToSam (which is a superset of those used in ExtractIlluminaBarcodes).  These data types vary slightly depending on whether or not the run is barcoded so READ_STRUCTURE should be the same as that which will be passed to IlluminaBasecallsToSam.  If this option is left unspecified then both ExtractIlluminaBarcodes and IlluminaBaseCallsToSam should complete successfully UNLESS the individual records of the files themselves are spurious.  This argument may be specified 0 or more times. Default value: null. Possible values: {Position, BaseCalls, QualityScores, PF, Barcodes} "
                ),
            ),
            ToolInput(
                tag="fake_files",
                input_type=Boolean(optional=True),
                prefix="--FAKE_FILES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-F) A flag to determine whether or not to create fake versions of the missing files. Default value: false. Possible values: {true, false} "
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
                tag="link_locs",
                input_type=Boolean(optional=True),
                prefix="--LINK_LOCS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-X) A flag to create symlinks to the loc file for the X Ten for each tile. @deprecated It is no longer necessary to create locs file symlinks.  Default value: false. Possible values: {true, false} "
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
                tag="reference_sequence",
                input_type=File(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R) Reference sequence file. Default value: null."
                ),
            ),
            ToolInput(
                tag="tile_numbers",
                input_type=Int(optional=True),
                prefix="--TILE_NUMBERS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-T) The number(s) of the tile(s) to check. This argument may be specified 0 or more times. Default value: null. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:04:07.516027"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:04:07.516028"),
            documentation="b'USAGE: CheckIlluminaDirectory [arguments]\nAsserts the validity for specified Illumina basecalling data.  <p>This tool will check that the basecall directory and\nthe internal files are available, exist, and are reasonably sized for every tile and cycle.  Reasonably sized means\nnon-zero sized for files that exist per tile and equal size for binary files that exist per cycle or per tile. If\nDATA_TYPES {Position, BaseCalls, QualityScores, PF, or Barcodes} are not specified, then the default data types used by\nIlluminaBasecallsToSam are used.  CheckIlluminaDirectory DOES NOT check that the individual records in a file are\nwell-formed. If there are errors, the number of errors is written in a file called 'errors.count' in the working\ndirectory</p><h4>Usage example:</h4> <pre>java -jar picard.jar CheckIlluminaDirectory \\<br />     \nBASECALLS_DIR=/BaseCalls/  \\<br />      READ_STRUCTURE=25T8B25T \\<br />      LANES=1 \\<br />      DATA_TYPES=BaseCalls\n</pre><hr />\nVersion:4.1.3.0\n",
        )
