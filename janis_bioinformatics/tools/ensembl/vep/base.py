from typing import List

from janis_core import (
    ToolOutput,
    ToolInput,
    Boolean,
    String,
    StringFormatter,
    File,
    Filename,
    Int,
    CpuSelector,
    Directory,
    Array,
)
from janis_unix import Tsv

from janis_bioinformatics.data_types import Fasta

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class VepBase(BioinformaticsTool):
    @staticmethod
    def tool() -> str:
        return "vep"

    def friendly_name(self) -> str:
        return "Variant Effect Predictor (VEP)"

    @staticmethod
    def base_command():
        return "vep"

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput(
                "inputFile",
                File(),
                prefix="--input_file",
                doc="Input file name. Can use compressed file (gzipped).",
            ),
            ToolInput(
                "vcf",
                Boolean(),
                default=True,
                prefix="--vcf",
                doc="Writes output in VCF format. Consequences are added in the INFO field of the VCF file, using the "
                'key "CSQ". Data fields are encoded separated by "|"; the order of fields is written in the VCF header.'
                ' Output fields in the "CSQ" INFO field can be selected by using --fields. If the input format was VCF,'
                " the file will remain unchanged save for the addition of the CSQ field (unless using any filtering). "
                "Custom data added with --custom are added as separate fields, using the key specified for each data "
                "file. Commas in fields are replaced with ampersands (&) to preserve VCF format.",
            ),
            ToolInput(
                "compressOutput",
                String(),
                default="bgzip",
                doc='Compress output: "gzip" or "bgzip"',
            ),
            ToolInput("outputFilename", Filename(), doc="Output file name"),
            ToolInput(
                "inputData",
                String(optional=True),
                prefix="--input_data",
                doc="Raw input data as a string. May be used, to input a single rsID or HGVS notation quickly to vep:",
            ),
            ToolInput(
                "verbose",
                Boolean(optional=True),
                prefix="--verbose",
                doc="Print out a bit more information while running. ",
            ),
            ToolInput(
                "species",
                String(optional=True),
                prefix="--species",
                doc='Species for your data. This can be the latin name e.g. "homo_sapiens" or any Ensembl alias e.g. '
                '"mouse". Specifying the latin name can speed up initial database connection as the registry does not '
                'have to load all available database aliases on the server. Default = "homo_sapiens"',
            ),
            ToolInput(
                "assembly",
                String(optional=True),
                prefix="--assembly",
                doc="Select the assembly version to use if more than one available. If using the cache, you must have "
                "the appropriate assembly's cache file installed. If not specified and you have only 1 assembly "
                "version installed, this will be chosen by default. Default = use found assembly version",
            ),
            ToolInput(
                "fileFormat",
                String(optional=True),
                prefix="--format",
                doc='one of "ensembl", "vcf", "hgvs", "id", "region", "spdi". By default, VEP auto-detects the input '
                "file format. Using this option you can specify the input file is Ensembl, VCF, IDs, HGVS, SPDI or "
                "region format. Can use compressed version (gzipped) of any file format listed above. "
                "Auto-detects format by default",
            ),
            ToolInput(
                "statsFilename",
                Filename(suffix=".txt_summary", extension=".html"),
                prefix="--stats_file",
                doc="Summary stats file name. This is an HTML file containing a summary of the VEP run - the file "
                'name must end ".htm" or ".html". Default = "variant_effect_output.txt_summary.html"',
            ),
            ToolInput(
                "maxSvSize",
                Int(optional=True),
                prefix="--max_sv_size",
                doc="Extend the maximum Structural Variant size VEP can process.",
            ),
            ToolInput(
                "noCheckVariantsOrder",
                Boolean(optional=True),
                prefix="--no_check_variants_order",
                doc="Permit the use of unsorted input files. However running VEP on unsorted "
                "input files slows down the tool and requires more memory.",
            ),
            ToolInput(
                "fork",
                Int(optional=True),
                default=CpuSelector(),
                prefix="--fork",
                doc="Enable forking, using the specified number of forks. Forking can dramatically improve runtime.",
            ),
            ToolInput(
                "plugin",
                Array(String(), optional=True),
                prefix="--plugin",
                separator=",",
                doc="[plugin name] Use named plugin. Plugin modules should be installed in the Plugins subdirectory "
                "of the VEP cache directory (defaults to $HOME/.vep/). Multiple plugins can be used by supplying "
                "the --plugin flag multiple times. See plugin documentation. .",
            ),
            ToolInput(
                "custom",
                String(optional=True),
                prefix="--custom",
                doc="[filename] Add custom annotation to the output. Files must be tabix indexed or in the bigWig "
                "format. Multiple files can be specified by supplying the --custom flag multiple times. See here "
                "for full details. ",
            ),
            ToolInput(
                "gff",
                String(optional=True),
                prefix="--gff",
                doc="[filename] Use GFF transcript annotations in [filename] as an annotation source. Requires a "
                "FASTA file of genomic sequence.",
            ),
            ToolInput(
                "gtf",
                String(optional=True),
                prefix="--gtf",
                doc="[filename] Use GTF transcript annotations in [filename] as an annotation source. "
                "Requires a FASTA file of genomic sequence.",
            ),
            ToolInput(
                "bam",
                String(optional=True),
                prefix="--bam",
                doc="[filename] ADVANCED Use BAM file of sequence alignments to correct transcript models not derived "
                "from reference genome sequence. Used to correct RefSeq transcript models. "
                "Enables --use_transcript_ref; add --use_given_ref to override this behaviour.",
            ),
            ToolInput(
                "useTranscriptRef",
                String(optional=True),
                prefix="--use_transcript_ref",
                doc="By default VEP uses the reference allele provided in the input file to calculate consequences for "
                "the provided alternate allele(s). Use this flag to force VEP to replace the provided reference "
                "allele with sequence derived from the overlapped transcript. This is especially relevant when "
                "using the RefSeq cache, see documentation for more details. The GIVEN_REF and USED_REF fields "
                "are set in the output to indicate any change.",
            ),
            ToolInput(
                "useGivenRef",
                String(optional=True),
                prefix="--use_given_ref",
                doc="Using --bam or a BAM-edited RefSeq cache by default enables --use_transcript_ref; add this flag "
                "to override this behaviour and use the provided reference allele from the input. ",
            ),
            ToolInput(
                "fields",
                Array(String(), optional=True),
                doc="Configure the output format using a comma separated list of fields. Can only be used with tab "
                "(--tab) or VCF format (--vcf) output. For the tab format output, the selected fields may be those "
                "present in the default output columns, or any of those that appear in the Extra column (including "
                "those added by plugins or custom annotations). Output remains tab-delimited. For the VCF format "
                'output, the selected fields are those present within the "CSQ" INFO field.',
            ),
            ToolInput(
                "variantClass",
                String(optional=True),
                prefix="--variant_class",
                doc="Output the Sequence Ontology variant class. ",
            ),
            ToolInput(
                "sift",
                String(optional=True),
                prefix="--sift",
                doc="[p|s|b] Species limited SIFT predicts whether an amino acid substitution affects protein function "
                "based on sequence homology and the physical properties of amino acids. VEP can output the prediction "
                "term, score or both. ",
            ),
            ToolInput(
                "polyphen",
                String(optional=True),
                prefix="--polyphen",
                doc="[p|s|b] Human only PolyPhen is a tool which predicts possible impact of an amino acid "
                "substitution on the structure and function of a human protein using straightforward physical and "
                "comparative considerations. VEP can output the prediction term, score or both. VEP uses the "
                "humVar score by default - use --humdiv to retrieve the humDiv score. ",
            ),
            ToolInput(
                "humdiv",
                String(optional=True),
                prefix="--humdiv",
                doc="Human only Retrieve the humDiv PolyPhen predictioninstead of the default humVar.",
            ),
            ToolInput(
                "nearest",
                String(optional=True),
                prefix="--nearest",
                doc="[transcript|gene|symbol] Retrieve the transcript or gene with the nearest protein-coding "
                'transcription start site (TSS) to each input variant. Use "transcript" to retrieve the transcript '
                'stable ID, "gene" to retrieve the gene stable ID, or "symbol" to retrieve the gene symbol. Note that '
                "the nearest TSS may not belong to a transcript that overlaps the input variant, and more than one may "
                "be reported in the case where two are equidistant from the input coordinates. Currently only available"
                " when using a cache annotation source, and requires the Set::IntervalTree perl module. Currently "
                "only available when using a cache annotation source, and requires the Set::IntervalTree perl module.",
            ),
            ToolInput(
                "distance",
                String(optional=True),
                prefix="--distance",
                doc="[bp_distance(,downstream_distance_if_different)] Modify the distance up and/or downstream between "
                "a variant and a transcript for which VEP will assign the upstream_gene_variant or downstream_gene_"
                "variant consequences. Giving one distance will modify both up- and downstream distances; prodiving two "
                "separated by commas will set the up- (5') and down- (3') stream distances respectively. Default: 5000",
            ),
            ToolInput(
                "overlaps",
                String(optional=True),
                prefix="--overlaps",
                doc="Report the proportion and length of a transcript overlapped by a structural variant in VCF format.",
            ),
            ToolInput(
                "genePhenotype",
                String(optional=True),
                prefix="--gene_phenotype",
                doc="Indicates if the overlapped gene is associated with a phenotype, disease or trait. "
                "See list of phenotype sources. ",
            ),
            ToolInput(
                "regulatory",
                String(optional=True),
                prefix="--regulatory",
                doc="Look for overlaps with regulatory regions. VEP can also report if a variant falls in a high "
                "information position within a transcription factor binding site. Output lines have a Feature "
                "type of RegulatoryFeature or MotifFeature. ",
            ),
            ToolInput(
                "cellType",
                String(optional=True),
                prefix="--cell_type",
                doc="Report only regulatory regions that are found in the given cell type(s). Can be a single cell "
                "type or a comma-separated list. The functional type in each cell type is reported under CELL_"
                "TYPE in the output. To retrieve a list of cell types, use --cell_type list.",
            ),
            ToolInput(
                "individual",
                String(optional=True),
                prefix="--individual",
                doc="[all|ind list] Consider only alternate alleles present in the genotypes of the specified "
                'individual(s). May be a single individual, a comma-separated list or "all" to assess all individuals '
                "separately. Individual variant combinations homozygous for the given reference allele will not be "
                "reported. Each individual and variant combination is given on a separate line of output. Only works "
                "with VCF files containing individual genotype data; individual IDs are taken from column headers. ",
            ),
            ToolInput(
                "phased",
                String(optional=True),
                prefix="--phased",
                doc="Force VCF genotypes to be interpreted as phased. For use with plugins that depend on phased data.",
            ),
            ToolInput(
                "alleleNumber",
                String(optional=True),
                prefix="--allele_number",
                doc="Identify allele number from VCF input, where 1 = first ALT allele, 2 = second ALT allele etc. "
                "Useful when using --minimal ",
            ),
            ToolInput(
                "showRefAllele",
                String(optional=True),
                prefix="--show_ref_allele",
                doc="Adds the reference allele in the output. Mainly useful for"
                ' the VEP "default" and tab-delimited output formats. ',
            ),
            ToolInput(
                "totalLength",
                String(optional=True),
                prefix="--total_length",
                doc="Give cDNA, CDS and protein positions as Position/Length. ",
            ),
            ToolInput(
                "numbers",
                String(optional=True),
                prefix="--numbers",
                doc="Adds affected exon and intron numbering to to output. Format is Number/Total. ",
            ),
            ToolInput(
                "noEscape",
                String(optional=True),
                prefix="--no_escape",
                doc="Don't URI escape HGVS strings. Default = escape",
            ),
            ToolInput(
                "keepCsq",
                String(optional=True),
                prefix="--keep_csq",
                doc="Don't overwrite existing CSQ entry in VCF INFO field. Overwrites by default",
            ),
            ToolInput(
                "vcfInfoField",
                String(optional=True),
                prefix="--vcf_info_field",
                doc="[CSQ|ANN|(other)] Change the name of the INFO key that VEP write the consequences to in its VCF "
                'output. Use "ANN" for compatibility with other tools such as snpEff. Default: CSQ',
            ),
            ToolInput(
                "terms",
                String(optional=True),
                prefix="--terms",
                doc="[SO|display|NCBI] The type of consequence terms to output. The Ensembl terms are described here. "
                "The Sequence Ontology is a joint effort by genome annotation centres to standardise descriptions "
                'of biological sequences. Default = "SO"',
            ),
            ToolInput(
                "noHeaders",
                String(optional=True),
                prefix="--no_headers",
                doc="Don't write header lines in output files. Default = add headers",
            ),
            *VepBase.identifiers,
        ]

    def metadata(self):
        self._metadata.documentation = """\


Getting VEP to run faster: https://asia.ensembl.org/info/docs/tools/vep/script/vep_other.html#faster
        """

    def outputs(self) -> List[ToolOutput]:
        pass

    identifiers = [
        ToolInput(
            "hgvs",
            Boolean(optional=True),
            prefix="--hgvs",
            doc="Add HGVS nomenclature based on Ensembl stable identifiers to the output. Both coding and protein "
            "sequence names are added where appropriate. To generate HGVS identifiers when using --cache or --offline "
            "you must use a FASTA file and --fasta. HGVS notations given on Ensembl identifiers are versioned. ",
        ),
        ToolInput(
            "hgvsg",
            Boolean(optional=True),
            prefix="--hgvsg",
            doc="Add genomic HGVS nomenclature based on the input chromosome name. To generate HGVS identifiers when "
            "using --cache or --offline you must use a FASTA file and --fasta. ",
        ),
        ToolInput(
            "shift_hgvs",
            Boolean(optional=True),
            prefix="--shift_hgvs",
            doc="[0|1]	Enable or disable 3' shifting of HGVS notations.When enabled, this causes ambiguous insertions "
            'or deletions(typically in repetetive sequence tracts) to be "shifted" to their most 3\' possible '
            "coordinates (relative to the transcript sequence and strand) before the HGVS notations are calculated; "
            "the flag HGVS_OFFSET is set to the number of bases by which the variant has shifted, relative to the input"
            " genomic coordinates. Disabling retains the original input coordinates of the variant. Default: 1 (shift)",
        ),
        ToolInput(
            "transcript_version",
            Boolean(optional=True),
            prefix="--transcript_version",
            doc="Add version numbers to Ensembl transcript identifiers",
        ),
        ToolInput(
            "protein",
            Boolean(optional=True),
            prefix="--protein",
            doc="Add the Ensembl protein identifier to the output where appropriate. ",
        ),
        ToolInput(
            "symbol",
            Boolean(optional=True),
            prefix="--symbol",
            doc="Adds the gene symbol (e.g. HGNC) (where available) to the output. ",
        ),
        ToolInput(
            "ccds",
            Boolean(optional=True),
            prefix="--ccds",
            doc="Adds the CCDS transcript identifer (where available) to the output. ",
        ),
        ToolInput(
            "uniprot",
            Boolean(optional=True),
            prefix="--uniprot",
            doc="Adds best match accessions for translated protein products from three UniProt-related databases "
            "(SWISSPROT, TREMBL and UniParc) to the output. ",
        ),
        ToolInput(
            "tsl",
            Boolean(optional=True),
            prefix="--tsl",
            doc="Adds the support level for this transcript to the output. Only available for human on the GRCh38",
        ),
        ToolInput(
            "appris",
            Boolean(optional=True),
            prefix="--appris",
            doc="Adds the APPRIS isoform annotation to the output. Only available for human on the GRCh38 assembly",
        ),
        ToolInput(
            "canonical",
            Boolean(optional=True),
            prefix="--canonical",
            doc="Adds a flag indicating if the transcript is the canonical transcript for the gene. ",
        ),
        ToolInput(
            "mane",
            Boolean(optional=True),
            prefix="--mane",
            doc="Adds a flag indicating if the transcript is the MANE Select transcript. "
            "Only available for human on the GRCh38 assembly",
        ),
        ToolInput(
            "biotype",
            Boolean(optional=True),
            prefix="--biotype",
            doc="Adds the biotype of the transcript or regulatory feature. ",
        ),
        ToolInput(
            "domains",
            Boolean(optional=True),
            prefix="--domains",
            doc="Adds names of overlapping protein domains to output. ",
        ),
        ToolInput(
            "xref_refseq",
            Boolean(optional=True),
            prefix="--xref_refseq",
            doc="Output aligned RefSeq mRNA identifier for transcript. The RefSeq and Ensembl transcripts aligned in "
            "this way MAY NOT, AND FREQUENTLY WILL NOT, match exactly in sequence, exon structure and protein product",
        ),
        ToolInput(
            "synonyms",
            Tsv(optional=True),
            prefix="--synonyms",
            doc="Load a file of chromosome synonyms. File should be tab-delimited with the primary identifier in "
            "column 1 and the synonym in column 2. Synonyms allow different chromosome identifiers to be used in the "
            "input file and any annotation source (cache, database, GFF, custom file, FASTA file). ",
        ),
    ]
