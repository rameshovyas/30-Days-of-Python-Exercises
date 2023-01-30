# Read the countries_data.json data file in data directory, create a function that finds the 
# ten most spoken languages
import json

def most_spoken_languages(fname, limit):
    # Read the josn file first
    with open(fname,'r', encoding="utf8") as f:
        data = f.read()

    # convert the data to dictionary
    
    country_data = json.loads(data)
    
    languages = []
    for country in country_data:
        if("languages" in country):
            for lang in country["languages"]:
                languages.append(lang)

    # Create a set from list of all langauges used, that will give us unique langauges       
    unique_languages = set()
    unique_languages = languages
    
    # Create a dictionary with frequency of each langauge
    lang_frequency = {}
    for lang in unique_languages:
        lang_frequency[lang] = languages.count(lang)

    # Now sort the dictionary on frequency (descending), which will give us a list of keys
    sorted_by_frq= sorted(lang_frequency.items(), key = lambda x: x[1], reverse=True)
    # Now slice the first 10 from the sorted list
    most_spoken =sorted_by_frq[:limit]
    return most_spoken


print(most_spoken_languages('countries_data.json',10))