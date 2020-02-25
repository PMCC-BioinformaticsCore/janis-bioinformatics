from abc import ABC

class GATK3_3_8_1(ABC):
    def container(self):
        return "broadinstitute/gatk3:3.8-1"

    def version(self):
        return "3.8-1"

GATK3Latest = GATK3_3_8_1