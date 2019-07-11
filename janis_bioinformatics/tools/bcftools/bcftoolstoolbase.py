from abc import ABC, abstractmethod
from datetime import date

from ..bioinformaticstoolbase import BioinformaticsTool
from janis.utils.metadata import ToolMetadata


class BcfToolsToolBase(BioinformaticsTool, ABC):
    @staticmethod
    def tool_provider():
        return "bcftools"

    @classmethod
    @abstractmethod
    def bcftools_command(cls):
        raise Exception(
            "Subclass must implement the bcftools_command method: expects one of: ["
            "   annotate, call, cnv, concat, consensus, convert, csq, "
            "   filter, gtcheck, index, isec, merge, mpileup, norm, "
            "   plugin, polysomy, query, reheader, roh, sort, stats, view"
            "]"
        )
