import numpy as np
import os
import sys

def read_num(file):
    f = open(os.path.join(sys.path[0], file), "r")
    str = f.read().rstrip()
    f.close()
    nums = str.split(' ')
    nums = [int(i) for i in nums]
    return nums

pop = np.array(read_num('rosalind_iev.txt'))
prob = np.array([1, 1, 1, 0.75, 0.5, 0])
print(2*np.dot(pop, prob))