# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
if(a > b):
    print("%s is greater than %s" % (a,b))
else:
    if(a<b):
       print("%s is less than %s" % (a,b))
    else:
        print("Both are equal")        
