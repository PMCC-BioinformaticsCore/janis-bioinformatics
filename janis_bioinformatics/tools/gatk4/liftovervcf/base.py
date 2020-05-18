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


class GatkLiftoverVcfBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "LiftoverVcf"

    def friendly_name(self) -> str:
        return "GATK4: LiftoverVcf"

    def tool(self) -> str:
        return "Gatk4LiftoverVcf"

    def inputs(self):
        return [
            ToolInput(
                tag="chain",
                input_type=File(optional=True),
                prefix="--CHAIN",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-C) The liftover chain file. See https://genome.ucsc.edu/goldenPath/help/chain.html for a description of chain files.  See http://hgdownload.soe.ucsc.edu/downloads.html#terms for where to download chain files.  Required. "
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) The input VCF/BCF file to be lifted over. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output location for the lifted over VCF/BCF. Required."
                ),
            ),
            ToolInput(
                tag="reference_sequence",
                input_type=File(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R) The reference sequence (fasta) for the TARGET genome build (i.e., the new one. The fasta file must have an accompanying sequence dictionary (.dict file).  Required. "
                ),
            ),
            ToolInput(
                tag="reject",
                input_type=File(optional=True),
                prefix="--REJECT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="File to which to write rejected records. Required."
                ),
            ),
            ToolInput(
                tag="allow_missing_fields_in_header",
                input_type=Boolean(optional=True),
                prefix="--ALLOW_MISSING_FIELDS_IN_HEADER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Allow INFO and FORMAT in the records that are not found in the header  Default value: false. Possible values: {true, false} "
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
                tag="disable_sort",
                input_type=Boolean(optional=True),
                prefix="--DISABLE_SORT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Output VCF file will be written on the fly but it won't be sorted and indexed. Default value: false. Possible values: {true, false} "
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
                tag="liftover_min_match",
                input_type=Double(optional=True),
                prefix="--LIFTOVER_MIN_MATCH",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The minimum percent match required for a variant to be lifted. Default value: 1.0."
                ),
            ),
            ToolInput(
                tag="log_failed_intervals",
                input_type=Boolean(optional=True),
                prefix="--LOG_FAILED_INTERVALS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-LFI)  If true, intervals failing due to match below LIFTOVER_MIN_MATCH will be logged as a warning to the console.  Default value: true. Possible values: {true, false} "
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
                tag="recover_swapped_ref_alt",
                input_type=Boolean(optional=True),
                prefix="--RECOVER_SWAPPED_REF_ALT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If the REF allele of the lifted site does not match the target genome, that variant is normally rejected. For bi-allelic SNPs, if this is set to true and the ALT allele equals the new REF allele, the REF and ALT alleles will be swapped.  This can rescue some variants; however, do this carefully as some annotations may become invalid, such as any that are alelle-specifc.  See also TAGS_TO_REVERSE and TAGS_TO_DROP.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="tags_to_drop",
                input_type=String(optional=True),
                prefix="--TAGS_TO_DROP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="INFO field annotations that should be deleted when swapping reference with variant alleles.  This argument may be specified 0 or more times. Default value: [MAX_AF]. "
                ),
            ),
            ToolInput(
                tag="tags_to_reverse",
                input_type=String(optional=True),
                prefix="--TAGS_TO_REVERSE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="INFO field annotations that behave like an Allele Frequency and should be transformed with x->1-x when swapping reference with variant alleles.  This argument may be specified 0 or more times. Default value: [AF]. "
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
                tag="warn_on_missing_contig",
                input_type=Boolean(optional=True),
                prefix="--WARN_ON_MISSING_CONTIG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-WMC)  Warn on missing contig.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="write_original_alleles",
                input_type=Boolean(optional=True),
                prefix="--WRITE_ORIGINAL_ALLELES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Write the original alleles for lifted variants to the INFO field.  If the alleles are identical, this attribute will be omitted.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="write_original_position",
                input_type=Boolean(optional=True),
                prefix="--WRITE_ORIGINAL_POSITION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Write the original contig/position for lifted variants to the INFO field.  Default value: false. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:07:13.344492"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:07:13.344493"),
            documentation="b'USAGE: LiftoverVcf [arguments]\nLifts over a VCF file from one reference build to another.  <h3>Summary</h3>\nTool for 'lifting over' a VCF from one genome build to another, producing a properly headered, sorted and indexed VCF in\none go.\n<h3>Details</h3>\nThis tool adjusts the coordinates of variants within a VCF file to match a new reference. The output file will be sorted\nand indexed using the target reference build. To be clear, REFERENCE_SEQUENCE should be the <em>target</em> reference\nbuild (that is, the 'new' one). The tool is based on the UCSC LiftOver tool (see\nhttp://genome.ucsc.edu/cgi-bin/hgLiftOver) and uses a UCSC chain file to guide its operation.\nFor each variant, the tool will look for the target coordinate, reverse-complement and left-align the variant if needed,\nand, in the case that the reference and alternate alleles of a SNP have been swapped in the new genome build, it will\nadjust the SNP, and correct AF-like INFO fields and the relevant genotypes.\n<h3>Example</h3>\njava -jar picard.jar LiftoverVcf \\\nI=input.vcf \\\nO=lifted_over.vcf \\\nCHAIN=b37tohg38.chain \\\nREJECT=rejected_variants.vcf \\\nR=reference_sequence.fasta\n<h3>Caveats</h3>\n<h4>Rejected Records</h4>\nRecords may be rejected because they cannot be lifted over or because of sequence incompatibilities between the source\nand target reference genomes.  Rejected records will be emitted to the REJECT file using the source genome build\ncoordinates. The reason for the rejection will be stated in the FILTER field, and more detail may be placed in the INFO\nfield.\n<h4>Memory Use</h4>\nLiftOverVcf sorts the output using a 'SortingCollection' which relies on MAX_RECORDS_IN_RAM to specify how many (vcf)\nrecords to hold in memory before 'spilling' to disk. The default value is reasonable when sorting SAM files, but not for\nVCFs as there is no good default due to the dependence on the number of samples and amount of information in the INFO\nand FORMAT fields. Consider lowering to 100,000 or even less if you have many genotypes.\nVersion:4.1.3.0\n",
        )
