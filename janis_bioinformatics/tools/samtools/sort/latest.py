from ..samtoolslatest import SamToolsLatest
from .base import SamToolsSortBase


class SamToolsSortLatest(SamToolsLatest, SamToolsSortBase):
    pass


if __name__ == "__main__":
    print(SamToolsSortLatest().help())
