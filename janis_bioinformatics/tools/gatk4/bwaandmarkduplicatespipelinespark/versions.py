from .base import GatkBwaandmarkduplicatespipelinesparkBase


class GatkBwaandmarkduplicatespipelinespark_4_1_3_0(
    GatkBwaandmarkduplicatespipelinesparkBase
):
    def version(self):
        return "4.1.3.0"

    def container(self):
        return "broadinstitute/gatk:4.1.3.0"
