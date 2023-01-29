# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [n for n in numbers if(n<=0)]
print(filtered)