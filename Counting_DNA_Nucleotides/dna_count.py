def read_seq(file):
    f = open(file, 'r')
    seq = f.read().rstrip()
    f.close()
    return seq
def dna_counter(seq):
    cnt_dict = {'A':0, 'T':0, 'C':0, 'G':0}
    for i in range(len(seq)):
        cnt_dict[seq[i]] += 1
    return cnt_dict
seq = read_seq('rosalind_dna.txt')
print('{} {} {} {}'.format(dna_counter(seq)['A'], dna_counter(seq)['C'], dna_counter(seq)['G'], dna_counter(seq)['T']))