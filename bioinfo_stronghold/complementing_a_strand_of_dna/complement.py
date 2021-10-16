def read_seq(file):
    f = open(file, 'r')
    seq = f.read().rstrip()
    f.close()
    return seq

def complement(seq):
    comp = ''
    for i in range(len(seq)):
        if seq[i] == 'A':
            comp += 'T'
        elif seq[i] == 'T':
            comp += 'A'
        elif seq[i] == 'C':
            comp += 'G'
        elif seq[i] == 'G':
            comp += 'C'
    return comp[::-1]

seq = read_seq('rosalind_revc.txt')
print(complement(seq))