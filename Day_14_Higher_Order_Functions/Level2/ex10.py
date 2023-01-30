# Use reduce to sum all the numbers in the numbers list.

# In python 3 reduce is available in functools module and not a s independent function
from functools import reduce 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def add(x,y):
    return x+y


print(reduce(add,numbers))


