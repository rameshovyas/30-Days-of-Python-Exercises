# Call your function factorial, it takes a whole number as a parameter 
# and it return a factorial of the number

def factorial(num : int):    
    fact = 1
    if(num>=0):
        if(num == 0 or num ==1):
            fact = 1
        else:
            for i in range(1, num+1):
                fact *=i
    else: fact = None  
              
    return fact

print(factorial(5))

print(factorial(-1))