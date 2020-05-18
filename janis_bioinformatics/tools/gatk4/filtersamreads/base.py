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


class GatkFilterSamReadsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "FilterSamReads"

    def friendly_name(self) -> str:
        return "GATK4: FilterSamReads"

    def tool(self) -> str:
        return "Gatk4FilterSamReads"

    def inputs(self):
        return [
            ToolInput(
                tag="filter",
                input_type=Boolean(optional=True),
                prefix="--FILTER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Which filter to use. Required. Possible values: { includeAligned (Output aligned reads only. INPUT SAM/BAM must be in queryname SortOrder. (Note: first and second of paired reads must both be aligned to be included in OUTPUT.)) excludeAligned (Output Unmapped reads only. INPUT SAM/BAM must be in queryname SortOrder. (Note: first and second of pair must both be aligned to be excluded from OUTPUT.)) includeReadList (Output reads with names contained in READ_LIST_FILE. See READ_LIST_FILE for more detail.) excludeReadList (Output reads with names *not* contained in READ_LIST_FILE. See READ_LIST_FILE for more detail.) includeJavascript (Output reads that have been accepted by the JAVASCRIPT_FILE script, that is, reads for which the value of the script is true. See the JAVASCRIPT_FILE argument for more detail. ) includePairedIntervals (Output reads that overlap with an interval from INTERVAL_LIST (and their mate). INPUT must be coordinate sorted.) includeTagValues (OUTPUT SAM/BAM will contain reads that have a value of tag TAG that is contained in the values for TAG_VALUES) excludeTagValues (OUTPUT SAM/BAM will contain reads that do not have a value of tag TAG that is contained in the values for TAG_VALUES) } "
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) The SAM or BAM file that will be filtered. Required."
                ),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) SAM or BAM file for resulting reads. Required."
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
                tag="interval_list",
                input_type=File(optional=True),
                prefix="--INTERVAL_LIST",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-IL) Interval List File containing intervals that will be included in the OUTPUT when using FILTER=includePairedIntervals  Default value: null. "
                ),
            ),
            ToolInput(
                tag="javascript_file",
                input_type=File(optional=True),
                prefix="--JAVASCRIPT_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-JS) Filters the INPUT with a javascript expression using the java javascript-engine, when using FILTER=includeJavascript.  The script puts the following variables in the script context:  'record' a SamRecord ( https://samtools.github.io/htsjdk/javadoc/htsjdk/htsjdk/samtools/SAMRecord.html ) and  'header' a SAMFileHeader ( https://samtools.github.io/htsjdk/javadoc/htsjdk/htsjdk/samtools/SAMFileHeader.html ). all the public members of SamRecord and SAMFileHeader are accessible. A record is accepted if the last value of the script evaluates to true.  Default value: null. "
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
                tag="read_list_file",
                input_type=File(optional=True),
                prefix="--READ_LIST_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-RLF) File containing reads that will be included in or excluded from the OUTPUT SAM or BAM file, when using FILTER=includeReadList or FILTER=excludeReadList.  Default value: null. "
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
                tag="sort_order",
                input_type=Boolean(optional=True),
                prefix="--SORT_ORDER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-SO) SortOrder of the OUTPUT file, otherwise use the SortOrder of the INPUT file. Default value: null. Possible values: {unsorted, queryname, coordinate, duplicate, unknown} "
                ),
            ),
            ToolInput(
                tag="tag",
                input_type=String(optional=True),
                prefix="--TAG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-T) The tag to select from input SAM/BAM Default value: null."
                ),
            ),
            ToolInput(
                tag="tag_value",
                input_type=String(optional=True),
                prefix="--TAG_VALUE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-TV) The tag value(s) to filter by This argument may be specified 0 or more times. Default value: null. "
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
                tag="write_reads_files",
                input_type=Boolean(optional=True),
                prefix="--WRITE_READS_FILES",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Create <OUTPUT>.reads file containing names of reads from INPUT and OUTPUT (for debugging purposes.)  Default value: false. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:57:01.072742"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:57:01.072743"),
            documentation="b'USAGE: FilterSamReads [arguments]\nSubsets reads from a SAM or BAM file by applying one of several filters.\nTakes a SAM or BAM file and subsets it by either excluding or only including certain reads such as aligned or unaligned\nreads, specific reads based on a list of reads names, an interval list, by Tag Values (type Z / String values only), or\nusing a JavaScript script.\n<br /><h3>Usage example:</h3><h4>Filter by queryname</h4><pre>java -jar picard.jar FilterSamReads \\<br />      \nI=input.bam \\ <br />       O=output.bam \\ <br />       READ_LIST_FILE=read_names.txt \\ <br />     \nFILTER=includeReadList</pre> <h4>Filter by interval</h4><pre>java -jar picard.jar FilterSamReads \\ <br />      \nI=input.bam \\ <br />       O=output.bam \\ <br />       INTERVAL_LIST=regions.interval_list \\ <br/>     \nFILTER=includePairedIntervals</pre> <h4>Filter by Tag Value (type Z / String values only)</h4><pre>java -jar picard.jar\nFilterSamReads \\ <br />       I=input.bam \\ <br />       O=output.bam \\ <br />       TAG=CR \\ <br/>     \nTAG_VALUE=TTTGTCATCTCGAGTA \\ <br/>      FILTER=includeTagValues</pre> <h4>Filter reads having a soft clip on the\nbeginning of the read larger than 2 bases with a JavaScript script</h4><pre>cat <<EOF > script.js <br/>/** reads having\na soft clip larger than 2 bases in beginning of read*/ <br/>function accept(rec) {   <br/>    if\n(rec.getReadUnmappedFlag()) return false; <br/>    var cigar = rec.getCigar(); <br/>    if (cigar == null) return false;\n<br/>    var ce = cigar.getCigarElement(0); <br/>    return ce.getOperator().name() == 'S' && ce.length() > 2; <br/>}\n<br /><br />accept(record); <br/>EOF <br/><br/>java -jar picard.jar FilterSamReads \\ <br />       I=input.bam \\ <br />  \nO=output.bam \\ <br />       JAVASCRIPT_FILE=script.js \\ <br/>      FILTER=includeJavascript</pre> \nVersion:4.1.3.0\n",
        )
