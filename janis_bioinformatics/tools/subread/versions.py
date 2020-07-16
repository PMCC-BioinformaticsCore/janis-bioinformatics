from abc import ABC


class Subread_2_0_1(ABC):
    def container(self):
        return "quay.io/biocontainers/subread:2.0.1--hed695b0_0"

    def version(self):
        return "2.0.1"
