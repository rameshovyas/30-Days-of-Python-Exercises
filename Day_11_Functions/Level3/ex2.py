# Write a functions which checks if all items are unique in the list.

def is_unique(lst):
    # Create a set from the list
    test_set = set()
    test_set.update(lst)    
    if(len(test_set) == len(lst)):
        return True
    return False


list1 = [1,2,3,4]

list2 = [1,2,2,3,4]

print(is_unique(list1))

print(is_unique(list2))
