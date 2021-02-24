from .base import FacetsSnpPileupBase
from ..versions import Facets_0_5_14_2


class FacetsSnpPileup_0_5_14_2(Facets_0_5_14_2, FacetsSnpPileupBase):
    pass


FacetsSnpPileupLatest = FacetsSnpPileup_0_5_14_2

if __name__ == "__main__":
    print(FacetsSnpPileup_0_5_14_2().help())