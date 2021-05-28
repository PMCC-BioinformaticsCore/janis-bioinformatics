from datetime import datetime
from typing import List, Dict, Any

from janis_core import TOutput, File, OutputDocumentation
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsPythonTool


class GenerateMantaConfig(BioinformaticsPythonTool):
    @staticmethod
    def code_block(output_filename: str = "output.txt") -> Dict[str, Any]:
        """
        :param output_filename: Filename to output to
        """
        with open(output_filename, "w+") as out:
            out.write("\n")
            out.write("#\n")
            out.write(
                "# This section contains all configuration settings for the top-level manta workflow,\n"
            )
            out.write("#\n")
            out.write("[manta]\n")
            out.write("\n")
            out.write(
                "referenceFasta = /illumina/development/Isis/Genomes/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFasta/genome.fa\n"
            )
            out.write("\n")
            out.write(
                "# Run discovery and candidate reporting for all SVs/indels at or above this size\n"
            )
            out.write(
                "# Separate option (to provide different default) used for runs in RNA-mode\n"
            )
            out.write("minCandidateVariantSize = 8\n")
            out.write("rnaMinCandidateVariantSize = 1000\n")
            out.write("\n")
            out.write(
                "# Remove all edges from the graph unless they're supported by this many 'observations'.\n"
            )
            out.write(
                "# Note that one supporting read pair or split read usually equals one observation, but evidence is sometimes downweighted.\n"
            )
            out.write("minEdgeObservations = 3\n")
            out.write("\n")
            out.write(
                "# If both nodes of an edge have an edge count higher than this, then skip evaluation of the edge.\n"
            )
            out.write("# Set to 0 to turn this filtration off\n")
            out.write("graphNodeMaxEdgeCount = 10\n")
            out.write("\n")
            out.write(
                "# Run discovery and candidate reporting for all SVs/indels with at least this\n"
            )
            out.write("# many spanning support observations\n")
            out.write("minCandidateSpanningCount = 3\n")
            out.write("\n")
            out.write(
                "# After candidate identification, only score and report SVs/indels at or above this size:\n"
            )
            out.write("minScoredVariantSize = 50\n")
            out.write("\n")
            out.write(
                '# minimum VCF "QUAL" score for a variant to be included in the diploid vcf:\n'
            )
            out.write("minDiploidVariantScore = 10\n")
            out.write("\n")
            out.write(
                '# VCF "QUAL" score below which a variant is marked as filtered in the diploid vcf:\n'
            )
            out.write("minPassDiploidVariantScore = 20\n")
            out.write("\n")
            out.write(
                "# minimum genotype quality score below which single samples are filtered for a variant in the diploid vcf:\n"
            )
            out.write("minPassDiploidGTScore = 15\n")
            out.write("\n")
            out.write(
                "# somatic quality scores below this level are not included in the somatic vcf:\n"
            )
            out.write("minSomaticScore = 10\n")
            out.write("\n")
            out.write(
                "# somatic quality scores below this level are filtered in the somatic vcf:\n"
            )
            out.write("minPassSomaticScore = 30\n")
            out.write("\n")
            out.write(
                "# Remote read retrieval is used ot improve the assembly of putative insertions by retrieving any mate reads in remote\n"
            )
            out.write(
                "# locations with poor mapping quality, which pair to confidently mapping reads near the insertion locus. These reads\n"
            )
            out.write(
                "# can help to fully assemble longer insertions, under certain circumstances this feature can add a very large runtime\n"
            )
            out.write(
                "# burden. For instance, given the very high chimeric pair rates found in degraded FFPE samples, the runtime of the read\n"
            )
            out.write(
                "# retrieval process can be unpredicable. For this reason the feature is disabled by default for somatic variant calling.\n"
            )
            out.write(
                "# This feature can be enabled/disabled separately for germline and cancer calling below.\n"
            )
            out.write("#\n")
            out.write(
                '# Here "CancerCallingModes" includes tumor-normal subtraction and tumor-only calling. "GermlineCallingModes" includes\n'
            )
            out.write("# all other calling modes.\n")
            out.write("# custom set-up: https://github.com/Illumina/manta/issues/213\n")
            out.write(
                "enableRemoteReadRetrievalForInsertionsInGermlineCallingModes = 0\n"
            )
            out.write(
                "enableRemoteReadRetrievalForInsertionsInCancerCallingModes = 0\n"
            )
            out.write("\n")
            out.write(
                "# Set if an overlapping read pair will be considered as evidence\n"
            )
            out.write("# Set to 0 to skip overlapping read pairs\n")
            out.write("useOverlapPairEvidence = 0\n")
            out.write("\n")
            return {"out": output_filename}

    def outputs(self) -> List[TOutput]:
        return [
            TOutput(
                "out",
                File,
                doc=OutputDocumentation(doc="Custom Manta config file"),
            )
        ]

    def id(self) -> str:
        return "GenerateMantaConfig"

    def friendly_name(self) -> str:
        return "GenerateMantaConfig"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def version(self):
        return "v0.1.0"

    def bind_metadata(self):
        self.metadata.dateCreated = datetime(2021, 5, 27)
        self.metadata.dateUpdated = datetime(2021, 5, 27)
        self.metadata.contributors = ["Jiaan Yu"]
        self.metadata.documentation = """\
Generate custom manta config file.       
        """
