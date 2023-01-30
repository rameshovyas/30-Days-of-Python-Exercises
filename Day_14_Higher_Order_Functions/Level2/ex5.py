# Use filter to filter out countries having exactly six characters.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def filter_by_length(str,num):
    if((num>0) and (len(str)==num)) : 
        return True
    return False

# We have to use lambda function sinece we want to pass arguments to filter function
filtered_countries = filter(lambda item: filter_by_length(item, 6), countries)

print(list(filtered_countries))