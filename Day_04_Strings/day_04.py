# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
_thirty = 'Thirty'
_days = 'Days'
_of = 'Of'
_python = 'Python'
space =' '
str = _thirty + space + _days + space + _of + space + _python
print(str)


# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
_coding = 'Coding'
_for = 'For'
_all = 'All'
space =' '
str = _coding + space + _for + space + _all
print(str)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
_first = company.split(' ')[0]
print(_first)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(True) if(company.index("Coding") > -1 ) else print(False)
print(True) if(company.find("Coding") > -1 ) else print(False)

# Replace the word coding in the string 'Coding For All' to Python.
company = company.replace("Coding","Python")
print(company)

# Change Python for All to Python for Everyone using the replace method or other methods.
company = company.replace("All","Everyone")
print(company)

# Split the string 'Coding For All' using space as the separator (split()) .
str = 'Coding For All'
print(str.split(' '))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(str.split(","))

# What is the character at index 0 in the string Coding For All.
str = 'Coding For All'
print(str[0])

# What is the last index of the string Coding For All.
print(len(str)-1)

# What character is at index 10 in "Coding For All" string.
print(str[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
str = 'Python For Everyone'
abr=''
for s in str.split(' '):
    abr = abr + s[0]
print(abr)

# Create an acronym or an abbreviation for the name 'Coding For All'.
str = 'Coding For All'
abr=''
for s in str.split(' '):
    abr = abr + s[0]
print(abr)

# Use index to determine the position of the first occurrence of C in Coding For All.
str = 'Coding For All'
print(str.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(str.index('F'))