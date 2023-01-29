# Declare a function named sum_of_numbers. It takes a number parameter and it 
# adds all the numbers in that range.

def sum_of_numbers(num):
    sum = 0
    if(num > 0):
        for i in range(1,num+1):
            sum+=i
    return sum


print(sum_of_numbers(5))

print(sum_of_numbers(10))

print(sum_of_numbers(100))