from .base import CloneFinderBase


class CloneFinder_0_2(CloneFinderBase):
    def container(self):
        return "shollizeck/clonefinder:0.2"

    def version(self):
        return "0.2"


CloneFinderLatest = CloneFinder_0_2
