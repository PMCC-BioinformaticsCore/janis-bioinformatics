from abc import ABC


class Arriba_1_1_0(ABC):
    def version(self):
        return "1.1.0"

    def container(self):
        return "quay.io/biocontainers/arriba:1.1.0--h10824c4_1"


class Arriba_2_1_0(ABC):
    def version(self):
        return "2.1.0"

    def container(self):
        return "quay.io/biocontainers/arriba:2.1.0--hd2e4403_0"
