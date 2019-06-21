from janis_bioinformatics.tools.pappenfuss.gridss.base import GridssBase


class Gridss_2_2_3(GridssBase):

    @staticmethod
    def base_command():
        return [
            *super(Gridss_2_2_3, Gridss_2_2_3).base_command(),
            "/data/gridss/gridss-2.2.3-gridss-jar-with-dependencies.jar",
            "gridss.CallVariants"
        ]

    @staticmethod
    def docker():
        return "gridss/gridss:v2.2.3"


GridssLatest = Gridss_2_2_3
