from abc import ABC, abstractmethod
from datetime import date

from ..bioinformaticstoolbase import BioinformaticsTool
from janis_core import ToolMetadata


class BedToolsToolBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "bedtools"
