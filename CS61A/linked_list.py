class Link:
    empty=None
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first=first
        self.rest=rest
    def __repr__(self):
        if self.rest:
            return "Link({0},{1})".format(self.first,repr(self.rest))
        else:
            return "Link({0})".format(self.first)
    def __str__(self):
        if self.rest:
            return "{0} {1}".format(self.first,str(self.rest))
        else:
            return str(self.first)
# The above code defines a class named `Link` that represents a linked list.
# The class has an initializer that takes a `first` element and an optional `rest`
#   which defaults to `Link.empty`. The class also includes methods for string representation.
def range_link(start,end):
    """Return a Link of the integers from start to end."""
    if start>=end:
        return Link.empty
    else:
        return Link(start,range_link(start+1,end))
# The above code defines a function named `range_link` that takes two parameters, `start` and `end`.
# The function returns a `Link` object that contains the integers from `start` to `end - 1`.
def map_link(f,s):
    """Return a Link that is the result of mapping f over s."""
    if s == Link.empty:
        return s
    else:
        return Link(f(s.first),map_link(f,s.rest))
# The above code defines a function named `map_link` that takes a function `f` and a `Link` object `s`.
# The function returns a new `Link` object that is the result of applying the function 
#  'f` to each element of the `Link` object `s`.
def filter_link(f,s):
    """Return a Link that is the result of filtering s by f."""
    if s == Link.empty:
        return s
    else:
        rest=filter_link(f,s.rest)
        if f(s.first):
            return Link(s.first,rest)
        else:
            return rest