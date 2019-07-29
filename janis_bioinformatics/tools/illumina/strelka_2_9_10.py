from abc import ABC
from janis_core import CommandTool


class Strelka_2_9_10(CommandTool, ABC):
    @staticmethod
    def tool_provider():
        return "Illumina"

    @staticmethod
    def container():
        return "michaelfranklin/strelka:2.9.10"

    @staticmethod
    def version():
        return "2.9.10"
