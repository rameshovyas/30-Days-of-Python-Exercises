# Write a function which generates a six digit/character random_user_id. 
import string
import random
def random_user_id():
    str = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=6))
    return str


print(random_user_id())                                 