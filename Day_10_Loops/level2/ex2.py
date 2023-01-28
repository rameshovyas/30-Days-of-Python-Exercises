# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds
sum_odd = 0
sum_even = 0
for i in range(0,101):
    if(i%2 ==0):
        sum_even += i
    else:
        sum_odd += i
print("The sum of all evens is %s . And the sum of all odds is %s." % (sum_even, sum_odd))            