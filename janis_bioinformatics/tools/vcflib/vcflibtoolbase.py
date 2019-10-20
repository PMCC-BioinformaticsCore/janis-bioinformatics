from abc import ABC, abstractmethod

from ..bioinformaticstoolbase import BioinformaticsTool
from janis_core import ToolMetadata


class VcfToolsToolBase(BioinformaticsTool, ABC):
    @staticmethod
    def tool_provider():
        return "ekg"
