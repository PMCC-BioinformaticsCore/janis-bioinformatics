from abc import ABC
from datetime import datetime

from janis_bioinformatics.data_types import Bam, FastaWithIndexes, BamBai

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
    Array,
)


class Gatk4SetNmMdAndUqTagsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "SetNmMdAndUqTags"

    def friendly_name(self) -> str:
        return "GATK4: SetNmMdAndUqTags"

    def tool(self) -> str:
        return "Gatk4SetNmMdAndUqTags"

    def inputs(self):
        return [
            *super().inputs(),
            ToolInput(
                tag="bam",
                input_type=Bam(),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) The BAM or SAM file to fix. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(
                    prefix=InputSelector("bam"), suffix=".sorted", extension=".bam"
                ),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The fixed BAM or SAM output file. Required."
                ),
            ),
            ToolInput(
                tag="reference",
                input_type=FastaWithIndexes(),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-R) Reference sequence file. Required."),
            ),
            ToolInput(
                tag="arguments_file",
                input_type=Array(File, optional=True),
                prefix="--arguments_file",
                separate_value_from_prefix=True,
                prefix_applies_to_all_elements=True,
                doc=InputDocumentation(
                    doc="read one or more arguments files and add them to the command line This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            # ToolInput(
            #     tag="compression_level",
            #     input_type=Int(optional=True),
            #     prefix="--COMPRESSION_LEVEL",
            #     separate_value_from_prefix=True,
            #     doc=InputDocumentation(
            #         doc="Compression level for all compressed files created (e.g. BAM and VCF). Default value: 2."
            #     ),
            # ),
            ToolInput(
                tag="create_index",
                input_type=Boolean(optional=True),
                prefix="--CREATE_INDEX",
                separate_value_from_prefix=True,
                default=True,
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
                tag="is_bisulfite_sequence",
                input_type=Boolean(optional=True),
                prefix="--IS_BISULFITE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Whether the file contains bisulfite sequence (used when calculating the NM tag).  Default value: false. Possible values: {true, false} "
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
                tag="set_only_uq",
                input_type=Boolean(optional=True),
                prefix="--SET_ONLY_UQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Only set the UQ tag, ignore MD and NM. Default value: false. Possible values: {true, false} "
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
        return [
            ToolOutput(
                "out",
                BamBai,
                glob=InputSelector("outputFilename"),
                secondaries_present_as={".bai": "^.bai"},
            )
        ]

    def metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=datetime.fromisoformat("2020-05-18T14:59:30.755792"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:59:30.755793"),
            documentation="USAGE: SetNmMdAndUqTags [arguments] This tool takes in a coordinate-sorted SAM or BAM "
            "and calculatesthe NM, MD, and UQ tags by comparing with the reference.<br />This may be "
            "needed when MergeBamAlignment was run with SORT_ORDER other than 'coordinate' and thus could not fix "
            "these tags then. The input must be coordinate sorted in order to run. If specified,the "
            "MD and NM tags can be\nignored and only the UQ tag be set.\n"
            "<h4>Usage example:</h4>"
            "<pre>java -jar picard.jar SetNmMdAndUqTags\n\tR=reference_sequence.fasta \n\tI=sorted.bam \n\tO=fixed.bam <br /></pre>"
            "\n\nVersion:4.1.3.0",
        )
