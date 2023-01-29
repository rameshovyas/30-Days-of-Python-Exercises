# Declare a function named sum_of_even. It takes a number parameter and it adds all the
# even numbers in that - range.

def sum_of_even(num):
    sum = 0
    if(num > 0):
        for i in range(0,num+1,2):
            sum+=i
    return sum


print(sum_of_even(5))

print(sum_of_even(10))

print(sum_of_even(100))