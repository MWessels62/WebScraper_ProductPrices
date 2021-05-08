import csv
import time
import urllib.request
import pandas as pd
import requests
from bs4 import BeautifulSoup
from extract import json_extract
import os 

# * User must first create a CSV where each line contains Product Description and URL
# * Read in CSV line by line
# * Get updated pricing iformation
# * Where it finds a matching description in the current database it appends the latest data
# * Where it is not found it creates a new entry
 


#read in text file into a data frame using pandas
recordedPrices = pd.read_csv('LatestPrices.csv', sep=",") 

# ! Delete. doesnt seem to be used anywhere
priceLog = pd.DataFrame(columns=['UUID','Product','Website','Prices'])

webScraperInput = pd.read_csv('WebScraper_Input.csv', sep=",")



# This will iterate through each line in the webScraperInput file
# It will fetch the latest price and then update the recordedPrices.csv file if the price is different
#iterator = 0

for ind in webScraperInput.index: 
    UUID = webScraperInput["UUID"][ind]
    url = webScraperInput["URL"][ind]
    url = url.strip("'")

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    capturedPrice = soup.find(webScraperInput["Container"][ind].strip("'"),{"class" : webScraperInput["TagToSearch"][ind].strip("'")})#.text
    capturedPrice = capturedPrice.text
    capturedPrice = capturedPrice.replace("ZAR","")
    capturedPrice = capturedPrice.strip()
    # ! find way of removing excess zeros at end of number

    s = pd.Series(recordedPrices['UUID'])


    if UUID in s.values:
        lineIndex = recordedPrices[recordedPrices['UUID']==UUID].index.values
        recordedPrices.loc[lineIndex,"Prices"] = capturedPrice
    else:
        recordedPrices = recordedPrices.append({'UUID':UUID,'Product': webScraperInput['Product Description'][ind],'Website': webScraperInput['Store'][ind],'Prices': capturedPrice}, ignore_index=True) 
print("RECORDED PRICES: ")
print(recordedPrices)
os.remove('LatestPrices.csv')
recordedPrices.to_csv(r'LatestPrices.csv',index=False, header=True)