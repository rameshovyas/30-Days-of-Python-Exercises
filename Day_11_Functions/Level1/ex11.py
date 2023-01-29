# Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.

def add_item(lst,item):
    if(isinstance(lst,list)):
        if(item!=None):
            lst.append(item)
    return lst   
    
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Ice Cream')) 

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5)) 