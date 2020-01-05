from abc import ABC
from janis_core import CommandTool


class Strelka_2_9_9(CommandTool):
    def tool_provider(self):
        return "Illumina"

    def container(self):
        return ""

    def version(self):
        return "2.9.9"
