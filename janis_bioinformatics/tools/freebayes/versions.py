from .base_1_2 import FreeBayesBase_1_2
from .base_1_3 import FreeBayesBase_1_3
from .base_1_3_cram import FreeBayesCramBase_1_3


class FreeBayes_1_2(FreeBayesBase_1_2):
    def container(self):
        return "papaemmelab/docker-freebayes:v0.1.5"

    def version(self):
        return "1.2"


class FreeBayes_1_3(FreeBayesBase_1_3):
    def container(self):
        return "shollizeck/freebayes:1.3.1"

    def version(self):
        return "1.3.1"


class FreeBayesCram_1_3(FreeBayesCramBase_1_3):
    def container(self):
        return "shollizeck/freebayes:1.3.1"

    def version(self):
        return "1.3.1"


FreeBayesLatest = FreeBayes_1_3
