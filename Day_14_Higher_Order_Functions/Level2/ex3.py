# Use map to change each name to uppercase in the names list
def to_upperCase(str):
    return str.upper()

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

names_uppercased = list(map(to_upperCase,names))

print(names_uppercased)