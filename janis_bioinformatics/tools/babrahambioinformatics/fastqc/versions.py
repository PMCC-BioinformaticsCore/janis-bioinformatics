from typing import Dict
from janis_core import Array, ToolMetadata, ToolInput
from janis_bioinformatics.data_types import FastqGz

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsWorkflow

from janis_bioinformatics.tools.babrahambioinformatics.fastqc.base import FastQCBase
from janis_bioinformatics.tools.babrahambioinformatics.fastqc.basesingle import (
    FastQCSingleBase,
)


class FastQCVersion_0_11_5:
    def version(self):
        return "v0.11.5"

    def container(self):
        return "quay.io/biocontainers/fastqc:0.11.5--pl5.22.0_3"


class FastQCVersion_0_11_8:
    def version(self):
        return "v0.11.8"

    def container(self):
        return "quay.io/biocontainers/fastqc:0.11.8--1"


# v0.11.5


class FastQC_0_11_5(FastQCVersion_0_11_5, FastQCBase):
    pass


class FastQCSingle_0_11_5(FastQCVersion_0_11_5, FastQCSingleBase):
    pass


# v0.11.8


class FastQC_0_11_8(FastQCVersion_0_11_8, FastQCBase):
    pass


class FastQCSingle_0_11_8(FastQCVersion_0_11_8, FastQCSingleBase):
    pass


# latest

FastQCLatest = FastQC_0_11_8
FastQCSingleLatest = FastQCSingle_0_11_8


## Single scatter

fastqc_single_instantiated = FastQCSingleLatest()


class FastqcSingleScattered(BioinformaticsWorkflow):
    f"""
    FastQC doesn't return a Directory unless it's the single variant, but Janis will make
    you double scatter if you're processing an array of array of fastqs.
    
    Note, this is bound to the LATEST version of FastQC: '{fastqc_single_instantiated.version()}'
    """

    def constructor(self):
        self.input("reads", Array(FastqGz))

        kwargs_to_process = {
            "casva",
            "nano",
            "nofilter",
            "noextract",
            "nogroup",
            "format",
            "contaminants",
            "adapters",
            "limits",
            "kmers",
        }
        tins: Dict[str, ToolInput] = {
            i.id(): i for i in fastqc_single_instantiated.inputs()
        }
        kwargs = {
            i.id(): self.input(i.id(), i.input_type, doc=i.doc)
            for i in tins.values()
            if i.id() in kwargs_to_process
        }

        self.step(
            "fastqc", FastQCSingleLatest(read=self.reads, **kwargs), scatter="read",
        )

        self.capture_outputs_from_step(self.fastqc)

    def friendly_name(self):
        return "FastQC (Single, Scattered)"

    def tool_provider(self):
        return "FastQC"

    def id(self) -> str:
        return "fastqc_single_scattered"

    def version(self):
        return fastqc_single_instantiated.version()

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated="2020-07-30",
            documentation=f"""
FastQC doesn't return a Directory unless it's the single variant, but Janis will make
you double scatter if you're processing an array of array of fastqs.

Note, this is bound to the LATEST version of FastQC: '{fastqc_single_instantiated.version()}'
    """,
        )
