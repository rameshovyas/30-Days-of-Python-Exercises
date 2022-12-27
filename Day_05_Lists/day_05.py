# Declare an empty list
myList =[]

# Declare a list with more than 5 items
gods = ['Shiva', 'Rama', 'Krishna', 'Hanumana', 'Vishnu', 'Ganesha']

# Find the length of your list
print(len(gods))

# Get the first item, the middle item and the last item of the list
print(gods[0])
print(gods[len(gods)-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Mr. Human', 15, 6, "Un Married", "Planet Earth"]
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
first = it_companies[0]
last = it_companies[len(it_companies)-1]
middle = it_companies[int(len(it_companies)/2)]

print(first)
print(middle)
print(last)

# Print the list after modifying one of the companies
it_companies[0] = "Firmonyx"
print(it_companies)

