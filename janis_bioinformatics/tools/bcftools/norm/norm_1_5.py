from ..bcftools_1_5 import BcfTools_1_5
from .base import BcfToolsNormBase


class BcfToolsNorm_1_5(BcfTools_1_5, BcfToolsNormBase):
    pass


if __name__ == "__main__":
    print(BcfToolsNorm_1_5().help())
