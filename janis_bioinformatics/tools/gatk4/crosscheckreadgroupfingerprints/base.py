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


class GatkCrosscheckReadGroupFingerprintsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CrosscheckReadGroupFingerprints"

    def friendly_name(self) -> str:
        return "GATK4: CrosscheckReadGroupFingerprints"

    def tool(self) -> str:
        return "Gatk4CrosscheckReadGroupFingerprints"

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
                    doc="(-I) One or more input files (or lists of files) with which to compare fingerprints. This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="allow_duplicate_reads",
                input_type=Boolean(optional=True),
                prefix="--ALLOW_DUPLICATE_READS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Allow the use of duplicate reads in performing the comparison. Can be useful when duplicate marking has been overly aggressive and coverage is low.  Default value: false. Possible values: {true, false} "
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
                tag="calculate_tumor_aware_results",
                input_type=Boolean(optional=True),
                prefix="--CALCULATE_TUMOR_AWARE_RESULTS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" specifies whether the Tumor-aware result should be calculated. These are time consuming and can roughly double the runtime of the tool. When crosschecking many groups not calculating the tumor-aware  results can result in a significant speedup.  Default value: true. Possible values: {true, false} "
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
                tag="crosscheck_by",
                input_type=Boolean(optional=True),
                prefix="--CROSSCHECK_BY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Specificies which data-type should be used as the basic comparison unit. Fingerprints from readgroups can be 'rolled-up' to the LIBRARY, SAMPLE, or FILE level before being compared. Fingerprints from VCF can be be compared by SAMPLE or FILE.  Default value: READGROUP. Possible values: {FILE, SAMPLE, LIBRARY, READGROUP} "
                ),
            ),
            ToolInput(
                tag="crosscheck_libraries",
                input_type=String(optional=True),
                prefix="--CROSSCHECK_LIBRARIES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(roll)  library level and print out a library x library matrix with LOD scores.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="crosscheck_mode",
                input_type=Boolean(optional=True),
                prefix="--CROSSCHECK_MODE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" An argument that controls how crosschecking with both INPUT and SECOND_INPUT should occur. Default value: CHECK_SAME_SAMPLE. Possible values: { CHECK_SAME_SAMPLE (In this mode, each sample in INPUT will only be checked against a single corresponding sample in SECOND_INPUT. If a corresponding sample cannot be found, the program will proceed, but report the missing samples and return the value specified in EXIT_CODE_WHEN_MISMATCH. The corresponding samples are those that equal each other, after possible renaming via INPUT_SAMPLE_MAP and SECOND_INPUT_SAMPLE_MAP. In this mode CROSSCHECK_BY must be SAMPLE.) CHECK_ALL_OTHERS (In this mode, each sample in INPUT will be checked against all the samples in SECOND_INPUT.) } "
                ),
            ),
            ToolInput(
                tag="crosscheck_samples",
                input_type=Boolean(optional=True),
                prefix="--CROSSCHECK_SAMPLES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Instead of producing the normal comparison of read-groups, roll fingerprints up to the sample level and print out a sample x sample matrix with LOD scores.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="exit_code_when_mismatch",
                input_type=Int(optional=True),
                prefix="--EXIT_CODE_WHEN_MISMATCH",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" When one or more mismatches between groups is detected, exit with this value instead of 0. Default value: 1. "
                ),
            ),
            ToolInput(
                tag="exit_code_when_no_valid_checks",
                input_type=Int(optional=True),
                prefix="--EXIT_CODE_WHEN_NO_VALID_CHECKS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" When all LOD score are zero, exit with this value.  Default value: 1. "
                ),
            ),
            ToolInput(
                tag="expect_all_groups_to_match",
                input_type=Boolean(optional=True),
                prefix="--EXPECT_ALL_GROUPS_TO_MATCH",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Expect all groups' fingerprints to match, irrespective of their sample names.  By default (with this value set to false), groups (readgroups, libraries, files, or samples) with different sample names are expected to mismatch, and those with the same sample name are expected to match.   Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="expect_all_read_groups_to_match",
                input_type=Boolean(optional=True),
                prefix="--EXPECT_ALL_READ_GROUPS_TO_MATCH",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Expect all read groups' fingerprints to match, irrespective of their sample names.  By default (with this value set to false), read groups with different sample names are expected to mismatch, and those with the same sample name are expected to match.  Default value: false. Possible values: {true, false}  Cannot be used in conjuction with argument(s) EXPECT_ALL_GROUPS_TO_MATCH"
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
                tag="genotyping_error_rate",
                input_type=Boolean(optional=True),
                prefix="--GENOTYPING_ERROR_RATE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" comes from the expected sample. Must be greater than zero.   Default value: 0.01. "
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
                tag="input_sample_map",
                input_type=File(optional=True),
                prefix="--INPUT_SAMPLE_MAP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="A tsv with two columns representing the sample as it appears in the INPUT data (in column 1) and the sample as it should be used for comparisons to SECOND_INPUT (in the second column). Need only include the samples that change. Values in column 1 should be unique. Values in column 2 should be unique even in union with the remaining unmapped samples. Should only be used with SECOND_INPUT.   Default value: null. "
                ),
            ),
            ToolInput(
                tag="lod_threshold",
                input_type=Double(optional=True),
                prefix="--LOD_THRESHOLD",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-LOD) If any two groups (with the same sample name) match with a LOD score lower than the threshold the tool will exit with a non-zero code to indicate error. Program will also exit with an error if it finds two groups with different sample name that match with a LOD score greater than -LOD_THRESHOLD."
                ),
            ),
            ToolInput(
                tag="loss_of_het_rate",
                input_type=Double(optional=True),
                prefix="--LOSS_OF_HET_RATE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The rate at which a heterozygous genotype in a normal sample turns into a homozygous (via loss of heterozygosity) in the tumor (model assumes independent events, so this needs to be larger than reality).  Default value: 0.5. "
                ),
            ),
            ToolInput(
                tag="matrix_output",
                input_type=File(optional=True),
                prefix="--MATRIX_OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-MO) Optional output file to write matrix of LOD scores to. This is less informative than the metrics output and only contains Normal-Normal LOD score (i.e. doesn't account for Loss of Heterozygosity). It is however sometimes easier to use visually.  Default value: null.  Cannot be used in conjuction with argument(s) SECOND_INPUT (SI)"
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
                tag="num_threads",
                input_type=Int(optional=True),
                prefix="--NUM_THREADS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The number of threads to use to process files and generate fingerprints. Default value: 1. "
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Optional output file to write metrics to. Default is to write to stdout. Default value: null. "
                ),
            ),
            ToolInput(
                tag="output_errors_only",
                input_type=Boolean(optional=True),
                prefix="--OUTPUT_ERRORS_ONLY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true then only groups that do not relate to each other as expected will have their LODs reported.  Default value: false. Possible values: {true, false} "
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
                tag="second_input",
                input_type=String(optional=True),
                prefix="--SECOND_INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-SI) A second set of input files (or lists of files) with which to compare fingerprints. If this option is provided the tool compares each sample in INPUT with the sample from SECOND_INPUT that has the same sample ID. In addition, data will be grouped by SAMPLE regardless of the value of CROSSCHECK_BY. When operating in this mode, each sample in INPUT must also have a corresponding sample in SECOND_INPUT. If this is violated, the tool will proceed to check the matching samples, but report the missing samples and return a non-zero error-code.  This argument may be specified 0 or more times. Default value: null. Cannot be used in conjuction with argument(s) MATRIX_OUTPUT (MO) MATRIX_OUTPUT (MO)"
                ),
            ),
            ToolInput(
                tag="second_input_sample_map",
                input_type=Boolean(optional=True),
                prefix="--SECOND_INPUT_SAMPLE_MAP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" column 1) and the sample as it should be used for comparisons to INPUT (in the second column). Need only include the samples that change. Values in column 1 should be unique. Values in column 2 should be unique even in union with the remaining unmapped samples. Should only be used with SECOND_INPUT.   Default value: null. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:12:01.575640"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:12:01.575641"),
            documentation="b'USAGE: CrosscheckReadGroupFingerprints [arguments]\nDEPRECATED: USE CrosscheckFingerprints.\nVersion:4.1.3.0\n",
        )
