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
    Float,
    Stdout,
    InputSelector,
    ToolArgument,
)
from janis_core.operators.logical import If, IsDefined, AndOperator
from janis_core.operators.standard import JoinOperator
from janis_unix import Tsv

from janis_bioinformatics.data_types import (
    Fasta,
    CompressedVcf,
    Bam,
    BedTabix,
    VcfTabix,
)

from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool


class VepBase_98_3(BioinformaticsTool):
    def tool(self) -> str:
        return "vep"

    def friendly_name(self) -> str:
        return "Variant Effect Predictor (VEP)"

    def tool_provider(self):
        return "Ensembl"

    def base_command(self):
        return "vep"

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput(
                "inputFile",
                CompressedVcf(),
                prefix="--input_file",
                doc="Input file name. Can use compressed file (gzipped).",
            ),
            ToolInput(
                "outputFilename",
                Filename(prefix=InputSelector("inputFile"), extension=".vcf"),
                prefix="--output_file",
                doc="(-o) Output file name. Results can write to STDOUT by specifying "
                ' as the output file name - this will force quiet mode. Default = "variant_effect_output.txt"',
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
            # ToolInput('plugin', [PLUGINS](optional=True), prefix='--plugin',
            #           doc='Use named plugin. Plugin modules should be installed in the Plugins subdirectory of the VEP cache directory (defaults to $HOME/.vep/). Multiple plugins can be used by supplying the --plugin flag multiple times. See plugin documentation. Not used by default'),
            ToolInput(
                "help",
                Boolean(optional=True),
                prefix="--help",
                doc="Display help message and quit",
            ),
            ToolInput(
                "quiet",
                Boolean(optional=True),
                prefix="--quiet",
                doc="(-q) Suppress warning messages.Not used by default",
            ),
            ToolInput(
                "verbose",
                Boolean(optional=True),
                prefix="--verbose",
                doc="(-v) Print out a bit more information while running. Not used by default",
            ),
            ToolInput(
                "config",
                File(optional=True),
                prefix="--config",
                doc="""Load configuration options from a config file. The config file should consist of whitespace-separated pairs of option names and settings e.g.:

            output_file   my_output.txt
            species       mus_musculus
            format        vcf
            host          useastdb.ensembl.org

            A config file can also be implicitly read; save the file as $HOME/.vep/vep.ini (or equivalent directory if 
            using --dir). Any options in this file will be overridden by those specified in a config file using --config, 
            and in turn by any options specified on the command line. You can create a quick version file of this by 
            setting the flags as normal and running VEP in verbose (-v) mode. This will output lines that can be copied 
            to a config file that can be loaded in on the next run using --config. Not used by default""",
            ),
            ToolInput(
                "everything",
                Boolean(optional=True),
                prefix="--everything",
                doc="(-e) Shortcut flag to switch on all of the following: --sift b, --polyphen b, --ccds, "
                "--uniprot, --hgvs, --symbol, --numbers, --domains, --regulatory, --canonical, --protein, "
                "--biotype, --uniprot, --tsl, --appris, --gene_phenotype --af, --af_1kg, --af_esp, "
                "--af_gnomad, --max_af, --pubmed, --variant_class, --mane",
            ),
            ToolInput(
                "species",
                String(optional=True),
                prefix="--species",
                doc='Species for your data. This can be the latin name e.g. "homo_sapiens" or any Ensembl alias e.g. '
                '"mouse". Specifying the latin name can speed up initial database connection as the registry does '
                'not have to load all available database aliases on the server. Default = "homo_sapiens"',
            ),
            ToolInput(
                "assembly",
                String(optional=True),
                prefix="--assembly",
                doc="""(-a) Select the assembly version to use if more than one available. If using the cache, you must 
                have the appropriate assembly's cache file installed. If not specified and you have only 1 assembly 
                version installed, this will be chosen by default. Default = use found assembly version""",
            ),
            ToolInput(
                "inputData",
                String(optional=True),
                prefix="--input_data",
                doc="(--id) Raw input data as a string. May be used, for example, to input a single rsID or HGVS "
                "notation quickly to vep: --input_data rs699",
            ),
            ToolInput(
                "format",
                String(optional=True),
                prefix="--format",
                doc='Input file format - one of "ensembl", "vcf", "hgvs", "id", "region", "spdi". By default, '
                "VEP auto-detects the input file format. Using this option you can specify the input file is "
                "Ensembl, VCF, IDs, HGVS, SPDI or region format. Can use compressed version (gzipped) of any "
                "file format listed above. Auto-detects format by default",
            ),
            ToolInput(
                "forceOverwrite",
                Boolean(optional=True),
                prefix="--force_overwrite",
                doc="(--force) By default, VEP will fail with an error if the output file already exists. You can "
                "force the overwrite of the existing file by using this flag. Not used by default",
            ),
            ToolInput(
                "statsFile",
                String(optional=True),
                default="variant_effect_output.txt_summary.html",
                prefix="--stats_file",
                doc="(--sf) Summary stats file name. This is an HTML file containing a summary of the VEP run - the "
                'file name must end ".htm" or ".html". Default = "variant_effect_output.txt_summary.html"',
            ),
            ToolInput(
                "noStats",
                Boolean(optional=True),
                prefix="--no_stats",
                doc="""Don\'t generate a stats file. Provides marginal gains in run time.""",
            ),
            ToolInput(
                "statsText",
                Boolean(optional=True),
                prefix="--stats_text",
                doc="Generate a plain text stats file in place of the HTML.",
            ),
            ToolInput(
                "warningFile",
                Filename(suffix="warning", extension=".txt"),
                prefix="--warning_file",
                doc="File name to write warnings and errors to. Default = STDERR (standard error)",
            ),
            ToolInput(
                "maxSvSize",
                Boolean(optional=True),
                prefix="--max_sv_size",
                doc="Extend the maximum Structural Variant size VEP can process.",
            ),
            ToolInput(
                "noCheckVariantsOrder",
                Boolean(optional=True),
                prefix="--no_check_variants_order",
                doc="Permit the use of unsorted input files. However running VEP on unsorted input files slows down "
                "the tool and requires more memory.",
            ),
            ToolInput(
                "fork",
                Int(optional=True),
                default=CpuSelector(),
                prefix="--fork",
                doc="Enable forking, using the specified number of forks. Forking can dramatically improve runtime. "
                "Not used by default",
            ),
            ToolInput(
                "custom",
                Array(BedTabix, optional=True),
                prefix="--custom",
                prefix_applies_to_all_elements=True,
                doc="Add custom annotation to the output. Files must be tabix indexed or in the bigWig format. "
                "Multiple files can be specified by supplying the --custom flag multiple times. "
                "See https://asia.ensembl.org/info/docs/tools/vep/script/vep_custom.html for full details. "
                "Not used by default",
            ),
            ToolInput(
                "gff",
                File(optional=True),
                prefix="--gff",
                doc="Use GFF transcript annotations in [filename] as an annotation source. "
                "Requires a FASTA file of genomic sequence.Not used by default",
            ),
            ToolInput(
                "gtf",
                File(optional=True),
                prefix="--gtf",
                doc="Use GTF transcript annotations in [filename] as an annotation source. "
                "Requires a FASTA file of genomic sequence.Not used by default",
            ),
            ToolInput(
                "bam",
                Bam(optional=True),
                prefix="--bam",
                doc="ADVANCED Use BAM file of sequence alignments to correct transcript models not derived from "
                "reference genome sequence. Used to correct RefSeq transcript models. "
                "Enables --use_transcript_ref; add --use_given_ref to override this behaviour. Not used by default",
            ),
            ToolInput(
                "useTranscriptRef",
                Boolean(optional=True),
                prefix="--use_transcript_ref",
                doc="By default VEP uses the reference allele provided in the input file to calculate consequences "
                "for the provided alternate allele(s). Use this flag to force VEP to replace the provided "
                "reference allele with sequence derived from the overlapped transcript. This is especially "
                "relevant when using the RefSeq cache, see documentation for more details. The GIVEN_REF and "
                "USED_REF fields are set in the output to indicate any change. Not used by default",
            ),
            ToolInput(
                "useGivenRef",
                Boolean(optional=True),
                prefix="--use_given_ref",
                doc="Using --bam or a BAM-edited RefSeq cache by default enables --use_transcript_ref; add this flag "
                "to override this behaviour and use the provided reference allele from the input. Not used by default",
            ),
            ToolInput(
                "customMultiAllelic",
                Boolean(optional=True),
                prefix="--custom_multi_allelic",
                doc="By default, comma separated lists found within the INFO field of custom annotation VCFs are "
                "assumed to be allele specific. For example, a variant with allele_string A/G/C with associated "
                'custom annotation "single,double,triple" will associate triple with C, double with G and single '
                "with A. This flag instructs VEP to return all annotations for all alleles. Not used by default",
            ),
            ToolInput(
                "tab",
                Boolean(optional=True),
                prefix="--tab",
                doc="Writes output in tab-delimited format. Not used by default",
            ),
            ToolInput(
                "json",
                Boolean(optional=True),
                prefix="--json",
                doc="Writes output in JSON format. Not used by default",
            ),
            ToolInput(
                "compressOutput",
                String(optional=True),
                default="bgzip",
                prefix="--compress_output",
                doc="Writes output compressed using either gzip or bgzip. Not used by default",
            ),
            ToolInput(
                "fields",
                Array(String, optional=True),
                prefix="--fields",
                doc="""Configure the output format using a comma separated list of fields.
Can only be used with tab (--tab) or VCF format (--vcf) output.
For the tab format output, the selected fields may be those present in the default output columns, or 
any of those that appear in the Extra column (including those added by plugins or custom annotations). 
Output remains tab-delimited. For the VCF format output, the selected fields are those present within the ""CSQ"" INFO field.

Example of command for the tab output:

--tab --fields ""Uploaded_variation,Location,Allele,Gene""
Example of command for the VCF format output:

--vcf --fields ""Allele,Consequence,Feature_type,Feature""
Not used by default""",
            ),
            ToolInput(
                "minimal",
                Boolean(optional=True),
                prefix="--minimal",
                doc="Convert alleles to their most minimal representation before consequence calculation i.e. "
                "sequence that is identical between each pair of reference and alternate alleles is trimmed "
                "off from both ends, with coordinates adjusted accordingly. Note this may lead to discrepancies "
                "between input coordinates and coordinates reported by VEP relative to transcript sequences; "
                "to avoid issues, use --allele_number and/or ensure that your input variants have unique "
                "identifiers. The MINIMISED flag is set in the VEP output where relevant. Not used by default",
            ),
            ToolInput(
                "variantClass",
                Boolean(optional=True),
                prefix="--variant_class",
                doc="Output the Sequence Ontology variant class. Not used by default",
            ),
            ToolInput(
                "sift",
                String(optional=True),
                prefix="--sift",
                doc="Species limited SIFT predicts whether an amino acid substitution affects protein function based "
                "on sequence homology and the physical properties of amino acids. VEP can output the prediction "
                "term, score or both. Not used by default",
            ),
            ToolInput(
                "polyphen",
                String(optional=True),
                prefix="--polyphen",
                doc="Human only PolyPhen is a tool which predicts possible impact of an amino acid substitution on "
                "the structure and function of a human protein using straightforward physical and comparative "
                "considerations. VEP can output the prediction term, score or both. VEP uses the humVar score "
                "by default - use --humdiv to retrieve the humDiv score. Not used by default",
            ),
            ToolInput(
                "humdiv",
                Boolean(optional=True),
                prefix="--humdiv",
                doc="Human only Retrieve the humDiv PolyPhen prediction instead of the default humVar. "
                "Not used by default",
            ),
            ToolInput(
                "nearest",
                String(optional=True),
                prefix="--nearest",
                doc="""Retrieve the transcript or gene with the nearest protein-coding transcription start site 
                (TSS) to each input variant. Use ""transcript"" to retrieve the transcript stable ID, ""gene"" to 
                retrieve the gene stable ID, or ""symbol"" to retrieve the gene symbol. Note that the nearest 
                TSS may not belong to a transcript that overlaps the input variant, and more than one may be 
                reported in the case where two are equidistant from the input coordinates.

            Currently only available when using a cache annotation source, and requires the Set::IntervalTree perl module.
            Not used by default""",
            ),
            ToolInput(
                "distance",
                Array(Int, optional=True),
                separator=",",
                prefix="--distance",
                doc="Modify the distance up and/or downstream between a variant and a transcript for which VEP will assign the upstream_gene_variant or downstream_gene_variant consequences. Giving one distance will modify both up- and downstream distances; prodiving two separated by commas will set the up- (5') and down - (3') stream distances respectively. Default: 5000",
            ),
            ToolInput(
                "overlaps",
                Boolean(optional=True),
                prefix="--overlaps",
                doc="Report the proportion and length of a transcript overlapped by a structural variant in VCF format.",
            ),
            ToolInput(
                "genePhenotype",
                Boolean(optional=True),
                prefix="--gene_phenotype",
                doc="Indicates if the overlapped gene is associated with a phenotype, disease or trait. See list of phenotype sources. Not used by default",
            ),
            ToolInput(
                "regulatory",
                Boolean(optional=True),
                prefix="--regulatory",
                doc="Look for overlaps with regulatory regions. VEP can also report if a variant falls in a high information position within a transcription factor binding site. Output lines have a Feature type of RegulatoryFeature or MotifFeature. Not used by default",
            ),
            ToolInput(
                "cellType",
                Boolean(optional=True),
                prefix="--cell_type",
                doc="Report only regulatory regions that are found in the given cell type(s). Can be a single cell type or a comma-separated list. The functional type in each cell type is reported under CELL_TYPE in the output. To retrieve a list of cell types, use --cell_type list. Not used by default",
            ),
            ToolInput(
                "individual",
                Array(String, optional=True),
                prefix="--individual",
                separator=",",
                doc='Consider only alternate alleles present in the genotypes of the specified individual(s). May be a single individual, a comma-separated list or "all" to assess all individuals separately. Individual variant combinations homozygous for the given reference allele will not be reported. Each individual and variant combination is given on a separate line of output. Only works with VCF files containing individual genotype data; individual IDs are taken from column headers. Not used by default',
            ),
            ToolInput(
                "phased",
                Boolean(optional=True),
                prefix="--phased",
                doc="Force VCF genotypes to be interpreted as phased. For use with plugins that depend on phased data. Not used by default",
            ),
            ToolInput(
                "alleleNumber",
                Boolean(optional=True),
                prefix="--allele_number",
                doc="Identify allele number from VCF input, where 1 = first ALT allele, 2 = second ALT allele etc. Useful when using --minimal Not used by default",
            ),
            ToolInput(
                "showRefAllele",
                Boolean(optional=True),
                prefix="--show_ref_allele",
                doc='Adds the reference allele in the output. Mainly useful for the VEP "default" and tab-delimited output formats. Not used by default',
            ),
            ToolInput(
                "totalLength",
                Boolean(optional=True),
                prefix="--total_length",
                doc="Give cDNA, CDS and protein positions as Position/Length. Not used by default",
            ),
            ToolInput(
                "numbers",
                Boolean(optional=True),
                prefix="--numbers",
                doc="Adds affected exon and intron numbering to to output. Format is Number/Total. Not used by default",
            ),
            ToolInput(
                "noEscape",
                Boolean(optional=True),
                prefix="--no_escape",
                doc="Don't URI escape HGVS strings. Default = escape",
            ),
            ToolInput(
                "keepCsq",
                Boolean(optional=True),
                prefix="--keep_csq",
                doc="Don't overwrite existing CSQ entry in VCF INFO field. Overwrites by default",
            ),
            ToolInput(
                "vcfInfoField",
                String(optional=True),
                prefix="--vcf_info_field",
                doc='Change the name of the INFO key that VEP write the consequences to in its VCF output. Use "ANN" for compatibility with other tools such as snpEff. Default: CSQ',
            ),
            ToolInput(
                "terms",
                String(optional=True),
                prefix="--terms",
                doc='(-t) The type of consequence terms to output. The Ensembl terms are described here. The Sequence Ontology is a joint effort by genome annotation centres to standardise descriptions of biological sequences. Default = "SO"',
            ),
            ToolInput(
                "noHeaders",
                Boolean(optional=True),
                prefix="--no_headers",
                doc="Don't write header lines in output files. Default = add headers",
            ),
            ToolInput(
                "hgvs",
                Boolean(optional=True),
                prefix="--hgvs",
                doc="Add HGVS nomenclature based on Ensembl stable identifiers to the output. Both coding and protein sequence names are added where appropriate. To generate HGVS identifiers when using --cache or --offline you must use a FASTA file and --fasta. HGVS notations given on Ensembl identifiers are versioned. Not used by default",
            ),
            ToolInput(
                "hgvsg",
                Boolean(optional=True),
                prefix="--hgvsg",
                doc="Add genomic HGVS nomenclature based on the input chromosome name. To generate HGVS identifiers when using --cache or --offline you must use a FASTA file and --fasta. Not used by default",
            ),
            ToolInput(
                "shiftHgvs",
                Boolean(optional=True),
                prefix="--shift_hgvs",
                doc="""Enable or disable 3\' shifting of HGVS notations. When enabled, this causes ambiguous insertions or deletions (typically in repetetive sequence tracts) to be "shifted" to their most 3' possible coordinates (relative to the transcript sequence and strand) before the HGVS notations are calculated; the flag HGVS_OFFSET is set to the number of bases by which the variant has shifted, relative to the input genomic coordinates. Disabling retains the original input coordinates of the variant. Default: 1 (shift)""",
            ),
            ToolInput(
                "transcriptVersion",
                Boolean(optional=True),
                prefix="--transcript_version",
                doc="Add version numbers to Ensembl transcript identifiers",
            ),
            ToolInput(
                "protein",
                Boolean(optional=True),
                prefix="--protein",
                doc="Add the Ensembl protein identifier to the output where appropriate. Not used by default",
            ),
            ToolInput(
                "symbol",
                Boolean(optional=True),
                prefix="--symbol",
                doc="Adds the gene symbol (e.g. HGNC) (where available) to the output. Not used by default",
            ),
            ToolInput(
                "ccds",
                Boolean(optional=True),
                prefix="--ccds",
                doc="Adds the CCDS transcript identifer (where available) to the output. Not used by default",
            ),
            ToolInput(
                "uniprot",
                Boolean(optional=True),
                prefix="--uniprot",
                doc="Adds best match accessions for translated protein products from three UniProt-related databases (SWISSPROT, TREMBL and UniParc) to the output. Not used by default",
            ),
            ToolInput(
                "tsl",
                Boolean(optional=True),
                prefix="--tsl",
                doc="Adds the transcript support level for this transcript to the output. Not used by default. Note: Only available for human on the GRCh38 assembly",
            ),
            ToolInput(
                "appris",
                Boolean(optional=True),
                prefix="--appris",
                doc="Adds the APPRIS isoform annotation for this transcript to the output. Not used by default. Note: Only available for human on the GRCh38 assembly",
            ),
            ToolInput(
                "canonical",
                Boolean(optional=True),
                prefix="--canonical",
                doc="Adds a flag indicating if the transcript is the canonical transcript for the gene. Not used by default",
            ),
            ToolInput(
                "mane",
                Boolean(optional=True),
                prefix="--mane",
                doc="Adds a flag indicating if the transcript is the MANE Select transcript for the gene. Not used by default. Note: Only available for human on the GRCh38 assembly",
            ),
            ToolInput(
                "biotype",
                Boolean(optional=True),
                prefix="--biotype",
                doc="Adds the biotype of the transcript or regulatory feature. Not used by default",
            ),
            ToolInput(
                "domains",
                Boolean(optional=True),
                prefix="--domains",
                doc="Adds names of overlapping protein domains to output. Not used by default",
            ),
            ToolInput(
                "xrefRefseq",
                Boolean(optional=True),
                prefix="--xref_refseq",
                doc="Output aligned RefSeq mRNA identifier for transcript. Not used by default. Note: The RefSeq and Ensembl transcripts aligned in this way MAY NOT, AND FREQUENTLY WILL NOT, match exactly in sequence, exon structure and protein product",
            ),
            ToolInput(
                "synonyms",
                Tsv(optional=True),
                prefix="--synonyms",
                doc="Load a file of chromosome synonyms. File should be tab-delimited with the primary identifier in column 1 and the synonym in column 2. Synonyms allow different chromosome identifiers to be used in the input file and any annotation source (cache, database, GFF, custom file, FASTA file). Not used by default",
            ),
            ToolInput(
                "checkExisting",
                Boolean(optional=True),
                prefix="--check_existing",
                doc="""Checks for the existence of known variants that are co-located with your input. By default the alleles are compared and variants on an allele-specific basis - to compare only coordinates, use --no_check_alleles.

            Some databases may contain variants with unknown (null) alleles and these are included by default; to exclude them use --exclude_null_alleles.

            See this page for more details.

            Not used by default""",
            ),
            ToolInput(
                "checkSvs",
                Boolean(optional=True),
                prefix="--check_svs",
                doc="Checks for the existence of structural variants that overlap your input. Currently requires database access. Not used by default",
            ),
            ToolInput(
                "clinSigAllele",
                Boolean(optional=True),
                prefix="--clin_sig_allele",
                doc="Return allele specific clinical significance. Setting this option to 0 will provide all known clinical significance values at the given locus. Default: 1 (Provide allele-specific annotations)",
            ),
            ToolInput(
                "excludeNullAlleles",
                Boolean(optional=True),
                prefix="--exclude_null_alleles",
                doc="Do not include variants with unknown alleles when checking for co-located variants. Our human database contains variants from HGMD and COSMIC for which the alleles are not publically available; by default these are included when using --check_existing, use this flag to exclude them. Not used by default",
            ),
            ToolInput(
                "noCheckAlleles",
                Boolean(optional=True),
                prefix="--no_check_alleles",
                doc="""When checking for existing variants, by default VEP only reports a co-located variant if none of the input alleles are novel. For example, if your input variant has alleles A/G, and an existing co-located variant has alleles A/C, the co-located variant will not be reported.

            Strand is also taken into account - in the same example, if the input variant has alleles T/G but on the negative strand, then the co-located variant will be reported since its alleles match the reverse complement of input variant.

            Use this flag to disable this behaviour and compare using coordinates alone. Not used by default""",
            ),
            ToolInput(
                "af",
                Boolean(optional=True),
                prefix="--af",
                doc="Add the global allele frequency (AF) from 1000 Genomes Phase 3 data for any known co-located variant to the output. For this and all --af_* flags, the frequency reported is for the input allele only, not necessarily the non-reference or derived allele. Not used by default",
            ),
            ToolInput(
                "maxAf",
                Boolean(optional=True),
                prefix="--max_af",
                doc="Report the highest allele frequency observed in any population from 1000 genomes, ESP or gnomAD. Not used by default",
            ),
            ToolInput(
                "af1kg",
                String(optional=True),
                prefix="--af_1kg",
                doc="Add allele frequency from continental populations (AFR,AMR,EAS,EUR,SAS) of 1000 Genomes Phase 3 to the output. Must be used with --cache. Not used by default",
            ),
            ToolInput(
                "afEsp",
                Boolean(optional=True),
                prefix="--af_esp",
                doc="Include allele frequency from NHLBI-ESP populations. Must be used with --cache. Not used by default",
            ),
            ToolInput(
                "afGnomad",
                Boolean(optional=True),
                prefix="--af_gnomad",
                doc="Include allele frequency from Genome Aggregation Database (gnomAD) exome populations. Note only data from the gnomAD exomes are included; to retrieve data from the additional genomes data set, see this guide. Must be used with --cache Not used by default",
            ),
            ToolInput(
                "afExac",
                Boolean(optional=True),
                prefix="--af_exac",
                doc="Include allele frequency from ExAC project populations. Must be used with --cache. Not used by default. Note: ExAC data has been superceded by gnomAD. This flag remains for those wishing to use older cache versions containing ExAC data.",
            ),
            ToolInput(
                "pubmed",
                Boolean(optional=True),
                prefix="--pubmed",
                doc="Report Pubmed IDs for publications that cite existing variant. Must be used with --cache. Not used by default",
            ),
            ToolInput(
                "failed",
                Boolean(optional=True),
                prefix="--failed",
                doc="When checking for co-located variants, by default VEP will exclude variants that have been flagged as failed. Set this flag to include such variants. Default: 0 (exclude)",
            ),
            ToolInput(
                "gencodeBasic",
                Boolean(optional=True),
                prefix="--gencode_basic",
                doc="Limit your analysis to transcripts belonging to the GENCODE basic set. This set has fragmented or problematic transcripts removed. Not used by default",
            ),
            ToolInput(
                "excludePredicted",
                Boolean(optional=True),
                prefix="--exclude_predicted",
                doc='When using the RefSeq or merged cache, exclude predicted transcripts (i.e. those with identifiers beginning with "XM_" or "XR_").',
            ),
            ToolInput(
                "transcriptFilter",
                Boolean(optional=True),
                prefix="--transcript_filter",
                doc='''ADVANCED Filter transcripts according to any arbitrary set of rules. Uses similar notation to filter_vep.

            You may filter on any key defined in the root of the transcript object; most commonly this will be ""stable_id"":

            --transcript_filter ""stable_id match N[MR]_""''',
            ),
            ToolInput(
                "checkRef",
                Boolean(optional=True),
                prefix="--check_ref",
                doc="Force VEP to check the supplied reference allele against the sequence stored in the Ensembl Core database or supplied FASTA file. Lines that do not match are skipped. Not used by default",
            ),
            ToolInput(
                "lookupRef",
                Boolean(optional=True),
                prefix="--lookup_ref",
                doc="Force overwrite the supplied reference allele with the sequence stored in the Ensembl Core database or supplied FASTA file. Not used by default",
            ),
            ToolInput(
                "dontSkip",
                Boolean(optional=True),
                prefix="--dont_skip",
                doc="Don't skip input variants that fail validation, e.g. those that fall on unrecognised sequences. Combining --check_ref with --dont_skip will add a CHECK_REF output field when the given reference does not match the underlying reference sequence.",
            ),
            ToolInput(
                "allowNonVariant",
                Boolean(optional=True),
                prefix="--allow_non_variant",
                doc="When using VCF format as input and output, by default VEP will skip non-variant lines of input (where the ALT allele is null). Enabling this option the lines will be printed in the VCF output with no consequence data added.",
            ),
            ToolInput(
                "chr",
                Array(String, optional=True),
                prefix="--chr",
                separator=",",
                doc='Select a subset of chromosomes to analyse from your file. Any data not on this chromosome in the input will be skipped. The list can be comma separated, with "-" characters representing an interval. For example, to include chromosomes 1, 2, 3, 10 and X you could use --chr 1-3,10,X Not used by default',
            ),
            ToolInput(
                "codingOnly",
                Boolean(optional=True),
                prefix="--coding_only",
                doc="Only return consequences that fall in the coding regions of transcripts. Not used by default",
            ),
            ToolInput(
                "noIntergenic",
                Boolean(optional=True),
                prefix="--no_intergenic",
                doc="Do not include intergenic consequences in the output. Not used by default",
            ),
            ToolInput(
                "pick",
                Boolean(optional=True),
                prefix="--pick",
                doc="Pick once line or block of consequence data per variant, including transcript-specific columns. Consequences are chosen according to the criteria described here, and the order the criteria are applied may be customised with --pick_order. This is the best method to use if you are interested only in one consequence per variant. Not used by default",
            ),
            ToolInput(
                "pickAllele",
                Boolean(optional=True),
                prefix="--pick_allele",
                doc="Like --pick, but chooses one line or block of consequence data per variant allele. Will only differ in behaviour from --pick when the input variant has multiple alternate alleles. Not used by default",
            ),
            ToolInput(
                "perGene",
                Boolean(optional=True),
                prefix="--per_gene",
                doc="Output only the most severe consequence per gene. The transcript selected is arbitrary if more than one has the same predicted consequence. Uses the same ranking system as --pick. Not used by default",
            ),
            ToolInput(
                "pickAlleleGene",
                Boolean(optional=True),
                prefix="--pick_allele_gene",
                doc="Like --pick_allele, but chooses one line or block of consequence data per variant allele and gene combination. Not used by default",
            ),
            ToolInput(
                "flagPick",
                Boolean(optional=True),
                prefix="--flag_pick",
                doc="As per --pick, but adds the PICK flag to the chosen block of consequence data and retains others. Not used by default",
            ),
            ToolInput(
                "flagPickAllele",
                Boolean(optional=True),
                prefix="--flag_pick_allele",
                doc="As per --pick_allele, but adds the PICK flag to the chosen block of consequence data and retains others. Not used by default",
            ),
            ToolInput(
                "flagPickAlleleGene",
                Boolean(optional=True),
                prefix="--flag_pick_allele_gene",
                doc="As per --pick_allele_gene, but adds the PICK flag to the chosen block of consequence data and retains others. Not used by default",
            ),
            ToolInput(
                "pickOrder",
                Array(String, optional=True),
                prefix="--pick_order",
                separator=",",
                doc="""Customise the order of criteria (and the list of criteria) applied when choosing a block of annotation data with one of the following options: --pick, --pick_allele, --per_gene, --pick_allele_gene, --flag_pick, --flag_pick_allele, --flag_pick_allele_gene. See this page for the default order.
            Valid criteria are: [ canonical appris tsl biotype ccds rank length mane ]. e.g.:

            --pick --pick_order tsl,appris,rank""",
            ),
            ToolInput(
                "mostSevere",
                Boolean(optional=True),
                prefix="--most_severe",
                doc="Output only the most severe consequence per variant. Transcript-specific columns will be left blank. Consequence ranks are given in this table. To include regulatory consequences, use the --regulatory option in combination with this flag. Not used by default",
            ),
            ToolInput(
                "summary",
                Boolean(optional=True),
                prefix="--summary",
                doc="Output only a comma-separated list of all observed consequences per variant. Transcript-specific columns will be left blank. Not used by default",
            ),
            ToolInput(
                "filterCommon",
                Boolean(optional=True),
                prefix="--filter_common",
                doc="Shortcut flag for the filters below - this will exclude variants that have a co-located existing variant with global AF > 0.01 (1%). May be modified using any of the following freq_* filters. Not used by default",
            ),
            ToolInput(
                "checkFrequency",
                Boolean(optional=True),
                prefix="--check_frequency",
                doc="Turns on frequency filtering. Use this to include or exclude variants based on the frequency of co-located existing variants in the Ensembl Variation database. You must also specify all of the --freq_* flags below. Frequencies used in filtering are added to the output under the FREQS key in the Extra field. Not used by default",
            ),
            ToolInput(
                "freqPop",
                String(optional=True),
                prefix="--freq_pop",
                doc="Name of the population to use in frequency filter. This must be one of the following: (1KG_ALL, 1KG_AFR, 1KG_AMR, 1KG_EAS, 1KG_EUR, 1KG_SAS, AA, EA, gnomAD, gnomAD_AFR, gnomAD_AMR, gnomAD_ASJ, gnomAD_EAS, gnomAD_FIN, gnomAD_NFE, gnomAD_OTH, gnomAD_SAS)",
            ),
            ToolInput(
                "freqFreq",
                Float(optional=True),
                prefix="--freq_freq",
                doc="Allele frequency to use for filtering. Must be a float value between 0 and 1",
            ),
            ToolInput(
                "freqGtLt",
                String(optional=True),
                prefix="--freq_gt_lt",
                doc="Specify whether the frequency of the co-located variant must be greater than (gt) or less than (lt) the value specified with --freq_freq",
            ),
            ToolInput(
                "freqFilter",
                String(optional=True),
                prefix="--freq_filter",
                doc="Specify whether to exclude or include only variants that pass the frequency filter",
            ),
            # CADD plugin
            ToolInput("caddReference", Array(VcfTabix, optional=True)),
            # Condel
            ToolInput(
                "condelConfig",
                Directory(optional=True),
                doc="Directory containing CondelPlugin config, in format: '<dir>/condel_SP.conf'",
            ),
            # dbNSFP
            ToolInput("dbnspReference", VcfTabix(optional=True), doc=""),
            ToolInput("dbsnpColumns", Array(String, optional=True)),
            # REVEL
            ToolInput("revelReference", VcfTabix(optional=True)),
            # CUSTOM
            ToolInput("custom1Reference", VcfTabix(optional=True)),
            ToolInput("custom1Columns", Array(String, optional=True)),
            ToolInput("custom2Reference", VcfTabix(optional=True)),
            ToolInput("custom2Columns", Array(String, optional=True)),
        ]

    def arguments(self):
        return [
            # CADD
            ToolArgument(
                If(
                    IsDefined(InputSelector("caddReference")),
                    "--plugin CADD,"
                    + JoinOperator(InputSelector("caddReference"), ","),
                    "",
                ),
                shell_quote=False,
            ),
            # Condel
            ToolArgument(
                If(
                    IsDefined(InputSelector("condelConfig")),
                    "--plugin "
                    + StringFormatter(
                        "Condel,{condelconfig},b",
                        condelconfig=InputSelector("condelConfig"),
                    ),
                    "",
                ),
                shell_quote=False,
            ),
            # dbNSFP
            ToolArgument(
                If(
                    AndOperator(
                        IsDefined(InputSelector("dbnspReference")),
                        IsDefined(InputSelector("dbsnpColumns")),
                    ),
                    "--plugin "
                    + StringFormatter(
                        "dbNSFP,{ref},{cols}",
                        ref=InputSelector("dbnspReference"),
                        cols=JoinOperator(InputSelector("dbsnpColumns"), ","),
                    ),
                    "",
                ),
                shell_quote=False,
            ),
            # REVEL
            ToolArgument(
                If(
                    IsDefined(InputSelector("revelReference")),
                    "--plugin "
                    + StringFormatter(
                        "REVEL,{ref}", ref=InputSelector("revelReference")
                    ),
                    "",
                ),
                shell_quote=False,
            ),
            # CUSTOM 1
            ToolArgument(
                If(
                    AndOperator(
                        IsDefined(InputSelector("custom1Reference")),
                        IsDefined(InputSelector("custom1Columns")),
                    ),
                    "--custom "
                    + StringFormatter(
                        "{ref},{cols}",
                        ref=InputSelector("custom1Reference"),
                        cols=JoinOperator(InputSelector("custom1Columns"), ","),
                    ),
                    "",
                ),
                shell_quote=False,
            ),
            # CUSTOM 2
            ToolArgument(
                If(
                    AndOperator(
                        IsDefined(InputSelector("custom2Reference")),
                        IsDefined(InputSelector("custom2Columns")),
                    ),
                    "--custom "
                    + StringFormatter(
                        "{ref},{cols}",
                        ref=InputSelector("custom2Reference"),
                        cols=JoinOperator(InputSelector("custom2Columns"), ","),
                    ),
                    "",
                ),
                shell_quote=False,
            ),
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput("std", Stdout),
            ToolOutput("out", File, glob=InputSelector("outputFilename")),
            ToolOutput(
                "stats", File(extension=".html"), glob=InputSelector("statsFile")
            ),
        ]
