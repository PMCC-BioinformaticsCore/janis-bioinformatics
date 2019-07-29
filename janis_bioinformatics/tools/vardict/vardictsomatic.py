from abc import ABC
from typing import List, Dict, Any

from janis_core import CpuSelector
from janis_core import get_value_for_hints_and_ordered_resource_tuple

from janis_bioinformatics.tools import BioinformaticsTool
from janis_bioinformatics.data_types import BamBai, Bed, FastaFai, Vcf
from janis_core import (
    ToolOutput,
    ToolInput,
    Array,
    Filename,
    ToolArgument,
    Boolean,
    Float,
    Int,
    String,
    InputSelector,
    CaptureType,
)

from janis_bioinformatics.tools.vardict.vardict import (
    VarDict_1_5_6,
    VarDict_1_5_7,
    VarDict_1_5_8,
)

CORES_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 2,
            CaptureType.CHROMOSOME: 4,
            CaptureType.EXOME: 4,
            CaptureType.THIRTYX: 4,
            CaptureType.NINETYX: 4,
            CaptureType.THREEHUNDREDX: 4,
        },
    )
]

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 4,
            CaptureType.CHROMOSOME: 16,
            CaptureType.EXOME: 32,
            CaptureType.THIRTYX: 64,
            CaptureType.NINETYX: 64,
            CaptureType.THREEHUNDREDX: 64,
        },
    )
]


class VarDictSomaticBase(BioinformaticsTool, ABC):
    def friendly_name(self) -> str:
        return "Vardict (Somatic)"

    @staticmethod
    def tool():
        return "vardict_somatic"

    @staticmethod
    def base_command():
        return "VarDict"

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 4

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 8

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput("tumorBam", BamBai(), doc="The indexed BAM file"),
            ToolInput("normalBam", BamBai(), doc="The indexed BAM file"),
            ToolInput("intervals", Bed(), position=2, shell_quote=False),
            ToolInput(
                "reference",
                FastaFai(),
                prefix="-G",
                position=1,
                shell_quote=False,
                doc="The reference fasta. Should be indexed (.fai). "
                "Defaults to: /ngs/reference_data/genomes/Hsapiens/hg19/seq/hg19.fa",
            ),
            ToolInput(
                "tumorName",
                String(),
                doc="The sample name to be used directly.  Will overwrite -n option",
            ),
            ToolInput(
                "normalName",
                String(),
                doc="The normal sample name to use with the -b option",
            ),
            ToolInput(
                "alleleFreqThreshold",
                Float(optional=True),
                doc="The threshold for allele frequency, default: 0.05 or 5%",
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf", suffix=".vardict"),
                prefix=">",
                position=6,
                shell_quote=False,
            ),
            *VarDictSomaticBase.vardict_inputs,
            *VarDictSomaticBase.var2vcf_inputs,
        ]

    def outputs(self):
        return [ToolOutput("out", Vcf(), glob=InputSelector("outputFilename"))]

    def arguments(self):
        return [
            ToolArgument("| testsomatic.R |", position=3, shell_quote=False),
            ToolArgument("var2vcf_paired.pl", position=4, shell_quote=False),
            ToolArgument(
                InputSelector("tumorBam") + "|" + InputSelector("normalBam"),
                prefix="-b",
                position=1,
                shell_quote=True,
            ),
            ToolArgument(
                InputSelector("tumorName"), prefix="-N", position=1, shell_quote=True
            ),
            ToolArgument(
                InputSelector("tumorName") + "|" + InputSelector("normalName"),
                prefix="-N",
                position=5,
                shell_quote=True,
            ),
            ToolArgument(
                InputSelector("alleleFreqThreshold"),
                prefix="-f",
                position=5,
                shell_quote=False,
            ),
            ToolArgument(
                InputSelector("alleleFreqThreshold"),
                prefix="-f",
                position=1,
                shell_quote=False,
            ),
        ]

    vardict_inputs = [
        ToolInput(
            "indels3prime",
            Boolean(optional=True),
            prefix="-3",
            position=1,
            shell_quote=False,
            doc="Indicate to move indels to 3-prime if alternative alignment can be achieved.",
        ),
        ToolInput(
            "amplicon",
            Float(optional=True),
            prefix="-a",
            position=1,
            shell_quote=False,
            doc="Indicate it's amplicon based calling.  Reads that don't map to the amplicon will be skipped.  "
            "A read pair is considered belonging  to the amplicon if the edges are less than int bp to "
            "the amplicon, and overlap fraction is at least float.  Default: 10:0.95",
        ),
        ToolInput(
            "minReads",
            Int(optional=True),
            prefix="-B",
            position=1,
            shell_quote=False,
            doc="The minimum # of reads to determine strand bias, default 2",
        ),
        ToolInput(
            "chromNamesAreNumbers",
            Boolean(optional=True),
            prefix="-C",
            position=1,
            shell_quote=False,
            doc="Indicate the chromosome names are just numbers, such as 1, 2, not chr1, chr2",
        ),
        ToolInput(
            "chromColumn",
            Int(optional=True),
            prefix="-c",
            position=1,
            shell_quote=False,
            doc="The column for chromosome",
        ),
        ToolInput(
            "debug",
            Boolean(optional=True),
            prefix="-D",
            position=1,
            shell_quote=False,
            doc="Debug mode.  Will print some error messages and append full genotype at the end.",
        ),
        ToolInput(
            "splitDelimeter",
            String(optional=True),
            prefix="-d",
            position=1,
            shell_quote=False,
            doc='The delimiter for split region_info, default to tab "\t"',
        ),
        ToolInput(
            "geneEndCol",
            Int(optional=True),
            prefix="-E",
            position=1,
            shell_quote=False,
            doc="The column for region end, e.g. gene end",
        ),
        ToolInput(
            "segEndCol",
            Int(optional=True),
            prefix="-e",
            position=1,
            shell_quote=False,
            doc="The column for segment ends in the region, e.g. exon ends",
        ),
        ToolInput(
            "filter",
            String(optional=True),
            prefix="-F",
            position=1,
            shell_quote=False,
            doc="The hexical to filter reads using samtools. Default: 0x500 (filter 2nd alignments and "
            "duplicates). Use -F 0 to turn it off.",
        ),
        ToolInput(
            "geneNameCol",
            Int(optional=True),
            prefix="-g",
            position=1,
            shell_quote=False,
            doc="The column for gene name, or segment annotation",
        ),
        # ToolInput("help", Boolean(optional=True), prefix="-H", position=1, shell_quote=False,
        #           doc="Print this help page"),
        ToolInput(
            "printHeaderRow",
            Boolean(optional=True),
            prefix="-h",
            position=1,
            shell_quote=False,
            doc="Print a header row describing columns",
        ),
        ToolInput(
            "indelSize",
            Int(optional=True),
            prefix="-I",
            position=1,
            shell_quote=False,
            doc="The indel size.  Default: 120bp",
        ),
        ToolInput(
            "outputSplice",
            Boolean(optional=True),
            prefix="-i",
            position=1,
            shell_quote=False,
            doc="Output splicing read counts",
        ),
        ToolInput(
            "performLocalRealignment",
            Int(optional=True),
            prefix="-k",
            position=1,
            shell_quote=False,
            doc="Indicate whether to perform local realignment.  Default: 1.  Set to 0 to disable it. "
            "For Ion or PacBio, 0 is recommended.",
        ),
        ToolInput(
            "minMatches",
            Int(optional=True),
            prefix="-M",
            position=1,
            shell_quote=False,
            doc="The minimum matches for a read to be considered. If, after soft-clipping, the matched "
            "bp is less than INT, then the read is discarded. It's meant for PCR based targeted sequencing "
            "where there's no insert and the matching is only the primers. Default: 0, or no filtering",
        ),
        ToolInput(
            "maxMismatches",
            Int(optional=True),
            prefix="-m",
            position=1,
            shell_quote=False,
            doc="If set, reads with mismatches more than INT will be filtered and ignored. "
            "Gaps are not counted as mismatches. Valid only for bowtie2/TopHat or BWA aln "
            "followed by sampe. BWA mem is calculated as NM - Indels. "
            "Default: 8, or reads with more than 8 mismatches will not be used.",
        ),
        ToolInput(
            "regexSampleName",
            String(optional=True),
            prefix="-n",
            position=1,
            shell_quote=False,
            doc="The regular expression to extract sample name from BAM filenames. "
            "Default to: /([^\/\._]+?)_[^\/]*.bam/",
        ),
        ToolInput(
            "mapq",
            String(optional=True),
            prefix="-O",
            position=1,
            shell_quote=False,
            doc="The reads should have at least mean MapQ to be considered a valid variant. "
            "Default: no filtering",
        ),
        ToolInput(
            "qratio",
            Float(optional=True),
            prefix="-o",
            position=1,
            shell_quote=False,
            doc="The Qratio of (good_quality_reads)/(bad_quality_reads+0.5). "
            "The quality is defined by -q option.  Default: 1.5",
        ),
        ToolInput(
            "readPosition",
            Float(optional=True),
            prefix="-P",
            position=1,
            shell_quote=False,
            doc="The read position filter. If the mean variants position is less that specified, "
            "it's considered false positive.  Default: 5",
        ),
        ToolInput(
            "pileup",
            Boolean(optional=True),
            prefix="-p",
            position=1,
            shell_quote=False,
            doc="Do pileup regardless of the frequency",
        ),
        ToolInput(
            "minMappingQual",
            Int(optional=True),
            prefix="-Q",
            position=1,
            shell_quote=False,
            doc="If set, reads with mapping quality less than INT will be filtered and ignored",
        ),
        ToolInput(
            "phredScore",
            Int(optional=True),
            prefix="-q",
            position=1,
            shell_quote=False,
            doc="The phred score for a base to be considered a good call.  "
            "Default: 25 (for Illumina) For PGM, set it to ~15, as PGM tends to under estimate base quality.",
        ),
        ToolInput(
            "region",
            String(optional=True),
            prefix="-R",
            position=1,
            shell_quote=False,
            doc="The region of interest.  In the format of chr:start-end.  If end is omitted, "
            "then a single position.  No BED is needed.",
        ),
        ToolInput(
            "minVariantReads",
            Int(optional=True),
            prefix="-r",
            position=1,
            shell_quote=False,
            doc="The minimum # of variant reads, default 2",
        ),
        ToolInput(
            "regStartCol",
            Int(optional=True),
            prefix="-S",
            position=1,
            shell_quote=False,
            doc="The column for region start, e.g. gene start",
        ),
        ToolInput(
            "segStartCol",
            Int(optional=True),
            prefix="-s",
            position=1,
            shell_quote=False,
            doc="The column for segment starts in the region, e.g. exon starts",
        ),
        ToolInput(
            "minReadsBeforeTrim",
            Int(optional=True),
            prefix="-T",
            position=1,
            shell_quote=False,
            doc="Trim bases after [INT] bases in the reads",
        ),
        ToolInput(
            "removeDuplicateReads",
            Boolean(optional=True),
            prefix="-t",
            position=1,
            shell_quote=False,
            doc="Indicate to remove duplicated reads.  Only one pair with same start positions will be kept",
        ),
        ToolInput(
            "threads",
            Int(optional=True),
            default=CpuSelector(),
            prefix="-th",
            position=1,
            shell_quote=False,
            doc="Threads count.",
        ),
        ToolInput(
            "freq",
            Int(optional=True),
            prefix="-V",
            position=1,
            shell_quote=False,
            doc="The lowest frequency in the normal sample allowed for a putative somatic mutation. "
            "Defaults to 0.05",
        ),
        ToolInput(
            "vcfFormat",
            Boolean(optional=True),
            prefix="-v",
            position=1,
            shell_quote=False,
            doc="VCF format output",
        ),
        ToolInput(
            "vs",
            String(optional=True),
            prefix="-VS",
            position=1,
            shell_quote=False,
            doc="[STRICT | LENIENT | SILENT] How strict to be when reading a SAM or BAM: "
            "STRICT   - throw an exception if something looks wrong. "
            "LENIENT	- Emit warnings but keep going if possible. "
            "SILENT	- Like LENIENT, only don't emit warning messages. "
            "Default: LENIENT",
        ),
        ToolInput(
            "bp",
            Int(optional=True),
            prefix="-X",
            position=1,
            shell_quote=False,
            doc="Extension of bp to look for mismatches after insersion or deletion.  "
            "Default to 3 bp, or only calls when they're within 3 bp.",
        ),
        ToolInput(
            "extensionNucleotide",
            Int(optional=True),
            prefix="-x",
            position=1,
            shell_quote=False,
            doc="The number of nucleotide to extend for each segment, default: 0",
        ),
        ToolInput(
            "yy",
            Boolean(optional=True),
            prefix="-y",
            position=1,
            shell_quote=False,
            doc="<No content>",
        ),
        ToolInput(
            "downsamplingFraction",
            Int(optional=True),
            prefix="-Z",
            position=1,
            shell_quote=False,
            doc="For downsampling fraction.  e.g. 0.7 means roughly 70% downsampling.  "
            "Default: No downsampling.  Use with caution.  "
            "The downsampling will be random and non-reproducible.",
        ),
        ToolInput(
            "zeroBasedCoords",
            Int(optional=True),
            prefix="-z",
            position=1,
            shell_quote=False,
            doc="0/1  Indicate whether coordinates are zero-based, as IGV uses.  "
            "Default: 1 for BED file or amplicon BED file. Use 0 to turn it off. "
            "When using the -R option, it's set to 0",
        ),
    ]

    var2vcf_inputs = []

    @staticmethod
    def docurl():
        return "https://github.com/AstraZeneca-NGS/VarDict"

    def doc(self):
        return """
    VarDict

    VarDict is an ultra sensitive variant caller for both single and paired sample variant 
    calling from BAM files. VarDict implements several novel features such as amplicon bias 
    aware variant calling from targeted sequencing experiments, rescue of long indels by 
    realigning bwa soft clipped reads and better scalability than many Java based variant callers.

    Due to the philosophy of VarDict in calling "everything", several downstream strategies have 
    been developed to filter variants to for example the most likely cancer driving events. 
    These strategies are based on evidence in different databases and/or quality metrics. 
    http://bcb.io/2016/04/04/vardict-filtering/ provides an overview of how to develop further 
    filters for VarDict. The script at https://github.com/AstraZeneca-NGS/VarDict/blob/master/vcf2txt.pl 
    can be used to put the variants into a context by including information from dbSNP, Cosmic and ClinVar. 
    We are open to suggestions from the community on how to best narrow down to the variants of most interest.

    A Java based drop-in replacement for vardict.pl is being developed at 
    https://github.com/AstraZeneca-NGS/VarDictJava. The Java implementation is approximately 
    10 times faster than the original Perl implementation and does not depend on samtools

    To enable amplicon aware variant calling (single sample mode only; not supported in paired 
    variant calling), please make sure the bed file has 8 columns with the 7th and 8th columns 
    containing the insert interval (therefore subset of the 2nd and 3rd column interval). 

    Requirements

        - Perl (uses /usr/bin/env perl)
        - R (uses /usr/bin/env R)
        - samtools (must be in path, not required if using the Java implementation in place of vardict.pl)
    """


class VarDictSomatic_1_5_6(VarDictSomaticBase, VarDict_1_5_6):
    pass


class VarDictSomatic_1_5_7(VarDictSomaticBase, VarDict_1_5_7):
    pass


class VarDictSomatic_1_5_8(VarDictSomaticBase, VarDict_1_5_8):
    pass


VarDictSomaticLatest = VarDictSomatic_1_5_8

if __name__ == "__main__":
    # print(VarDictSomaticLatest().help())
    VarDictSomaticLatest().translate("wdl")
