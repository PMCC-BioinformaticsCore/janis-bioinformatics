from abc import ABC
from janis_core import CommandTool


class PeterMacUtils_0_0_4(CommandTool, ABC):
    @staticmethod
    def tool_provider():
        return "Peter MacCallum Cancer Centre"

    @staticmethod
    def container():
        return "michaelfranklin/pmacutil:0.0.4"

    @staticmethod
    def version():
        return "0.0.4"
