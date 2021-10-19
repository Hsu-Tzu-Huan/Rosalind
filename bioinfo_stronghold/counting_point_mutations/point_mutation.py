import numpy as np
import os
import sys

def read_seq(file):
    f = open(os.path.join(sys.path[0], file), "r")
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    f.close()
    return lines

# lines = ['GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT']
lines = read_seq('rosalind_hamm.txt')
cnt = 0
for i in range(len(lines[0])):
    if lines[0][i] != lines[1][i]:
        cnt += 1 
print(cnt)