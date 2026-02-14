def oven(start,end):
    oven=start+start%2
    while oven<=end:
        yield oven
        oven+=2
#yield语句把一个函数变成一个生成器，生成器是一个迭代器
print(oven(1,10))
print(list(oven(1,10)))
print('------------------')
def countdown(k):
    if k>0:
        yield k
        yield from countdown(k-1)
    else:
        yield 'Blastoff'
#yield from语句用于在一个生成器函数中调用另一个生成器
print(list(countdown(5)))
print('------------------')
def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s
#prefixes函数生成字符串s的所有前缀
print(list(prefixes('abcd')))
print('------------------')
def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
#substrings函数生成字符串s的所有子串
print(list(substrings('abc')))
"""
now, it is time to learn about generators,
  which are a powerful tool for creating iterators in Python.
A generator is a special type of function that can be paused and resumed,
  allowing it to produce a sequence of values over time instead of computing them all at once.
This can be particularly useful when working with large datasets
  or when you want to generate an infinite sequence of values.
"""
def list_partition(n,m):
    if n<0 or m==0:
        return []
    else:
        exact_match=[]
        if n==m:
            exact_match=[[m]]
        with_m=[p+[m] for p in list_partition(n-m,m)]
        without_m=list_partition(n,m-1)
        return exact_match+with_m+without_m
#list_partition函数计算将n分成不超过m的整数之和的不同方法的列表
#now we use generators to compute the same thing
def partition(n,m):
    if n>0 and m>0:
        if n==m:
            yield str(m)
        for p in partition(n-m,m):
            yield p+'+'+str(m)
        yield from partition(n,m-1)
    