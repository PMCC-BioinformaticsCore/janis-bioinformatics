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


class GatkGtcToVcfBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "GtcToVcf"

    def friendly_name(self) -> str:
        return "GATK4: GtcToVcf"

    def tool(self) -> str:
        return "Gatk4GtcToVcf"

    def inputs(self):
        return [
            ToolInput(
                tag="cluster_file",
                input_type=File(optional=True),
                prefix="--CLUSTER_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CF) An Illumina cluster file (egt) Required."
                ),
            ),
            ToolInput(
                tag="extended_illumina_manifest",
                input_type=File(optional=True),
                prefix="--EXTENDED_ILLUMINA_MANIFEST",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MANIFEST)  An Extended Illumina Manifest file (csv).  This is an extended version of the Illumina manifest it contains additional reference-specific fields  Required. "
                ),
            ),
            ToolInput(
                tag="illumina_normalization_manifest",
                input_type=File(optional=True),
                prefix="--ILLUMINA_NORMALIZATION_MANIFEST",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-NORM_MANIFEST)  An Illumina bead pool manifest (a manifest containing the Illumina normalization ids) (bpm.csv)  Required. "
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-I) GTC file to be converted Required."),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output VCF file to write. Required."
                ),
            ),
            ToolInput(
                tag="reference_sequence",
                input_type=File(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-R) Reference sequence file. Required."),
            ),
            ToolInput(
                tag="sample_alias",
                input_type=String(optional=True),
                prefix="--SAMPLE_ALIAS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="The sample alias Required."),
            ),
            ToolInput(
                tag="analysis_version_number",
                input_type=Int(optional=True),
                prefix="--ANALYSIS_VERSION_NUMBER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" The analysis version of the data used to generate this VCF  Default value: null. "
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
                tag="do_not_allow_calls_on_zeroed_out_assays",
                input_type=Boolean(optional=True),
                prefix="--DO_NOT_ALLOW_CALLS_ON_ZEROED_OUT_ASSAYS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Causes the program to fail if it finds a case where there is a call on an assay that is flagged as 'zeroed-out' in the Illumina cluster file.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="expected_gender",
                input_type=String(optional=True),
                prefix="--EXPECTED_GENDER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-E_GENDER)  The expected gender for this sample.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="fingerprint_genotypes_vcf_file",
                input_type=File(optional=True),
                prefix="--FINGERPRINT_GENOTYPES_VCF_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-FP_VCF)  The fingerprint VCF for this sample  Default value: null. "
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
                tag="gender_gtc",
                input_type=File(optional=True),
                prefix="--GENDER_GTC",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-G_GTC) An optional GTC file that was generated by calling the chip using a cluster file designed to optimize gender calling.  Default value: null. "
                ),
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
        return []

    def metadata(self):
        return ToolMetadata(
            contributors=[],
            dateCreated=datetime.fromisoformat("2020-05-18T14:52:21.028217"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:52:21.028218"),
            documentation="b'USAGE: GtcToVcf [arguments]\nGtcToVcf takes an Illumina GTC file and converts it to a VCF file using several supporting files. A GTC file is an\nIllumina-specific file containing called genotypes in AA/AB/BB format. <a\nhref='https://github.com/Illumina/BeadArrayFiles/blob/develop/docs/GTC_File_Format_v5.pdf'></a> A VCF, aka Variant\nCalling Format, is a text file for storing how a sequenced sample differs from the reference genome. <a\nhref='http://software.broadinstitute.org/software/igv/book/export/html/184'></a><h4>Usage example:</h4><pre>java -jar\npicard.jar GtcToVcf \\<br />      INPUT=input.gtc \\<br />      REFERENCE_SEQUENCE=reference.fasta \\<br />     \nOUTPUT=output.vcf \\<br />      EXTENDED_ILLUMINA_MANIFEST=chip_name.extended.csv \\<br />      CLUSTER_FILE=chip_name.egt\n\\<br />      ILLUMINA_NORMALIZATION_MANIFEST=chip_name.bpm.csv \\<br />      SAMPLE_ALIAS=my_sample_alias \\<br /></pre>\nVersion:4.1.3.0\n",
        )
