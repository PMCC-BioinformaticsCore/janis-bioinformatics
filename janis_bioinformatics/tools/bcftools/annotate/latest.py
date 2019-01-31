from bioinformatics.janis_bioinformatics.tools.bcftools.annotate.base import BcfToolsAnnotateBase
from bioinformatics.janis_bioinformatics.tools.bcftools.bcftools_latest import BcfToolsLatest


class BcfToolsAnnotateLatest(BcfToolsLatest, BcfToolsAnnotateBase):
    pass


if __name__ == "__main__":
    print(BcfToolsAnnotateLatest().help())
