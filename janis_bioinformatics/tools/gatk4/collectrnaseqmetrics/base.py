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


class GatkCollectRnaSeqMetricsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CollectRnaSeqMetrics"

    def friendly_name(self) -> str:
        return "GATK4: CollectRnaSeqMetrics"

    def tool(self) -> str:
        return "Gatk4CollectRnaSeqMetrics"

    def inputs(self):
        return [
            ToolInput(
                tag="ignore_sequence",
                input_type=String(optional=True),
                prefix="--IGNORE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If a read maps to a sequence specified with this option, all the bases in the read are counted as ignored bases.  These reads are not counted as   This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=File(optional=True),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-I) Input SAM or BAM file. Required."),
            ),
            ToolInput(
                tag="outputFilename",
                input_type=Filename(optional=True),
                prefix="--OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-O) File to write the output to. Required."
                ),
            ),
            ToolInput(
                tag="ref_flat",
                input_type=File(optional=True),
                prefix="--REF_FLAT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Gene annotations in refFlat form. Format described here: http://genome.ucsc.edu/goldenPath/gbdDescriptionsOld.html#RefFlat  Required. "
                ),
            ),
            ToolInput(
                tag="strand_specificity",
                input_type=Boolean(optional=True),
                prefix="--STRAND_SPECIFICITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-STRAND)  For strand-specific library prep. For unpaired reads, use FIRST_READ_TRANSCRIPTION_STRAND if the reads are expected to be on the transcription strand.  Required. Possible values: {NONE, FIRST_READ_TRANSCRIPTION_STRAND, SECOND_READ_TRANSCRIPTION_STRAND} "
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
                tag="assume_sorted",
                input_type=Boolean(optional=True),
                prefix="--ASSUME_SORTED",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-AS) If true (default), then the sort order in the header file will be ignored. Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="chart_output",
                input_type=File(optional=True),
                prefix="--CHART_OUTPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CHART) The PDF file to write out a plot of normalized position vs. coverage. Default value: null. "
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
                tag="metric_accumulation_level",
                input_type=Boolean(optional=True),
                prefix="--METRIC_ACCUMULATION_LEVEL",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-LEVEL)  The level(s) at which to accumulate metrics.    This argument may be specified 0 or more times. Default value: [ALL_READS]. Possible values: {ALL_READS, SAMPLE, LIBRARY, READ_GROUP} "
                ),
            ),
            ToolInput(
                tag="minimum_length",
                input_type=Int(optional=True),
                prefix="--MINIMUM_LENGTH",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When calculating coverage based values (e.g. CV of coverage) only use transcripts of this length or greater.  Default value: 500. "
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
                tag="ribosomal_intervals",
                input_type=File(optional=True),
                prefix="--RIBOSOMAL_INTERVALS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Location of rRNA sequences in genome, in interval_list format. If not specified no bases will be identified as being ribosomal.  Format described <a href='http://samtools.github.io/htsjdk/javadoc/htsjdk/htsjdk/samtools/util/IntervalList.html'>here</a>: Default value: null. "
                ),
            ),
            ToolInput(
                tag="rrna_fragment_percentage",
                input_type=Double(optional=True),
                prefix="--RRNA_FRAGMENT_PERCENTAGE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" This percentage of the length of a fragment must overlap one of the ribosomal intervals for a read or read pair to be considered rRNA.  Default value: 0.8. "
                ),
            ),
            ToolInput(
                tag="stop_after",
                input_type=Boolean(optional=True),
                prefix="--STOP_AFTER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Stop after processing N reads, mainly for debugging. Default value: 0."
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
            dateCreated=datetime.fromisoformat("2020-05-18T14:10:35.239794"),
            dateUpdated=datetime.fromisoformat("2020-05-18T14:10:35.239796"),
            documentation="b'USAGE: CollectRnaSeqMetrics [arguments]\nProduces RNA alignment metrics for a SAM or BAM file.  <p>This tool takes a SAM/BAM file containing the aligned reads\nfrom an RNAseq experiment and produces metrics describing the distribution of the bases within the transcripts.  It\ncalculates the total numbers and the fractions of nucleotides within specific genomic regions including untranslated\nregions (UTRs), introns, intergenic sequences (between discrete genes), and peptide-coding sequences (exons). This tool\nalso determines the numbers of bases that pass quality filters that are specific to Illumina data (PF_BASES).  For more\ninformation please see the corresponding GATK <a\nhref='https://www.broadinstitute.org/gatk/guide/article?id=6329'>Dictionary</a> entry.</p><p>Other metrics include the\nmedian coverage (depth), the ratios of 5 prime /3 prime-biases, and the numbers of reads with the correct/incorrect\nstrand designation. The 5 prime /3 prime-bias results from errors introduced by reverse transcriptase enzymes during\nlibrary construction, ultimately leading to the over-representation of either the 5 prime or 3 prime ends of\ntranscripts.  Please see the CollectRnaSeqMetrics <a\nhref='http://broadinstitute.github.io/picard/picard-metric-definitions.html#RnaSeqMetrics'>definitions</a> for details\non how these biases are calculated. </p><p>The sequence input must be a valid SAM/BAM file containing RNAseq data\naligned by an RNAseq-aware genome aligner such a <a href='http://github.com/alexdobin/STAR'>STAR</a> or <a\nhref='http://ccb.jhu.edu/software/tophat/index.shtml'>TopHat</a>. The tool also requires a REF_FLAT file, a\ntab-delimited file containing information about the location of RNA transcripts, exon start and stop sites, etc. For an\nexample refFlat file for GRCh38, see refFlat.txt.gz at <a\nhref='http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database'>http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database</a>.\nThe first five lines of the tab-limited text file appear as\nfollows.</p><pre>DDX11L1\tNR_046018\tchr1\t+\t11873\t14409\t14409\t14409\t3\t11873,12612,13220,\t12227,12721,14409,WASH7P\tNR_024540\tchr1\t-\t14361\t29370\t29370\t29370\t11\t14361,14969,15795,16606,16857,17232,17605,17914,18267,24737,29320,\t14829,15038,15947,16765,17055,17368,17742,18061,18366,24891,29370,DLGAP2-AS1\tNR_103863\tchr8_KI270926v1_alt\t-\t33083\t35050\t35050\t35050\t3\t33083,33761,35028,\t33281,33899,35050,MIR570\tNR_030296\tchr3\t+\t195699400\t195699497\t195699497\t195699497\t1\t195699400,\t195699497,MIR548A3\tNR_030330\tchr8\t-\t104484368\t104484465\t104484465\t104484465\t1\t104484368,\t104484465,</pre><p>Note:\nMetrics labeled as percentages are actually expressed as fractions!</p><h4>Usage example:</h4><pre>java -jar picard.jar\nCollectRnaSeqMetrics \\<br />      I=input.bam \\<br />      O=output.RNA_Metrics \\<br />      REF_FLAT=ref_flat.txt \\<br\n/>      STRAND=SECOND_READ_TRANSCRIPTION_STRAND \\<br />      RIBOSOMAL_INTERVALS=ribosomal.interval_list</pre>Please see\nthe CollectRnaSeqMetrics <a\nhref='http://broadinstitute.github.io/picard/picard-metric-definitions.html#RnaSeqMetrics'>definitions</a> for a\ncomplete description of the metrics produced by this tool.<hr />\nVersion:4.1.3.0\n",
        )
