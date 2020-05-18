from .base import GatkGathervcfscloudBase


class GatkGathervcfscloud_4_1_3_0(GatkGathervcfscloudBase):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
