from abc import ABC
from typing import List

from janis_core import ToolOutput, InputSelector, Directory, WildcardSelector

from janis_bioinformatics.tools.star.base import StarBase


class StarGenerateIndexesBase(StarBase, ABC):
    def run_mode(self):
        return "genomeGenerate"

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput(
                "out", Directory, selector=WildcardSelector(".", select_first=True)
            )
        ]
