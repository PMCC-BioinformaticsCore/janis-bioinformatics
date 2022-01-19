from abc import ABC

from janis_bioinformatics.tools import BioinformaticsTool


class HTSeqToolBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "HTSeq"
