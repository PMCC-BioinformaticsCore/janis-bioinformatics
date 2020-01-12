from abc import ABC
from janis_core import CommandTool


class PeterMacUtils_0_0_4(CommandTool, ABC):
    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def container(self):
        return "michaelfranklin/pmacutil:0.0.4"

    def version(self):
        return "0.0.4"


class PeterMacUtils_0_0_5(CommandTool, ABC):
    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def container(self):
        return "michaelfranklin/pmacutil:0.0.5"

    def version(self):
        return "0.0.5"
