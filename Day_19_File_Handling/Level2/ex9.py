# Read the hacker news csv file and find out: a) Count the number of lines containing python or Python 
# b) Count the number lines containing JavaScript, javascript or Javascript 
# c) Count the number lines containing Java and not JavaScript

import csv
with open("hacker_news.csv", "r") as f:
    csv_reader = csv.reader(f,delimiter=",")
    python_count = 0
    js_count = 0
    java_count = 0
    for row in csv_reader:
      for sentence in row:
        if(('Python' in sentence) or ('python' in sentence)):
            python_count +=1

        if(('JavaScript' in sentence) or ('javascript' in sentence) or ('Javascript' in sentence)):
            js_count +=1
            
        if(('Java' in sentence)):
            java_count +=1
            
    

print("Lines containing Python : ", python_count)  
print("Lines containing JavaScript : ", js_count)  
print("Lines containing Java : ", java_count)  

