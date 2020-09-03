from typing import List
from abc import ABC, abstractmethod

from janis_core import (
    ToolInput,
    Array,
    File,
    String,
    Int,
    Double,
    ToolArgument,
    CpuSelector,
    ToolMetadata,
    Float,
    Directory,
)

from janis_bioinformatics.data_types import FastaWithIndexes, Fasta, Vcf, Bam, FastqGz
from janis_bioinformatics.tools import BioinformaticsTool


class StarBase(BioinformaticsTool, ABC):
    @abstractmethod
    def run_mode(self):
        """
        (default: alignReads) type of the run.
            - alignReads ... map reads
            - genomeGenerate:  ... generate genome file
            - inputAlignmentsFromBAM ... input alignments from BAM. Presently only works with --outWigType and --bamRemoveDuplicates
            - liftOver ... lift-over of GTF files (--sjdbGTFfile) between genome assemblies using chain file(s) from --genomeChainFiles
        :return: str: ["alignReads", "genomeGenerate", "inputALignmentsFromBAM", "liftOver"]
        """
        pass

    def tool(self):
        return "star_" + self.run_mode()

    def tool_provider(self):
        return "Cold Spring Harbor Laboratory"

    def base_command(self):
        return "STAR"

    def friendly_name(self):
        return "STAR Aligner"

    # Need a better way to specify memory
    def memory(self, hints):
        return 32

    def cpus(self, hints):
        return 4

    def arguments(self):
        return [
            ToolArgument(
                self.run_mode(),
                prefix="--runMode",
                doc="(default: alignReads) type of the run. \n"
                "- alignReads ... map reads \n"
                "- genomeGenerate:  ... generate genome files\n"
                "- inputAlignmentsFromBAM ... input alignments from BAM. Presently only works with --outWigType and --bamRemoveDuplicates.\n"
                "- liftOver ... lift-over of GTF files (--sjdbGTFfile) between genome assemblies using chain file(s) from --genomeChainFiles.",
            ),
        ]

    def inputs(self) -> List[ToolInput]:
        return [
            # ToolInput(
            #     "versionGenome",
            #     String(optional=True),
            #     prefix="--versionGenome",
            #     doc="(default: 2.7.1a) earliest genome index version compatible with this STAR release. Please do not change this value!",
            # ),
            ToolInput(
                "parametersFiles",
                String(optional=True),
                prefix="--parametersFiles",
                doc="(default: -) none. Can only be defined on the command line.",
            ),
            ToolInput(
                "sysShell",
                String(optional=True),
                prefix="--sysShell",
                doc="(default: -) path to the shell binary, preferably bash, e.g. /bin/bash.\n"
                "- ... the default shell is executed, typically /bin/sh. This was reported to fail on some "
                "Ubuntu systems - then you need to specify path to bash.",
            ),
            ToolInput(
                "runThreadN",
                Int(optional=True),
                default=CpuSelector(),
                prefix="--runThreadN",
                doc="(default: 1) number of threads to run STAR",
            ),
            ToolInput(
                "runDirPerm",
                String(optional=True),
                prefix="--runDirPerm",
                doc="(default: User_RWX) permissions for the directories created at the run-time. \n"
                "- User_RWX ... user-read/write/execute \n"
                "- All_RWX  ... all-read/write/execute (same as chmod 777)",
            ),
            ToolInput(
                "runRNGseed",
                Int(optional=True),
                prefix="--runRNGseed",
                doc="(default: 777) random number generator seed.",
            ),
            ToolInput(
                "genomeDir",
                Directory(optional=True),
                prefix="--genomeDir",
                doc="(default: GenomeDir/) path to the directory where genome files are stored \n"
                "(for --runMode alignReads) or will be generated (for --runMode generateGenome)",
            ),
            ToolInput(
                "genomeLoad",
                String(optional=True),
                prefix="--genomeLoad",
                doc="(default: NoSharedMemory) mode of shared memory usage for the genome files. Only used with --runMode alignReads.\n"
                "- LoadAndKeep     ... load genome into shared and keep it in memory after run,\n"
                "- LoadAndRemove   ... load genome into shared but remove it after run,\n"
                "- LoadAndExit     ... load genome into shared memory and exit, keeping the genome in memory for future runs,\n"
                "- Remove:   ... do not map anything, just remove loaded genome from memory,\n"
                "- NoSharedMemory  ... do not use shared memory, each job will have its own private copy of the genome",
            ),
            ToolInput(
                "genomeFastaFiles",
                Array(Fasta, optional=True),
                prefix="--genomeFastaFiles",
                doc="(default: -) path(s) to the fasta files with the genome sequences, separated by spaces. "
                "These files should be plain text FASTA files, they *cannot* be zipped. Required for the genome "
                "generation (--runMode genomeGenerate). Can also be used in the mapping (--runMode alignReads) "
                "to add extra (new) sequences to the genome (e.g. spike-ins).",
            ),
            ToolInput(
                "genomeChainFiles",
                Array(File, optional=True),
                prefix="--genomeChainFiles",
                doc="(default: -) chain files for genomic liftover. Only used with --runMode liftOver .",
            ),
            ToolInput(
                "genomeFileSizes",
                Int(optional=True),
                prefix="--genomeFileSizes",
                doc="(default: 0) genome files exact sizes in bytes. Typically, this should not be defined by the user.",
            ),
            ToolInput(
                "genomeConsensusFile",
                Vcf(optional=True),
                prefix="--genomeConsensusFile",
                doc="(default: -) VCF file with consensus SNPs (i.e. alternative allele is the major (AF>0.5) allele)",
            ),
            ToolInput(
                "genomeChrBinNbits",
                Int(optional=True),
                prefix="--genomeChrBinNbits",
                doc="(default: 18) each chromosome will occupy an integer number of bins. For a genome with large "
                "number of contigs, it is recommended to scale this parameter as "
                "``min(18, log2[max(GenomeLength/NumberOfReferences,ReadLength)])``.",
            ),
            ToolInput(
                "genomeSAindexNbases",
                Int(optional=True),
                prefix="--genomeSAindexNbases",
                doc="(default: 14) length (bases) of the SA pre-indexing string. Typically between 10 and 15. "
                "Longer strings will use much more memory, but allow faster searches. For small genomes, "
                "the parameter --genomeSAindexNbases must be scaled down to min(14, log2(GenomeLength)/2 - 1).",
            ),
            ToolInput(
                "genomeSAsparseD",
                Int(optional=True),
                prefix="--genomeSAsparseD",
                doc="(default: 1) use bigger numbers to decrease needed RAM at the cost of mapping speed reduction",
            ),
            ToolInput(
                "genomeSuffixLengthMax",
                Int(optional=True),
                prefix="--genomeSuffixLengthMax",
                doc="(default: -1) maximum length of the suffixes, has to be longer than read length. -1 = infinite.",
            ),
            ToolInput(
                "sjdbFileChrStartEnd",
                String(optional=True),
                prefix="--sjdbFileChrStartEnd",
                doc="(default: -) path to the files with genomic coordinates (chr <tab> start <tab> end <tab> strand) "
                "for the splice junction introns. Multiple files can be supplied wand will be concatenated.",
            ),
            ToolInput(
                "sjdbGTFfile",
                String(optional=True),
                prefix="--sjdbGTFfile",
                doc="(default: -) path to the GTF file with annotations",
            ),
            ToolInput(
                "sjdbGTFchrPrefix",
                String(optional=True),
                prefix="--sjdbGTFchrPrefix",
                doc="(default: -) prefix for chromosome names in a GTF file (e.g. 'chr' "
                "for using ENSMEBL annotations with UCSC genomes)",
            ),
            ToolInput(
                "sjdbGTFfeatureExon",
                String(optional=True),
                prefix="--sjdbGTFfeatureExon",
                doc="(default: exon) feature type in GTF file to be used as exons for building transcripts",
            ),
            ToolInput(
                "sjdbGTFtagExonParentTranscript",
                String(optional=True),
                prefix="--sjdbGTFtagExonParentTranscript",
                doc="(default: transcript_id) GTF attribute name for parent transcript ID "
                '(default "transcript_id" works for GTF files)',
            ),
            ToolInput(
                "sjdbGTFtagExonParentGene",
                String(optional=True),
                prefix="--sjdbGTFtagExonParentGene",
                doc='(default: gene_id) GTF attribute name for parent gene ID (default "gene_id" works for GTF files)',
            ),
            ToolInput(
                "sjdbGTFtagExonParentGeneName",
                String(optional=True),
                prefix="--sjdbGTFtagExonParentGeneName",
                doc="(default: gene_name) GTF attrbute name for parent gene name",
            ),
            ToolInput(
                "sjdbGTFtagExonParentGeneType",
                String(optional=True),
                prefix="--sjdbGTFtagExonParentGeneType",
                doc="(default: gene_type gene_biotype) GTF attrbute name for parent gene type",
            ),
            ToolInput(
                "sjdbOverhang",
                Int(optional=True),
                prefix="--sjdbOverhang",
                doc="(default: 100) length of the donor/acceptor sequence on each side of the junctions, "
                "ideally = (mate_length - 1)",
            ),
            ToolInput(
                "sjdbScore",
                Int(optional=True),
                prefix="--sjdbScore",
                doc="(default: 2) extra alignment score for alignmets that cross database junctions",
            ),
            ToolInput(
                "sjdbInsertSave",
                String(optional=True),
                prefix="--sjdbInsertSave",
                doc="(default: Basic) which files to save when sjdb junctions are inserted on the fly at the mapping step\n"
                "- Basic ... only small junction / transcript files \n"
                "- All   ... all files including big Genome, SA and SAindex - this will create a complete genome directory",
            ),
            ToolInput(
                "varVCFfile",
                Vcf(optional=True),
                prefix="--varVCFfile",
                doc="(default: -) path to the VCF file that contains variation data.",
            ),
            ToolInput(
                "inputBAMfile",
                Bam(optional=True),
                prefix="--inputBAMfile",
                doc="(default: -) path to BAM input file, to be used with --runMode inputAlignmentsFromBAM",
            ),
            ToolInput(
                "readFilesType",
                String(optional=True),
                prefix="--readFilesType",
                doc="(default: Fastx) format of input read files\n"
                "- Fastx       ... FASTA or FASTQ\n"
                "- SAM SE      ... SAM or BAM single-end reads; for BAM use --readFilesCommand samtools view\n"
                "- SAM PE      ... SAM or BAM paired-end reads; for BAM use --readFilesCommand samtools view\n",
            ),
            ToolInput(
                "readFilesIn",
                Array(FastqGz(optional=True)),
                prefix="--readFilesIn",
                separator=" ",
                doc="(default: Read1 Read2) paths to files that contain input read1 (and, if needed,  read2)",
            ),
            ToolInput(
                "readFilesPrefix",
                String(optional=True),
                prefix="--readFilesPrefix",
                doc="(default: -)   for the read files names, i.e. it will be added in front of the strings in --readFilesIn no prefix",
            ),
            ToolInput(
                "readFilesCommand",
                String(optional=True),
                prefix="--readFilesCommand",
                doc="(default: -) command line to execute for each of the input file. This command should generate FASTA or FASTQ text and send it to stdout zcat - to uncompress .gz files, bzcat - to uncompress .bz2 files, etc.",
            ),
            ToolInput(
                "readMapNumber",
                Int(optional=True),
                prefix="--readMapNumber",
                doc="(default: 1) number of reads to map from the beginning of the file map all reads",
            ),
            ToolInput(
                "readMatesLengthsIn",
                String(optional=True),
                prefix="--readMatesLengthsIn",
                doc="(default: NotEqual) Equal/NotEqual - lengths of names,sequences,qualities for both mates are the same  / not the same. NotEqual is safe in all situations.",
            ),
            ToolInput(
                "readNameSeparator",
                String(optional=True),
                prefix="--readNameSeparator",
                doc="(default: /) character(s) separating the part of the read names that will be trimmed in output (read name after space is always trimmed)",
            ),
            ToolInput(
                "readQualityScoreBase",
                Int(optional=True),
                prefix="--readQualityScoreBase",
                doc="(default: 33) number to be subtracted from the ASCII code to get Phred quality score",
            ),
            ToolInput(
                "clip3pNbases",
                Int(optional=True),
                prefix="--clip3pNbases",
                doc="(default: 0) number(s) of bases to clip from 3p of each mate. If one value is given, it will be assumed the same for both mates.",
            ),
            ToolInput(
                "clip5pNbases",
                Int(optional=True),
                prefix="--clip5pNbases",
                doc="(default: 0) number(s) of bases to clip from 5p of each mate. If one value is given, it will be assumed the same for both mates.",
            ),
            ToolInput(
                "clip3pAdapterSeq",
                String(optional=True),
                prefix="--clip3pAdapterSeq",
                doc="(default: -) adapter sequences to clip from 3p of each mate.  If one value is given, it will be assumed the same for both mates.",
            ),
            ToolInput(
                "clip3pAdapterMMp",
                Double(optional=True),
                prefix="--clip3pAdapterMMp",
                doc="(default: 0.1) max proportion of mismatches for 3p adpater clipping for each mate.  If one value is given, it will be assumed the same for both mates.",
            ),
            ToolInput(
                "clip3pAfterAdapterNbases",
                Int(optional=True),
                prefix="--clip3pAfterAdapterNbases",
                doc="(default: 0) number of bases to clip from 3p of each mate after the adapter clipping. If one value is given, it will be assumed the same for both mates.",
            ),
            ToolInput(
                "limitGenomeGenerateRAM",
                Int(optional=True),
                prefix="--limitGenomeGenerateRAM",
                doc="(default: 31000000000) maximum available RAM (bytes) for genome generation",
            ),
            ToolInput(
                "limitIObufferSize",
                Int(optional=True),
                prefix="--limitIObufferSize",
                doc="(default: 150000000) max available buffers size (bytes) for input/output, per thread",
            ),
            ToolInput(
                "limitOutSAMoneReadBytes",
                Int(optional=True),
                prefix="--limitOutSAMoneReadBytes",
                doc="(default: 100000) >(2*(LengthMate1+LengthMate2+100)*outFilterMultimapNmax",
            ),
            ToolInput(
                "limitOutSJoneRead",
                Int(optional=True),
                prefix="--limitOutSJoneRead",
                doc="(default: 1000) max number of junctions for one read (including all multi-mappers)",
            ),
            ToolInput(
                "limitOutSJcollapsed",
                Int(optional=True),
                prefix="--limitOutSJcollapsed",
                doc="(default: 1000000) max number of collapsed junctions",
            ),
            ToolInput(
                "limitBAMsortRAM",
                Int(optional=True),
                prefix="--limitBAMsortRAM",
                doc="(default: 0) maximum available RAM (bytes) for sorting BAM. If =0, it will be set to the genome index size. 0 value can only be used with --genomeLoad NoSharedMemory option.",
            ),
            ToolInput(
                "limitSjdbInsertNsj",
                Int(optional=True),
                prefix="--limitSjdbInsertNsj",
                doc="(default: 1000000) maximum number of junction to be inserted to the genome on the fly at the mapping stage, including those from annotations and those detected in the 1st step of the 2-pass run",
            ),
            ToolInput(
                "limitNreadsSoft",
                Int(optional=True),
                prefix="--limitNreadsSoft",
                doc="(default: 1) soft limit on the number of reads",
            ),
            ToolInput(
                "outFileNamePrefix",
                String(optional=True),
                prefix="--outFileNamePrefix",
                doc="(default: ./) output files name prefix (including full or relative path). Can only be defined on the command line.",
            ),
            ToolInput(
                "outTmpDir",
                String(optional=True),
                prefix="--outTmpDir",
                doc="(default: -) path to a directory that will be used as temporary by STAR. All contents of this directory will be removed!     - the temp directory will default to outFileNamePrefix_STARtmp",
            ),
            ToolInput(
                "outTmpKeep",
                String(optional=True),
                prefix="--outTmpKeep",
                doc="(default: None) whether to keep the tempporary files after STAR runs is finished None ... remove all temporary files All .. keep all files",
            ),
            ToolInput(
                "outStd",
                String(optional=True),
                prefix="--outStd",
                doc="(default: Log) which output will be directed to stdout (standard out) Log     ... log messages SAM        ... alignments in SAM format (which normally are output to Aligned.out.sam file), normal standard output will go into Log.std.out BAM_Unsorted     ... alignments in BAM format, unsorted. Requires --outSAMtype BAM Unsorted BAM_SortedByCoordinate ... alignments in BAM format, unsorted. Requires --outSAMtype BAM SortedByCoordinate BAM_Quant        ... alignments to transcriptome in BAM format, unsorted. Requires --quantMode TranscriptomeSAM       ",
            ),
            ToolInput(
                "outReadsUnmapped",
                String(optional=True),
                prefix="--outReadsUnmapped",
                doc="(default: None) which output will be directed to stdout (standard out) [Log ... log messages SAM ... alignments in SAM format (which normally are output to Aligned.out.sam file), normal standard output will go into Log.std.out BAM_Unsorted           ... alignments in BAM format, unsorted. Requires --outSAMtype BAM Unsorted BAM_SortedByCoordinate ... alignments in BAM format, unsorted. Requires --outSAMtype BAM SortedByCoordinate BAM_Quant ... alignments to transcriptome in BAM format, unsorted. Requires --quantMode TranscriptomeSAM]",
            ),
            ToolInput(
                "outQSconversionAdd",
                Int(optional=True),
                prefix="--outQSconversionAdd",
                doc="(default: 0) add this number to the quality score (e.g. to convert from Illumina to Sanger, use -31)",
            ),
            ToolInput(
                "outMultimapperOrder",
                String(optional=True),
                prefix="--outMultimapperOrder",
                doc="(default: Old_2.4) order of multimapping alignments in the output files Old_2.4",
            ),
            ToolInput(
                "outSAMtype",
                Array(String(), optional=True),
                prefix="--outSAMtype",
                doc="(default: SAM) ... quasi-random order used before 2.5.0 Random ... random order of alignments for each multi-mapper. Read mates (pairs) are always adjacent, all alignment for each read stay together. This option will become default in the future releases. ... standard unsorted SortedByCoordinate ... sorted by coordinate. This option will allocate extra memory for sorting which can be specified by --limitBAMsortRAM.",
            ),
            ToolInput(
                "outSAMmode",
                String(optional=True),
                prefix="--outSAMmode",
                doc="(default: Full) mode of SAM output None ... no SAM output Full ... full SAM output NoQS ... full SAM but without quality scores ... no attributes Standard    ... NH HI AS nM All   ... NH HI AS nM NM MD jM jI MC ch vA    ... variant allele vG    ... genomic coordiante of the variant overlapped by the read vW    ... 0/1 - alignment does not pass / passes WASP filtering. Requires --waspOutputMode SAMtag STARsolo: CR CY UR UY ... sequences and quality scores of cell barcodes and UMIs for the solo* demultiplexing CB UB       ... error-corrected cell barcodes and UMIs for solo* demultiplexing. Requires --outSAMtype BAM SortedByCoordinate. sM    ... assessment of CB and UMI sS    ... sequence of the entire barcode (CB,UMI,adapter...) sQ    ... quality of the entire barcode Unsupported/undocumented: rB    ... alignment block read/genomic coordinates vR    ... read coordinate of the variant",
            ),
            ToolInput(
                "outSAMstrandField",
                String(optional=True),
                prefix="--outSAMstrandField",
                doc="(default: None) Cufflinks-like strand field flag None",
            ),
            ToolInput(
                "outSAMattributes",
                String(optional=True),
                prefix="--outSAMattributes",
                doc="(default: Standard) a string of desired SAM attributes, in the order desired for the output SAM NH HI AS nM NM MD jM jI XS MC ch ... any combination in any order None",
            ),
            ToolInput(
                "outSAMattrIHstart",
                Int(optional=True),
                prefix="--outSAMattrIHstart",
                doc="(default: 1) start value for the IH attribute. 0 may be required by some downstream software, such as Cufflinks or StringTie.",
            ),
            ToolInput(
                "outSAMunmapped",
                String(optional=True),
                prefix="--outSAMunmapped",
                doc="(default: None) output of unmapped reads in the SAM format 1st word: None   ... no output Within ... output unmapped reads within the main SAM file (i.e. Aligned.out.sam) 2nd word: KeepPairs ... record unmapped mate for each alignment, and, in case of unsorted output, keep it adjacent to its mapped mate. Only affects multi-mapping reads.",
            ),
            ToolInput(
                "outSAMorder",
                String(optional=True),
                prefix="--outSAMorder",
                doc="(default: Paired) type of sorting for the SAM output one mate after the other for all paired alignments one mate after the other for all paired alignments, the order is kept the same as in the input FASTQ files",
            ),
            ToolInput(
                "outSAMprimaryFlag",
                String(optional=True),
                prefix="--outSAMprimaryFlag",
                doc="(default: OneBestScore) which alignments are considered primary - all others will be marked with 0x100 bit in the FLAG OneBestScore ... only one alignment with the best score is primary AllBestScore ... all alignments with the best score are primary",
            ),
            ToolInput(
                "outSAMreadID",
                String(optional=True),
                prefix="--outSAMreadID",
                doc="(default: Standard) read ID record type Standard ... first word (until space) from the FASTx read ID line, removing /1,/2 from the end Number   ... read number (index) in the FASTx file",
            ),
            ToolInput(
                "outSAMmapqUnique",
                Int(optional=True),
                prefix="--outSAMmapqUnique",
                doc="(default: 255) the MAPQ value for unique mappers",
            ),
            ToolInput(
                "outSAMflagOR",
                Int(optional=True),
                prefix="--outSAMflagOR",
                doc="(default: 0) sam FLAG will be bitwise OR'd with this value, i.e. FLAG=FLAG | outSAMflagOR. This is applied after all flags have been set by STAR, and after outSAMflagAND. Can be used to set specific bits that are not set otherwise.",
            ),
            ToolInput(
                "outSAMflagAND",
                Int(optional=True),
                prefix="--outSAMflagAND",
                doc="(default: 65535) sam FLAG will be bitwise AND'd with this value, i.e. FLAG=FLAG & outSAMflagOR. This is applied after all flags have been set by STAR, but before outSAMflagOR. Can be used to unset specific bits that are not set otherwise.",
            ),
            ToolInput(
                "outSAMattrRGline",
                String(optional=True),
                prefix="--outSAMattrRGline",
                doc='(default: -) SAM/BAM read group line. The first word contains the read group identifier and must start with "ID:", e.g. --outSAMattrRGline ID:xxx CN:yy "DS:z z z".     xxx will be added as RG tag to each output alignment. Any spaces in the tag values have to be double quoted.     Comma separated RG lines correspons to different (comma separated) input files in --readFilesIn. Commas have to be surrounded by spaces, e.g.     --outSAMattrRGline ID:xxx , ID:zzz "DS:z z" , ID:yyy DS:yyyy',
            ),
            ToolInput(
                "outSAMheaderHD",
                Array(String(), optional=True),
                prefix="--outSAMheaderHD",
                doc="(default: -) @HD (header) line of the SAM header",
            ),
            ToolInput(
                "outSAMheaderPG",
                Array(String(), optional=True),
                prefix="--outSAMheaderPG",
                doc="(default: -) extra @PG (software) line of the SAM header (in addition to STAR)",
            ),
            ToolInput(
                "outSAMheaderCommentFile",
                String(optional=True),
                prefix="--outSAMheaderCommentFile",
                doc="(default: -) path to the file with @CO (comment) lines of the SAM header",
            ),
            ToolInput(
                "outSAMfilter",
                String(optional=True),
                prefix="--outSAMfilter",
                doc="(default: None) filter the output into main SAM/BAM files KeepOnlyAddedReferences ... only keep the reads for which all alignments are to the extra reference sequences added with --genomeFastaFiles at the mapping stage. KeepAllAddedReferences ...  keep all alignments to the extra reference sequences added with --genomeFastaFiles at the mapping stage.",
            ),
            ToolInput(
                "outSAMmultNmax",
                Int(optional=True),
                prefix="--outSAMmultNmax",
                doc="(default: 1) max number of multiple alignments for a read that will be output to the SAM/BAM files. -1 ... all alignments (up to --outFilterMultimapNmax) will be output",
            ),
            ToolInput(
                "outSAMtlen",
                Int(optional=True),
                prefix="--outSAMtlen",
                doc="(default: 1) calculation method for the TLEN field in the SAM/BAM files 1 ... leftmost base of the (+)strand mate to rightmost base of the (-)mate. (+)sign for the (+)strand mate 2 ... leftmost base of any mate to rightmost base of any mate. (+)sign for the mate with the leftmost base. This is different from 1 for overlapping mates with protruding ends",
            ),
            ToolInput(
                "outBAMcompression",
                Int(optional=True),
                prefix="--outBAMcompression",
                doc="(default: 1) -1 to 10  BAM compression level, -1=default compression (6?), 0=no compression, 10=maximum compression",
            ),
            ToolInput(
                "outBAMsortingThreadN",
                Int(optional=True),
                prefix="--outBAMsortingThreadN",
                doc="(default: 0) number of threads for BAM sorting. 0 will default to min(6,--runThreadN).",
            ),
            ToolInput(
                "outBAMsortingBinsN",
                Int(optional=True),
                prefix="--outBAMsortingBinsN",
                doc="(default: 50) number of genome bins fo coordinate-sorting",
            ),
            ToolInput(
                "bamRemoveDuplicatesType",
                String(optional=True),
                prefix="--bamRemoveDuplicatesType",
                doc="(default: -) mark duplicates in the BAM file, for now only works with (i) sorted BAM fed with inputBAMfile, and (ii) for paired-end alignments only -",
            ),
            ToolInput(
                "bamRemoveDuplicatesMate2basesN",
                Int(optional=True),
                prefix="--bamRemoveDuplicatesMate2basesN",
                doc="(default: 0) number of bases from the 5' of mate 2 to use in collapsing (e.g. for RAMPAGE)",
            ),
            ToolInput(
                "outWigType",
                String(optional=True),
                prefix="--outWigType",
                doc="(default: None) --outSAMtype BAM SortedByCoordinate .     1st word:     None       ... no signal output     bedGraph   ... bedGraph format     wiggle     ... wiggle format     2nd word:     read1_5p   ... signal from only 5' of the 1st read, useful for CAGE/RAMPAGE etc     read2      ... signal from only 2nd read",
            ),
            ToolInput(
                "outWigStrand",
                String(optional=True),
                prefix="--outWigStrand",
                doc="(default: Stranded) strandedness of wiggle/bedGraph output     Stranded   ...  separate strands, str1 and str2     Unstranded ...  collapsed strands",
            ),
            ToolInput(
                "outWigReferencesPrefix",
                String(optional=True),
                prefix="--outWigReferencesPrefix",
                doc='(default: -) prefix matching reference names to include in the output wiggle file, e.g. "chr", default "-" - include all references',
            ),
            ToolInput(
                "outWigNorm",
                String(optional=True),
                prefix="--outWigNorm",
                doc='(default: RPM) type of normalization for the signal RPM    ... reads per million of mapped reads None   ... no normalization, "raw" counts',
            ),
            ToolInput(
                "outFilterType",
                String(optional=True),
                prefix="--outFilterType",
                doc="(default: Normal) type of filtering Normal  ... standard filtering using only current alignment BySJout ... keep only those reads that contain junctions that passed filtering into SJ.out.tab",
            ),
            ToolInput(
                "outFilterMultimapScoreRange",
                Int(optional=True),
                prefix="--outFilterMultimapScoreRange",
                doc="(default: 1) the score range below the maximum score for multimapping alignments",
            ),
            ToolInput(
                "outFilterMultimapNmax",
                Int(optional=True),
                prefix="--outFilterMultimapNmax",
                doc='(default: 10) maximum number of loci the read is allowed to map to. Alignments (all of them) will be output only if the read maps to no more loci than this value.  Otherwise no alignments will be output, and the read will be counted as "mapped to too many loci" in the Log.final.out .',
            ),
            ToolInput(
                "outFilterMismatchNmax",
                Int(optional=True),
                prefix="--outFilterMismatchNmax",
                doc="(default: 10) alignment will be output only if it has no more mismatches than this value.",
            ),
            ToolInput(
                "outFilterMismatchNoverLmax",
                Float(optional=True),
                prefix="--outFilterMismatchNoverLmax",
                doc="(default: 0.3) alignment will be output only if its ratio of mismatches to *mapped* length is less than or equal to this value.",
            ),
            ToolInput(
                "outFilterMismatchNoverReadLmax",
                Float(optional=True),
                prefix="--outFilterMismatchNoverReadLmax",
                doc="(default: 1) alignment will be output only if its ratio of mismatches to *read* length is less than or equal to this value.",
            ),
            ToolInput(
                "outFilterScoreMin",
                Int(optional=True),
                prefix="--outFilterScoreMin",
                doc="(default: 0) alignment will be output only if its score is higher than or equal to this value.",
            ),
            ToolInput(
                "outFilterScoreMinOverLread",
                Float(optional=True),
                prefix="--outFilterScoreMinOverLread",
                doc="(default: 0.66) same as outFilterScoreMin, but  normalized to read length (sum of mates' lengths for paired-end reads)",
            ),
            ToolInput(
                "outFilterMatchNmin",
                Int(optional=True),
                prefix="--outFilterMatchNmin",
                doc="(default: 0) alignment will be output only if the number of matched bases is higher than or equal to this value.",
            ),
            ToolInput(
                "outFilterMatchNminOverLread",
                Float(optional=True),
                prefix="--outFilterMatchNminOverLread",
                doc="(default: 0.66) sam as outFilterMatchNmin, but normalized to the read length (sum of mates' lengths for paired-end reads).",
            ),
            ToolInput(
                "outFilterIntronMotifs",
                String(optional=True),
                prefix="--outFilterIntronMotifs",
                doc="(default: None) filter alignment using their motifs None",
            ),
            ToolInput(
                "outFilterIntronStrands",
                String(optional=True),
                prefix="--outFilterIntronStrands",
                doc="(default: RemoveInconsistentStrands) filter alignments RemoveInconsistentStrands      ... remove alignments that have junctions with inconsistent strands None",
            ),
            ToolInput(
                "outSJfilterReads",
                String(optional=True),
                prefix="--outSJfilterReads",
                doc="(default: All) which reads to consider for collapsed splice junctions output all reads, unique- and multi-mappers uniquely mapping reads only",
            ),
            ToolInput(
                "outSJfilterOverhangMin",
                Int(optional=True),
                prefix="--outSJfilterOverhangMin",
                doc="(default: 30 12 12 12) minimum overhang length for splice junctions on both sides for: (1) non-canonical motifs, (2) GT/AG and CT/AC motif, (3) GC/AG and CT/GC motif, (4) AT/AC and GT/AT motif. -1 means no output for that motif does not apply to annotated junctions",
            ),
            ToolInput(
                "outSJfilterCountUniqueMin",
                Int(optional=True),
                prefix="--outSJfilterCountUniqueMin",
                doc="(default: 3 1 1 1) minimum uniquely mapping read count per junction for: (1) non-canonical motifs, (2) GT/AG and CT/AC motif, (3) GC/AG and CT/GC motif, (4) AT/AC and GT/AT motif. -1 means no output for that motif Junctions are output if one of outSJfilterCountUniqueMin OR outSJfilterCountTotalMin conditions are satisfied does not apply to annotated junctions",
            ),
            ToolInput(
                "outSJfilterCountTotalMin",
                Int(optional=True),
                prefix="--outSJfilterCountTotalMin",
                doc="(default: 3 1 1 1) minimum total (multi-mapping+unique) read count per junction for: (1) non-canonical motifs, (2) GT/AG and CT/AC motif, (3) GC/AG and CT/GC motif, (4) AT/AC and GT/AT motif. -1 means no output for that motif Junctions are output if one of outSJfilterCountUniqueMin OR outSJfilterCountTotalMin conditions are satisfied does not apply to annotated junctions",
            ),
            ToolInput(
                "outSJfilterDistToOtherSJmin",
                Int(optional=True),
                prefix="--outSJfilterDistToOtherSJmin",
                doc="(default: 10 0 5 10) minimum allowed distance to other junctions' donor/acceptor does not apply to annotated junctions",
            ),
            ToolInput(
                "outSJfilterIntronMaxVsReadN",
                Int(optional=True),
                prefix="--outSJfilterIntronMaxVsReadN",
                doc="(default: 50000 100000 200000) maximum gap allowed for junctions supported by 1,2,3,,,N reads <=200000. by >=4 reads any gap <=alignIntronMax does not apply to annotated junctions",
            ),
            ToolInput(
                "scoreGap",
                Int(optional=True),
                prefix="--scoreGap",
                doc="(default: 0) splice junction penalty (independent on intron motif)",
            ),
            ToolInput(
                "scoreGapNoncan",
                Int(optional=True),
                prefix="--scoreGapNoncan",
                doc="(default: 8) non-canonical junction penalty (in addition to scoreGap)",
            ),
            ToolInput(
                "scoreGapGCAG",
                Int(optional=True),
                prefix="--scoreGapGCAG",
                doc="(default: 4) GC/AG and CT/GC junction penalty (in addition to scoreGap)",
            ),
            ToolInput(
                "scoreGapATAC",
                Int(optional=True),
                prefix="--scoreGapATAC",
                doc="(default: 8) AT/AC  and GT/AT junction penalty  (in addition to scoreGap)",
            ),
            ToolInput(
                "scoreGenomicLengthLog2scale",
                Float(optional=True),
                prefix="--scoreGenomicLengthLog2scale",
                doc="(default: -0.25) scoreGenomicLengthLog2scale*log2(genomicLength)",
            ),
            ToolInput(
                "scoreDelOpen",
                Int(optional=True),
                prefix="--scoreDelOpen",
                doc="(default: 2) deletion open penalty",
            ),
            ToolInput(
                "scoreDelBase",
                Int(optional=True),
                prefix="--scoreDelBase",
                doc="(default: 2) deletion extension penalty per base (in addition to scoreDelOpen)",
            ),
            ToolInput(
                "scoreInsOpen",
                Int(optional=True),
                prefix="--scoreInsOpen",
                doc="(default: 2) insertion open penalty",
            ),
            ToolInput(
                "scoreInsBase",
                Int(optional=True),
                prefix="--scoreInsBase",
                doc="(default: 2) insertion extension penalty per base (in addition to scoreInsOpen)",
            ),
            ToolInput(
                "scoreStitchSJshift",
                Int(optional=True),
                prefix="--scoreStitchSJshift",
                doc="(default: 1) maximum score reduction while searching for SJ boundaries inthe stitching step",
            ),
            ToolInput(
                "seedSearchStartLmax",
                Int(optional=True),
                prefix="--seedSearchStartLmax",
                doc="(default: 50) defines the search start point through the read - the read is split into pieces no longer than this value",
            ),
            ToolInput(
                "seedSearchStartLmaxOverLread",
                Float(optional=True),
                prefix="--seedSearchStartLmaxOverLread",
                doc="(default: 1) seedSearchStartLmax normalized to read length (sum of mates' lengths for paired-end reads)",
            ),
            ToolInput(
                "seedSearchLmax",
                Int(optional=True),
                prefix="--seedSearchLmax",
                doc="(default: 0) defines the maximum length of the seeds, if =0 max seed lengthis infinite",
            ),
            ToolInput(
                "seedMultimapNmax",
                Int(optional=True),
                prefix="--seedMultimapNmax",
                doc="(default: 10000) only pieces that map fewer than this value are utilized in the stitching procedure",
            ),
            ToolInput(
                "seedPerReadNmax",
                Int(optional=True),
                prefix="--seedPerReadNmax",
                doc="(default: 1000) max number of seeds per read",
            ),
            ToolInput(
                "seedPerWindowNmax",
                Int(optional=True),
                prefix="--seedPerWindowNmax",
                doc="(default: 50) max number of seeds per window",
            ),
            ToolInput(
                "seedNoneLociPerWindow",
                Int(optional=True),
                prefix="--seedNoneLociPerWindow",
                doc="(default: 10) max number of one seed loci per window",
            ),
            ToolInput(
                "seedSplitMin",
                Int(optional=True),
                prefix="--seedSplitMin",
                doc="(default: 12) min length of the seed sequences split by Ns or mate gap",
            ),
            ToolInput(
                "alignIntronMin",
                Int(optional=True),
                prefix="--alignIntronMin",
                doc="(default: 21) genomic gap is considered intron if its length>=alignIntronMin, otherwise it is considered Deletion",
            ),
            ToolInput(
                "alignIntronMax",
                Int(optional=True),
                prefix="--alignIntronMax",
                doc="(default: 0) maximum intron size, if 0, max intron size will be determined by (2^winBinNbits)*winAnchorDistNbins",
            ),
            ToolInput(
                "alignMatesGapMax",
                Int(optional=True),
                prefix="--alignMatesGapMax",
                doc="(default: 0) maximum gap between two mates, if 0, max intron gap will be determined by (2^winBinNbits)*winAnchorDistNbins",
            ),
            ToolInput(
                "alignSJoverhangMin",
                Int(optional=True),
                prefix="--alignSJoverhangMin",
                doc="(default: 5) minimum overhang (i.e. block size) for spliced alignments",
            ),
            ToolInput(
                "alignSJstitchMismatchNmax",
                Array(Int(), optional=True),
                prefix="--alignSJstitchMismatchNmax",
                doc="(default: 0 -1 0 0) maximum number of mismatches for stitching of the splice junctions (-1: no limit).     (1) non-canonical motifs, (2) GT/AG and CT/AC motif, (3) GC/AG and CT/GC motif, (4) AT/AC and GT/AT motif.",
            ),
            ToolInput(
                "alignSJDBoverhangMin",
                Int(optional=True),
                prefix="--alignSJDBoverhangMin",
                doc="(default: 3) minimum overhang (i.e. block size) for annotated (sjdb) spliced alignments",
            ),
            ToolInput(
                "alignSplicedMateMapLmin",
                Int(optional=True),
                prefix="--alignSplicedMateMapLmin",
                doc="(default: 0) minimum mapped length for a read mate that is spliced",
            ),
            ToolInput(
                "alignSplicedMateMapLminOverLmate",
                Float(optional=True),
                prefix="--alignSplicedMateMapLminOverLmate",
                doc="(default: 0.66) alignSplicedMateMapLmin normalized to mate length",
            ),
            ToolInput(
                "alignWindowsPerReadNmax",
                Int(optional=True),
                prefix="--alignWindowsPerReadNmax",
                doc="(default: 10000) max number of windows per read",
            ),
            ToolInput(
                "alignTranscriptsPerWindowNmax",
                Int(optional=True),
                prefix="--alignTranscriptsPerWindowNmax",
                doc="(default: 100) max number of transcripts per window",
            ),
            ToolInput(
                "alignTranscriptsPerReadNmax",
                Int(optional=True),
                prefix="--alignTranscriptsPerReadNmax",
                doc="(default: 10000) max number of different alignments per read to consider",
            ),
            ToolInput(
                "alignEndsType",
                String(optional=True),
                prefix="--alignEndsType",
                doc="(default: Local) type of read ends alignment Local",
            ),
            ToolInput(
                "alignEndsProtrude",
                Int(optional=True),
                prefix="--alignEndsProtrude",
                doc="(default: 0 ConcordantPair) allow protrusion of alignment ends, i.e. start (end) of the +strand mate downstream of the start (end) of the -strand mate maximum number of protrusion bases allowed string:     ConcordantPair ... report alignments with non-zero protrusion as concordant pairs     DiscordantPair ... report alignments with non-zero protrusion as discordant pairs",
            ),
            ToolInput(
                "alignSoftClipAtReferenceEnds",
                String(optional=True),
                prefix="--alignSoftClipAtReferenceEnds",
                doc="(default: Yes) allow the soft-clipping of the alignments past the end of the chromosomes Yes ... allow No  ... prohibit, useful for compatibility with Cufflinks",
            ),
            ToolInput(
                "alignInsertionFlush",
                String(optional=True),
                prefix="--alignInsertionFlush",
                doc="(default: None) how to flush ambiguous insertion positions None    ... insertions are not flushed Right   ... insertions are flushed to the right",
            ),
            ToolInput(
                "peOverlapNbasesMin",
                Int(optional=True),
                prefix="--peOverlapNbasesMin",
                doc="(default: 0) minimum number of overlap bases to trigger mates merging and realignment",
            ),
            ToolInput(
                "peOverlapMMp",
                Float(optional=True),
                prefix="--peOverlapMMp",
                doc="(default: 0.01) maximum proportion of mismatched bases in the overlap area",
            ),
            ToolInput(
                "winAnchorMultimapNmax",
                Int(optional=True),
                prefix="--winAnchorMultimapNmax",
                doc="(default: 50) max number of loci anchors are allowed to map to",
            ),
            ToolInput(
                "winBinNbits",
                Int(optional=True),
                prefix="--winBinNbits",
                doc="(default: 16) =LOG2(winBin), where winBin is the size of the bin for the windows/clustering, each window will occupy an integer number of bins.",
            ),
            ToolInput(
                "winAnchorDistNbins",
                Int(optional=True),
                prefix="--winAnchorDistNbins",
                doc="(default: 9) max number of bins between two anchors that allows aggregation of anchors into one window",
            ),
            ToolInput(
                "winFlankNbins",
                Int(optional=True),
                prefix="--winFlankNbins",
                doc="(default: 4) log2(winFlank), where win Flank is the size of the left and right flanking regions for each window",
            ),
            ToolInput(
                "winReadCoverageRelativeMin",
                Float(optional=True),
                prefix="--winReadCoverageRelativeMin",
                doc="(default: 0.5) minimum relative coverage of the read sequence by the seeds in a window, for STARlong algorithm only.",
            ),
            ToolInput(
                "winReadCoverageBasesMin",
                Int(optional=True),
                prefix="--winReadCoverageBasesMin",
                doc="(default: 0) minimum number of bases covered by the seeds in a window , for STARlong algorithm only.",
            ),
            ToolInput(
                "chimOutType",
                String(optional=True),
                prefix="--chimOutType",
                doc="(default: Junctions) type of chimeric output     Junctions       ... Chimeric.out.junction     SeparateSAMold  ... output old SAM into separate Chimeric.out.sam file     WithinBAM       ... output into main aligned BAM files (Aligned.*.bam)     WithinBAM HardClip  ... (default) hard-clipping in the CIGAR for supplemental chimeric alignments (defaultif no 2nd word is present)     WithinBAM SoftClip  ... soft-clipping in the CIGAR for supplemental chimeric alignments",
            ),
            ToolInput(
                "chimSegmentMin",
                Int(optional=True),
                prefix="--chimSegmentMin",
                doc="(default: 0) minimum length of chimeric segment length, if ==0, no chimeric output",
            ),
            ToolInput(
                "chimScoreMin",
                Int(optional=True),
                prefix="--chimScoreMin",
                doc="(default: 0) minimum total (summed) score of the chimeric segments",
            ),
            ToolInput(
                "chimScoreDropMax",
                Int(optional=True),
                prefix="--chimScoreDropMax",
                doc="(default: 20) max drop (difference) of chimeric score (the sum of scores of all chimeric segments) from the read length",
            ),
            ToolInput(
                "chimScoreSeparation",
                Int(optional=True),
                prefix="--chimScoreSeparation",
                doc="(default: 10) minimum difference (separation) between the best chimeric score and the next one",
            ),
            ToolInput(
                "chimScoreJunctionNonGTAG",
                Int(optional=True),
                prefix="--chimScoreJunctionNonGTAG",
                doc="(default: -1) penalty for a non-GT/AG chimeric junction",
            ),
            ToolInput(
                "chimJunctionOverhangMin",
                Int(optional=True),
                prefix="--chimJunctionOverhangMin",
                doc="(default: 20) minimum overhang for a chimeric junction",
            ),
            ToolInput(
                "chimSegmentReadGapMax",
                Int(optional=True),
                prefix="--chimSegmentReadGapMax",
                doc="(default: 0) maximum gap in the read sequence between chimeric segments",
            ),
            ToolInput(
                "chimFilter",
                String(optional=True),
                prefix="--chimFilter",
                doc="(default: banGenomicN) different filters for chimeric alignments     None ... no filtering     banGenomicN ... Ns are not allowed in the genome sequence around the chimeric junction",
            ),
            ToolInput(
                "chimMainSegmentMultNmax",
                Int(optional=True),
                prefix="--chimMainSegmentMultNmax",
                doc="(default: 10) maximum number of multi-alignments for the main chimeric segment. =1 will prohibit multimapping main segments.",
            ),
            ToolInput(
                "chimMultimapNmax",
                Int(optional=True),
                prefix="--chimMultimapNmax",
                doc="(default: 0) maximum number of chimeric multi-alignments 0 ... use the old scheme for chimeric detection which only considered unique alignments",
            ),
            ToolInput(
                "chimMultimapScoreRange",
                Int(optional=True),
                prefix="--chimMultimapScoreRange",
                doc="(default: 1) the score range for multi-mapping chimeras below the best chimeric score. Only works with --chimMultimapNmax > 1",
            ),
            ToolInput(
                "chimNonchimScoreDropMin",
                Int(optional=True),
                prefix="--chimNonchimScoreDropMin",
                doc="(default: 20) to trigger chimeric detection, the drop in the best non-chimeric alignment score with respect to the read length has to be greater than this value ... none     TranscriptomeSAM ... output SAM/BAM alignments to transcriptome into a separate file     GeneCounts       ... count reads per gene",
            ),
            ToolInput(
                "chimOutJunctionFormat",
                Int(optional=True),
                prefix="--chimOutJunctionFormat",
                doc="(default: 0) formatting type for the Chimeric.out.junction file 0 ... no comment lines/headers total, unique, multi",
            ),
            ToolInput(
                "quantMode",
                String(optional=True),
                prefix="--quantMode",
                doc="(default: -) types of quantification requested     -        ... prohibit single-end alignments",
            ),
            ToolInput(
                "quantTranscriptomeBAMcompression",
                Int(optional=True),
                prefix="--quantTranscriptomeBAMcompression",
                doc="(default: 1 1) -2 to 10  transcriptome BAM compression level     -2  ... no BAM output     -1  ... default compression (6?)      0  ... no compression      10 ... maximum compression ... 1-pass mapping     Basic       ... basic 2-pass mapping, with all 1st pass junctions inserted into the genome indices on the fly",
            ),
            ToolInput(
                "quantTranscriptomeBan",
                String(optional=True),
                prefix="--quantTranscriptomeBan",
                doc="(default: IndelSoftclipSingleend) prohibit various alignment type     IndelSoftclipSingleend  ... prohibit indels, soft clipping and single-end alignments - compatible with RSEM     Singleend",
            ),
            ToolInput(
                "twopassMode",
                String(optional=True),
                prefix="--twopassMode",
                doc="(default: None) 2-pass mapping mode.     None",
            ),
            ToolInput(
                "twopass1readsN",
                Int(optional=True),
                prefix="--twopass1readsN",
                doc="(default: 1) number of reads to process for the 1st step. Use very large number (or default -1) to map all reads in the first step.",
            ),
            ToolInput(
                "waspOutputMode",
                String(optional=True),
                prefix="--waspOutputMode",
                doc="(default: None) Nature Methods 12, 1061–1063 (2015), https://www.nature.com/articles/nmeth.3582 .     SAMtag      ... add WASP tags to the alignments that pass WASP filtering",
            ),
            ToolInput(
                "soloType",
                String(optional=True),
                prefix="--soloType",
                doc="(default: None) type of single-cell RNA-seq     CB_UMI_Simple   ... (a.k.a. Droplet) one UMI and one Cell Barcode of fixed length in read2, e.g. Drop-seq and 10X Chromium     CB_UMI_Complex  ... one UMI of fixed length, but multiple Cell Barcodes of varying length, as well as adapters sequences are allowed in read2 only, e.g. inDrop.",
            ),
            ToolInput(
                "soloCBwhitelist",
                String(optional=True),
                prefix="--soloCBwhitelist",
                doc="(default: -) file(s) with whitelist(s) of cell barcodes. Only one file allowed with ",
            ),
            ToolInput(
                "soloCBstart",
                Int(optional=True),
                prefix="--soloCBstart",
                doc="(default: 1) cell barcode start base",
            ),
            ToolInput(
                "soloCBlen",
                Int(optional=True),
                prefix="--soloCBlen",
                doc="(default: 16) cell barcode length",
            ),
            ToolInput(
                "soloUMIstart",
                Int(optional=True),
                prefix="--soloUMIstart",
                doc="(default: 17) UMI start base",
            ),
            ToolInput(
                "soloUMIlen",
                Int(optional=True),
                prefix="--soloUMIlen",
                doc="(default: 10) UMI length",
            ),
            ToolInput(
                "soloBarcodeReadLength",
                Int(optional=True),
                prefix="--soloBarcodeReadLength",
                doc="(default: 1) length of the barcode read     1   ... equal to sum of soloCBlen+soloUMIlen     0   ... not defined, do not check",
            ),
            ToolInput(
                "soloCBposition",
                Array(String(), optional=True),
                prefix="--soloCBposition",
                doc="(default: -) position of Cell Barcode(s) on the barcode read.     Presently only works with --soloType CB_UMI_Complex, and barcodes are assumed to be on Read2. startAnchor_startDistance_endAnchor_endDistance adapter end     start(end)Distance is the distance from the CB start(end) to the Anchor base     String for different barcodes are separated by space. inDrop (Zilionis et al, Nat. Protocols, 2017):     --soloCBposition  0_0_2_-1  3_1_3_8",
            ),
            ToolInput(
                "soloUMIposition",
                String(optional=True),
                prefix="--soloUMIposition",
                doc="(default: -) position of the UMI on the barcode read, same as soloCBposition inDrop (Zilionis et al, Nat. Protocols, 2017):     --soloCBposition  3_9_3_14",
            ),
            ToolInput(
                "soloAdapterSequence",
                String(optional=True),
                prefix="--soloAdapterSequence",
                doc="(default: -) adapter sequence to anchor barcodes.    ... only exact matches allowed     1MM         ... only one match in whitelist with 1 mismatched base allowed. Allowed CBs have to have at least one read with exact match.     1MM_multi         ... multiple matches in whitelist with 1 mismatched base allowed, posterior probability calculation is used choose one of the matches.  Allowed CBs have to have at least one read with exact match. Similar to CellRanger 2.2.0     1MM_multi_pseudocounts  ... same as 1MM_Multi, but pseudocounts of 1 are added to all whitelist barcodes. Similar to CellRanger 3.x.x ",
            ),
            ToolInput(
                "soloAdapterMismatchesNmax",
                Int(optional=True),
                prefix="--soloAdapterMismatchesNmax",
                doc="(default: 1) maximum number of mismatches allowed in adapter sequence.",
            ),
            ToolInput(
                "soloCBmatchWLtype",
                String(optional=True),
                prefix="--soloCBmatchWLtype",
                doc="(default: 1MM_multi) matching the Cell Barcodes to the WhiteList     Exact",
            ),
            ToolInput(
                "soloStrand",
                String(optional=True),
                prefix="--soloStrand",
                doc='(default: Forward) strandedness of the solo libraries:     Unstranded  ... no strand information     Forward     ... read strand same as the original RNA molecule     Reverse     ... read strand opposite to the original RNA molecule .. all UMIs with 1 mismatch distance to each other are collapsed (i.e. counted once)     1MM_Directional     ... follows the "directional" method from the UMI-tools by Smith, Heger and Sudbery (Genome Research 2017).     Exact       ... only exactly matching UMIs are collapsed',
            ),
            ToolInput(
                "soloFeatures",
                String(optional=True),
                prefix="--soloFeatures",
                doc="(default: Gene) genomic features for which the UMI counts per Cell Barcode are collected reads match the gene transcript reported in SJ.out.tab count all reads overlapping genes' exons and introns     Transcript3p   ... quantification of transcript for 3' protocols",
            ),
            ToolInput(
                "soloUMIdedup",
                String(optional=True),
                prefix="--soloUMIdedup",
                doc="(default: 1MM_All) type of UMI deduplication (collapsing) algorithm     1MM_All",
            ),
            ToolInput(
                "soloUMIfiltering",
                String(optional=True),
                prefix="--soloUMIfiltering",
                doc="(default: -) type of UMI filtering remove UMIs with N and homopolymers (similar to CellRanger 2.2.0)     MultiGeneUMI    ... remove lower-count UMIs that map to more than one gene (introduced in CellRanger 3.x.x)",
            ),
            ToolInput(
                "soloOutFileNames",
                String(optional=True),
                prefix="--soloOutFileNames",
                doc="(default: Solo.out/  features.tsv barcodes.tsv matrix.mtx) file names for STARsolo output:     file_name_prefix   gene_names   barcode_sequences   cell_feature_count_matrix",
            ),
            ToolInput(
                "soloCellFilter",
                String(optional=True),
                prefix="--soloCellFilter",
                doc='(default: CellRanger2.2 3000 0.99 10) ... all UMIs with 1 mismatch distance to each other are collapsed (i.e. counted once)     1MM_Directional     ... follows the "directional" method from the UMI-tools by Smith, Heger and Sudbery (Genome Research 2017).     Exact       ... only exactly matching UMIs are collapsed',
            ),
        ]

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Jiaan Yu", "Michael Franklin"],
            dateCreated=date(2020, 5, 29),
            dateUpdated=date(2020, 5, 29),
            institution="Cold Spring Harbor Laboratory",
            doi="https://doi.org/10.1093/bioinformatics/bts635",
            citation="Dobin A, Davis CA, Schlesinger F, et al. STAR: ultrafast universal RNA-seq aligner. Bioinformatics. 2013;29(1):15‐21. doi:10.1093/bioinformatics/bts635",
            keywords=["star", "align", "rna", "rnaSeq"],
            documentationUrl="https://github.com/alexdobin/STAR",
            documentation="""\
Spliced Transcripts Alignment to a Reference © Alexander Dobin, 2009-2019 

For more details see:

- https://www.ncbi.nlm.nih.gov/pubmed/23104886
- https://github.com/alexdobin/STAR
- https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf
""",
        )
