from datetime import datetime
from typing import Dict, List, Any

from janis_core import TOutput, Array, ToolMetadata

from janis_bioinformatics.data_types import FastaFai
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsPythonTool


class CreateCallRegions(BioinformaticsPythonTool):
    def tool_provider(self):
        return "Dawson Labs"

    @staticmethod
    def code_block(
        reference: FastaFai, regionSize: int, equalize: bool = True
    ) -> Dict[str, Any]:
        import csv
        import math

        regions = []

        with open(f"{reference}.fai", "r") as tmpF:
            tsvreader = csv.reader(tmpF, delimiter="\t")
            for line in tsvreader:

                # start point of the region per chr (which is per line)
                start = 1
                chr = line[0]
                chrLength = int(line[1])
                chrRegionSize = regionSize

                if equalize:
                    # in this case we make the regions as equal in size as we can an treat the
                    # input size as a guide and not as nessecity
                    steps = math.ceil(chrLength / chrRegionSize)
                    # change the regionSize to the equalized version
                    chrRegionSize = math.ceil(chrLength / steps)

                # while the start of the new region is still inside of the chromosomal boundaries
                # we create a new region
                while start < chrLength:
                    end = start + chrRegionSize
                    if end > chrLength:
                        end = chrLength

                    # add the region to the list of regions to be used
                    regions.append(f"{chr}:{start}-{end}")

                    # update the new start to be one base behind the previous stop
                    start = end + 1

        return {"regions": regions}

    def outputs(self) -> List[TOutput]:
        return [TOutput("regions", Array(str))]

    def id(self) -> str:
        return "CreateCallRegions"

    def version(self):
        return "v0.1.0"

    def friendly_name(self):
        return "Create genomic call regions"

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Sebastian Hollizeck"],
            dateCreated=datetime(2020, 6, 17),
            dateUpdated=datetime(2020, 7, 16),
            documentation="",
        )
