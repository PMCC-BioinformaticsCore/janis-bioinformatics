from datetime import datetime
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
        """
        This tool generates a list of BED intervals based on the reference input.
        It supports breaking up the intervals into subregions of length 'max_size',
        with an overlap (to consider indels spanning regions). Note the max_size is
        EXCLUSIVE of overlap, so the actual interval_size is (max_size + overlap).
        :param reference: FASTA reference with ^.dict reference
        :param prefix: contig prefix, default 'chr'
        :param allowed_contigs: Limits allowed_contigs to a list, this defaults of Human CHRs, 1-23,X,Y,Z
        :param max_size: Max size of interval, maybe 5000 for VarDict.
        :param overlap: Consider indels spanning regions, so choose
        """
        from re import sub

        if max_size is not None and overlap >= max_size:
            raise Exception(
                f"max_size ({max_size}) must be greater than overlap ({overlap})"
            )

        # Allowed contigs: use the standard human genome if none are provided
        # include M / MT for hg19 / hg39
        if allowed_contigs is None:
            allowed_contigs = map(
                lambda el: f"{prefix}{el}", [*range(23), "X", "Y", "M", "MT"]
            )
        allowed_contigs = set(allowed_contigs)

        def contig_label(contig: str) -> str:
            """
            Add the prefix if the contig doesn't already contain it
            """
            if prefix and not contig.startswith(prefix):
                return prefix + contig
            return contig

        def get_contig_and_length_from_line(line):
            """
            Iterate through each col in TSV line, and find SN / LN
            :returns CONTIG, LENGTH (ordered tuple)
            """
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
            """
            Split the region into INTERVALS for (max_size + overlap) if REQUIRED,
            else return a 
            :param contig:
            :param length:
            :return:
            """
            length = int(length)
            label = contig_label(contig)

            # BASE case, the interval fits within the max_size, just return a single row
            if max_size is None or length < max_size:
                return [[contig, "1", str(length), str(label)]]

            # ELSE split into subregions
            subregions = []
            # BED regions start at 1
            start, counter, finish = 1, 1, None
            while finish is None or finish < length:
                finish = min((finish or 0) + max_size, length)
                subregions.append(
                    [str(contig), str(start), str(finish), f"{label}_{counter}"]
                )
                start = finish - overlap + 1
                counter += 1

            return subregions

        # Get the ^.dict from the end of the .fasta | .fa filename
        ref_dict = sub("\.fa(sta)?$", ".dict", reference)

        regions = []

        with open(ref_dict) as ref:
            for line in ref:
                if "GL" in line or "SN" not in line:
                    continue

                contig, length = get_contig_and_length_from_line(line)
                # If we couldn't find a contig or sequence length, skip
                if contig is None or length is None:
                    continue
                # Only proceed if the contig OR (prefix + contig) in allowed_contigs
                if not (
                    contig in allowed_contigs or prefix + contig in allowed_contigs
                ):
                    continue

                regions.append(f"{contig_label(contig)}.bed")

                # Get total region list for contig, and considering max_size
                regions_to_write = prepare_regions(contig, length)
                prepped = [("\t".join(region) + "\n") for region in regions_to_write]
                with open(regions[-1], "w") as f:
                    f.writelines(prepped)

        return {"out_regions": regions}

    def outputs(self) -> List[j.TOutput]:
        return [j.TOutput("out_regions", j.Array(Bed))]

    def id(self) -> str:
        return "GenerateIntervalsByChromosome"

    def friendly_name(self) -> Optional[str]:
        return "Generating genomic intervals by chromosome"

    def version(self):
        return "v0.1.0"

    def bind_metadata(self):
        meta: j.ToolMetadata = self.metadata

        meta.contributors = ["Michael Franklin"]
        meta.dateCreated = datetime(2020, 10, 19)
        meta.dateUpdated = datetime(2020, 10, 19)

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"
