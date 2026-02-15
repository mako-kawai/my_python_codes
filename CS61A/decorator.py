def square(x):
    return x*x
def trace1(f):
    def traced(x):
        print('TRACE: {}({}) -> {}'.format(f.__name__,x,f(x)))
        return f(x)
    return traced
traced_square = trace1(square)
print(traced_square(3))

"""
@trace1 is equivalent to traced_square = trace1(square) and square = traced_square.
The @ syntax is just a convenient way to apply a decorator to a function.
"""