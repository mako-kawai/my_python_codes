odds=[1,3,5,7,9]
squares=[x**2 for x in odds]
# Output: [1, 9, 25, 49, 81]
def divisors(n):
    return [x for x in range(1,n) if n%x==0]
"""
This function returns a list of all the divisors of n, excluding n itself.
For example, divisors(10) would return [1, 2, 5] since those are the numbers 
that divide 10 evenly without leaving a remainder.
"""