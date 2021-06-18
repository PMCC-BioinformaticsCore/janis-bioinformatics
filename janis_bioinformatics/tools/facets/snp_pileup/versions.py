from .base import FacetsSnpPileupBase
from ..versions import Facets_2_0_8


class FacetsSnpPileup_2_0_8(Facets_2_0_8, FacetsSnpPileupBase):
    pass


FacetsSnpPileupLatest = FacetsSnpPileup_2_0_8

if __name__ == "__main__":
    print(FacetsSnpPileup_2_0_8().help())
