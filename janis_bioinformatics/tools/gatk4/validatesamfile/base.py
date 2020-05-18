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


class GatkValidateSamFileBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "ValidateSamFile"

    def friendly_name(self) -> str:
        return "GATK4: ValidateSamFile"

    def tool(self) -> str:
        return "Gatk4ValidateSamFile"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-I) Input SAM/BAM file Required."),
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
                tag="ignore",
                input_type=Boolean(optional=True),
                prefix="--IGNORE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="List of validation error types to ignore. This argument may be specified 0 or more times. Default value: null. Possible values: {INVALID_QUALITY_FORMAT, INVALID_FLAG_PROPER_PAIR, INVALID_FLAG_MATE_UNMAPPED, MISMATCH_FLAG_MATE_UNMAPPED, INVALID_FLAG_MATE_NEG_STRAND, MISMATCH_FLAG_MATE_NEG_STRAND, INVALID_FLAG_FIRST_OF_PAIR, INVALID_FLAG_SECOND_OF_PAIR, PAIRED_READ_NOT_MARKED_AS_FIRST_OR_SECOND, INVALID_FLAG_NOT_PRIM_ALIGNMENT, INVALID_FLAG_SUPPLEMENTARY_ALIGNMENT, INVALID_FLAG_READ_UNMAPPED, INVALID_INSERT_SIZE, INVALID_MAPPING_QUALITY, INVALID_CIGAR, ADJACENT_INDEL_IN_CIGAR, INVALID_MATE_REF_INDEX, MISMATCH_MATE_REF_INDEX, INVALID_REFERENCE_INDEX, INVALID_ALIGNMENT_START, MISMATCH_MATE_ALIGNMENT_START, MATE_FIELD_MISMATCH, INVALID_TAG_NM, MISSING_TAG_NM, MISSING_HEADER, MISSING_SEQUENCE_DICTIONARY, MISSING_READ_GROUP, RECORD_OUT_OF_ORDER, READ_GROUP_NOT_FOUND, RECORD_MISSING_READ_GROUP, INVALID_INDEXING_BIN, MISSING_VERSION_NUMBER, INVALID_VERSION_NUMBER, TRUNCATED_FILE, MISMATCH_READ_LENGTH_AND_QUALS_LENGTH, EMPTY_READ, CIGAR_MAPS_OFF_REFERENCE, MISMATCH_READ_LENGTH_AND_E2_LENGTH, MISMATCH_READ_LENGTH_AND_U2_LENGTH, E2_BASE_EQUALS_PRIMARY_BASE, BAM_FILE_MISSING_TERMINATOR_BLOCK, UNRECOGNIZED_HEADER_TYPE, POORLY_FORMATTED_HEADER_TAG, HEADER_TAG_MULTIPLY_DEFINED, HEADER_RECORD_MISSING_REQUIRED_TAG, HEADER_TAG_NON_CONFORMING_VALUE, INVALID_DATE_STRING, TAG_VALUE_TOO_LARGE, INVALID_INDEX_FILE_POINTER, INVALID_PREDICTED_MEDIAN_INSERT_SIZE, DUPLICATE_READ_GROUP_ID, MISSING_PLATFORM_VALUE, INVALID_PLATFORM_VALUE, DUPLICATE_PROGRAM_GROUP_ID, MATE_NOT_FOUND, MATES_ARE_SAME_END, MISMATCH_MATE_CIGAR_STRING, MATE_CIGAR_STRING_INVALID_PRESENCE, INVALID_UNPAIRED_MATE_REFERENCE, INVALID_UNALIGNED_MATE_START, MISMATCH_CIGAR_SEQ_LENGTH, MISMATCH_SEQ_QUAL_LENGTH, MISMATCH_FILE_SEQ_DICT, QUALITY_NOT_STORED, DUPLICATE_SAM_TAG, CG_TAG_FOUND_IN_ATTRIBUTES, REF_SEQ_TOO_LONG_FOR_BAI} "
                ),
            ),
            ToolInput(
                tag="ignore_warnings",
                input_type=Boolean(optional=True),
                prefix="--IGNORE_WARNINGS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true, only report errors and ignore warnings. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="index_validation_stringency",
                input_type=Boolean(optional=True),
                prefix="--INDEX_VALIDATION_STRINGENCY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If set to anything other than IndexValidationStringency.NONE and input is a BAM file with an index file, also validates the index at the specified stringency. Until VALIDATE_INDEX is retired, VALIDATE INDEX and INDEX_VALIDATION_STRINGENCY must agree on whether to validate the index.  Default value: EXHAUSTIVE. Possible values: {EXHAUSTIVE, LESS_EXHAUSTIVE, NONE} "
                ),
            ),
            ToolInput(
                tag="is_bisulfite_sequenced",
                input_type=Boolean(optional=True),
                prefix="--IS_BISULFITE_SEQUENCED",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-BISULFITE)  Whether the SAM or BAM file consists of bisulfite sequenced reads. If so, C->T is not counted as an error in computing the value of the NM tag.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="max_open_temp_files",
                input_type=Boolean(optional=True),
                prefix="--MAX_OPEN_TEMP_FILES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" handles to keep open when spilling mate info to disk. Set this number a little lower than the per-process maximum number of file that may be open. This number can be found by executing the 'ulimit -n' command on a Unix system.  Default value: 8000. "
                ),
            ),
            ToolInput(
                tag="max_output",
                input_type=Int(optional=True),
                prefix="--MAX_OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MO) The maximum number of lines output in verbose mode Default value: 100."
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
                tag="mode",
                input_type=Boolean(optional=True),
                prefix="--MODE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-M) Mode of output Default value: VERBOSE. Possible values: {VERBOSE, SUMMARY}"
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Output file or standard out if missing Default value: null."
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
                tag="skip_mate_validation",
                input_type=Boolean(optional=True),
                prefix="--SKIP_MATE_VALIDATION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-SMV)  If true, this tool will not attempt to validate mate information. In general cases, this option should not be used.  However, in cases where samples have very high duplication or chimerism rates (> 10%), the mate validation process often requires extremely large amounts of memory to run, so this flag allows you to forego that check.  Default value: false. Possible values: {true, false} "
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
                tag="validate_index",
                input_type=Boolean(optional=True),
                prefix="--VALIDATE_INDEX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="DEPRECATED. Use INDEX_VALIDATION_STRINGENCY instead. If true and input is a BAM file with an index file, also validates the index.  Until this parameter is retired VALIDATE INDEX and INDEX_VALIDATION_STRINGENCY must agree on whether to validate the index.  Default value: true. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:52:03.761281"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:52:03.761282"),
            documentation="b'USAGE: ValidateSamFile [arguments]\nValidates a SAM or BAM file.<p>This tool reports on the validity of a SAM or BAM file relative to the SAM format\nspecification.  This is useful for troubleshooting errors encountered with other tools that may be caused by improper\nformatting, faulty alignments, incorrect flag values, etc. </p> <p>By default, the tool runs in VERBOSE mode and will\nexit after finding 100 errors and output them to the console (stdout). Therefore, it is often more practical to run this\ntool initially using the MODE=SUMMARY option.  This mode outputs a summary table listing the numbers of all 'errors' and\n'warnings'.</p> <p>When fixing errors in your file, it is often useful to prioritize the severe validation errors and\nignore the errors/warnings of lesser concern.  This can be done using the IGNORE and/or IGNORE_WARNINGS arguments.  For\nhelpful suggestions on error prioritization, please follow this link to obtain additional documentation on <a\nhref='https://www.broadinstitute.org/gatk/guide/article?id=7571'>ValidateSamFile</a>.</p><p>After identifying and fixing\nyour 'warnings/errors', we recommend that you rerun this tool to validate your SAM/BAM file prior to proceeding with\nyour downstream analysis.  This will verify that all problems in your file have been addressed.</p><h4>Usage\nexample:</h4><pre>java -jar picard.jar ValidateSamFile \\<br />      I=input.bam \\<br />      MODE=SUMMARY</pre><p>To\nobtain a complete list with descriptions of both 'ERROR' and 'WARNING' messages, please see our additional  <a\nhref='https://www.broadinstitute.org/gatk/guide/article?id=7571'>documentation</a> for this tool.</p><hr />Return codes\ndepend on the errors/warnings discovered:<p>-1 failed to complete execution\n0  ran successfully\n1  warnings but no errors\n2  errors and warnings\n3  errors but no warnings\nVersion:4.1.3.0\n",
        )
