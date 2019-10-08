from ..freebayeslatest import freebayesLatest
from .base import freebayesBase


class freebayesLatest(freebayesLatest, freebayesBase):
    pass


if __name__ == "__main__":
        print(freebayesLatest().help())
