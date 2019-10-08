from .base import BcfToolsViewBase
from ..bcftools_1_5 import BcfTools_1_5
from ..bcftools_1_9 import BcfTools_1_9


class BcfToolsView_1_5(BcfTools_1_5, BcfToolsViewBase):
    pass


class BcfToolsView_1_9(BcfTools_1_9, BcfToolsViewBase):
    pass


BcfToolsViewLatest = BcfToolsView_1_9
