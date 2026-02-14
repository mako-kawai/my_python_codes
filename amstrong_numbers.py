for n in range(100,1000):
    if n==sum([int(i)**3 for i in str(n)]):
        print(n,end='\t')
# This code finds and prints all Armstrong numbers (also known as narcissistic numbers) between 100 and 999.
# An Armstrong number is a three-digit number that is equal to the sum of the cubes of its digits.
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
# The output will be the Armstrong numbers separated by tabs.