from datetime import datetime
from typing import List, Dict, Any, Optional

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsPythonTool
from janis_core import TOutput, File, ToolMetadata

from janis_unix import Csv


class PrepareALLSortsInput_0_1_0(BioinformaticsPythonTool):
    @staticmethod
    def code_block(
        inputs: List[File],
        labels: List[str] = None,
        output_filename: str = "output.csv",
        fusion_caller: str = "featureCounts",
    ) -> Dict[str, Any]:
        combined_count_list = []
        if fusion_caller == "featureCounts":
            for i, file in enumerate(inputs):
                gene_list = [""]
                count_list = [labels[i]]
                with open(file, "r") as f:
                    for line in f:
                        if line.startswith("#"):
                            pass
                        elif line.startswith("Geneid"):
                            pass
                        else:
                            line = line.strip("\n").split("\t")
                            gene = line[0]
                            count = line[6]
                            gene_list.append(gene)
                            count_list.append(count)
                combined_count_list.append(count_list)

        with open(output_filename, "w") as out_f:
            out_f.write(",".join(gene_list) + "\n")
            for i in combined_count_list:
                out_f.write(",".join(i) + "\n")

        return {"out": output_filename}

    def outputs(self) -> List[TOutput]:
        return [TOutput("out", Csv)]

    def id(self):
        return "prepareALLSortsInput"

    def version(self):
        return "v0.1.0"

    def friendly_name(self) -> Optional[str]:
        return "Prepare ALLSorts Input"

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=datetime(2020, 9, 21),
            dateUpdated=datetime(2020, 9, 21),
            documentation="",
        )


if __name__ == "__main__":
    PrepareALLSortsInput_0_1_0().translate("wdl")
