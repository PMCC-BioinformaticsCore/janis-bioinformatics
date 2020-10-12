from janis_core import StringFormatter, Directory, File, WorkflowMetadata

from janis_bioinformatics.data_types import FastqGzPair, Fasta
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.star.versions import (
    StarAlignReads_2_7_1,
    StarGenerateIndexes_2_7_1,
)
from janis_bioinformatics.tools.usadellab import TrimmomaticPairedEnd_0_35


class OncopipeStarAligner(BioinformaticsWorkflow):
    def id(self) -> str:
        return "oncopipe_STAR"

    # def friendly_name(self):
    #     return "Oncopipe: StarAligner"

    def bind_metadata(self):
        return WorkflowMetadata(
            version="v0.1.0", contributors=["Michael Franklin", "Jiaan Yu"]
        )

    def constructor(self):

        self.input("sampleName", str)
        self.input("reads", FastqGzPair)
        self.input("genomeDir", Directory)

        self.input("reference", Fasta)
        self.input("gtf", File)

        self.input("lane", str)
        self.input("library", str)
        self.input("platform", str)

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
            "star_map_1pass_PE",
            StarAlignReads_2_7_1(
                readFilesIn=self.trim.pairedOut,
                genomeDir=self.genomeDir,
                limitOutSJcollapsed=3000000,  # lots of splice junctions may need more than default 1M buffer
                readFilesCommand="zcat",
                outSAMtype=["None"],
            ),
            doc="Map reads using the STAR aligner: 1st pass",
        )

        self.step(
            "star_gen2pass",
            StarGenerateIndexes_2_7_1(
                genomeFastaFiles=self.reference,
                sjdbFileChrStartEnd=self.star_map_1pass_PE.SJ_out_tab,
                sjdbOverhang=99,
                sjdbGTFfile=self.gtf,
                limitOutSJcollapsed=3000000,  # lots of splice junctions may need more than default 1M buffer
                outputGenomeDir=".",
            ),
            doc="Map reads using the STAR aligner: generate genome",
        )

        self.step(
            "star_map_2pass_PE",
            StarAlignReads_2_7_1(
                readFilesIn=self.trim.pairedOut,
                readFilesCommand="zcat",
                genomeDir=self.star_gen2pass.out,
                outSAMattrRGline=StringFormatter(
                    "ID:{sample} SM:{lane} LB:{library} PL:{platform} PU:1",
                    sample=self.sampleName,
                    lane=self.lane,
                    library=self.library,
                    platform=self.platform,
                ),
                outSAMtype=["BAM", "SortedByCoordinate"],
            ),
        )

        self.output(
            "out_bam", source=self.star_map_2pass_PE.out_sorted_bam.assert_not_null()
        )


if __name__ == "__main__":
    OncopipeStarAligner().translate("cwl")
