# Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
import requests

url = 'http://www.gutenberg.org/files/1112/1112.txt'
print("Getting data from : %s" % (url))
print("Please wait........")
response = requests.get(url)
if(response.status_code == 200):
    
   lines = response.iter_lines()
   words = []
   for line in lines:
        for word in line.decode().split():
          words.append(word)    
        
   unqiue_words= set()
   unqiue_words= words
   
   # Create a dictionary with frequency of each word
   word_frequency = {}
   for word in unqiue_words:
       word_frequency[word] = words.count(word)
            

   # Now sort the dictionary on frequency (descending), which will give us a list of keys
   sorted_by_frq= sorted(word_frequency.items(), key = lambda x: x[1], reverse=True)
   # Now slice the first 10 from the sorted list
   most_common_words =sorted_by_frq[:10]
   print("Most common words")
   print("--------------")
   print(most_common_words)
else:
    print("Something panic happended, system return : %s" % response.status_code)    