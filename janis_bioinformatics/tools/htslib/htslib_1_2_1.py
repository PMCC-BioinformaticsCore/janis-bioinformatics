from .htslibbase import HtsLibBase


class HTSLib_1_2_1(HtsLibBase):
    def container(self):
        return "biodckrdev/htslib:1.2.1"

    def version(self):
        return "1.2.1"
