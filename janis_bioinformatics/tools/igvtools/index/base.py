from datetime import datetime
from abc import ABC
from typing import List, Optional, Union

from janis_core import ToolOutput, ToolInput, InputSelector, ToolMetadata

from janis_bioinformatics.data_types import Vcf, VcfIdx
from janis_bioinformatics.tools.igvtools.igvtoolsbase import IgvToolsBase


class IgvIndexBase(IgvToolsBase, ABC):
    # Implement this on the IgvIndex subclasses (feature / alignment)
    # def tool(self) -> str:

    def base_command(self) -> Optional[Union[str, List[str]]]:
        return ["igvtools", "index"]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=datetime(2020, 6, 4),
            dateUpdated=datetime(2020, 6, 15),
            documentation="",
        )


class IgvIndexFeatureBase(IgvIndexBase, ABC):
    def tool(self) -> str:
        return "IgvToolsIndexFeatures"

    def friendly_name(self) -> Optional[str]:
        return "IGVTools: Index Features"

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput(
                "inp", Vcf, position=1, presents_as="sample.vcf", localise_file=True
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [ToolOutput("out", VcfIdx, glob=InputSelector("inp"))]
