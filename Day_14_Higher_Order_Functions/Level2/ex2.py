# Use map to create a new list by changing each number to its square in the numbers list
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_squared = list(map(square,numbers))

print(numbers_squared)