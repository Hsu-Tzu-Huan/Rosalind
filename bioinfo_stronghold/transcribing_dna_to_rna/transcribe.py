def read_seq(file):
    f = open(file, 'r')
    seq = f.read().rstrip()
    f.close()
    return seq

def transcribe(seq):
    return seq.replace("T", "U")

seq = read_seq('rosalind_rna.txt')
print(transcribe(seq))