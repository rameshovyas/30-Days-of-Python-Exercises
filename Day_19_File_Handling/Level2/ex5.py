def find_most_common_words(fname,limit):
    f = open(fname,"r")    
    lines = f.readlines()
    words = []
    for line in lines:
        for word in line.split():
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
    most_common_words =sorted_by_frq[:limit]
    return most_common_words

       


print(find_most_common_words("sample.txt", 5))