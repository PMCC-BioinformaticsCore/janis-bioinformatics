from .base import CloneFinderBase


class CloneFinder_0_2(CloneFinderBase_0_2):
    @staticmethod
    def container():
        return "shollizeck/clonefinder:0.2"

    @staticmethod
    def version():
        return "0.2"


CloneFinderLatest = CloneFinder_0_2
