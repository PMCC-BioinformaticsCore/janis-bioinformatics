from .base import Gatk4BaseRecalibratorBase
from ..gatk_latest import Gatk4Latest


class Gatk4BaseRecalibratorLatest(Gatk4Latest, Gatk4BaseRecalibratorBase):
    pass

if __name__ == "__main__":
    print(Gatk4BaseRecalibratorLatest().help())
