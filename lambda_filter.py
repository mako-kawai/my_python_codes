a=[3,4,5,6,7]
print(list(filter(lambda x:x%2,a)))
print(list(filter(lambda x:x%2==0,a)))
"""
The filter function takes a function and a sequence and returns a new sequence consisting
of those elements of the original sequence for which the function returns true.

In this example, we use a lambda function to check if each element of the list is odd (x%2) 
or even (x%2==0).

The filter function applies this lambda function to each element of the list 'a' 
and returns a new list containing only the odd or even numbers, respectively.
"""