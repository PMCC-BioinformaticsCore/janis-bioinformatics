from abc import ABC
from janis_core import CommandTool


class Strelka_2_9_9(CommandTool):
    @staticmethod
    def tool_provider():
        return "Illumina"

    @staticmethod
    def container():
        return ""

    @staticmethod
    def version():
        return "2.9.9"
