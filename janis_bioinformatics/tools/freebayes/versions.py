from .base_1_2 import FreeBayesBase_1_2
from .base_1_3 import FreeBayesBase_1_3


class FreeBayes_1_2(FreeBayesBase_1_2):
    @staticmethod
    def container():
        return "papaemmelab/docker-freebayes:v0.1.5"

    @staticmethod
    def version():
        return "1.2"


class FreeBayes_1_3(FreeBayesBase_1_3):
    @staticmethod
    def container():
        return "shollizeck/freebayes:1.3.1"

    @staticmethod
    def version():
        return "1.3.1-dirty"


FreeBayesLatest = FreeBayes_1_3
