# Given sets
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
len_list = len(age)
len_set = len(age_set)
print("Length of list : ", len_list)
print("Length of set : ", len_set)
print("Length of list is bigger than length of set : ", len_list > len_set)

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.

str = "I am a teacher and I love to inspire and teach people"
splitted_string = str.split()
unique_words = set(splitted_string)
print(splitted_string)
print(unique_words)
print("Unique words in string : ", len(unique_words))
