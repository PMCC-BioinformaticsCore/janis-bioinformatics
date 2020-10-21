from abc import ABC, abstractmethod

from janis_bioinformatics.tools import BioinformaticsTool


class SubreadToolBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "Subread"

    @classmethod
    @abstractmethod
    def subread_command(cls):
        raise Exception("Tool or command not found")

    @classmethod
    def base_command(cls):
        return ["", cls.subread_command()]

    def inputs(self):
        return []

    def doc(self):
        return """
    Subread package: high-performance read alignment, quantification and mutation discovery
The Subread package comprises a suite of software programs for processing next-gen sequencing read data including:

Subread: a general-purpose read aligner which can align both genomic DNA-seq and RNA-seq reads. It can also be used to discover genomic mutations including short indels and structural variants.
Subjunc: a read aligner developed for aligning RNA-seq reads and for the detection of exon-exon junctions. Gene fusion events can be detected as well.
featureCounts: a software program developed for counting reads to genomic features such as genes, exons, promoters and genomic bins.
Sublong: a long-read aligner that is designed based on seed-and-vote.
exactSNP: a SNP caller that discovers SNPs by testing signals against local background noises.
These programs were also implemented in Bioconductor R package Rsubread.

    Documentation: http://subread.sourceforge.net/""".strip()

    @abstractmethod
    def container(self):
        raise Exception(
            "An error likely occurred when resolving the method order for docker"
        )

    def arguments(self):
        return []
