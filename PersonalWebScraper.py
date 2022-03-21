#Replaced parser with LXML parser to speed up process of parsing HTML




#need to install lxml parser - 'pip install lxml' 
import os
from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup

from extract import json_extract

#To-DO
#Log each new price rather than overwrite
#ensure prices cant be over-written by zero value
#notification when price changes



# * User must first create a CSV where each line contains Product Description and URL
# * Read in CSV line by line
# * Get updated pricing iformation
# * Where it finds a matching description in the current database it appends the latest data
# * Where it is not found it creates a new entry
 


#read in text file into a data frame using pandas
recordedPrices = pd.read_csv('LatestPrices.csv', sep=",") 

webScraperInput = pd.read_csv('WebScraper_Input.csv', sep=",")

# This will iterate through each line in the webScraperInput file
# It will fetch the latest price and then update the recordedPrices.csv file if the price is different

logFileAppend = pd.DataFrame()

for ind in webScraperInput.index: 
    UUID = webScraperInput["UUID"][ind]
    url = webScraperInput["URL"][ind]
    url = url.strip("'")

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    capturedPrice = soup.find(webScraperInput["Container"][ind].strip("'"),{"class" : webScraperInput["TagToSearch"][ind].strip("'")})
    capturedPrice = capturedPrice.text
    capturedPrice = capturedPrice.replace("ZAR","")
    capturedPrice = capturedPrice.strip()
    capturedPrice = capturedPrice.strip(".00") # remove cents values
    # ! find way of removing excess zeros at end of number

    # if there is already an entry for this item (matching on UUID) it will find the price field and update it, ELSE it will add a new entry
    s = pd.Series(recordedPrices['UUID'])
    if UUID in s.values:
        lineIndex = recordedPrices[recordedPrices['UUID']==UUID].index.values
        recordedPrices.loc[lineIndex,"Prices"] = capturedPrice
    else:
        recordedPrices = recordedPrices.append({'UUID':UUID,'Product': webScraperInput['Product Description'][ind],'Product Variant': webScraperInput['Product Variant'][ind],'Website': webScraperInput['Store'][ind],'Prices': capturedPrice}, ignore_index=True) 
    
    # Add pricing to log
    logFileAppend = logFileAppend.append({'Date Updated':datetime.now(), 'Product UUID':UUID,'Product': webScraperInput['Product Description'][ind],'Product Variant': webScraperInput['Product Variant'][ind],'Website': webScraperInput['Store'][ind],'Prices': capturedPrice}, ignore_index=True)     


print("RECORDED PRICES: ")
print(recordedPrices)
os.remove('LatestPrices.csv')

#Overwrite file with latest prices
recordedPrices.to_csv(r'LatestPrices.csv',index=False, header=True)


# email notifications 
# Check if the value just fetched is different than the last value in the log file (per product)
# Highlight which ones are different and by how much 
# only notify if the prices change


#Write new entries to log file
logFileAppend.to_csv(r'PriceLog.csv', mode='a', index=False, header=not os.path.exists('PriceLog.csv'))