from abc import ABC, abstractmethod

from ..bioinformaticstoolbase import BioinformaticsTool
from janis_core import ToolMetadata


class VcfToolsToolBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "ekg"
