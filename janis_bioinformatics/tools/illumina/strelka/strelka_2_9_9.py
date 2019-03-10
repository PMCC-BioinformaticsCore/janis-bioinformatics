import ruamel.yaml

from janis_bioinformatics.tools.illumina.strelka.base import StrelkaBase


class Strelka_2_9_9(StrelkaBase):
    @staticmethod
    def docker():
        return "michaelfranklin/strelka:2.9.9"

    @staticmethod
    def version():
        return "2.9.9"


class Strelka_2_9_10(StrelkaBase):
    @staticmethod
    def docker():
        return "michaelfranklin/strelka:2.9.10"

    @staticmethod
    def version():
        return "2.9.10"


StrelkaLatest = Strelka_2_9_10


if __name__ == "__main__":
    from janis.translations.cwl import translate_tool
    print(Strelka_2_9_9().help())
    cwl = translate_tool(Strelka_2_9_9(), with_docker=True).get_dict()
    print("\n\n" + ruamel.yaml.dump(cwl))
