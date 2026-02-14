d={'one':1,"two":2,"three":3}
d['zero']=0
k=iter(d.keys()) #iter()函数返回一个迭代器对象
print(next(k)) #next()函数返回迭代器的下一个项目
print(next(k))
print(next(k))
print(next(k))
#print(next(k)) #StopIteration异常，迭代器没有更多的值了