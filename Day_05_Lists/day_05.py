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

# Add an IT company to it_companies
it_companies.append("TCS")
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies)/2)-1, "Infosys")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())

# Check if a certain company exists in the it_companies list.
print()

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
num_of_elements = 3
start = (len(it_companies) // 2) - (num_of_elements // 2)
end = (len(it_companies) // 2) + (num_of_elements // 2)
print(it_companies[start: end + 1])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del(it_companies)


# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack.append("Python")
full_stack.append("SQL")
print(full_stack)