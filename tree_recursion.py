from ftracer import trace
@trace
def fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
@trace
def count_partition(n,m):
    if n==0:
        return 1
    elif n<0:
        return 0
    elif m==0:
        return 0
    else:
        return count_partition(n-m,m)+count_partition(n,m-1)
#partition函数计算将n分成不超过m的整数之和的不同方法的数量