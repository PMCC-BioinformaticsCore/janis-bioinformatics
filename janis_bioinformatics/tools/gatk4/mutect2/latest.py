from .base import Gatk4Mutect2Base
from ..gatk_latest import Gatk4Latest


class Gatk4Mutect2Latest(Gatk4Latest, Gatk4Mutect2Base):
    pass


if __name__ == "__main__":
    print(Gatk4Mutect2Latest().help())
