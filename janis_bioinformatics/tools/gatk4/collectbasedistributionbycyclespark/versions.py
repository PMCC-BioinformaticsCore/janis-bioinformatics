from .base import GatkCollectbasedistributionbycyclesparkBase


class GatkCollectbasedistributionbycyclespark_4_1_3_0(
    GatkCollectbasedistributionbycyclesparkBase
):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
