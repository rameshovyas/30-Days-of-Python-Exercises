# Compare the values of my_age and your_age using if … else. Who is older (me or you)?
#  Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 
# 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age 
my_age = 25
your_age = int(input("Enter your age: "))
if(your_age >0):
    if(my_age == your_age):
        print("We are of same age")
    else:
        if(my_age>your_age):
            if(my_age-your_age==1):
                print("I am 1 year older than you")
            else:
                print("I am %s years older than you" % (my_age-your_age))
        else:
           if(your_age-my_age==1):
                print("You are 1 year older than me")
           else:
                print("You are %s years older than me" % (your_age-my_age))  
else:
    print("Enter a valid age in years")    