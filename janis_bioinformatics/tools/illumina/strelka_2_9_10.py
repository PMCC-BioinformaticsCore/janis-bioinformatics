from abc import ABC
from janis_core import CommandTool


class Strelka_2_9_10(CommandTool, ABC):
    def tool_provider(self):
        return "Illumina"

    def container(self):
        return "michaelfranklin/strelka:2.9.10"

    def version(self):
        return "2.9.10"
