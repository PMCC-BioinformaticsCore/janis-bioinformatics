from abc import ABC
from janis_core import CommandTool


class VarDict_1_5_6(CommandTool, ABC):
    def container(self):
        return "michaelfranklin/vardict:1.5.6"

    def version(self):
        return "1.5.6"


class VarDict_1_5_7(CommandTool):
    def container(self):
        return "michaelfranklin/vardict:1.5.7"

    def version(self):
        return "1.5.7"


class VarDict_1_5_8(CommandTool):
    def container(self):
        return "michaelfranklin/vardict:1.5.8"

    def version(self):
        return "1.5.8"


class VarDict_1_6_0(CommandTool):
    def container(self):
        return "michaelfranklin/vardict:1.6.0"

    def version(self):
        return "1.6.0"


class VarDict_1_7_0(CommandTool):
    def container(self):
        return "michaelfranklin/vardict:1.7.0"

    def version(self):
        return "1.7.0"
