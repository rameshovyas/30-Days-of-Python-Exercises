# Write a function which returns an array of seven random numbers in a range of 0-9. 
# All the numbers must be unique

import random 
def unique_numbers():
   return(random.sample(range(0,9),7))

print(unique_numbers())