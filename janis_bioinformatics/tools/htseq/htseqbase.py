from abc import ABC

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class HtseqToolBase(BioinformaticsTool, ABC):

    @staticmethod
    def tool_provider():
        return "htseq"