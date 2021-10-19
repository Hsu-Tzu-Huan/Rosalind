from math import comb

def read_num(file):
    f = open(file, 'r')
    str = f.read().rstrip()
    f.close()
    nums = str.split(' ')
    return nums

def mendel_prob(k,m,n):
    prob = (comb(k,2)+ k*m + k*n + comb(m,2)*0.75 + m*n*0.5)/comb(k+m+n,2)
    return prob

pop = read_num('rosalind_iprb.txt')
print(mendel_prob(int(pop[0]), int(pop[1]), int(pop[2])))