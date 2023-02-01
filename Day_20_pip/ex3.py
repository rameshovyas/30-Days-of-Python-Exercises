from bs4 import BeautifulSoup
import requests

print("Reading data, please wait.....")
url = "https://archive.ics.uci.edu/ml/datasets.php"

response = requests.get(url).text
soup = BeautifulSoup(response,"html.parser")

# Creating list with all tables
tables = soup.find_all('table')

#  Looking for the table with the cellpadding = 5
table = soup.find('table', cellpadding=5)

columns = table.find_all('tr') 
print(columns)