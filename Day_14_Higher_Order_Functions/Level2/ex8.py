# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

def to_upperCase(str):
    return str.upper()

def filter_by_char(str):
    if((len(str)>0) and (str.startswith('E'))) : 
        return True
    return False

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

filtered_countries = list(filter(filter_by_char ,list(map(to_upperCase, countries))))

print(filtered_countries)