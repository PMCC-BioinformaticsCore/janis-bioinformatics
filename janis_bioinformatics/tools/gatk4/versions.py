from abc import ABC


class Gatk_4_0_12(ABC):
    def container(self):
        return "broadinstitute/gatk:4.0.12.0"

    def version(self):
        return "4.0.12.0"


class Gatk_4_1_2_0(ABC):
    def container(self):
        return "broadinstitute/gatk:4.1.2.0"

    def version(self):
        return "4.1.2.0"


class Gatk_4_1_3_0(ABC):
    def container(self):
        return "broadinstitute/gatk:4.1.3.0"

    def version(self):
        return "4.1.3.0"


class Gatk_4_1_4_0(ABC):
    def container(self):
        return "broadinstitute/gatk:4.1.4.0"

    def version(self):
        return "4.1.4.0"


class Gatk_4_1_4_1(ABC):
    def container(self):
        return "broadinstitute/gatk:4.1.4.1"

    def version(self):
        return "4.1.4.1"


class Gatk_4_1_5_0(ABC):
    def container(self):
        return "broadinstitute/gatk:4.1.5.0"

    def version(self):
        return "4.1.5.0"


class Gatk_4_1_6_0(ABC):
    def container(self):
        return "broadinstitute/gatk:4.1.6.0"

    def version(self):
        return "4.1.6.0"


Gatk4Latest = Gatk_4_1_6_0
