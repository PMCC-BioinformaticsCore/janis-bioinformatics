from janis.bioinformatics.tools.bcftools.latest import BcfToolsLatest
from janis.bioinformatics.tools.bcftools.norm.base import BcfToolsNormBase


class BcfToolsNormLatest(BcfToolsLatest, BcfToolsNormBase):
    pass


if __name__ == "__main__":
    print(BcfToolsNormLatest().help())
