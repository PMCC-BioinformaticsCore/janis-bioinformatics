from abc import ABC, abstractmethod
from datetime import date

from ..bioinformaticstoolbase import BioinformaticsTool
from janis_core import ToolMetadata


class BcfToolsToolBase(BioinformaticsTool, ABC):
    @staticmethod
    def tool_provider():
        return "bcftools"
