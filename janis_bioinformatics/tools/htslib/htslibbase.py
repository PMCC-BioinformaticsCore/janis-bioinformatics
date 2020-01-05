from abc import ABC

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class HtsLibBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "HTSLib"
