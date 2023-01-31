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
        
        # min, max, median ... of cats' weight in metric
        weight = []
        for cat in cats_data:
          if("weight" in cat):
            if("metric" in cat["weight"]):
                low,hi = cat["weight"]['metric'].split("-")
                weight.append((int(low) + int(hi))/2) 
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
        
    else:
        print("Error loading data : Response %s" % (response.status_code))    
except :
    print("Something went wrong....")
