# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts
# number of evens and odds in the number.
def evens_and_odds(num):
    evens = 0
    odds = 0
    for i in range(0,num+1):
        if(i%2 ==0):
            evens+=1
        else:
            odds+=1

    print("The number of odds are ", odds)
    print("The number of evens are ", evens)
            

evens_and_odds(100)