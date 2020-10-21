from abc import ABC
from datetime import datetime
from janis_bioinformatics.tools.gatk4.gatk4toolbase import Gatk4ToolBase
from janis_bioinformatics.data_types import Bam, BamBai

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


class Gatk4GatherBamFilesBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "GatherBamFiles"

    def friendly_name(self) -> str:
        return "GATK4: GatherBamFiles"

    def tool(self) -> str:
        return "Gatk4GatherBamFiles"

    def inputs(self):
        return [
            *super().inputs(),
            ToolInput(
                tag="bams",
                input_type=Array(Bam, optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                prefix_applies_to_all_elements=True,
                doc=InputDocumentation(
                    doc="(-I) Two or more BAM files or text files containing lists of BAM files (one per line). This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(suffix=".merged", extension=".bam"),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output BAM file to write to. Required."
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
            contributors=[],
            dateCreated=datetime(2020, 5, 18),
            dateUpdated=datetime(2020, 5, 18),
            documentation="b'USAGE: GatherBamFiles [arguments]\n<p>Concatenate efficiently BAM files that resulted from a scattered parallel analysis.</p><p>This tool performs a rapid\n'gather' or concatenation on BAM files. This is often needed in operations that have been run in parallel across\ngenomics regions by scattering their execution across computing nodes and cores thus resulting in smaller BAM\nfiles.</p><p>This tool does not support SAM files</p><h3>Inputs</h3><p>A list of BAM files to combine using the INPUT\nargument. These files must be provided in the order that they should be concatenated.</p><h3>Output</h3><p>A single BAM\nfile. The header is copied from the first input file.</p><h3>Usage example:</h3><pre>java -jar picard.jar GatherBamFiles\n\\\nI=input1.bam \\\nI=input2.bam \\\nO=gathered_files.bam</pre><h3>Notes</h3><p>Operates via copying of the gzip blocks directly for speed but also supports\ngeneration of an MD5 on the output and indexing of the output BAM file.</p><hr/>\nVersion:4.1.3.0\n",
        )
