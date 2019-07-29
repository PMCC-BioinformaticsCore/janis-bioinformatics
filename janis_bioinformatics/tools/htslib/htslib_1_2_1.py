from .htslibbase import HtsLibBase


class HTSLib_1_2_1(HtsLibBase):

    @staticmethod
    def container():
        return "biodckrdev/htslib:1.2.1"

    @staticmethod
    def version():
        return "1.2.1"
