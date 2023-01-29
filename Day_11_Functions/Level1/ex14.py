# Declare a function named sum_of_odds. It takes a number parameter and it adds all the 
# odd numbers in that range.

def sum_of_odds(num):
    sum = 0
    if(num > 0):
        for i in range(1,num+1,2):
            sum+=i
    return sum


print(sum_of_odds(5))

print(sum_of_odds(10))

print(sum_of_odds(100))