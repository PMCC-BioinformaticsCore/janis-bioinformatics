from .base import Gatk4MergeSamFilesBase
from ..gatk_latest import Gatk4Latest


class Gatk4MergeSamFilesLatest(Gatk4Latest, Gatk4MergeSamFilesBase):
    pass


if __name__ == "__main__":
    print(Gatk4MergeSamFilesLatest().help())
