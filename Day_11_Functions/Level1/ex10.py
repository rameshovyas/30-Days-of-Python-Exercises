# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a 
# capitalized list of items

def capitalize_list_items(lst):
    result=[]
    if(len(lst) > 0):
        for l in lst:
            if(isinstance(l,str)):
                result.append(l.capitalize())
    return result


print(capitalize_list_items(["banana","apple", "grapes","oranges"]))            

# Test for non string items
print(capitalize_list_items([1,2,3,4]))
