from bioinformatics.janis_bioinformatics.tools import BGZipBase
from bioinformatics.janis_bioinformatics.tools.htslib.latest import HTSLibLatest


class BGZipLatest(HTSLibLatest, BGZipBase):
    pass


if __name__ == "__main__":
    print(BGZipLatest().help())
