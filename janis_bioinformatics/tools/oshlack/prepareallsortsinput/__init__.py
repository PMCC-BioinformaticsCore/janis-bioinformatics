from typing import List, Dict, Any, Optional

from janis_core import PythonTool, TOutput, File

from janis_unix import Csv


class PrepareALLSortsInput_0_1_0(PythonTool):
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


if __name__ == "__main__":
    PrepareALLSortsInput_0_1_0().translate("wdl")
