from .base import Gatk4MarkDuplicatesBase
from ..gatk_latest import Gatk4Latest


class Gatk4MarkDuplicatesLatest(Gatk4Latest, Gatk4MarkDuplicatesBase):
    pass

if __name__ == "__main__":
    print(Gatk4MarkDuplicatesLatest().help())
