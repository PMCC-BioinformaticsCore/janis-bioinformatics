from abc import ABC


class HTSeq_1_99_2(ABC):
    def container(self):
        return "quay.io/biocontainers/htseq:1.99.2--py39haf81c86_0"

    def version(self):
        return "1.99.2"
