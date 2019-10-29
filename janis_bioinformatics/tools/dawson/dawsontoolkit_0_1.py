from abc import ABC
from janis_core import CommandTool


class DawsonToolkit_0_1(CommandTool, ABC):
    @staticmethod
    def tool_provider():
        return "Dawson Labs"

    @staticmethod
    def container():
        return "shollizeck/dawsontoolkit:0.1.4"

    @staticmethod
    def version():
        return "0.1.3"
