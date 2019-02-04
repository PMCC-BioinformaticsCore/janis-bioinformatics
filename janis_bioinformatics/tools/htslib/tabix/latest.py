from .base import TabixBase
from ..latest import HTSLibLatest


class TabixLatest(HTSLibLatest, TabixBase):
    pass


if __name__ == "__main__":
    print(TabixLatest().help())
