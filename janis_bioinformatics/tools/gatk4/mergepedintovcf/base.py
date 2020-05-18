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


class GatkMergePedIntoVcfBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "MergePedIntoVcf"

    def friendly_name(self) -> str:
        return "GATK4: MergePedIntoVcf"

    def tool(self) -> str:
        return "Gatk4MergePedIntoVcf"

    def inputs(self):
        return [
            ToolInput(
                tag="map_file",
                input_type=File(optional=True),
                prefix="--MAP_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MAP) MAP file for the PED file. Required."
                ),
            ),
            ToolInput(
                tag="original_vcf",
                input_type=File(optional=True),
                prefix="--ORIGINAL_VCF",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-VCF) The vcf containing the original autocall genotypes. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output VCF file to write with merged genotype calls. Required."
                ),
            ),
            ToolInput(
                tag="ped_file",
                input_type=File(optional=True),
                prefix="--PED_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PED) PED file to be merged into VCF. Required."
                ),
            ),
            ToolInput(
                tag="zcall_thresholds_file",
                input_type=File(optional=True),
                prefix="--ZCALL_THRESHOLDS_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ZCALL_T_FILE)  The zcall thresholds file.  Required. "
                ),
            ),
            ToolInput(
                tag="zcall_version",
                input_type=String(optional=True),
                prefix="--ZCALL_VERSION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ZCALL_VERSION)  The version of zcall used  Required. "
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
        return []

    def metadata(self):
        return ToolMetadata(
            contributors=[],
            dateCreated=datetime.fromisoformat("2020-05-18T14:52:26.586927"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:52:26.586928"),
            documentation="b'USAGE: MergePedIntoVcf [arguments]\nMergePedIntoVcf takes a single-sample ped file output from zCall and merges into a single-sample vcf file using several\nsupporting files.A VCF, aka Variant Calling Format, is a text file for storing how a sequenced sample differs from the\nreference genome. <a href='https://samtools.github.io/hts-specs/VCFv4.2.pdf'></a>A PED file is a whitespace-separated\ntext file for storing genotype information. <a href='http://zzz.bwh.harvard.edu/plink/data.shtml#ped'></a>A MAP file is\na whitespace-separated text file for storing information about genetic distance. <a\nhref='http://zzz.bwh.harvard.edu/plink/data.shtml#map'></a>A zCall thresholds file is a whitespace-separated text file\nfor storing the thresholds for genotype clustering for a SNP as determined by zCall.<a\nhref='https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3463112/#SEC2title'></a><h4>Usage example:</h4><pre>java -jar\npicard.jar MergePedIntoVcf \\<br />      VCF=input.vcf \\<br />      PED=zcall.output.ped \\<br />     \nMAP=zcall.output.map \\<br />      ZCALL_T_FILE=zcall.thresholds.7.txt \\<br />      OUTPUT=output.vcf <br /></pre>\nVersion:4.1.3.0\n",
        )
