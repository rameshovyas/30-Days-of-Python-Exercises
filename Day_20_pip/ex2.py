# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find : 
import requests
import statistics

url = 'https://api.thecatapi.com/v1/breeds'
try:
    print()
    print("Fetching data from %s, please wait...." % (url))
    response = requests.get(url)
    if(response.status_code == 200):
        cats_data = response.json()      
        
        weight = []
        lifespan = []
        freq_table = []

        for cat in cats_data:
          # weight  
          if("weight" in cat):
            if("metric" in cat["weight"]):
                low,hi = cat["weight"]['metric'].split("-")
                weight.append((int(low) + int(hi))/2) 
          
          #lifespan      
          if("life_span" in cat):
                low,hi = cat["life_span"].split("-")
                lifespan.append((int(low) + int(hi))/2) 
                    
        # the min, max, mean, median, standard deviation of cats' weight in metric units.
        min_weight = min(weight)
        max_weight = max(weight)   
        mean = sum(weight) / len(weight)
        median = statistics.median(weight)
        std = statistics.stdev(weight)
        print()
        print("************* Statistics of Cat Weight ***************")
        print()
        print("Min : ", min_weight)
        print("Max : ", max_weight)
        print("Mean : ", mean)
        print("Median : ", median)
        print("Standard Deviation : ", std)
        print()
        print("******************************************************")
        
        # the min, max, mean, median, standard deviation of cats' lifespan in years.
        min_lf = min(lifespan)
        max_lf = max(lifespan)   
        mean_lf = sum(lifespan) / len(lifespan)
        median_lf = statistics.median(lifespan)
        std_lf = statistics.stdev(lifespan)
        print()
        print("************* Statistics of Cat Life Span ***************")
        print()
        print("Min : ", min_lf)
        print("Max : ", max_lf)
        print("Mean : ", mean_lf)
        print("Median : ", median_lf)
        print("Standard Deviation : ", std_lf)
        print()
        print("******************************************************")

        # Create a frequency table of country and breed of cats
        print("** Frequency table of country and breed of cats *******")
        print()
        countries = set((cat['origin']) for cat in cats_data)
        for country in countries:
            freq_table.append((country, len([cat['name'] for cat in cats_data if cat['origin'] == country])))
        print(freq_table)    
        print()
        print("******************************************************")
    else:
        print("Error loading data : Response %s" % (response.status_code))    
except Exception as e:
    print(e)
