# Declare a function named print_list. It takes a list as a parameter 
# and it prints out each element of the list.

def print_list(lst):
    if(len(lst)>0):
        for l in lst:
            print(l)
    else:
        print("List is empty")

gods = ['Shiva', 'Rama', 'Krishna', 'Hanumana', 'Vishnu', 'Ganesha']

print_list(gods)