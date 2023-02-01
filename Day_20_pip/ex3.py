from bs4 import BeautifulSoup
import requests

print("Reading data, please wait.....")
url = "https://archive.ics.uci.edu/ml/datasets.php"

response = requests.get(url).text
soup = BeautifulSoup(response,"html.parser")
print(soup)
