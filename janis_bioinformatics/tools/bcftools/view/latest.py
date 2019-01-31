from bioinformatics.janis_bioinformatics.tools.bcftools.bcftools_latest import BcfToolsLatest
from bioinformatics.janis_bioinformatics.tools.bcftools.view.base import BcfToolsViewBase


class BcfToolsViewLatest(BcfToolsLatest, BcfToolsViewBase):
    pass


if __name__ == "__main__":
    print(BcfToolsViewLatest().help())
