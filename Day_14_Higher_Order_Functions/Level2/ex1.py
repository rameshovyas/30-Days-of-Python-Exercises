# Use map to create a new list by changing each country to uppercase in the countries list
def to_upperCase(str):
    return str.upper()

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

countries_uppercased = map(to_upperCase,countries)

print(list(countries_uppercased))