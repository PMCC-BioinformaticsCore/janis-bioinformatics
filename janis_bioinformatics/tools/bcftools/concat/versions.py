from ..versions import BcfTools_1_5, BcfTools_1_9, BcfTools_1_12
from .base import BcfToolsConcatBase


class BcfToolsConcat_1_9(BcfTools_1_9, BcfToolsConcatBase):
    pass


BcfToolsConcatLatest = BcfToolsConcat_1_9
