from abc import ABC
from typing import List

from janis_core import ToolOutput, InputSelector, Directory, WildcardSelector

from janis_bioinformatics.tools.star.base import StarBase


class StarGenerateIndexesBase(StarBase, ABC):
    def memory(self):
        return 64

    def run_mode(self):
        return "genomeGenerate"

    def directories_to_create(self):
        return [InputSelector("outputGenomeDir")]

    def outputs(self) -> List[ToolOutput]:
        return [ToolOutput("out", Directory, selector=InputSelector("outputGenomeDir"))]


# if __name__ == "__main__":
#     StarGenerateIndexesBase().translate("cwl")
