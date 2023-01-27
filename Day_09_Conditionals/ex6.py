# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input ("Enter any fruit name : ")

if(fruit!=""):
    if fruit in fruits:
        print("%s already exist in the list" % (fruit))
    else:
        fruits.append(fruit)
        print(fruits)    
else:
    print("Please provide a valid string for fruit name")    