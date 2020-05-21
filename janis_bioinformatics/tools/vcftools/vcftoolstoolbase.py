from abc import ABC, abstractmethod

from janis_bioinformatics.tools import BioinformaticsTool


class VcfToolsToolBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "VCFtools"

    @classmethod
    @abstractmethod
    def vcftools_command(cls):
        raise Exception("Tool or command not found")

    @classmethod
    def base_command(cls):
        return [""]

    def inputs(self):
        return []

    def doc(self):
        return """vcftools is a suite of functions for use on genetic variation data in the form of VCF and BCF files. The tools provided will be used mainly to summarize data, run calculations on data, filter out data, and convert data into other useful file formats.
        
        Documentation:https://vcftools.github.io/man_latest.html#NAME""".strip()

    @abstractmethod
    def container(self):
        raise Exception(
            "An error likely occurred when resolving the method order for docker"
        )

    def arguments(self):
        return []
