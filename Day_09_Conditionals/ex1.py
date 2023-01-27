# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 

age = int(input("Enter your age( In Years): "))
if(age>0):
    if (age >=18):
        print("You are old enough to learn to drive")
    else:
        print("You need %s more years to learn to drive." %(18-age))
else:
    print("Enter a valid age")
