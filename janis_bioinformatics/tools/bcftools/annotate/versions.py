from ..versions import BcfTools_1_5, BcfTools_1_9, BcfTools_1_12
from .base import BcfToolsAnnotateBase


class BcfToolsAnnotate_1_9(BcfTools_1_9, BcfToolsAnnotateBase):
    pass


class BcfToolsAnnotate_1_5(BcfTools_1_5, BcfToolsAnnotateBase):
    pass


BcfToolsAnnotateLatest = BcfToolsAnnotate_1_9
