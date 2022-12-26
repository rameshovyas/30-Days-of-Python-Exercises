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
