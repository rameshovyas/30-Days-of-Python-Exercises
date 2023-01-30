# Use filter to filter out countries containing 'land'.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def filter_land(str):
    if ('land' in str):
        return True
    return False

filtered_countries = list(filter(filter_land, countries))

print(filtered_countries)