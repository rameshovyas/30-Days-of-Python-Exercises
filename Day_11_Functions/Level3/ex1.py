# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    flag = True
    if(type(num) is int):
        if(num > 1):
            for i in range(2, int(num/2) + 1):
                if(i %2 == 0):
                    flag = False
                    break
        else : flag = False    
    else: flag =  False    

    return flag



print(is_prime(2))