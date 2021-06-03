from abc import ABC
from janis_core import CommandTool


class DawsonToolkit_0_1(CommandTool, ABC):
    @staticmethod
    def container():
        return "shollizeck/dawsontoolkit:0.1.8.1"

    @staticmethod
    def version():
        return "0.1.8"


class DawsonToolkit_0_2(CommandTool, ABC):
    @staticmethod
    def container():
        return "shollizeck/dawsontoolkit:0.2"

    @staticmethod
    def version():
        return "0.2"


DawsonToolkitLatest = DawsonToolkit_0_2
