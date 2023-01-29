# Write a function which check if provided variable is a valid python variable
def is_valid(data):
    return data.isidentifier()


print(is_valid("1Ramesh"))

print(is_valid("Jodhpur"))

