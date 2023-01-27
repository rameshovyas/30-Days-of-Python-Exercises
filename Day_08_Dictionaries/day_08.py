# Create an empty dictionary called dog
dog = {}
print(dog)
# alternative way
dog = dict()
print(dog)

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] ="dog1"
dog["breed"] = "bulldog"
dog["legs"] = "4"
dog["age"] = "2"

print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name" : "Rajendra", 
    "last_name" : "Raj", 
    "gender" : "male", 
    "age": "25", 
    "maritial status" : "unmarried", 
    "skills" : ["frondend", "database design", "CSS"],
    "country" : "India", 
    "city" : "Jodhpur",
    "address" : "Sardarpura"
    }

print(student)   

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
skills = student["skills"]
print(type(skills))

# Modify the skills values by adding one or two skills
student["skills"].append("RESP Api")
print(student["skills"])

# Get the dictionary keys as a list
keys = student.keys()
print(keys)

# Get the dictionary values as a list
values = student.values()
print(values)

# Change the dictionary to a list of tuples using items() method
list_of_tuples = student.items()
print(list_of_tuples)

# Delete one of the items in the dictionary
student.pop("last_name")
print(student)

# Delete the dictionaries
del student