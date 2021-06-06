from ..versions import BcfTools_1_5, BcfTools_1_9
from .base import BcfToolsViewBase


class BcfToolsView_1_5(BcfTools_1_5, BcfToolsViewBase):
    pass


class BcfToolsView_1_9(BcfTools_1_9, BcfToolsViewBase):
    pass


BcfToolsViewLatest = BcfToolsView_1_9
