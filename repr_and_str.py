class ratio:
    def __init__(self,n,d):
        self.numer = n
        self.demon = d
    def __repr__(self):
        return "ratio({0},{1})".format(self.numer,self.demon)
    def __str__(self):
        return "{0}/{1}".format(self.numer,self.demon)
# The above code defines a class named `ratio` with an initializer that takes two parameters,
#   `n` and `d`, which are assigned to instance attributes `numer` and `demon`.
# The class also defines two special methods, `__repr__` and `__str__`, which return string representations of the object.
r = ratio(1,2)
print(repr(r))
print(str(r))