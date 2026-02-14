"""
Mutual recursion is when two or more functions call each other. 
In this example, we have two functions, luhn_sum and luhn_sum_double,
that call each other to compute the Luhn sum of a number.  
The Luhn sum is used in credit card validation.

"""
def split(n):
    return n//10,n%10
def digit_sum(n):
    if n<10:
        return n
    else:
        return digit_sum(split(n)[0])+split(n)[1]
def luhn_sum(n):
    if n<10:
        return n
    else:
        all_but_last,last=split(n)
        return luhn_sum_double(all_but_last)+last
def luhn_sum_double(n):
    all_but_last,last=split(n)
    luhn_digit=digit_sum(2*last)
    if n<10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last)+luhn_digit