from .base_1_3_cram import FreeBayesBase_1_3


class FreeBayes_1_3(FreeBayesBase_1_3):
    def container(self):
        return "shollizeck/freebayes:1.3.1"

    def version(self):
        return "1.3.1"


FreeBayesLatest = FreeBayes_1_3
