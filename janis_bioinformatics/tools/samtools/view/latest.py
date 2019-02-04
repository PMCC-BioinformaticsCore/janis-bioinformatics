from ..samtoolslatest import SamToolsLatest
from .base import SamToolsViewBase


class SamToolsViewLatest(SamToolsLatest, SamToolsViewBase):
    pass


if __name__ == "__main__":
    print(SamToolsViewLatest().help())
