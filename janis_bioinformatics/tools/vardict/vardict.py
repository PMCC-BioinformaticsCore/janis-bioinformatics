from abc import ABC
from janis_core import CommandTool


class VarDict_1_5_6(CommandTool, ABC):
    @staticmethod
    def docker():
        return "michaelfranklin/vardict:1.5.6"


class VarDict_1_5_7(CommandTool):
    @staticmethod
    def docker():
        return "michaelfranklin/vardict:1.5.7"


class VarDict_1_5_8(CommandTool):
    @staticmethod
    def docker():
        return "michaelfranklin/vardict:1.5.8"
