import csv
import time
import urllib.request

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

#Create a CSV where each line contains Product Description and URL
#Read in CSV, running a loop for each line
#Where it finds a matchin description in the current database it appends the latest data
#Where it is not found it creates a new entry


priceLog = pd.DataFrame(columns=['Product','Website','Prices'])
# First entry
url = 'https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Home-&-Outdoor/Garden-&-Patio/Growing-Fertilisers/Plant-Foods/EFEKTO-SEAGRO-1L/p/000000000000262286_EA'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
capturedPrice = soup.findAll('div',class_="normalPrice")[0].text
capturedPrice = capturedPrice.strip('0')
capturedPrice = capturedPrice.strip()

print(capturedPrice)

priceLog = priceLog.append({'Product':'Seagro 1L','Website':'PicknPay','Prices':capturedPrice}, ignore_index=True)

# second entry
url = 'https://www.builders.co.za/Garden-%26-Outdoor-Living/Garden/Fertilizers-%26-Plant-Food/All-Purpose-Plant-Food/Seagro-B2051-Fish-Emulsion-%281L%29/p/000000000000036845'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
capturedPrice = soup.findAll('div',class_="price")[0].text
#capturedPrice = capturedPrice.strip('0')
capturedPrice = capturedPrice.strip()

print(capturedPrice)

priceLog = priceLog.append({'Product':'Seagro 1L','Website':'Builders','Prices':capturedPrice}, ignore_index=True)

# Third entry
url = 'https://www.builders.co.za/Garden-%26-Outdoor-Living/Garden/Fertilizers-%26-Plant-Food/All-Purpose-Plant-Food/Seagro-B2051-Fish-Emulsion-(5L)/p/000000000000044837?gclid=CjwKCAjwusrtBRBmEiwAGBPgE-LRetDedHWlwo2fewi5sEsXBwXep8IBm85o9r2L_47C5WpgDJr4nxoCcjUQAvD_BwE'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
capturedPrice = soup.findAll('div',class_="price")[0].text
#capturedPrice = capturedPrice.strip('0')
capturedPrice = capturedPrice.strip()


priceLog = priceLog.append({'Product':'Seagro 5L','Website':'Builders','Prices':capturedPrice}, ignore_index=True)

# Fourth entry
url = 'https://www.bonsaitree.co.za/products/bonsaiboost-organic-bonsai-fertilizer?_pos=2&_sid=25dc18131&_ss=r&variant=5108685955'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
capturedPrice = soup.findAll('span',class_="current_price")[0].text


priceLog = priceLog.append({'Product':'BonsaiBoost 240x','Website':'BonsaiTree','Prices':capturedPrice[1:5]}, ignore_index=True)
print(priceLog)
# Adding a comment