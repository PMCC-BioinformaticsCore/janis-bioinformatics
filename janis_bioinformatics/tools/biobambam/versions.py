from abc import ABC


class BioBamBam_2_0_87(ABC):
    def container(self):
        return "quay.io/biocontainers/biobambam:2.0.87-1"

    def version(self):
        return "2.0.87"


BioBamBamLatest = BioBamBam_2_0_87
