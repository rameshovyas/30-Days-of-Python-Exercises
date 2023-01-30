# Declare a function called get_string_lists which takes a list as a parameter and 
# then returns a list containing only string items.

def get_string_lists(lst):
    return list(filter(lambda item : type(item) is str, lst))

my_list = ['Jodhpur', 23, False, 'Ramesh', 'Love My India']

filtered_list = get_string_lists(my_list)

print(filtered_list)
