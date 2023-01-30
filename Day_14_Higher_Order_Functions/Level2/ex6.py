# Use filter to filter out countries containing six letters and more in the country list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def filter_by_length(str,min_len):
    if((min_len>0) and (len(str)>=min_len)) : 
        return True
    return False

# We have to use lambda function sience we want to pass arguments to filter function
filtered_countries = filter(lambda item: filter_by_length(item, 6), countries)

print(list(filtered_countries))