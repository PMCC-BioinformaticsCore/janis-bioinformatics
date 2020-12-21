from janis_unix import UncompressArchive

from janis_bioinformatics.tools.common import IndexFasta
from janis_core import JanisTransformation, JanisTransformationGraph

from janis_bioinformatics.data_types import (
    CompressedVcf,
    VcfTabix,
    Vcf,
    Bam,
    BamBai,
    VcfIdx,
    Fasta,
    FastaWithIndexes,
    BedGz,
    Bed,
    BedTabix,
)

from janis_bioinformatics.tools.samtools import SamToolsIndex_1_9
from janis_bioinformatics.tools.htslib import Tabix_1_9, BGZip_1_9
from janis_bioinformatics.tools.igvtools import IgvIndexFeature_2_5_3

transformations = [
    JanisTransformation(Bam, BamBai, SamToolsIndex_1_9(), relevant_tool_input="bam"),
    JanisTransformation(Vcf, VcfIdx, IgvIndexFeature_2_5_3()),
    JanisTransformation(
        Vcf,
        CompressedVcf,
        BGZip_1_9(),
        relevant_tool_input="file",
        relevant_tool_output="out",
    ),
    JanisTransformation(
        CompressedVcf,
        VcfTabix,
        Tabix_1_9(),
        relevant_tool_input="inp",
        relevant_tool_output="out",
    ),
    JanisTransformation(Fasta, FastaWithIndexes, IndexFasta(bwa_algorithm="bwtsa")),
    JanisTransformation(
        BedGz,
        Bed,
        UncompressArchive(),
        relevant_tool_input="file",
        relevant_tool_output="out",
    ),
    JanisTransformation(
        Bed, BedGz, BGZip_1_9(), relevant_tool_input="file", relevant_tool_output="out",
    ),
    JanisTransformation(
        BedGz,
        BedTabix,
        Tabix_1_9(),
        relevant_tool_input="inp",
        relevant_tool_output="out",
    ),
]

if __name__ == "__main__":
    start = Bam

    graph = JanisTransformationGraph()
    graph.add_edges(transformations)

    wf = graph.build_workflow_to_translate(BamBai, BamBai)

    if wf is None:
        print("Types are already compatible")

    wf.translate("wdl")

# wf.get_dot_plot(show=True)
