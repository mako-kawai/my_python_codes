"""
Count how many pairs in the list have equal elements.
"""
sequence=[[1,2],[2,2],[3,2],[4,4]]
total=0
for x,y in sequence:
    if x==y:
        total+=1
print(total)