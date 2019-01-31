from bioinformatics.janis_bioinformatics.tools import IgvToolsBase


class IgvTools_2_0(IgvToolsBase):
    @staticmethod
    def docker():
        return "maxulysse/igvtools:2.0.0"
