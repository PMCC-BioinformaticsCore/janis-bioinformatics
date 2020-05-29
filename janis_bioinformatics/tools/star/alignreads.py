from abc import ABC
from typing import List

from janis_core import ToolOutput

from janis_bioinformatics.tools.star.base import StarBase


class StarAlignReadsBase(StarBase, ABC):
    def run_mode(self):
        return "alignReads"

    def outputs(self) -> List[ToolOutput]:
        pass
