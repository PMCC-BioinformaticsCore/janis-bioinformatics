from bioinformatics.janis_bioinformatics.tools.bcftools.bcftools_latest import BcfToolsLatest
from bioinformatics.janis_bioinformatics.tools.bcftools.norm.base import BcfToolsNormBase


class BcfToolsNormLatest(BcfToolsLatest, BcfToolsNormBase):
    pass


if __name__ == "__main__":
    print(BcfToolsNormLatest().help())
