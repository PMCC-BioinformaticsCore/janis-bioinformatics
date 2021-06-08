from abc import ABC

from janis_bioinformatics.tools import BioinformaticsTool


class BcfToolsToolBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "bcftools"
