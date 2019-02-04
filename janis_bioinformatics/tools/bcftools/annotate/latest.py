from .base import BcfToolsAnnotateBase
from ..bcftools_latest import BcfToolsLatest


class BcfToolsAnnotateLatest(BcfToolsLatest, BcfToolsAnnotateBase):
    pass


if __name__ == "__main__":
    print(BcfToolsAnnotateLatest().help())
