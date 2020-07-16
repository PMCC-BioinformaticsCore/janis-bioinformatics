from abc import ABC
from janis_core import CommandTool


class DawsonToolkit_0_1(CommandTool, ABC):
    def tool_provider(self):
        return "Dawson Labs"

    def container(self):
        return "shollizeck/dawsontoolkit:0.1.6.1"

    def version(self):
        return "0.1.6"
