# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
import json

def most_populated_countries(fname, limit):
    # Read the josn file first
    with open(fname,'r', encoding="utf8") as f:
        data = f.read()

    # convert the data to dictionary
    
    country_data = json.loads(data)

    country_population = {}
    for country in country_data:
       if("population" in country):
         country_population[country["name"]] = country["population"]
          
    return(sorted(country_population.items(), key = lambda x:x[1], reverse=True)[:limit])


print(most_populated_countries('countries_data.json', 3))