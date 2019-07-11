from abc import ABC, abstractmethod
from datetime import date

from ..bioinformaticstoolbase import BioinformaticsTool
from janis.utils.metadata import ToolMetadata


class BcfToolsToolBase(BioinformaticsTool, ABC):
    @staticmethod
    def tool_provider():
        return "bcftools"
