from abc import ABC

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class HtsLibBase(BioinformaticsTool, ABC):
    @staticmethod
    def tool_provider():
        return "HTSLib"
