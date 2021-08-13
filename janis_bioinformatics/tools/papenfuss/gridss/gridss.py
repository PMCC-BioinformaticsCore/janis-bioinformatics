from janis_bioinformatics.tools.papenfuss.gridss.base_2_2 import GridssBase_2_2
from janis_bioinformatics.tools.papenfuss.gridss.base_2_4 import GridssBase_2_4
from janis_bioinformatics.tools.papenfuss.gridss.base_2_10 import GridssBase_2_10


class Gridss_2_2_3(GridssBase_2_2):
    def base_command(self):
        return [
            *super().base_command(),
            "/data/gridss/gridss-2.2.3-gridss-jar-with-dependencies.jar",
            "gridss.CallVariants",
        ]

    def container(self):
        return "gridss/gridss:v2.2.3"

    def version(self):
        return "v2.2.3"


class Gridss_2_4_0(GridssBase_2_2):
    def base_command(self):
        return [
            *super().base_command(),
            "/data/gridss/gridss-2.4.0-gridss-jar-with-dependencies.jar",
            "gridss.CallVariants",
        ]

    def container(self):
        return "gridss/gridss:2.4.0"

    def version(self):
        return "v2.4.0"


class Gridss_2_5_1(GridssBase_2_4):
    def base_command(self):
        return "gridss.sh"

    def container(self):
        return "michaelfranklin/gridss:2.5.1-dev2"

    def version(self):
        return "v2.5.1-dev"


class Gridss_2_6_2(GridssBase_2_4):
    def container(self):
        # https://hub.docker.com/r/gridss/gridss
        return "gridss/gridss:2.6.2"

    def version(self):
        return "v2.6.2"


class Gridss_2_9_4(GridssBase_2_4):
    def container(self):
        return "gridss/gridss:2.9.4"

    def version(self) -> str:
        return "v2.9.4"


# 2.8.3 is last version before library optimisation
class Gridss_2_8_3(GridssBase_2_10):
    def container(self):
        return "gridss/gridss:2.8.3"

    def version(self) -> str:
        return "v2.8.3"


class Gridss_2_10_2(GridssBase_2_10):
    def container(self):
        return "gridss/gridss:2.10.2"

    def version(self) -> str:
        return "v2.10.2"


GridssLatest = Gridss_2_10_2
