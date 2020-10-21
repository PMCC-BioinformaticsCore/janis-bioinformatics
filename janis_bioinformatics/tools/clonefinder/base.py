from abc import ABC
from typing import Dict, Any

from janis_core import (
    ToolInput,
    Filename,
    ToolOutput,
    CpuSelector,
    get_value_for_hints_and_ordered_resource_tuple,
    ToolMetadata,
    CaptureType,
    WildcardSelector,
)

from janis_unix import TextFile

from janis_bioinformatics.data_types import VcfTabix, Vcf

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class CloneFinderBase(BioinformaticsTool, ABC):
    def tool(self) -> str:
        return "clonefinder"

    def friendly_name(self) -> str:
        return "CloneFinder"

    def tool_provider(self):
        return "Dawson Labs"

    def base_command(self):
        return ["clonefinder.py" "snv"]

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 4

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 12

    def inputs(self):
        return [
            ToolInput(
                tag="snvInput",
                input_type=TextFile(),
                position=2,
                doc="tab seperated file of snvs to find clones for",
            ),
            ToolInput(
                tag="outputFolder",
                input_type=Filename(),
                prefix="-o",
                doc="folder to write output to (default: current working dir)",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "meg",
                TextFile(),
                glob=WildcardSelector("*_CloneFinder.meg"),
                doc="To determine type",
            ),
            ToolOutput(
                "clonalFractions",
                TextFile(),
                glob=WildcardSelector("*_CloneFinder.txt"),
                doc="To determine type",
            ),
            ToolOutput(
                "summary",
                TextFile(),
                glob=WildcardSelector("*_summary.txt"),
                doc="To determine type",
            ),
        ]

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val:
            return val
        return 4

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val:
            return val
        return 12

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Sebastian Hollizeck"],
            dateCreated=date(2019, 12, 5),
            dateUpdated=date(2019, 12, 5),
            institution="Institute for Genomics and Evolutionary Medicine",
            doi="10.1093/bioinformatics/bty469",
            citation="https://www.ncbi.nlm.nih.gov/pubmed/29931046",
            keywords=["clonal deconvolution"],
            documentationUrl=None,
            documentation="Usage: clonefinder snv <input> [-o <outputFolder>]\n",
        )
