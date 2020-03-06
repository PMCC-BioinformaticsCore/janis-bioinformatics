from ..versions import ioLib_1_14_1_2
from .base import ScrambleBase


class Scramble_1_14_1_2(ioLib_1_14_1_2, ScrambleBase):
    pass


ScrambleLatest = Scramble_1_14_1_2


if __name__ == "__main__":
    print(ScrambleLatest().help())
