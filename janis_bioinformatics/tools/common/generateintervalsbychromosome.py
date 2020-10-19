from typing import Dict, Any, List, Optional

import janis_core as j

from janis_bioinformatics.data_types import FastaDict, Bed


class GenerateIntervalsByChromosome(j.PythonTool):
    @staticmethod
    def code_block(
        reference: FastaDict,
        prefix="chr",
        allowed_contigs: Optional[List[str]] = None,
        max_size: Optional[int] = None,
        overlap: Optional[int] = 0,
    ) -> Dict[str, Any]:
        from re import sub
        import sys

        if allowed_contigs is None:
            allowed_contigs = map(
                lambda el: f"{prefix}{el}", [*range(23), "X", "T", "M", "MT"]
            )
        allowed_contigs = set(allowed_contigs)

        # cat $fasta_dict | grep -v GL | tail -n +2 | cut -f2,3 > genome_size.txt

        # grep -v GL    (Remove all lines with GL)
        # tail -n +2    (skip the first line)
        # cut -f2,3     (grab the second and third TSV fields)

        def contig_label(contig: str):
            if prefix and not contig.startswith(prefix):
                return prefix + contig
            return contig

        def get_contig_and_length_from_line(line):
            contig, length = None, None
            for col in line.split("\t"):
                if col.startswith("SN:") and len(col) > 3:
                    contig = col.strip("SN:")
                elif col.startswith("LN:") and len(col) > 3:
                    length = col.strip("LN:")
                if contig is not None and length is not None:
                    break

            return contig, length

        def prepare_regions(contig, length) -> List[List[str]]:
            length = int(length)
            label = contig_label(contig)

            if max_size is None or length < max_size:
                return [[contig, "1", str(length), str(label)]]

            subregions = []
            start, counter, finish = 1, 1, None
            counter = 1
            while finish is None or finish < length:
                finish = min((finish or 0) + max_size, length)
                subregions.append(
                    [str(contig), str(start), str(finish), f"{label}_{counter}"]
                )
                print(
                    f"Processing {label}_{counter} ({start} > {finish})",
                    file=sys.stderr,
                )
                start = finish + 1 - overlap
                counter += 1

            return subregions

        ref_dict = sub("\.fa(sta)?$", ".dict", reference)

        regions = []

        with open(ref_dict) as ref:
            for line in ref:
                if "GL" in line:
                    continue
                if "SN" not in line:
                    continue

                contig, length = get_contig_and_length_from_line(line)
                print(f"CONTIG: {contig} | LENGTH: {length}", file=sys.stderr)
                if (
                    contig is not None
                    and length is not None
                    and contig in allowed_contigs
                ):
                    regions.append(f"{contig_label(contig)}.bed")
                    prepped = [
                        ("\t".join(region) + "\n")
                        for region in prepare_regions(contig, length)
                    ]
                    with open(regions[-1], "w") as f:
                        f.writelines(prepped)

        return {"out_regions": regions}

    def outputs(self) -> List[j.TOutput]:
        return [j.TOutput("out_regions", j.Array(Bed))]


if __name__ == "__main__":
    from janis_assistant.main import run_with_outputs

    GenerateIntervalsByChromosome().translate("cwl")

    ref = "/Users/franklinmichael/reference/hg38/assembly/Homo_sapiens_assembly38.fasta"
    from janis_core import Logger

    Logger.set_console_level(5)
    run_with_outputs(
        GenerateIntervalsByChromosome(),
        {"reference": ref},
        output_dir="~/janis/intervalgeneratoreftest2/",
    )
