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


class GatkBedToIntervalListBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "BedToIntervalList"

    def friendly_name(self) -> str:
        return "GATK4: BedToIntervalList"

    def tool(self) -> str:
        return "Gatk4BedToIntervalList"

    def inputs(self):
        return [
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-I) The input BED file Required."),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) The output Picard Interval List Required."
                ),
            ),
            ToolInput(
                tag="sequence_dictionary",
                input_type=Boolean(optional=True),
                prefix="--SEQUENCE_DICTIONARY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-SD, or)  Required. "),
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
                tag="sort",
                input_type=Boolean(optional=True),
                prefix="--SORT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true, sort the output interval list before writing it. Default value: true. Possible values: {true, false} "
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
                    doc="If true, unique the output interval list by merging overlapping regions, before writing it (implies sort=true).  Default value: false. Possible values: {true, false} "
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:52:37.528649"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:52:37.528650"),
            documentation="b'USAGE: BedToIntervalList [arguments]\nConverts a BED file to a Picard Interval List.  This tool provides easy conversion from BED to the Picard interval_list\nformat which is required by many Picard processing tools. Note that the coordinate system of BED files is such that the\nfirst base or position in a sequence is numbered '0', while in interval_list files it is numbered '1'.<br /><br />BED\nfiles contain sequence data displayed in a flexible format that includes nine optional fields, in addition to three\nrequired fields within the annotation tracks. The required fields of a BED file include:<pre>     chrom - The name of\nthe chromosome (e.g. chr20) or scaffold (e.g. scaffold10671) <br />     chromStart - The starting position of the\nfeature in the chromosome or scaffold. The first base in a chromosome is numbered '0' <br />     chromEnd - The ending\nposition of the feature in the chromosome or scaffold.  The chromEnd base is not included in the display of the feature.\nFor example, the first 100 bases of a chromosome are defined as chromStart=0, chromEnd=100, and span the bases numbered\n0-99.</pre>In each annotation track, the number of fields per line must be consistent throughout a data set. For\nadditional information regarding BED files and the annotation field options, please see:\nhttp://genome.ucsc.edu/FAQ/FAQformat.html#format1.<br /> <br /> Interval_list files contain sequence data distributed\ninto intervals. The interval_list file format is relatively simple and reflects the SAM alignment format to a degree.  A\nSAM style header must be present in the file that lists the sequence records against which the intervals are described. \nAfter the header, the file then contains records, one per line in plain text format with the following values\ntab-separated::<pre>      -Sequence name (SN) - The name of the sequence in the file for identification purposes, can be\nchromosome number e.g. chr20 <br />      -Start position - Interval start position (starts at +1) <br />      -End\nposition - Interval end position (1-based, end inclusive) <br />      -Strand - Indicates +/- strand for the interval\n(either + or -) <br />      -Interval name - (Each interval should have a unique name) </pre><br/>This tool requires a\nsequence dictionary, provided with the SEQUENCE_DICTIONARY or SD argument. The value given to this argument can be any\nof the following:<pre>    - A file with .dict extension generated using Picard's CreateSequenceDictionaryTool</br>    -\nA reference.fa or reference.fasta file with a reference.dict in the same directory</br>    - Another IntervalList with\n@SQ lines in the header from which to generate a dictionary</br>    - A VCF that contains #contig lines from which to\ngenerate a sequence dictionary</br>    - A SAM or BAM file with @SQ lines in the header from which to generate a\ndictionary</br></pre><h4>Usage example:</h4><pre>java -jar picard.jar BedToIntervalList \\<br />      I=input.bed \\<br />\nO=list.interval_list \\<br />      SD=reference_sequence.dict</pre><br /> <br /> <hr />\nVersion:4.1.3.0\n",
        )
