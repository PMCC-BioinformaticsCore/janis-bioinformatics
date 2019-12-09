from abc import ABC, abstractmethod
from datetime import date

from ..bioinformaticstoolbase import BioinformaticsTool
from janis_core import ToolMetadata


class BcfToolsToolBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "bcftools"
