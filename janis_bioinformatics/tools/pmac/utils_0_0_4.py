from abc import ABC
from janis import CommandTool


class PeterMacUtils_0_0_4(CommandTool, ABC):
    @staticmethod
    def tool_provider():
        return "PeterMac"

    @staticmethod
    def docker():
        return "michaelfranklin/pmacutil:0.0.4"
