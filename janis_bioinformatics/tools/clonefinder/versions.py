from .base import CloneFinderBase


class CloneFinder_0_2(CloneFinderBase_0_2):
    def container(self):
        return "shollizeck/clonefinder:0.2"

    def version(self):
        return "0.2"


CloneFinderLatest = CloneFinder_0_2
