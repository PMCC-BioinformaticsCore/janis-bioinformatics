from ..dawsontoolkitlatest import DawsonToolkitLatest
from .base import RefilterStrelka2CallsBase

class RefilterStrelka2CallsLatest(DawsonToolkitLatest, RefilterStrelka2CallsBase):
    pass

if __name__ == "__main__":
        print(RefilterStrelka2CallsLatest().help())
