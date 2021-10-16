def read_num(file):
    f = open(file, 'r')
    str = f.read().rstrip()
    f.close()
    nums = str.split(' ')
    return nums

nums = read_num('rosalind_fibd.txt')
n = int(nums[0])
m = int(nums[1])
rab = [1, 1]                                                               
mon = 2                                                                     

while mon < n:
    if mon < m:               
        rab.append(rab[-2] + rab[-1])
    elif mon == m or mon == m + 1:
        rab.append(rab[-2] + rab[-1] - 1)
    else:
        rab.append(rab[-2] + rab[-1] - rab[-(m + 1)])
    mon += 1
print(rab[-1])