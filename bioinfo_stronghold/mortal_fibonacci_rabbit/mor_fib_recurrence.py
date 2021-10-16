def read_num(file):
    f = open(file, 'r')
    str = f.read().rstrip()
    f.close()
    nums = str.split(' ')
    return nums

def mor_fib(n, m):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n <= m:
        return mor_fib(n-1, m) + mor_fib(n-2, m)
    elif n == m+1:
        return mor_fib(n-1, m) + mor_fib(n-2, m) - 1
    else:
        return mor_fib(n-1, m) + mor_fib(n-2, m) - mor_fib(n-(m+1), m)
print(mor_fib(86,17))
# nums = read_num('rosalind_fibd.txt')
# print(mor_fib(int(nums[0]),int(nums[1])))