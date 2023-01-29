# Declare a function named remove_item. It takes a list and an item parameters. 
# It returns a list with the item removed from it.

def remove_item(lst,item):
    if(isinstance(lst,list) and len(lst)>0):
        if(item!=None):
            lst.remove(item)
    return lst   
    
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3)) 