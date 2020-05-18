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


class GatkSamToFastqWithTagsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "SamToFastqWithTags"

    def friendly_name(self) -> str:
        return "GATK4: SamToFastqWithTags"

    def tool(self) -> str:
        return "Gatk4SamToFastqWithTags"

    def inputs(self):
        return [
            ToolInput(
                tag="fastq",
                input_type=File(optional=True),
                prefix="--FASTQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-F) Output FASTQ file (single-end fastq or, if paired, first end of the pair FASTQ). Required.  Cannot be used in conjuction with argument(s) OUTPUT_PER_RG (OPRG) COMPRESS_OUTPUTS_PER_RG (GZOPRG) OUTPUT_DIR (ODIR) OUTPUT_PER_RG (OPRG) COMPRESS_OUTPUTS_PER_RG (GZOPRG)"
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input SAM/BAM file to extract reads from Required."
                ),
            ),
            ToolInput(
                tag="sequence_tag_group",
                input_type=String(optional=True),
                prefix="--SEQUENCE_TAG_GROUP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-STG)  List of comma separated tag values to extract from Input SAM/BAM to be used as read sequence  This argument must be specified at least once. Required. "
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
                tag="clipping_action",
                input_type=String(optional=True),
                prefix="--CLIPPING_ACTION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CLIP_ACT)  The action that should be taken with clipped reads: 'X' means the reads and qualities should be trimmed at the clipped position; 'N' means the bases should be changed to Ns in the clipped region; and any integer means that the base qualities should be set to that value in the clipped region.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="clipping_attribute",
                input_type=String(optional=True),
                prefix="--CLIPPING_ATTRIBUTE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CLIP_ATTR)  The attribute that stores the position at which the SAM record should be clipped  Default value: null. "
                ),
            ),
            ToolInput(
                tag="clipping_min_length",
                input_type=Int(optional=True),
                prefix="--CLIPPING_MIN_LENGTH",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CLIP_MIN)  When performing clipping with the CLIPPING_ATTRIBUTE and CLIPPING_ACTION parameters, ensure that the resulting reads after clipping are at least CLIPPING_MIN_LENGTH bases long. If the original read is shorter than CLIPPING_MIN_LENGTH then the original read length will be maintained.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="compress_outputs_per_rg",
                input_type=Boolean(optional=True),
                prefix="--COMPRESS_OUTPUTS_PER_RG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-GZOPRG)  Compress output FASTQ files per read group using gzip and append a .gz extension to the file names.  Default value: false. Possible values: {true, false}  Cannot be used in conjuction with argument(s) FASTQ (F) SECOND_END_FASTQ (F2) UNPAIRED_FASTQ (FU)"
                ),
            ),
            ToolInput(
                tag="compress_outputs_per_tag_group",
                input_type=Boolean(optional=True),
                prefix="--COMPRESS_OUTPUTS_PER_TAG_GROUP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-GZOPTG)  Compress output FASTQ files per Tag grouping using gzip and append a .gz extension to the file names.  Default value: false. Possible values: {true, false} "
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
                tag="include_non_pf_reads",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_NON_PF_READS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-NON_PF)  Include non-PF reads from the SAM file into the output FASTQ files. PF means 'passes filtering'. Reads whose 'not passing quality controls' flag is set are non-PF reads. See GATK Dictionary for more info.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="include_non_primary_alignments",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_NON_PRIMARY_ALIGNMENTS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If true, include non-primary alignments in the output.  Support of non-primary alignments in SamToFastq is not comprehensive, so there may be exceptions if this is set to true and there are paired reads with non-primary alignments.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="interleave",
                input_type=Boolean(optional=True),
                prefix="--INTERLEAVE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-INTER) Will generate an interleaved fastq if paired, each line will have /1 or /2 to describe which end it came from  Default value: false. Possible values: {true, false} "
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
                tag="output_dir",
                input_type=File(optional=True),
                prefix="--OUTPUT_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ODIR) Directory in which to output the FASTQ file(s). Used only when OUTPUT_PER_RG is true. Default value: null. "
                ),
            ),
            ToolInput(
                tag="output_per_rg",
                input_type=Boolean(optional=True),
                prefix="--OUTPUT_PER_RG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OPRG)  paired).  Default value: false. Possible values: {true, false}  Cannot be used in conjuction with argument(s) FASTQ (F) SECOND_END_FASTQ (F2) UNPAIRED_FASTQ (FU)"
                ),
            ),
            ToolInput(
                tag="quality",
                input_type=Int(optional=True),
                prefix="--QUALITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-Q) End-trim reads using the phred/bwa quality trimming algorithm and this quality. Default value: null. "
                ),
            ),
            ToolInput(
                tag="quality_tag_group",
                input_type=String(optional=True),
                prefix="--QUALITY_TAG_GROUP",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-QTG)  List of comma separated tag values to extract from Input SAM/BAM to be used as read qualities  This argument may be specified 0 or more times. Default value: null. "
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
                tag="re_reverse",
                input_type=Boolean(optional=True),
                prefix="--RE_REVERSE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-RC) Re-reverse bases and qualities of reads with negative strand flag set before writing them to FASTQ  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="read1_max_bases_to_write",
                input_type=Int(optional=True),
                prefix="--READ1_MAX_BASES_TO_WRITE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R1_MAX_BASES)  The maximum number of bases to write from read 1 after trimming. If there are fewer than this many bases left after trimming, all will be written.  If this value is null then all bases left after trimming will be written.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="read1_trim",
                input_type=Boolean(optional=True),
                prefix="--READ1_TRIM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-R1_TRIM) Default value: 0."),
            ),
            ToolInput(
                tag="read2_max_bases_to_write",
                input_type=Int(optional=True),
                prefix="--READ2_MAX_BASES_TO_WRITE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R2_MAX_BASES)  The maximum number of bases to write from read 2 after trimming. If there are fewer than this many bases left after trimming, all will be written.  If this value is null then all bases left after trimming will be written.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="read2_trim",
                input_type=Boolean(optional=True),
                prefix="--READ2_TRIM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-R2_TRIM) Default value: 0."),
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
                tag="rg_tag",
                input_type=String(optional=True),
                prefix="--RG_TAG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-RGT) The read group tag (PU or ID) to be used to output a FASTQ file per read group. Default value: PU. "
                ),
            ),
            ToolInput(
                tag="second_end_fastq",
                input_type=File(optional=True),
                prefix="--SECOND_END_FASTQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-F2) Output FASTQ file (if paired, second end of the pair FASTQ). Default value: null. Cannot be used in conjuction with argument(s) OUTPUT_PER_RG (OPRG) COMPRESS_OUTPUTS_PER_RG (GZOPRG) OUTPUT_PER_RG (OPRG) COMPRESS_OUTPUTS_PER_RG (GZOPRG)"
                ),
            ),
            ToolInput(
                tag="tag_group_seperator",
                input_type=String(optional=True),
                prefix="--TAG_GROUP_SEPERATOR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-SEP)  List of any sequences (e.g. 'AACCTG`) to put in between each comma separated list of sequence tags in each SEQUENCE_TAG_GROUP (STG)  This argument may be specified 0 or more times. Default value: null. "
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
                tag="unpaired_fastq",
                input_type=File(optional=True),
                prefix="--UNPAIRED_FASTQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-FU) Output FASTQ file for unpaired reads; may only be provided in paired-FASTQ mode Default value: null.  Cannot be used in conjuction with argument(s) OUTPUT_PER_RG (OPRG) COMPRESS_OUTPUTS_PER_RG (GZOPRG) OUTPUT_PER_RG (OPRG) COMPRESS_OUTPUTS_PER_RG (GZOPRG)"
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:59:17.268202"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:59:17.268204"),
            documentation="b'USAGE: SamToFastqWithTags [arguments]\nConverts a SAM or BAM file to FASTQ alongside FASTQs created from tags. Extracts read sequences and qualities from the\ninput SAM/BAM file and SAM/BAM tags and writes them into the output file in Sanger FASTQ format. See <a\nhref='http://maq.sourceforge.net/fastq.shtml'>MAQ FASTQ specification</a> for details.<br /> <br />The following example\nwill create two FASTQs from tags.  One will be converted with the base sequence coming from the 'CR' tag and base\nquality from the 'CY' tag.  The other fastq will be converted with the base sequence coming from the 'CB' and 'UR' tags\nconcatenated together with no separator (not specified on command line) with the base qualities coming from the 'CY' and\n'UY' tags concatenated together.  The two files will be named CR.fastq and CB_UR.fastq.<br /><pre>java -jar picard.jar\nSamToFastqWithTags <br />     I=input.bam<br />     FASTQ=output.fastq<br />     SEQUENCE_TAG_GROUP=CR<br />    \nQUALITY_TAG_GROUP=CY<br />     SEQUENCE_TAG_GROUP='CB,UR'<br />     QUALITY_TAG_GROUP='CY,UY'</pre><hr />\nVersion:4.1.3.0\n",
        )
