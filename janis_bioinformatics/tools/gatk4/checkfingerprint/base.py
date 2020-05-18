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


class GatkCheckFingerprintBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CheckFingerprint"

    def friendly_name(self) -> str:
        return "GATK4: CheckFingerprint"

    def tool(self) -> str:
        return "Gatk4CheckFingerprint"

    def inputs(self):
        return [
            ToolInput(
                tag="detail_output",
                input_type=File(optional=True),
                prefix="--DETAIL_OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-D) The text file to which to write detail metrics. Required. Cannot be used in conjuction with argument(s) OUTPUT (O)"
                ),
            ),
            ToolInput(
                tag="genotypes",
                input_type=String(optional=True),
                prefix="--GENOTYPES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-G) File of genotypes (VCF) to be used in comparison. May contain any number of genotypes; CheckFingerprint will use only those that are usable for fingerprinting.  Required. "
                ),
            ),
            ToolInput(
                tag="haplotype_map",
                input_type=File(optional=True),
                prefix="--HAPLOTYPE_MAP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-H) The file lists a set of SNPs, optionally arranged in high-LD blocks, to be used for fingerprinting. See https://software.broadinstitute.org/gatk/documentation/article?id=9526 for details.  Required. "
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=String(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input file SAM/BAM or VCF. If a VCF is used, it must have at least one sample. If there are more than one samples in the VCF, the parameter OBSERVED_SAMPLE_ALIAS must be provided in order to indicate which sample's data to use.  If there are no samples in the VCF, an exception will be thrown.  Required. "
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The base prefix of output files to write. The summary metrics will have the file extension 'fingerprinting_summary_metrics' and the detail metrics will have the extension 'fingerprinting_detail_metrics'.  Required.  Cannot be used in conjuction with argument(s) SUMMARY_OUTPUT (S) DETAIL_OUTPUT (D) SUMMARY_OUTPUT (S) DETAIL_OUTPUT (D)"
                ),
            ),
            ToolInput(
                tag="summary_output",
                input_type=File(optional=True),
                prefix="--SUMMARY_OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-S) The text file to which to write summary metrics. Required. Cannot be used in conjuction with argument(s) OUTPUT (O)"
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
                tag="expected_sample_alias",
                input_type=String(optional=True),
                prefix="--EXPECTED_SAMPLE_ALIAS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-SAMPLE_ALIAS)  This parameter can be used to specify which sample's genotypes to use from the expected VCF file (the GENOTYPES file).  If it is not supplied, the sample name from the input (VCF or BAM read group header) will be used.  Default value: null. "
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
                tag="genotype_lod_threshold",
                input_type=Double(optional=True),
                prefix="--GENOTYPE_LOD_THRESHOLD",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-LOD)  When counting haplotypes checked and matching, count only haplotypes where the most likely haplotype achieves at least this LOD.  Default value: 5.0. "
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
                tag="ignore_read_groups",
                input_type=Boolean(optional=True),
                prefix="--IGNORE_READ_GROUPS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-IGNORE_RG)  If the input is a SAM/BAM, and this parameter is true, treat the entire input BAM as one single read group in the calculation, ignoring RG annotations, and producing a single fingerprint metric for the entire BAM.  Default value: false. Possible values: {true, false} "
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
                tag="observed_sample_alias",
                input_type=Boolean(optional=True),
                prefix="--OBSERVED_SAMPLE_ALIAS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(this)  use.  Default value: null. "),
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:08:34.911133"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:08:34.911134"),
            documentation="b'USAGE: CheckFingerprint [arguments]\nChecks the sample identity of the sequence/genotype data in the provided file (SAM/BAM or VCF) against a set of known\ngenotypes in the supplied genotype file (in VCF format).\n<h3>Summary</h3> Computes a fingerprint (essentially, genotype information from different parts of the genome) from the\nsupplied input file (SAM/BAM or VCF) file and compares it to the expected fingerprint genotypes provided. The key output\nis a LOD score which represents the relative likelihood of the sequence data originating from the same sample as the\ngenotypes vs. from a random sample. <br/> Two outputs are produced: <ol> <li>A summary metrics file that gives metrics\nof the fingerprint matches when comparing the input to a set of genotypes for the expected sample.  At the single sample\nlevel (if the input was a VCF) or at the read level (lane or index within a lane) (if the input was a SAM/BAM) </li>\n<li>A detail metrics file that contains an individual SNP/Haplotype comparison within a fingerprint comparison.</li>\n</ol> The metrics files fill the fields of the classes FingerprintingSummaryMetrics and FingerprintingDetailMetrics. The\noutput files may be specified individually using the SUMMARY_OUTPUT and DETAIL_OUTPUT options. Alternatively the OUTPUT\noption may be used instead to give the base of the two output files, with the summary metrics having a file extension\n'.fingerprinting_summary_metrics', and the detail metrics having a file extension '.fingerprinting_detail_metrics'.\n<br/> <h3>Example comparing a bam against known genotypes:</h3> <pre>     java -jar picard.jar CheckFingerprint \\\nINPUT=sample.bam \\\nGENOTYPES=sample_genotypes.vcf \\\nHAPLOTYPE_MAP=fingerprinting_haplotype_database.txt \\\nOUTPUT=sample_fingerprinting </pre> <br/> <h3>Detailed Explanation</h3>This tool calculates a single number that reports\nthe LOD score for identity check between the INPUT and the GENOTYPES. A positive value indicates that the data seems to\nhave come from the same individual or, in other words the identity checks out. The scale is logarithmic (base 10), so a\nLOD of 6 indicates that it is 1,000,000 more likely that the data matches the genotypes than not. A negative value\nindicates that the data do not match. A score that is near zero is inconclusive and can result from low coverage or\nnon-informative genotypes. \nThe identity check makes use of haplotype blocks defined in the HAPLOTYPE_MAP file to enable it to have higher\nstatistical power for detecting identity or swap by aggregating data from several SNPs in the haplotype block. This\nenables an identity check of samples with very low coverage (e.g. ~1x mean coverage). \nWhen provided a VCF, the identity check looks at the PL, GL and GT fields (in that order) and uses the first one that it\nfinds. \nVersion:4.1.3.0\n",
        )
