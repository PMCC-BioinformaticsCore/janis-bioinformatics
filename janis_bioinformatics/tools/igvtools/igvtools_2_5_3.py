from abc import ABC

from .igvtoolsbase import IgvToolsBase


class IgvTools_2_5_3(IgvToolsBase, ABC):
    def container(self):
        return "quay.io/biocontainers/igvtools:2.5.3--0"

    def version(self):
        return "2.5.3"
