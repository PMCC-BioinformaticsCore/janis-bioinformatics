from .base import CallSomaticFreeBayesBase
from ..versions import DawsonToolkit_0_2


class CallSomaticFreeBayes_0_1(CallSomaticFreeBayesBase, DawsonToolkit_0_2):
    pass


CallSomaticFreeBayesLatest = CallSomaticFreeBayes_0_1
