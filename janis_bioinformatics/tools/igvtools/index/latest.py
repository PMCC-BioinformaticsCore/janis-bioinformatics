from ..igvtoolslatest import IgvToolsLatest
from .base import IgvToolsIndexBase


class IgvToolsIndexLatest(IgvToolsLatest, IgvToolsIndexBase):
    pass


if __name__ == "__main__":
    print(IgvToolsIndexLatest().help())
