from .base import BcfToolsAnnotateBase
from ..bcftools_1_5 import BcfTools_1_5
from ..bcftools_1_9 import BcfTools_1_9


class BcfToolsAnnotate_1_9(BcfTools_1_9, BcfToolsAnnotateBase):
    pass


class BcfToolsAnnotate_1_5(BcfTools_1_5, BcfToolsAnnotateBase):
    pass


BcfToolsAnnotateLatest = BcfToolsAnnotate_1_9
