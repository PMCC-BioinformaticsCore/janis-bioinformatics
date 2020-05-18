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


class GatkCalculateFingerprintMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CalculateFingerprintMetrics"

    def friendly_name(self) -> str:
        return "GATK4: CalculateFingerprintMetrics"

    def tool(self) -> str:
        return "Gatk4CalculateFingerprintMetrics"

    def inputs(self):
        return [
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
                    doc="(-I) One or more input files (SAM/BAM/CRAM or VCF). This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output file to write (Metrics). Required."
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
                tag="calculate_by",
                input_type=Boolean(optional=True),
                prefix="--CALCULATE_BY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Specificies which data-type should be used as the basic unit. Fingerprints from readgroups can be 'rolled-up' to the LIBRARY, SAMPLE, or FILE level before being used. Fingerprints from VCF can be be examined by SAMPLE or FILE.  Default value: READGROUP. Possible values: {FILE, SAMPLE, LIBRARY, READGROUP} "
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
                tag="genotype_lod_threshold",
                input_type=Double(optional=True),
                prefix="--GENOTYPE_LOD_THRESHOLD",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" LOD score threshold for considering a genotype to be definitive.  Default value: 3.0. "
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
                tag="number_of_sampling",
                input_type=Int(optional=True),
                prefix="--NUMBER_OF_SAMPLING",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Number of randomization trials for calculating the DISCRIMINATORY_POWER metric. Default value: 100. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:08:22.703527"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:08:22.703528"),
            documentation="b'USAGE: CalculateFingerprintMetrics [arguments]\nCalculate statistics on fingerprints, checking their viabilityThis tools collects various statistics that pertain to a\nsingle fingerprint (<b>not</b> the comparison, or 'fingerprinting' of two distinct samples) and reports the results in a\nmetrics file. <p>The statistics collected are p-values, where the null-hypothesis is that the fingerprint is collected\nfrom a non-contaminated, diploid human, whose genotypes are modelled by the probabilities given in the HAPLOTYPE_MAP\nfile.<p>Please see the FingerprintMetrics <a\nhref='http://broadinstitute.github.io/picard/picard-metric-definitions.html#FingerprintMetrics'>definitions</a> for a\ncomplete description of the metrics produced by this tool.</p><hr /><p><h3>Example</h3>\n<pre>' +\njava -jar picard.jar CalculateFingerprintMetrics \\\nINPUT=sample.bam \\\nHAPLOTYPE_MAP=fingerprinting_haplotype_database.txt \\\nOUTPUT=sample.fingerprint_metrics\n</pre>\nVersion:4.1.3.0\n",
        )
