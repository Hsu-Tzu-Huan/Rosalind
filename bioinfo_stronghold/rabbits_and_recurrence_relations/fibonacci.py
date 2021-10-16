def read_num(file):
    f = open(file, 'r')
    str = f.read().rstrip()
    f.close()
    nums = str.split(' ')
    return nums

def fib(n, k):
    if n == 2:
        return 1
    if n == 1:
        return 1
    return fib(n-1, k) + k*fib(n-2, k)

nums = read_num('rosalind_fib.txt')
print(fib(int(nums[0]),int(nums[1])))