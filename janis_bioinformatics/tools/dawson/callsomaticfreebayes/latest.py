from ..dawsontoolkitlatest import DawsonToolkitLatest
from .base import CallSomaticFreeBayesBase

class CallSomaticFreeBayesLatest(DawsonToolkitLatest, CallSomaticFreeBayesBase):
    pass

if __name__ == "__main__":
    print(CallSomaticFreeBayesLatest().help())
