# Write a function which checks if all the items of the list are of the same data type.

def is_same_type(lst):
    flag = True
    for i in range(0,len(lst)-1):
        if(type(lst[i]) != type(lst[i+1])):
            flag = False
            break

    return flag



print(is_same_type([1,2,True,"Jodhpur"]))
print(is_same_type([1,2]))
