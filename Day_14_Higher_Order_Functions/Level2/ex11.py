# Use reduce to concatenate all the countries and to 
# produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

last_item = countries.pop()

def concatenate(s1,s2):
    if( (type(s1) is str) and (type(s1) is str) ):
        return s1 + ", " + s2

str = reduce(concatenate, countries) + ", and " + last_item + " are north European countries"

print(str)


