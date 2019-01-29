from janis.bioinformatics.tools.htslib.latest import HTSLibLatest
from janis.bioinformatics.tools.htslib.tabix.base import TabixBase


class TabixLatest(HTSLibLatest, TabixBase):
    pass


if __name__ == "__main__":
    print(TabixLatest().help())
