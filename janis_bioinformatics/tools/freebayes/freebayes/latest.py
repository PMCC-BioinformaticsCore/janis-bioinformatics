from ..freebayeslatest import FreeBayesLatest
from .base import FreeBayesBase


class FreeBayesLatest(FreeBayesLatest, FreeBayesBase):
    pass


if __name__ == "__main__":
    print(FreeBayesLatest().help())
