# Use filter to filter out countries starting with an 'E'
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def filter_by_char(str):
    if((len(str)>0) and (str.startswith('E'))) : 
        return True
    return False

# We have to use lambda function sience we want to pass arguments to filter function
filtered_countries = list(filter(filter_by_char, countries))

print(filtered_countries)