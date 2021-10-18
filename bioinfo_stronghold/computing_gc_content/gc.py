from __future__ import division
import sys
import os

def read_file(file_name):
    f = open(os.path.join(sys.path[0], file_name), "r")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n')
    f.close()
    return lines

def form_seq(seq):
    fasta = []
    for line in seq:
        if line[0] == '>':
            fasta.append(line.rstrip())
            fasta.append('')
        else:
            fasta[-1] += line.rstrip()
    return fasta

def highest_gc_content(fasta):
    gc = {}
    for i in range(0, len(fasta), 2):
        if fasta[i][0] == '>':
            gc[fasta[i][1:]] = 0
            gc[fasta[i][1:]] = (fasta[i+1].count('G') + fasta[i+1].count("C"))*100/len(fasta[i+1])
    return gc

seq = read_file('rosalind_gc.txt')
fasta = form_seq(seq)
gc = highest_gc_content(fasta)
print(max(gc, key=gc.get))
print("{:.6f}".format(gc[max(gc, key=gc.get)]))
