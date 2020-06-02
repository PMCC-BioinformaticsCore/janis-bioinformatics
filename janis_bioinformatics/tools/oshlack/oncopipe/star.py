from janis_core import StringFormatter, Directory

from janis_bioinformatics.data_types import Vcf, FastqGzPairedEnd, Fasta
from janis_bioinformatics.tools import BioinformaticsWorkflow
from janis_bioinformatics.tools.ensembl import VepCacheLatest, FilterVep_98_3
from janis_bioinformatics.tools.star.versions import (
    StarAlignReads_2_7_1,
    StarGenerateIndexes_2_7_1,
)
from janis_bioinformatics.tools.usadellab import TrimmomaticPairedEnd_0_35


class OncopipeStarAligner(BioinformaticsWorkflow):
    def id(self) -> str:
        return "oncopipe_STAR"

    def friendly_name(self):
        return "Oncopipe: StarAligner"

    def constructor(self):

        #     trim +
        #     star_map_1pass_PE +
        #     star_gen2pass +
        #     star_map_2pass_PE

        self.input("sampleName", str)
        self.input("reads", FastqGzPairedEnd)
        self.input("genomeDir", Directory)

        self.input("reference", Fasta)
        self.input("gtf", str)  # ?

        self.input("sample", str)
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
                    "ILLUMINACLIP:$ADAPTERS_FASTA:2:30:10",
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
            ),
            doc="Map reads using the STAR aligner: 1st pass",
        )

        self.step(
            "star_gen2pass",
            StarGenerateIndexes_2_7_1(
                genomeFastaFiles=self.reference,
                genomeDir=None,
                # sjdbFileChrStartEnd=self.star_map_1pass_PE.sjout, # will fail for now
                sjdbOverhang=99,
                sjdbGTFfile=self.gtf,
                limitOutSJcollapsed=3000000,  # lots of splice junctions may need more than default 1M buffer
            ),
            doc="Map reads using the STAR aligner: generate genome",
        )

        self.step(
            "star_map_2pass_PE",
            StarAlignReads_2_7_1(
                readFilesCommand="zcat",
                outSAMattrRGline=StringFormatter(
                    "ID:{sample} SM:{lane} LB:{library} PL:{platform} PU:1",
                    sample=self.sample,
                    lane=self.lane,
                    library=self.library,
                    platform=self.platform,
                ),
                outSAMtype=["BAM", "Unsorted", "SortedByCoordinate"],
                quantMode="TranscriptomeSAM",
            ),
        )


if __name__ == "__main__":
    OncopipeStarAligner().translate("cwl")
