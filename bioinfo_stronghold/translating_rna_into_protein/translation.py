import Bio
import numpy as np
import os
import sys
from Bio.Seq import Seq

def read_seq(file):
    f = open(os.path.join(sys.path[0], file), "r")
    str = f.read().rstrip()
    f.close()
    return str

rna = read_seq('rosalind_prot.txt')
coding_dna = Seq(rna)
protein = coding_dna.translate().strip('*')
print(protein)