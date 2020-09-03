from .base import ArribaBase


class Arriba_1_2_0(ArribaBase):
    def version(self):
        return "1.2.0"

    def container(self):
        return "quay.io/biocontainers/arriba:1.2.0--hd2e4403_2"
