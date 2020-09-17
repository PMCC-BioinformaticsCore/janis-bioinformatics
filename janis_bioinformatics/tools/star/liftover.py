from abc import ABC
from typing import List

from janis_core import ToolOutput

from janis_bioinformatics.tools.star.base import StarBase


class StarLiftOverBase(StarBase, ABC):
    def run_mode(self):
        return "liftOver"

    def outputs(self) -> List[ToolOutput]:
        pass
