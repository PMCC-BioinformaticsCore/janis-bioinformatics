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


class GatkFilterVcfBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "FilterVcf"

    def friendly_name(self) -> str:
        return "GATK4: FilterVcf"

    def tool(self) -> str:
        return "Gatk4FilterVcf"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-I) The INPUT VCF or BCF file. Required."),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-O) The output VCF or BCF. Required."),
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
                    doc="Whether to create a BAM index when writing a coordinate-sorted BAM file. Default value: true. Possible values: {true, false} "
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
                tag="javascript_file",
                input_type=File(optional=True),
                prefix="--JAVASCRIPT_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-JS) Filters a VCF file with a javascript expression interpreted by the java javascript engine. The script puts the following variables in the script context:  'variant' a VariantContext ( https://samtools.github.io/htsjdk/javadoc/htsjdk/htsjdk/variant/variantcontext/VariantContext.html ) and  'header' a VCFHeader ( https://samtools.github.io/htsjdk/javadoc/htsjdk/htsjdk/variant/vcf/VCFHeader.html ). Last value of the script should be a boolean to tell whether we should accept or reject the record.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="max_fs",
                input_type=Double(optional=True),
                prefix="--MAX_FS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The maximum phred scaled fisher strand value before a site will be filtered out. Default value: 1.7976931348623157E308. "
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
                tag="min_ab",
                input_type=Double(optional=True),
                prefix="--MIN_AB",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The minimum allele balance acceptable before filtering a site. Allele balance is calculated for heterozygotes as the number of bases supporting the least-represented allele over the total number of base observations. Different heterozygote genotypes at the same locus are measured independently. The locus is filtered if any allele balance is below the limit.  Default value: 0.0. "
                ),
            ),
            ToolInput(
                tag="min_dp",
                input_type=Int(optional=True),
                prefix="--MIN_DP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The minimum sequencing depth supporting a genotype before the genotype will be filtered out.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="min_gq",
                input_type=Int(optional=True),
                prefix="--MIN_GQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The minimum genotype quality that must be achieved for a sample otherwise the genotype will be filtered out.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="min_qd",
                input_type=Double(optional=True),
                prefix="--MIN_QD",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The minimum QD value to accept or otherwise filter out the variant. Default value: 0.0."
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:06:37.440062"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:06:37.440063"),
            documentation="b'USAGE: FilterVcf [arguments]\nApplies one or more hard filters to a VCF file to filter out genotypes and variants.\nVersion:4.1.3.0\n",
        )
