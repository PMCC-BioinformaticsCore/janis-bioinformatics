from .base import BGZipBase
from ..latest import HTSLibLatest


class BGZipLatest(HTSLibLatest, BGZipBase):
    pass


if __name__ == "__main__":
    print(BGZipLatest().help())
