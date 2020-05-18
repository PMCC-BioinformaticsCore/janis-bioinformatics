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


class GatkSplitSamByNumberOfReadsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "SplitSamByNumberOfReads"

    def friendly_name(self) -> str:
        return "GATK4: SplitSamByNumberOfReads"

    def tool(self) -> str:
        return "Gatk4SplitSamByNumberOfReads"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input SAM/BAM file to split Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) Directory in which to output the split BAM files. Required."
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
                tag="out_prefix",
                input_type=String(optional=True),
                prefix="--OUT_PREFIX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OUT_PREFIX)  Output files will be named <OUT_PREFIX>_N.bam, where N enumerates the output file.  Default value: shard. "
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
                tag="split_to_n_files",
                input_type=Int(optional=True),
                prefix="--SPLIT_TO_N_FILES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-N_FILES)  Split to N files.  Default value: 0.  Cannot be used in conjuction with argument(s) SPLIT_TO_N_READS (N_READS)"
                ),
            ),
            ToolInput(
                tag="split_to_n_reads",
                input_type=Int(optional=True),
                prefix="--SPLIT_TO_N_READS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-N_READS)  Split to have approximately N reads per output file. The actual number of reads per output file will vary by no more than the number of output files * (the maximum number of reads with the same queryname - 1).  Default value: 0.  Cannot be used in conjuction with argument(s) SPLIT_TO_N_FILES (N_FILES) SPLIT_TO_N_FILES (N_FILES)"
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
                tag="total_reads_in_input",
                input_type=Boolean(optional=True),
                prefix="--TOTAL_READS_IN_INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-TOTAL_READS)  Total number of reads in the input file. If this is not provided, the input will be read twice, the first time to get a count of the total reads.  Default value: 0. "
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
            dateCreated=datetime.fromisoformat("2020-05-18T15:00:10.291604"),
            dateUpdated=datetime.fromisoformat("2020-05-18T15:00:10.291605"),
            documentation="b'USAGE: SplitSamByNumberOfReads [arguments]\nSplits a SAM or BAM file to multiple BAMs.This tool splits the input query-grouped SAM/BAM file into multiple BAM files\nwhile maintaining the sort order. This can be used to split a large unmapped BAM in order to parallelize alignment. It\nwill traverse the bam twice unless TOTAL_READS_IN_INPUT is provided.<br /><h4>Usage example:</h4><pre>java -jar\npicard.jar SplitSamByNumberOfReads \\<br />     I=paired_unmapped_input.bam \\<br />     OUTPUT=out_dir \\ <br />    \nTOTAL_READS_IN_INPUT=800000000 \\ <br />     SPLIT_TO_N_READS=48000000</pre><hr />\nVersion:4.1.3.0\n",
        )
