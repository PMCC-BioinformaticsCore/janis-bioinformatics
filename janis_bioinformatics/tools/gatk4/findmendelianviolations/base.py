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


class GatkFindMendelianViolationsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "FindMendelianViolations"

    def friendly_name(self) -> str:
        return "GATK4: FindMendelianViolations"

    def tool(self) -> str:
        return "Gatk4FindMendelianViolations"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input VCF or BCF with genotypes. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-O) Output metrics file. Required."),
            ),
            ToolInput(
                tag="trios",
                input_type=File(optional=True),
                prefix="--TRIOS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-PED) File of Trio information in PED format (with no genotype columns). Required."
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
                tag="female_chroms",
                input_type=String(optional=True),
                prefix="--FEMALE_CHROMS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="List of possible names for female sex chromosome(s) This argument may be specified 0 or more times. Default value: [chrX, X]. "
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
                tag="male_chroms",
                input_type=String(optional=True),
                prefix="--MALE_CHROMS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="List of possible names for male sex chromosome(s) This argument may be specified 0 or more times. Default value: [chrY, Y]. "
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
                tag="min_dp",
                input_type=Int(optional=True),
                prefix="--MIN_DP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DP) Minimum depth in each sample to consider possible mendelian violations. Default value: 0."
                ),
            ),
            ToolInput(
                tag="min_gq",
                input_type=Int(optional=True),
                prefix="--MIN_GQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-GQ) Minimum genotyping quality (or non-ref likelihood) to perform tests. Default value: 30."
                ),
            ),
            ToolInput(
                tag="min_het_fraction",
                input_type=Double(optional=True),
                prefix="--MIN_HET_FRACTION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MINHET)  Minimum allele balance at sites that are heterozygous in the offspring.  Default value: 0.3. "
                ),
            ),
            ToolInput(
                tag="pseudo_autosomal_regions",
                input_type=String(optional=True),
                prefix="--PSEUDO_AUTOSOMAL_REGIONS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" List of chr:start-end for pseudo-autosomal regions on the female sex chromosome. Defaults to HG19/b37 & HG38 coordinates.  This argument may be specified 0 or more times. Default value: [chrX:10000-2781479, X:10001-2649520, chrX:155701382-156030895, X:59034050-59373566]. "
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
                tag="skip_chroms",
                input_type=String(optional=True),
                prefix="--SKIP_CHROMS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="List of chromosome names to skip entirely. This argument may be specified 0 or more times. Default value: [MT, chrM]. "
                ),
            ),
            ToolInput(
                tag="tab_mode",
                input_type=Boolean(optional=True),
                prefix="--TAB_MODE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true then fields need to be delimited by a single tab. If false the delimiter is one or more whitespace characters. Note that tab mode does not strictly follow the PED spec  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="thread_count",
                input_type=Int(optional=True),
                prefix="--THREAD_COUNT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The number of threads that will be used to collect the metrics. Default value: 1."
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
                tag="vcf_dir",
                input_type=File(optional=True),
                prefix="--VCF_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If provided, output per-family VCFs of mendelian violations into this directory. Default value: null. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:04:34.635691"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:04:34.635692"),
            documentation="b'USAGE: FindMendelianViolations [arguments]\nTakes in VCF or BCF and a pedigree file and looks for high confidence calls where the genotype of the offspring is\nincompatible with the genotypes of the parents.  \nKey features:\n- Checks for regular MVs in diploid regions and invalid transmissions in haploid regions (using the declared gender of\nthe offspring in the pedigree file to determine how to deal with the male and female chromosomes.)\n- Outputs metrics about the different kinds of MVs found.\n- Can output a per-trio VCF with violations; INFO field will indicate the type of violation in the MV field\n<h3>Example</h3>\njava -jar picard.jar FindMendelianViolations\\\nI=input.vcf \\\nTRIO=pedigree.fam \\\nO=report.mendelian_violation_metrics \\\nMIN_DP=20\n<h3>Caveates</h3>\n<h4>Assumptions</h4>\nThe tool assumes the existence of FORMAT fields AD, DP, GT, GQ, and PL. \n<h4>Ignored Variants</h4>\nThis tool ignores variants that are:\n- Not SNPs\n- Filtered\n- Multiallelic (i.e., trio has more than 2 alleles)\n- Within the SKIP_CHROMS contigs\n<h4>PseudoAutosomal Region</h4>\nThis tool assumes that variants in the PAR will be mapped onto the female chromosome, and will treat variants in that\nregion as as autosomal. The mapping to female requires that the PAR in the male chromosome be masked so that the aligner\nmaps reads to single contig. This is normally done for the public releases of the human reference. The tool has default\nvalues for PAR that are sensible for humans on either build b37 or hg38.\nVersion:4.1.3.0\n",
        )
