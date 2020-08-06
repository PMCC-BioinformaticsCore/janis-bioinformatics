from abc import ABC
from janis_core import CommandTool


class DawsonToolkit_0_1(CommandTool, ABC):
    def tool_provider(self):
        return "Dawson Labs"

    @staticmethod
    def container():
        return "shollizeck/dawsontoolkit:0.1.7.1"

    @staticmethod
    def version():
        return "0.1.7"
