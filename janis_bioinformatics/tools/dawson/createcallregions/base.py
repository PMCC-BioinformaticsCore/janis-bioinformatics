from janis_core import PythonTool, TOutput, File
from typing import Dict, Optional, List, Any

from janis_core import Array
from janis_bioinformatics.data_types import FastaFai


class CreateCallRegions(PythonTool):
    @staticmethod
    def code_block(
        reference: FastaFai, regionSize: int, equalize: bool = True
    ) -> Dict[str, Any]:
        from shutil import copyfile
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

                if equalize:
                    # in this case we make the regions as equal in size as we can an treat the
                    # input size as a guide and not as nessecity
                    steps = math.ceil(chrLength / regionSize)
                    # change the regionSize to the equalized version
                    regionSize = math.ceil(chrLength / steps)

                # while the start of the new region is still inside of the chromosomal boundaries
                # we create a new region
                while start < chrLength:
                    end = start + regionSize
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


# CreateCallRegions().translate("cwl")
