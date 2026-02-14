def adder(n):
    def add(x):
        return x+n
    return add
def square(x):
    return x*x
def compose(f,g):
    def h(x):
        return f(g(x))
    return h
def double(x):
    return 2*x
def identity(x):
    return x
# %%
compose(double,square)(3)