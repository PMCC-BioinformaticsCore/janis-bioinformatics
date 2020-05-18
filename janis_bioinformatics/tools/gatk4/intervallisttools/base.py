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


class GatkIntervalListToolsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "IntervalListTools"

    def friendly_name(self) -> str:
        return "GATK4: IntervalListTools"

    def tool(self) -> str:
        return "Gatk4IntervalListTools"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) One or more interval lists. If multiple interval lists are provided the output is theresult of merging the inputs. Supported formats are interval_list and VCF.  This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="action",
                input_type=Boolean(optional=True),
                prefix="--ACTION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Action to take on inputs. Default value: CONCAT. Possible values: { CONCAT (The concatenation of all the intervals in all the INPUTs, no sorting or merging of overlapping/abutting intervals implied. Will result in a possibly unsorted list unless requested otherwise.) UNION (Like CONCATENATE but with UNIQUE and SORT implied, the result being the set-wise union of all INPUTS, with overlapping and abutting intervals merged into one.) INTERSECT (The sorted and merged set of all loci that are contained in all of the INPUTs.) SUBTRACT (Subtracts the intervals in SECOND_INPUT from those in INPUT. The resulting loci are those in INPUT that are not in SECOND_INPUT.) SYMDIFF (Results in loci that are in INPUT or SECOND_INPUT but are not in both.) OVERLAPS (Outputs the entire intervals from INPUT that have bases which overlap any interval from SECOND_INPUT. Note that this is different than INTERSECT in that each original interval is either emitted in its entirety, or not at all.) } "
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
                tag="break_bands_at_multiples_of",
                input_type=Int(optional=True),
                prefix="--BREAK_BANDS_AT_MULTIPLES_OF",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-BRK)  If set to a positive value will create a new interval list with the original intervals broken up at integer multiples of this value. Set to 0 to NOT break up intervals.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="comment",
                input_type=String(optional=True),
                prefix="--COMMENT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="One or more lines of comment to add to the header of the output file (as @CO lines in the SAM header).  This argument may be specified 0 or more times. Default value: null. "
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
                tag="count_output",
                input_type=File(optional=True),
                prefix="--COUNT_OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="File to which to print count of bases or intervals in final output interval list. When not set, value indicated by OUTPUT_VALUE will be printed to stdout.  If this parameter is set, OUTPUT_VALUE must not be NONE.  Default value: null. "
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
                tag="include_filtered",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_FILTERED",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to include filtered variants in the vcf when generating an interval list from vcf. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="invert",
                input_type=Boolean(optional=True),
                prefix="--INVERT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Produce the inverse list of intervals, that is, the regions in the genome that are <br>not</br> covered by any of the input intervals. Will merge abutting intervals first. Output will be sorted.  Default value: false. Possible values: {true, false} "
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
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output interval list file to write (if SCATTER_COUNT == 1) or the directory into which to write the scattered interval sub-directories (if SCATTER_COUNT > 1).  Default value: null. "
                ),
            ),
            ToolInput(
                tag="output_value",
                input_type=Boolean(optional=True),
                prefix="--OUTPUT_VALUE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="What value to output to COUNT_OUTPUT file or stdout (for scripting). If COUNT_OUTPUT is provided, this parameter must not be NONE.  Default value: NONE. Possible values: {NONE, BASES, INTERVALS} "
                ),
            ),
            ToolInput(
                tag="padding",
                input_type=Int(optional=True),
                prefix="--PADDING",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The amount to pad each end of the intervals by before other operations are undertaken. Negative numbers are allowed and indicate intervals should be shrunk. Resulting intervals < 0 bases long will be removed. Padding is applied to the interval lists (both INPUT and SECOND_INPUT, if provided) <b> before </b> the ACTION is performed.  Default value: 0. "
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
                tag="scatter_content",
                input_type=Int(optional=True),
                prefix="--SCATTER_CONTENT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When scattering with this argument, each of the resultant files will (ideally) have this amount of 'content', which  means either base-counts or interval-counts depending on SUBDIVISION_MODE. When provided, overrides SCATTER_COUNT  Default value: null. "
                ),
            ),
            ToolInput(
                tag="scatter_count",
                input_type=Int(optional=True),
                prefix="--SCATTER_COUNT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The number of files into which to scatter the resulting list by locus; in some situations, fewer intervals may be emitted.    Default value: 1. "
                ),
            ),
            ToolInput(
                tag="second_input",
                input_type=File(optional=True),
                prefix="--SECOND_INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-SI) Second set of intervals for SUBTRACT and DIFFERENCE operations. This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="sort",
                input_type=Boolean(optional=True),
                prefix="--SORT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true, sort the resulting interval list by coordinate. Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="subdivision_mode",
                input_type=String(optional=True),
                prefix="--SUBDIVISION_MODE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-M)  The mode used to scatter the interval list.  Default value: INTERVAL_SUBDIVISION. Possible values: { INTERVAL_SUBDIVISION (Scatter the interval list into similarly sized interval lists (by base count), breaking up intervals as needed.) BALANCING_WITHOUT_INTERVAL_SUBDIVISION (Scatter the interval list into similarly sized interval lists (by base count), but without breaking up intervals.) BALANCING_WITHOUT_INTERVAL_SUBDIVISION_WITH_OVERFLOW (Scatter the interval list into similarly sized interval lists (by base count), but without breaking up intervals. Will overflow current interval list so that the remaining lists will not have too many bases to deal with.) INTERVAL_COUNT (Scatter the interval list into similarly sized interval lists (by interval count, not by base count). Resulting interval lists will contain similar number of intervals.) } "
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
                tag="unique",
                input_type=Boolean(optional=True),
                prefix="--UNIQUE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true, merge overlapping and adjacent intervals to create a list of unique intervals. Implies SORT=true.  Default value: false. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:53:39.060851"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:53:39.060851"),
            documentation="b'USAGE: IntervalListTools [arguments]\nA tool for performing various IntervalList manipulations <h3>Summary</h3>This tool offers multiple interval list file\nmanipulation capabilities, including: sorting, merging, subtracting, padding, and other set-theoretic operations. The\ndefault action is to merge and sort the intervals provided in the INPUTs. Other options, e.g. interval subtraction, are\ncontrolled by the arguments.<br />Both IntervalList and VCF files are accepted as input. IntervalList should be denoted\nwith the extension .interval_list, while a VCF must have one of .vcf, .vcf.gz, .bcf When VCF file is used as input, each\nvariant is translated into an using its reference allele or the END INFO annotation (if present) to determine the extent\nof the interval. \nIntervalListTools can also 'scatter' the resulting interval-list into many interval-files. This can be useful for\ncreating multiple interval lists for scattering an analysis over.\n<h3>Details</h3> The IntervalList file format is designed to help the users avoid mixing references when supplying\nintervals and other genomic data to a single tool. A SAM style header must be present at the top of the file. After the\nheader, the file then contains records, one per line in text format with the followingvalues tab-separated: \n- Sequence name (SN) \n- Start position (1-based)\n- End position (1-based, inclusive)\n- Strand (either + or -)\n- Interval name (ideally unique names for intervals)\nThe coordinate system is 1-based, closed-ended so that the first base in a sequence has position 1, and both the start\nand the end positions are included in an interval.\nExample interval list file<pre>@HD\tVN:1.0\n@SQ\tSN:chr1\tLN:501\n@SQ\tSN:chr2\tLN:401\nchr1\t1\t100\t+\tstarts at the first base of the contig and covers 100 bases\nchr2\t100\t100\t+\tinterval with exactly one base\n</pre>\n<h3>Usage Examples</h3><h4>1. Combine the intervals from two interval lists:</h4><pre>java -jar picard.jar\nIntervalListTools \\\nACTION=CONCAT \\\nI=input.interval_list \\\nI=input_2.interval_list \\\nO=new.interval_list</pre> <h4>2. Combine the intervals from two interval lists, sorting the resulting in list and\nmerging overlapping and abutting intervals:</h4> <pre> java -jar picard.jar IntervalListTools \\\nACTION=CONCAT \\\nSORT=true \\\nUNIQUE=true \\\nI=input.interval_list \\\nI=input_2.interval_list \\\nO=new.interval_list </pre> <h4>3. Subtract the intervals in SECOND_INPUT from those in INPUT</h4> <pre> java -jar\npicard.jar IntervalListTools \\\nACTION=SUBTRACT \\\nI=input.interval_list \\\nSI=input_2.interval_list \\\nO=new.interval_list </pre> <h4>4. Find bases that are in either input1.interval_list or input2.interval_list, and also\nin input3.interval_list:</h4> <pre> java -jar picard.jar IntervalListTools \\\nACTION=INTERSECT \\\nI=input1.interval_list \\\nI=input2.interval_list \\\nSI=input3.interval_list \\\nO=new.interval_list </pre>\nVersion:4.1.3.0\n",
        )
