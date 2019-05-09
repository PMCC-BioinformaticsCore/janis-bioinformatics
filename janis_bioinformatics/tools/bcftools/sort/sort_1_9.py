from janis_bioinformatics.tools.bcftools.sort.base import BCFToolsSortBase


class BcfToolsSort_1_9(BCFToolsSortBase):

    @staticmethod
    def docker():
        return "michaelfranklin/bcftools:1.9"
