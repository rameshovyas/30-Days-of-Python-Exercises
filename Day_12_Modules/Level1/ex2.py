# Declare a function named user_id_gen_by_user. 
import string
import random

def user_id_gen_by_user():
    num_char, num = input().split()
    num_char = int(num_char)
    num = int(num)
    if((num_char>0) and (num>0)):
        for i in range(1,num+1):
            str = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=num_char))
            print(str)                             

user_id_gen_by_user()