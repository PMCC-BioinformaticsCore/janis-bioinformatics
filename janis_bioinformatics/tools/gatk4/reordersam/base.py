from abc import ABC
from datetime import datetime
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

from janis_bioinformatics.data_types import BamBai, Bam, FastaWithIndexes
from janis_bioinformatics.tools.gatk4.gatk4toolbase import Gatk4ToolBase


class Gatk4ReorderSamBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "ReorderSam"

    def friendly_name(self) -> str:
        return "Gatk4: ReorderSam"

    def tool(self) -> str:
        return "GatkReorderSam"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=Bam(),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input file (SAM or BAM) to extract reads from. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(prefix=InputSelector("inp"), extension=".bam"),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Output file (SAM or BAM) to write extracted reads to. Required."
                ),
            ),
            ToolInput(
                tag="reference",
                input_type=FastaWithIndexes(),
                prefix="--REFERENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R) Reference sequence to reorder reads to match. A sequence dictionary corresponding to the reference fasta is required.  Create one with CreateSequenceDictionary.  Required. "
                ),
            ),
            ToolInput(
                tag="allow_contig_length_discordance",
                input_type=Boolean(optional=True),
                prefix="--ALLOW_CONTIG_LENGTH_DISCORDANCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-U)  If true, then permits mapping from a read contig to a new reference contig with the same name but a different length.  Highly dangerous, only use if you know what you are doing.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="allow_incomplete_dict_concordance",
                input_type=Boolean(optional=True),
                prefix="--ALLOW_INCOMPLETE_DICT_CONCORDANCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-S)  If true, then allows only a partial overlap of the original contigs with the new reference sequence contigs.  By default, this tool requires a corresponding contig in the new reference for each read contig  Default value: false. Possible values: {true, false} "
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
                default=True,
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
                BamBai(),
                glob=InputSelector("outputFilename"),
                doc="BAM to write extracted reads to",
                secondaries_present_as={".bai": "^.bai"},
            )
        ]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["illusional"],
            dateCreated=datetime.fromisoformat("2020-05-15T16:11:13.566578"),
            dateUpdated=datetime.fromisoformat("2020-05-15T16:11:13.566579"),
            documentation="""
USAGE: ReorderSam [arguments]

Not to be confused with SortSam which sorts a SAM or BAM file with a valid sequence dictionary, 
ReorderSam reorders\nreads in a SAM/BAM file to match the contig ordering in a provided reference file, 
as determined by exact name matching\nof contigs.  Reads mapped to contigs absent in the new reference 
are dropped. Runs substantially faster if the input is\nan indexed BAM file.

Example:

.. code-tool: none

   java -jar picard.jar ReorderSam \\
       INPUT=sample.bam \\
       OUTPUT=reordered.bam \\
       REFERENCE=reference_with_different_order.fasta
       
Version:4.1.3.0""",
        )
