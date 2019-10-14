from .base import FreeBayesBase


class FreeBayes_1_2(FreeBayesBase):
    @staticmethod
    def container():
        return "papaemmelab/docker-freebayes:latest"

    @staticmethod
    def version():
        return "1.2"
