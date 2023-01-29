# Declare a function named reverse_list. It takes an array as a parameter and it returns
# the reverse of the array (use loops).
def reverse_list(lst):
    rev=[]
    if(len(lst)>0):
        for i in range(len(lst)-1,-1,-1):
            rev.append(lst[i])
    return rev

gods = ['Shiva', 'Rama', 'Krishna', 'Hanumana', 'Vishnu', 'Ganesha']

print(reverse_list(gods))