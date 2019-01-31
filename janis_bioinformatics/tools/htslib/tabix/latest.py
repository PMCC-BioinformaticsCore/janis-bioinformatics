from bioinformatics.janis_bioinformatics.tools.htslib.latest import HTSLibLatest
from bioinformatics.janis_bioinformatics.tools import TabixBase


class TabixLatest(HTSLibLatest, TabixBase):
    pass


if __name__ == "__main__":
    print(TabixLatest().help())
