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


class GatkRevertSamBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "RevertSam"

    def friendly_name(self) -> str:
        return "GATK4: RevertSam"

    def tool(self) -> str:
        return "Gatk4RevertSam"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) The input SAM/BAM file to revert the state of. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output SAM/BAM file to create, or an output directory if OUTPUT_BY_READGROUP is true. Required.  Cannot be used in conjuction with argument(s) OUTPUT_MAP (OM) OUTPUT_MAP (OM)"
                ),
            ),
            ToolInput(
                tag="output_map",
                input_type=File(optional=True),
                prefix="--OUTPUT_MAP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OM) Tab separated file with two columns, READ_GROUP_ID and OUTPUT, providing file mapping only used if OUTPUT_BY_READGROUP is true.  Required.  Cannot be used in conjuction with argument(s) OUTPUT (O)"
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
                tag="attribute_to_clear",
                input_type=String(optional=True),
                prefix="--ATTRIBUTE_TO_CLEAR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When removing alignment information, the set of optional tags to remove. This argument may be specified 0 or more times. Default value: [NM, UQ, PG, MD, MQ, SA, MC, AS]. "
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
                tag="keep_first_duplicate",
                input_type=String(optional=True),
                prefix="--KEEP_FIRST_DUPLICATE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" name for R1/R2/unpaired reads respectively. For paired end reads, keeps only the first R1 and R2 found respectively, and discards all unpaired reads. Duplicates do not refer to the duplicate flag in the FLAG field, but instead reads with the same name.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="library_name",
                input_type=String(optional=True),
                prefix="--LIBRARY_NAME",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-LIB) The library name to use in the reverted output file. This will override the existing sample alias in the file and is used only if all the read groups in the input file have the same library name.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="max_discard_fraction",
                input_type=Boolean(optional=True),
                prefix="--MAX_DISCARD_FRACTION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" sanitization thenthe program will exit with an Exception instead of exiting cleanly. Output BAM will still be valid.  Default value: 0.01. "
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
                tag="output_by_readgroup",
                input_type=Boolean(optional=True),
                prefix="--OUTPUT_BY_READGROUP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OBR)  When true, outputs each read group in a separate file.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="output_by_readgroup_file_format",
                input_type=Boolean(optional=True),
                prefix="--OUTPUT_BY_READGROUP_FILE_FORMAT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OBRFF)  When using OUTPUT_BY_READGROUP, the output file format can be set to a certain format.  Default value: dynamic. Possible values: { sam (Generate SAM files.) bam (Generate BAM files.) cram (Generate CRAM files.) dynamic (Generate files based on the extention of INPUT.) } "
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
                tag="remove_alignment_information",
                input_type=Boolean(optional=True),
                prefix="--REMOVE_ALIGNMENT_INFORMATION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Remove all alignment information from the file.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="remove_duplicate_information",
                input_type=Boolean(optional=True),
                prefix="--REMOVE_DUPLICATE_INFORMATION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Remove duplicate read flags from all reads.  Note that if this is false and REMOVE_ALIGNMENT_INFORMATION==true,  the output may have the unusual but sometimes desirable trait of having unmapped reads that are marked as duplicates.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="restore_original_qualities",
                input_type=Boolean(optional=True),
                prefix="--RESTORE_ORIGINAL_QUALITIES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OQ)  True to restore original qualities from the OQ field to the QUAL field if available.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="sample_alias",
                input_type=String(optional=True),
                prefix="--SAMPLE_ALIAS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ALIAS) The sample alias to use in the reverted output file. This will override the existing sample alias in the file and is used only if all the read groups in the input file have the same sample alias.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="sanitize",
                input_type=Boolean(optional=True),
                prefix="--SANITIZE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="WARNING: This option is potentially destructive. If enabled will discard reads in order to produce a consistent output BAM. Reads discarded include (but are not limited to) paired reads with missing mates, duplicated records, records with mismatches in length of bases and qualities. This option can only be enabled if the output sort order is queryname and will always cause sorting to occur.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="sort_order",
                input_type=Boolean(optional=True),
                prefix="--SORT_ORDER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-SO) The sort order to create the reverted output file with. Default value: queryname. Possible values: {unsorted, queryname, coordinate, duplicate, unknown} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:58:50.171370"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:58:50.171371"),
            documentation="b'USAGE: RevertSam [arguments]\nReverts SAM or BAM files to a previous state.  This tool removes or restores certain properties of the SAM records,\nincluding alignment information, which can be used to produce an unmapped BAM (uBAM) from a previously aligned BAM. It\nis also capable of restoring the original quality scores of a BAM file that has already undergone base quality score\nrecalibration (BQSR) if theoriginal qualities were retained.\n<h3>Examples</h3>\n<h4>Example with single output:</h4>\njava -jar picard.jar RevertSam \\\nI=input.bam \\\nO=reverted.bam\n<h4>Example outputting by read group with output map:</h4>\njava -jar picard.jar RevertSam \\\nI=input.bam \\\nOUTPUT_BY_READGROUP=true \\\nOUTPUT_MAP=reverted_bam_paths.tsv\nWill output a BAM/SAM file per read group.\n<h4>Example outputting by read group without output map:</h4>\njava -jar picard.jar RevertSam \\\nI=input.bam \\\nOUTPUT_BY_READGROUP=true \\\nO=/write/reverted/read/group/bams/in/this/dir\nWill output a BAM file per read group. Output format can be overridden with the OUTPUT_BY_READGROUP_FILE_FORMAT option.\nNote: If the program fails due to a SAM validation error, consider setting the VALIDATION_STRINGENCY option to LENIENT\nor SILENT if the failures are expected to be obviated by the reversion process (e.g. invalid alignment information will\nbe obviated when the REMOVE_ALIGNMENT_INFORMATION option is used).\nVersion:4.1.3.0\n",
        )
