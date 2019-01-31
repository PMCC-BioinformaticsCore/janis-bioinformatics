from bioinformatics.janis_bioinformatics.tools import IgvToolsLatest
from bioinformatics.janis_bioinformatics.tools.igvtools.index.base import IgvToolsIndexBase


class IgvToolsIndexLatest(IgvToolsLatest, IgvToolsIndexBase):
    pass


if __name__ == "__main__":
    print(IgvToolsIndexLatest().help())
