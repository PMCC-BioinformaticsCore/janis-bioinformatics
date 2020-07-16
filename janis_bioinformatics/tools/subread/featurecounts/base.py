from abc import ABC

from janis_unix import TextFile
from janis_core import (
    ToolInput,
    Int,
    Boolean,
    ToolOutput,
    Array,
    Stdout,
    InputSelector,
    Filename,
    File,
    String,
    Float,
)
from janis_core import ToolMetadata
from janis_bioinformatics.data_types import Bam
from janis_bioinformatics.tools.subread.subreadtoolbase import SubreadToolBase


class featureCountsBase(SubreadToolBase, ABC):
    def tool(self):
        return "featureCounts"

    @classmethod
    def subread_command(cls):
        return "featureCounts"

    def inputs(self):
        return [
            *self.additional_inputs,
            ToolInput(
                "bam",
                Array(Bam),
                position=10,
                doc="A list of SAM or BAM format files. They can be either name or location sorted. If no files provided, <stdin> input is expected. Location-sorted paired-end reads are automatically sorted by read names.",
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".txt"),
                prefix="-o",
                doc="Name of output file including read counts. A separate file including summary statistics of counting results is also included in the output ('<string>.summary'). Both files are in tab delimited format.",
            ),
            ToolInput(
                "annotationFile",
                File,
                prefix="-a",
                doc="Name of an annotation file. GTF/GFF format by default. See -F option for more format information. Inbuilt annotations (SAF format) is available in 'annotation' directory of the package. Gzipped file is also accepted.",
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", TextFile, glob=InputSelector("outputFilename"))]

    def friendly_name(self):
        return "featureCounts"

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=date(2020, 7, 16),
            dateUpdated=date(2020, 7, 16),
            institution="Walter and Eliza Hall Institute of Medical Research",
            doi=None,
            citation=None,
            keywords=["subread", "featureCounts"],
            documentationUrl="https://www.rdocumentation.org/packages/Rsubread/versions/1.22.2/topics/featureCounts",
            documentation="""FeatureCounts: A General-Purpose Read Summarization Function
This function assigns mapped sequencing reads to genomic features""".strip(),
        )

    additional_inputs = [
        ToolInput(
            "format",
            String(optional=True),
            prefix="-F",
            doc="Specify format of the provided annotation file. Acceptable formats include 'GTF' (or compatible GFF format) and 'SAF'. 'GTF' by default.  For SAF format, please refer to Users Guide.",
        ),
        ToolInput(
            "featureType",
            Array(String(), optional=True),
            prefix="-t",
            separator=",",
            doc="Specify feature type(s) in a GTF annotation. If multiple types are provided, they should be separated by ',' with no space in between. 'exon' by default. Rows in the annotation with a matched feature will be extracted and used for read mapping.",
        ),
        ToolInput(
            "attributeType",
            String(optional=True),
            prefix="-g",
            doc="Specify attribute type in GTF annotation. 'gene_id' by default. Meta-features used for read counting will be extracted from annotation using the provided value.",
        ),
        ToolInput(
            "extraAttributes",
            Array(String(), optional=True),
            separator=",",
            prefix="--extraAttributes",
            doc="Extract extra attribute types from the provided GTF annotation and include them in the counting output. These attribute types will not be used to group features. If more than one attribute type is provided they should be separated by comma.",
        ),
        ToolInput(
            "chromsomeAlias",
            String(optional=True),
            prefix="-A",
            doc="Provide a chromosome name alias file to match chr names inannotation with those in the reads. This should be a two-column comma-delimited text file. Its first column should include chr names in the annotation and its second column should include chr names in the reads. Chr names are case sensitive. No column header should be included in the file.",
        ),
        ToolInput(
            "featureLevel",
            Boolean(optional=True),
            prefix="-f",
            doc="Perform read counting at feature level (eg. counting reads for exons rather than genes).",
        ),
        ToolInput(
            "overlap",
            Boolean(optional=True),
            prefix="-O",
            doc="Assign reads to all their overlapping meta-features (or features if -f is specified).",
        ),
        ToolInput(
            "minOverlap",
            Int(optional=True),
            prefix="--minOverlap",
            doc="Minimum number of overlapping bases in a read that isrequired for read assignment. 1 by default. Number ofoverlapping bases is counted from both reads if pairedend. If a negative value is provided, then a gap of upto specified size will be allowed between read and the feature that the read is assigned to.",
        ),
        ToolInput(
            "fracOverlap",
            Float(optional=True),
            prefix="--fracOverlap",
            doc="Minimum fraction of overlapping bases in a read that isrequired for read assignment. Value should be within range [0,1]. 0 by default. Number of overlapping bases is counted from both reads if paired end. Both this option and '--minOverlap' option need to be satisfied for read assignment.",
        ),
        ToolInput(
            "fracOverlapFeature",
            Float(optional=True),
            prefix="--fracOverlapFeature",
            doc="Minimum fraction of overlapping bases in a feature that is required for read assignment. Value should be within range [0,1]. 0 by default.",
        ),
        ToolInput(
            "largestOverlap",
            Boolean(optional=True),
            prefix="--largestOverlap",
            doc="Assign reads to a meta-feature/feature that has the  largest number of overlapping bases.",
        ),
        ToolInput(
            "nonOverlap",
            Int(optional=True),
            prefix="--nonOverlap",
            doc="Maximum number of non-overlapping bases in a read (or a read pair) that is allowed when being assigned to a feature. No limit is set by default.",
        ),
        ToolInput(
            "nonOverlapFeature",
            Int(optional=True),
            prefix="--nonOverlapFeature",
            doc="Maximum number of non-overlapping bases in a feature that is allowed in read assignment. No limit is set by default.",
        ),
        ToolInput(
            "readExtensionFive",
            Int(optional=True),
            prefix="--readExtension5",
            doc="Reads are extended upstream by <int> bases from their 5' end.",
        ),
        ToolInput(
            "readExtensionThree",
            String(optional=True),
            prefix="--readExtension3",
            doc="Reads are extended upstream by <int> bases from their 3' end.",
        ),
        ToolInput(
            "readToPos",
            String(optional=True),
            prefix="--read2pos",
            doc="Reduce reads to their 5' most base or 3' most base. Read counting is then performed based on the single base the read is reduced to.",
        ),
        ToolInput(
            "multiMapping",
            Boolean(optional=True),
            prefix="-M",
            doc="Multi-mapping reads will also be counted. For a multi-mapping read, all its reported alignments will be counted. The 'NH' tag in BAM/SAM input is used to detect multi-mapping reads.",
        ),
        ToolInput(
            "fration",
            Boolean(optional=True),
            prefix="--fraction",
            doc="Assign fractional counts to features. This option must be used together with '-M' or '-O' or both. When '-M' is specified, each reported alignment from a multi-mapping read (identified via 'NH' tag) will carry a fractional count of 1/x, instead of 1 (one), where x is the total number of alignments reported for the same read. When '-O' is specified, each overlapping feature will receive a fractional count of 1/y, where y is the total number of features overlapping with the read. When both '-M' and '-O' are specified, each alignment will carry a fractional count of 1/(x*y).",
        ),
        ToolInput(
            "quality",
            String(optional=True),
            prefix="-Q",
            doc="The minimum mapping quality score a read must satisfy in order to be counted. For paired-end reads, at least one end should satisfy this criteria. 0 by default.",
        ),
        ToolInput(
            "splitOnly",
            Boolean(optional=True),
            prefix="--splitOnly",
            doc="Count split alignments only (ie. alignments with CIGAR string containing 'N'). An example of split alignments is exon-spanning reads in RNA-seq data.",
        ),
        ToolInput(
            "nonSplitOnly",
            Boolean(optional=True),
            prefix="--nonSplitOnly",
            doc="If specified, only non-split alignments (CIGAR strings do not contain letter 'N') will be counted. All the other alignments will be ignored.",
        ),
        ToolInput(
            "primary",
            Boolean(optional=True),
            prefix="--primary",
            doc="Count primary alignments only. Primary alignments are identified using bit 0x100 in SAM/BAM FLAG field.",
        ),
        ToolInput(
            "ignoreDup",
            Boolean(optional=True),
            prefix="--ignoreDup",
            doc="Ignore duplicate reads in read counting. Duplicate reads are identified using bit Ox400 in BAM/SAM FLAG field. The whole read pair is ignored if one of the reads is a duplicate read for paired end data.",
        ),
        ToolInput(
            "strandness",
            String(optional=True),
            prefix="-",
            doc="Perform strand-specific read counting. A single integer value (applied to all input files) or a string of comma-separated values (applied to each corresponding input file) should be provided. Possible values include: 0 (unstranded), 1 (stranded) and 2 (reversely stranded). Default value is 0 (ie. unstranded read counting carried out for all input files).",
        ),
        ToolInput(
            "junction",
            String(optional=True),
            prefix="-J",
            doc="Count number of reads supporting each exon-exon junction. Junctions were identified from those exon-spanning reads in the input (containing 'N' in CIGAR string). Counting results are saved to a file named '<output_file>.jcounts'",
        ),
        ToolInput(
            "genome",
            File(optional=True),
            prefix="-G",
            doc="Provide the name of a FASTA-format file that contains thereference sequences used in read mapping that produced the provided SAM/BAM files. This optional argument can be used with '-J' option to improve read counting for junctions.",
        ),
        ToolInput(
            "pairEnd",
            Boolean(optional=True),
            prefix="-p",
            doc="If specified, fragments (or templates) will be counted instead of reads. This option is only applicable for paired-end reads; single-end reads are always counted as reads.",
        ),
        ToolInput(
            "both",
            Boolean(optional=True),
            prefix="-B",
            doc="Only count read pairs that have both ends aligned.",
        ),
        ToolInput(
            "pairEndDistance",
            Boolean(optional=True),
            prefix="-P",
            doc="Check validity of paired-end distance when counting read  pairs. Use -d and -D to set thresholds.",
        ),
        ToolInput(
            "minDistance",
            Int(optional=True),
            prefix="-d",
            doc="Minimum fragment/template length, 50 by default.",
        ),
        ToolInput(
            "maxDistance",
            Int(optional=True),
            prefix="-D",
            doc="Maximum fragment/template length, 600 by default.",
        ),
        ToolInput(
            "countRead",
            Boolean(optional=True),
            prefix="-C",
            doc="Do not count read pairs that have their two ends mapping to different chromosomes or mapping to same chromosome but on different strands.",
        ),
        ToolInput(
            "doNotSort",
            Boolean(optional=True),
            prefix="--donotsort",
            doc="Do not sort reads in BAM/SAM input. Note that reads from the same pair are required to be located next to each other in the input.",
        ),
        ToolInput(
            "threads",
            Int(optional=True),
            prefix="-T",
            doc="Number of the threads. 1 by default.",
        ),
        ToolInput(
            "byReadGroup",
            Boolean(optional=True),
            prefix="--byReadGroup",
            doc="Assign reads by read group. 'RG' tag is required to be present in the input BAM/SAM files.",
        ),
        ToolInput(
            "longRead",
            Boolean(optional=True),
            prefix="-L",
            doc="Count long reads such as Nanopore and PacBio reads. Long read counting can only run in one thread and only reads (not read-pairs) can be counted. There is no limitation on the number of 'M' operations allowed in a CIGAR string in long read counting.",
        ),
        ToolInput(
            "outputFormat",
            String(optional=True),
            prefix="-R",
            doc="Output detailed assignment results for each read or read-pair. Results are saved to a file that is in one of the following formats: CORE, SAM and BAM. See Users Guide for more info about these formats.",
        ),
        ToolInput(
            "outputDirectory",
            String(optional=True),
            prefix="--Rpath",
            doc="Specify a directory to save the detailed assignment results. If unspecified, the directory where counting results are saved is used.",
        ),
        ToolInput(
            "tmpDir",
            String(optional=True),
            prefix="--tmpDir",
            doc="Directory under which intermediate files are saved (later removed). By default, intermediate files will be saved to the directory specified in '-o' argument.",
        ),
        ToolInput(
            "maxMOp",
            Int(optional=True),
            prefix="--maxMOp",
            doc="Maximum number of 'M' operations allowed in a CIGAR string. 10 by default. Both 'X' and '=' are treated as 'M' and adjacent 'M' operations are merged in the CIGAR string.",
        ),
    ]

