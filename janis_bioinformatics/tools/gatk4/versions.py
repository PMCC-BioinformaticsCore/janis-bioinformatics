from abc import ABC


class Gatk_4_0_12(ABC):
    @staticmethod
    def container():
        return "broadinstitute/gatk:4.0.12.0"

    @staticmethod
    def version():
        return "4.0.12.0"


class Gatk_4_1_2_0(ABC):
    @staticmethod
    def container():
        return "broadinstitute/gatk:4.1.2.0"

    @staticmethod
    def version():
        return "4.1.2.0"


class Gatk_4_1_3_0(ABC):
    @staticmethod
    def container():
        return "broadinstitute/gatk:4.1.3.0"

    @staticmethod
    def version():
        return "4.1.3.0"


class Gatk_4_1_4_0(ABC):
    @staticmethod
    def container():
        return "broadinstitute/gatk:4.1.4.0"

    @staticmethod
    def version():
        return "4.1.4.0"


Gatk4Latest = Gatk_4_1_4_0
