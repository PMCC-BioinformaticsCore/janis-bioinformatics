from .htslibbase import HTSLibBase


class HTSLib_1_2_1(HTSLibBase):

    @staticmethod
    def docker():
        return "biodckrdev/htslib:1.2.1"

    @staticmethod
    def version():
        return "1.2.1"
