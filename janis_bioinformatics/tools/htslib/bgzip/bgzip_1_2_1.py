from bioinformatics.janis_bioinformatics.tools import BGZipBase
from bioinformatics.janis_bioinformatics.tools import HTSLib_1_2_1


class BGZip_1_2_1(HTSLib_1_2_1, BGZipBase):
    pass


if __name__ == "__main__":
    print(BGZip_1_2_1().help())
