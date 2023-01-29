# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(lst):
    if(len(lst) == 0):
        return True
    return False


print(is_empty([]))

print(is_empty([1,2,3,4]))

print(is_empty(()))
