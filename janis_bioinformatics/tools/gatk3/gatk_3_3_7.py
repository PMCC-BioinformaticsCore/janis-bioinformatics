from abc import ABC


class Gatk_3_3_7(ABC):
    def container(self):
        return "broadinstitute/gatk3:3.7-0"
