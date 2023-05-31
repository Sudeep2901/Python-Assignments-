#Fuel Rates for Petrol pump simulation Assignmets

petrol = 105.96
diesel = 92.48
cng = 92
'''  
# import module
import pandas as pd
import requests
from bs4 import BeautifulSoup

# user define function
# Scrape the data
def getdata(url):
	r = requests.get(url)
	return r.text

# link for extract html data
htmldata = getdata("https://www.goodreturns.in/petrol-price.html")
soup = BeautifulSoup(htmldata, 'html.parser')
result = soup.find_all("div", class_="gold_silver_table")
print(result)

# Declare string var
# Declare list
mydatastr = ''
result = []

# searching all tr in the html data
# storing as a string
for table in soup.find_all('tr'):
	mydatastr += table.get_text()

# set according to your required
mydatastr = mydatastr[1:]
itemlist = mydatastr.split("\n\n")

for item in itemlist[:-5]:
	result.append(item.split("\n"))

'''
