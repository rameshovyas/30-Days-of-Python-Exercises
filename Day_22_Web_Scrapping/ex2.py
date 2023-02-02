import requests
from bs4 import BeautifulSoup
import json
url = 'https://archive.ics.uci.edu/ml/datasets.php'
print("Getting Data from %s" % (url))
response = requests.get(url)
content = response.content 
soup = BeautifulSoup(content, 'html.parser') 

# Targeting the table with cellpadding attribute with the value of 3
tables = soup.find_all('table', {'cellpadding':'3'})

table = tables[0] # the result is a list, we are taking out data from it
data = {}
rows = []

for tr in table.find_all('tr'):
    tmp_list = []  
    for td in tr.find_all('td'):      
      for p in td.find_all('p', {'class' : 'normal'}):
        if(p.get_text()!=""):
            tmp_list.append(p.get_text(strip=True))
    
    if(len(tmp_list)==8):
        rows.append((tmp_list))
data = rows
# Saving data in json file
fname= "uci_machine_learning.json"
with open(fname, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Created %s with the scrapped data" % (fname))     


