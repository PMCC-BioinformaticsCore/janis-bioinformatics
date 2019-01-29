from janis.bioinformatics.tools.bcftools.annotate.base import BcfToolsAnnotateBase
from janis.bioinformatics.tools.bcftools.latest import BcfToolsLatest


class BcfToolsAnnotateLatest(BcfToolsLatest, BcfToolsAnnotateBase):
    pass


if __name__ == "__main__":
    print(BcfToolsAnnotateLatest().help())
