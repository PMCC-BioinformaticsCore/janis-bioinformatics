from janis_core import WorkflowMetadata, Directory, String, File

from janis_bioinformatics.data_types import Fasta, FastqGzPair

from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.star import StarAlignReads_2_7_1
from janis_bioinformatics.tools.suhrig import Arriba_1_2_0
from janis_bioinformatics.tools.usadellab import TrimmomaticPairedEnd_0_35


class StarArriba_0_1_0(BioinformaticsWorkflow):
    def id(self) -> str:
        return "StarArriba"

    def friendly_name(self):
        return "Star Arriba Workflow"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def bind_metadata(self):
        return WorkflowMetadata(version="v0.1.0", contributors=["Jiaan Yu"])

    def constructor(self):
        self.input("sampleName", String)
        self.input("reads", FastqGzPair)
        self.input("genomeDir", Directory)
        self.input("reference", Fasta)
        self.input("gtf", File)
        self.input("blacklist", File)
        self.input("contigs", String(optional=True))

        self.step(
            "trim",
            TrimmomaticPairedEnd_0_35(
                sampleName=self.sampleName,
                inp=self.reads,
                phred33=True,
                steps=[
                    "ILLUMINACLIP:/usr/local/share/trimmomatic-0.35-6/adapters/TruSeq2-PE.fa:2:30:10",
                    "LEADING:15",
                    "TRAILING:15",
                    "SLIDINGWINDOW:4:15",
                    "MINLEN:35",
                ],
            ),
            doc="Trim reads using Trimmomatic",
        )

        self.step(
            "star",
            StarAlignReads_2_7_1(
                readFilesIn=self.trim.pairedOut,
                genomeDir=self.genomeDir,
                limitOutSJcollapsed=3000000,  # lots of splice junctions may need more than default 1M buffer
                readFilesCommand="zcat",
                outSAMtype=["BAM", "Unsorted"],
                outSAMunmapped="Within",
                outBAMcompression=0,
                outFilterMultimapNmax=1,
                outFilterMismatchNmax=3,
                chimSegmentMin=10,
                chimOutType=["WithinBAM", "SoftClip"],
                chimJunctionOverhangMin=10,
                chimScoreMin=1,
                chimScoreDropMax=30,
                chimScoreJunctionNonGTAG=0,
                chimScoreSeparation=1,
                alignSJstitchMismatchNmax=[5, -1, 5, 5],
                chimSegmentReadGapMax=3,
            ),
        )

        self.step(
            "arriba",
            Arriba_1_2_0(
                aligned_inp=self.star.out_bam.assert_not_null(),
                blacklist=self.blacklist,
                fusion_transcript=True,
                peptide_sequence=True,
                reference=self.reference,
                gtf_file=self.gtf,
                contigs=self.contigs,
            ),
        )

        self.output("out_fusion", source=self.arriba.out)
        self.output("out_fusion_discarded", source=self.arriba.out_discarded)


if __name__ == "__main__":
    StarArriba_0_1_0.translate("cwl")
