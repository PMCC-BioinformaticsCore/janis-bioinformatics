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

from janis_bioinformatics.data_types import Bam, BamBai
from janis_bioinformatics.tools.gatk4.gatk4toolbase import Gatk4ToolBase


class Gatk4AddOrReplaceReadGroupsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "AddOrReplaceReadGroups"

    def friendly_name(self) -> str:
        return "Gatk4: AddOrReplaceReadGroups"

    def tool(self) -> str:
        return "GatkAddOrReplaceReadGroups"

    def inputs(self):
        return [
            super().inputs(),
            ToolInput(
                tag="inp",
                input_type=Bam(),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input file (BAM or SAM or a GA4GH url). Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(prefix=InputSelector("inp"), extension=".bam"),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-O) Output file (BAM or SAM). Required."),
            ),
            ToolInput(
                tag="rglb",
                input_type=String(),
                prefix="--RGLB",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-LB) Read-Group library Required."),
            ),
            ToolInput(
                tag="rgpl",
                input_type=String(),
                prefix="--RGPL",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PL) Read-Group platform (e.g. ILLUMINA, SOLID) Required."
                ),
            ),
            ToolInput(
                tag="rgpu",
                input_type=String(),
                prefix="--RGPU",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PU) Read-Group platform unit (eg. run barcode) Required."
                ),
            ),
            ToolInput(
                tag="rgsm",
                input_type=String(),
                prefix="--RGSM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-SM) Read-Group sample name Required."),
            ),
            ToolInput(
                tag="arguments_file",
                input_type=File(optional=True),
                prefix="--arguments_file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="read one or more arguments files and add them to the command line This argument may be "
                    "specified 0 or more times. Default value: null. "
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
                    doc="Whether to create a BAM index when writing a coordinate-sorted BAM file. "
                    "Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="create_md5_file",
                input_type=Boolean(optional=True),
                prefix="--CREATE_MD5_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to create an MD5 digest for any BAM or FASTQ files created. "
                    "Default value: false. Possible values: {true, false} "
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
                    doc="When writing files that need to be sorted, this will specify the number of records "
                    "stored in RAM before spilling to disk. Increasing this number reduces the number of file "
                    "handles needed to sort the file, and increases the amount of RAM needed.  "
                    "Default value: 500000. "
                ),
            ),
            ToolInput(
                tag="quiet",
                input_type=Boolean(optional=True),
                prefix="--QUIET",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to suppress job-summary info on System.err. "
                    "Default value: false. Possible values: {true, false} "
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
                tag="rgcn",
                input_type=String(optional=True),
                prefix="--RGCN",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CN) Read-Group sequencing center name Default value: null."
                ),
            ),
            ToolInput(
                tag="rgds",
                input_type=String(optional=True),
                prefix="--RGDS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DS) Read-Group description Default value: null."
                ),
            ),
            ToolInput(
                tag="rgdt",
                input_type=Boolean(optional=True),
                prefix="--RGDT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DT) Read-Group run date Default value: null."
                ),
            ),
            ToolInput(
                tag="rgfo",
                input_type=String(optional=True),
                prefix="--RGFO",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-FO) Read-Group flow order Default value: null."
                ),
            ),
            ToolInput(
                tag="rgid",
                input_type=String(optional=True),
                prefix="--RGID",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-ID) Read-Group ID Default value: 1."),
            ),
            ToolInput(
                tag="rgks",
                input_type=String(optional=True),
                prefix="--RGKS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-KS) Read-Group key sequence Default value: null."
                ),
            ),
            ToolInput(
                tag="rgpg",
                input_type=String(optional=True),
                prefix="--RGPG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PG) Read-Group program group Default value: null."
                ),
            ),
            ToolInput(
                tag="rgpi",
                input_type=Int(optional=True),
                prefix="--RGPI",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PI) Read-Group predicted insert size Default value: null."
                ),
            ),
            ToolInput(
                tag="rgpm",
                input_type=String(optional=True),
                prefix="--RGPM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PM) Read-Group platform model Default value: null."
                ),
            ),
            ToolInput(
                tag="sort_order",
                input_type=String(optional=True),
                prefix="--SORT_ORDER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-SO) Optional sort order to output in. If not supplied OUTPUT is in the same order as INPUT. "
                    "Default value: null. Possible values: {unsorted, queryname, coordinate, duplicate, unknown} "
                ),
            ),
            ToolInput(
                tag="tmp_dir",
                input_type=File(optional=True),
                prefix="--TMP_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="One or more directories with space available to be used by this program for temporary storage "
                    "of working files  This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="use_jdk_deflater",
                input_type=Boolean(optional=True),
                prefix="--USE_JDK_DEFLATER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-use_jdk_deflater)  Use the JDK Deflater instead of the Intel Deflater for writing "
                    "compressed output  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="use_jdk_inflater",
                input_type=Boolean(optional=True),
                prefix="--USE_JDK_INFLATER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-use_jdk_inflater)  Use the JDK Inflater instead of the Intel Inflater for reading "
                    "compressed input  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="validation_stringency",
                input_type=String(optional=True),
                prefix="--VALIDATION_STRINGENCY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Validation stringency for all SAM files read by this program.  Setting stringency to "
                    "SILENT can improve performance when processing a BAM file in which variable-length data "
                    "(read, qualities, tags) do not otherwise need to be decoded.  Default value: STRICT. "
                    "Possible values: {STRICT, LENIENT, SILENT} "
                ),
            ),
            ToolInput(
                tag="verbosity",
                input_type=Boolean(optional=True),
                prefix="--VERBOSITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Control verbosity of logging. Default value: INFO. "
                    "Possible values: {ERROR, WARNING, INFO, DEBUG} "
                ),
            ),
            ToolInput(
                tag="version",
                input_type=Boolean(optional=True),
                prefix="--version",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="display the version number for this tool Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="showhidden",
                input_type=Boolean(optional=True),
                prefix="--showHidden",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-showHidden)  display hidden arguments  Default value: false. Possible values: {true, false}"
                ),
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                BamBai(),
                glob=InputSelector("outputFilename"),
                secondaries_present_as={".bai": "^.bai"},
            )
        ]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["illusional"],
            dateCreated=datetime(2020, 5, 15),
            dateUpdated=datetime(2020, 5, 15),
            documentation="""\
USAGE: AddOrReplaceReadGroups [arguments]"
Assigns all the reads in a file to a single new read-group.
This tool accepts INPUT BAM and SAM files or URLs from the <a href='http://ga4gh.org/#/documentation'>Global Alliance
for Genomics and Health (GA4GH)</a>.

Usage example:
++++++++++++++++

.. code-tool: none
   
   java -jar picard.jar AddOrReplaceReadGroups \\
      I=input.bam \\
      O=output.bam \\
      RGID=4 \\
      RGLB=lib1 \\
      RGPL=ILLUMINA \\
      RGPU=unit1 \\
      RGSM=20
      
Caveats
+++++++++

The value of the tags must adhere (according to the 
<ahref='https://samtools.github.io/hts-specs/SAMv1.pdf'>SAM-spec</a>) with the regex 
<code>'^[ -~]+$'</code> (one or more\ncharacters from the ASCII range 32 through 126). 
In particular &lt;Space&gt; is the only non-printing character allowed.
The program enables only the wholesale assignment of all the reads in the INPUT to a 
single read-group. If your file\nalready has reads assigned to multiple read-groups, 
the original RG value will be lost. \nFor more information about read-groups, see the 
<a href='https://www.broadinstitute.org/gatk/guide/article?id=6472'>GATK Dictionary entry.</a>

Version:4.1.3.0""",
        )
