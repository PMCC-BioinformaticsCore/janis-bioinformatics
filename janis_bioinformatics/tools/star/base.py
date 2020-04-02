from abc import ABC

from janis_core import (
    ToolInput,
    Boolean,
    String,
    ToolOutput,
    Int,
    Stdout,
    File,
    Float,
    InputSelector,
    Filename,
    CpuSelector,
    Directory,
    Array,
    get_value_for_hints_and_ordered_resource_tuple,
    CaptureType,
    WildcardSelector,
    ToolMetadata,
)

from janis_bioinformatics.data_types import Bam, FastqGz

from janis_bioinformatics.tools import BioinformaticsTool

MEM_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 4,
            CaptureType.EXOME: 4,
            CaptureType.CHROMOSOME: 8,
            CaptureType.THIRTYX: 16,
            CaptureType.NINETYX: 16,
            CaptureType.THREEHUNDREDX: 24,
        },
    )
]

CPU_TUPLE = [
    (
        CaptureType.key(),
        {
            CaptureType.TARGETED: 2,
            CaptureType.EXOME: 4,
            CaptureType.CHROMOSOME: 5,
            CaptureType.THIRTYX: 8,
            CaptureType.NINETYX: 12,
            CaptureType.THREEHUNDREDX: 16,
        },
    )
]


class StarAlignerBase(BioinformaticsTool, ABC):
    @staticmethod
    def tool():
        return "star_aligner"

    @staticmethod
    def base_command():
        return "STAR"

    # Need a better way to specify memory
    def memory(self, hints):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 32

    def cpus(self, hints):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CPU_TUPLE)
        if val:
            return val
        return 4

    def inputs(self):
        return [
            *StarAlignerBase.additional_inputs,
            ToolInput("help", Boolean(optional=True), prefix="--help", doc="help page"),
            ToolInput(
                "runThreadN",
                Int(optional=True),
                default=CpuSelector(),
                prefix="--runThreadN",
                doc="int: number of threads to run STAR. Default: 1.",
            ),
            ToolInput(
                "genomeDir",
                Directory(optional=True),
                prefix="--genomeDir",
                doc="string: path to the directory where genome files are stored (for –runMode alignReads) or will be generated (for –runMode generateGenome). Default: ./GenomeDir",
            ),
            ToolInput(
                "readFilesIn",
                Array(FastqGz, optional=True),
                prefix="--readFilesIn",
                separator=",",
                doc="string(s): paths to files that contain input read1 (and, if needed, read2). Default: Read1,Read2.",
            ),
            ToolInput(
                "outFileNamePrefix",
                String(optional=True),
                prefix="--outFileNamePrefix",
                doc="string: output files name prefix (including full or relative path). Can only be defined on the command line.",
            ),
            ToolInput(
                "outSAMtype",
                String(optional=True),
                prefix="--outSAMtype",
                doc='strings: type of SAM/BAM output. 1st word: "BAM": outputBAMwithoutsorting, "SAM": outputSAMwithoutsorting, "None": no SAM/BAM output. 2nd,3rd: "Unsorted": standard unsorted. "SortedByCoordinate": sorted by coordinate. This option will allocate extra memory for sorting which can be specified by –limitBAMsortRAM.',
            ),
            ToolInput(
                "outSAMunmapped",
                String(optional=True),
                prefix="--outSAMunmapped",
                doc="string(s): output of unmapped reads in the SAM format",
            ),
            ToolInput(
                "outSAMattributes",
                String(optional=True),
                prefix="--outSAMattributes",
                doc="string: a string of desired SAM attributes, in the order desired for the output SAM",
            ),
            ToolInput(
                "readFilesCommand",
                String(optional=True),
                prefix="--readFilesCommand",
                doc="string(s): command line to execute for each of the input file. This command should generate FASTA or FASTQ text and send it to stdout",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "logFinalOut",
                File,
                glob=InputSelector("outFileNamePrefix") + "Log.final.out",
            ),
            ToolOutput(
                "LogOut", File, glob=InputSelector("outFileNamePrefix") + "Log.out"
            ),
            ToolOutput(
                "LogProgressOut",
                File,
                glob=InputSelector("outFileNamePrefix") + "Log.progress.out",
            ),
            ToolOutput(
                "SJOutTab",
                File,
                glob=InputSelector("outFileNamePrefix") + "SJ.out.tab",
            ),
            # Problem will occur if more than one *.out.bam is found. Only the first one will get.
            ToolOutput("out", Bam, glob=WildcardSelector("*.out.bam"),),
        ]

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=date(2020, 4, 2),
            dateUpdated=date(2020, 4, 2),
            institution="Cold Spring Harbor Laboratory",
            doi="https://doi.org/10.1093/bioinformatics/bts635",
            citation="Dobin, A., Davis, C. A., Schlesinger, F., Drenkow, J., Zaleski, C., Jha, S., Batut, P., Chaisson, M., & Gingeras, T. R. (2013). STAR: ultrafast universal RNA-seq aligner. Bioinformatics (Oxford, England), 29(1), 15–21. https://doi.org/10.1093/bioinformatics/bts635",
            keywords=["star", "align"],
            documentationUrl="https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf",
            documentation="""Usage: STAR  [options]... --genomeDir /path/to/genome/index/   --readFilesIn R1.fq R2.fq
Spliced Transcripts Alignment to a Reference (c) Alexander Dobin, 2009-2019

For more details see:
<https://github.com/alexdobin/STAR>
<https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf>
            """,
        )

    # Additional parameters here
    additional_inputs = []
