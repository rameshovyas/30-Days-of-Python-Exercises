# Write a function which count number of lines and number of words in a text file.
from functools import reduce
import os
def add(a,b):
    return a+b

def count_lines_words(fname):
   result = {"lines" : 0, "words" : 0} 
   # open file and check it exists or not 
   try:
       if(fname): 
        f = open(fname)
        if(f):
            lines = f.readlines()
            for line in lines:                
                line = line.strip(os.linesep)
                result["lines"] +=1
                result["words"] += len(line.split())
            # Trying the same with comprehensions
            #lines_no_newline = list([line] for line in lines if line !='\n')
            #result["lines"] = len(lines_no_newline)   
            #word_list =   ([(len(line)] for lines in lines_no_newline for line in lines)               
           # result["words"] = reduce(add,word_list)
   except Exception as e: print(e)
   finally: return result 

print(count_lines_words("ex1.data"))
