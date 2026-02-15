class ratio:
    def __init__(self,n,d):
        self.numer = n
        self.demon = d
    def __repr__(self):
        return "ratio({},{})".format(self.numer,self.demon)
    def __str__(self):
        return "{}/{}".format(self.numer,self.demon)
    def __add__(self,other):
        if isinstance(other,ratio):
            n=self.numer*other.demon+other.numer*self.demon
            d=self.demon*other.demon
            g=gcd(n,d)
            return ratio(n//g,d//g)
        elif isinstance(other,int):
            n=self.numer+other*self.demon
            d=self.demon
            g=gcd(n,d)
            return ratio(n//g,d//g)
        elif isinstance(other,float):
            return float(self.numer/self.demon)+other
        else:
            return NotImplemented
    __radd__=__add__
def gcd(n,d):
    while n!=d:
        n,d = min(n,d),abs(n-d)
    return n
# The above code defines a class named `ratio` that represents a rational number with a numerator and denominator.
# The class includes methods for string representation and addition with other `ratio` instances, integers,