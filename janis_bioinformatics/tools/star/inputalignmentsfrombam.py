from abc import ABC
from typing import List

from janis_core import ToolOutput

from janis_bioinformatics.tools.star.base import StarBase


class StarInputAlignmentsFromBamBase(StarBase, ABC):
    def run_mode(self):
        return "inputAlignmentsFromBAM"

    def outputs(self) -> List[ToolOutput]:
        pass

    def skip_test(cls) -> bool:
        return True
