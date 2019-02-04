from ..bcftools_latest import BcfToolsLatest
from .base import BcfToolsViewBase


class BcfToolsViewLatest(BcfToolsLatest, BcfToolsViewBase):
    pass


if __name__ == "__main__":
    print(BcfToolsViewLatest().help())
