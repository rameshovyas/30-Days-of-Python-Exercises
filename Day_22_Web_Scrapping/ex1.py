# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
try:
    print("Fetching data from %s" % (url))
    print("Please wait.......")
    print()
    response = requests.get(url)
    if(response.status_code == 200):
        
        data = {} # Dictionary to store scrapped data
        content = response.content 
        soup = BeautifulSoup(content, 'html.parser')     
        
        data["title"] = soup.title.get_text()

        data["facts-stats"] = {}
        facts=[]
        values=[]
        # Get all h4 text
        for key in soup.find('section', {'class' : 'facts-stats'}).find_all('h4'):
            facts.append(key.get_text())
        # Get all h2 text    
        for value in soup.find('section', {'class' : 'facts-stats'}).find_all('h2'):
            values.append(value.get_text())
        # Facts stats    
        data["facts-stats"] = dict(zip(facts,values))

        # Facts categories
        data['facts-categories'] = {}
        categories = []
        
        for cat in soup.find('section', {'class' : 'facts-categories'}).find_all('div', {'class' : 'facts-wrapper'}):
            #categories.append(cat.find('h5').get_text())
          
            facts_key=[]
            facts_value=[]
            
            # Getting all fact text of  
            for key in cat.find_all('p', {'class' : 'text'}):                
                facts_key.append(key.get_text())
           

            # Getting all fact values
            for key in cat.find_all('span', {'class' : 'value'}):
                facts_value.append(key.get_text())    
           

            # Finally append the fact value with  categories    
            data['facts-categories'][cat.find('h5').get_text()] = dict(zip(facts_key,facts_value))



        
        #print(data)

        # Save the scrapped data to json file
        with open('scrapped.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Created scarpped.json with the data")    
    else:
        print("Something panic, status : ", response.status_code)
except Exception as e:
    print(e)