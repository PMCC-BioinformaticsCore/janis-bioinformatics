# from os.path import dirname, basename, isfile
# import glob

from .bioinformaticstoolbase import BioinformaticsTool, BioinformaticsWorkflow
from . import bcftools, bwa, common, gatk4, htslib, igvtools, illumina, samtools, validation

# directory = dirname(__file__)
# modules = glob.glob(directory+"/*")
# __all__ = [ (basename(f) if isfile(f) else basename(directory) + '.' + basename(f)) for f in modules if not f.endswith('__init__.py')]
# print(__all__)
