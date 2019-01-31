from bioinformatics.janis_bioinformatics.tools import SamToolsLatest
from bioinformatics.janis_bioinformatics.tools import SamToolsViewBase


class SamToolsViewLatest(SamToolsLatest, SamToolsViewBase):
    pass


if __name__ == "__main__":
    print(SamToolsViewLatest().help())
