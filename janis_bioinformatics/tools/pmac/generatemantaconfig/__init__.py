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
            out.write(
                "# change default value of \
enableRemoteReadRetrievalForInsertionsInGermlineCallingModes to 0\n\
minCandidateSpanningCount = 3\n\
minDiploidVariantScore = 10\n\
minPassDiploidVariantScore = 20\n\
minPassDiploidGTScore = 15\n\
minSomaticScore = 10\n\
minPassSomaticScore = 30\n\
enableRemoteReadRetrievalForInsertionsInGermlineCallingModes = 0\n\
enableRemoteReadRetrievalForInsertionsInCancerCallingModes = 0\n\
useOverlapPairEvidence = 0"
            )
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
