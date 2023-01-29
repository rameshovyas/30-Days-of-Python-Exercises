# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

lst = [2,56,87,23]
print(lst)

print(shuffle_list(lst))