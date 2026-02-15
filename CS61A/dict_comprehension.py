def index(keys,values,match):
    return {k:[v for v in values if match(k,v)] for k in keys}
print(index([7,9,11],range(30,50),lambda x,y:y%x==0))