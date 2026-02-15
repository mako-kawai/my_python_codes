a=[5,7,2,11,3,4,9,8]
b=sorted(a)
print("a:",a)
print("b:",b)
test=[('b',6),('a',3),('c',1),('d',4),('e',2),('f',5)]
print(sorted(test,key=lambda x:x[0]))
print(sorted(test,key=lambda x:x[1]))
print(sorted(test,key=lambda x:x[1],reverse=True))