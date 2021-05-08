import csv
import time
import urllib.request

#import numpy
import pandas as pd
import requests
from bs4 import BeautifulSoup
from extract import json_extract

# * User must first create a CSV where each line contains Product Description and URL
# * Read in CSV line by line
# * Get updated pricing iformation
# * Where it finds a matching description in the current database it appends the latest data
# * Where it is not found it creates a new entry
 


#read in text file into a data frame using pandas
recordedPrices = pd.read_csv('LatestPrices.csv', sep=",", index_col="UUID")
print(recordedPrices)

# ! Delete. doesnt seem to be used anywhere
priceLog = pd.DataFrame(columns=['UUID','Product','Website','Prices'])

webScraperInput = pd.read_csv('WebScraper_Input.csv', sep=",")
print("Web scraper input")
print(webScraperInput)

# This will iterate through each line in the webScraperInput file
# It will fetch the latest price and then update the recordedPrices.csv file if the price is different
#iterator = 0

for ind in webScraperInput.index: 
    #print("Line is: " + line)
    #print("ind is:")
    #print(ind)
    UUID = webScraperInput["UUID"][ind]
    print("UUID is: " + UUID)
    #iterator += 1
    url = webScraperInput["URL"][ind]
    url = url.strip("'")
    #url = "'" + url + "'"
    #print("URL is: " + url)

    response = requests.get(url)
    #print("REPONSE IS: ")
    #print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    #print ("soup equals")
    #print(soup)
    capturedPrice = soup.find(webScraperInput["Container"][ind].strip("'"),{"class" : webScraperInput["TagToSearch"][ind].strip("'")})#.text
    #capturedPrice = soup.find(webScraperInput["Container"][ind],class_="%s" % (webScraperInput["TagToSearch"][ind]))#.text
    print(capturedPrice)
    capturedPrice = capturedPrice.text
# g4f5g,Baby Formula,Novalac,AR Digest,Takealot,https://www.takealot.com/novalac-ar-digest-800g/PLID34154854,'span',currency plus currency-module_currency_29IIm
    #capturedPrice = soup.findAll(webScraperInput["Container"][ind],class_="%s" % (webScraperInput["TagToSearch"][ind]))[0].text
    capturedPrice = capturedPrice.strip('0')
    capturedPrice = capturedPrice.strip()
    
    s = pd.Series(recordedPrices.index)
    print("UUID list: " )
    print(s)
    if UUID in s.values:
        #print(recordedPrices.loc[UUID,"Prices"])
        recordedPrices.loc[UUID,"Prices"] = capturedPrice
        print("UUID = " + UUID)
        print(recordedPrices.loc[UUID,"Prices"])
        print("UUID in s.values is WORKING!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        #recordedPrices.append({'Product': line['Product Description'],'Website':line.Store,'Prices':capturedPrice}, ignore_index=True) 
        print("APPENDING ATTEMPTED.......")
        recordedPrices = recordedPrices.append({'UUID':UUID,'Product': webScraperInput['Product Description'][ind],'Website': webScraperInput['Store'][ind],'Prices': capturedPrice}, ignore_index=True) 
    print("RECORDED PRICES IS .........................")
    print(recordedPrices)

#Product Category;Product Description;Product Variant;Store;URL;TagToSearch
    

## First entry
#url = 'https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Home-&-Outdoor/Garden-&-Patio/Growing-Fertilisers/Plant-Foods/EFEKTO-SEAGRO-1L/p/000000000000262286_EA'
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#capturedPrice = soup.findAll('div',class_="normalPrice")[0].text
#capturedPrice = capturedPrice.strip('0')
#capturedPrice = capturedPrice.strip()

#priceLog = priceLog.append({'Product':'Seagro 1L','Website':'PicknPay','Prices':capturedPrice}, ignore_index=True)
##if captured price is different to price field in text file (from same line number as iterator) then change price value in text file

## second entry
#url = 'https://www.builders.co.za/Garden-%26-Outdoor-Living/Garden/Fertilizers-%26-Plant-Food/All-Purpose-Plant-Food/Seagro-B2051-Fish-Emulsion-%281L%29/p/000000000000036845'
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#capturedPrice = soup.findAll('div',class_="price")[0].text
##capturedPrice = capturedPrice.strip('0')
#capturedPrice = capturedPrice.strip()

#priceLog = priceLog.append({'Product':'Seagro 1L','Website':'Builders','Prices':capturedPrice}, ignore_index=True)

## Third entry
#url = 'https://www.builders.co.za/Garden-%26-Outdoor-Living/Garden/Fertilizers-%26-Plant-Food/All-Purpose-Plant-Food/Seagro-B2051-Fish-Emulsion-(5L)/p/000000000000044837?gclid=CjwKCAjwusrtBRBmEiwAGBPgE-LRetDedHWlwo2fewi5sEsXBwXep8IBm85o9r2L_47C5WpgDJr4nxoCcjUQAvD_BwE'
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#capturedPrice = soup.findAll('div',class_="price")[0].text
##capturedPrice = capturedPrice.strip('0')
#capturedPrice = capturedPrice.strip()


#priceLog = priceLog.append({'Product':'Seagro 5L','Website':'Builders','Prices':capturedPrice}, ignore_index=True)



## Fourth entry
#url = 'https://www.bonsaitree.co.za/products/bonsaiboost-organic-bonsai-fertilizer?_pos=2&_sid=25dc18131&_ss=r&variant=5108685955'
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#capturedPrice = soup.findAll('span',class_="current_price")[0].text


#priceLog = priceLog.append({'Product':'BonsaiBoost 240x','Website':'BonsaiTree','Prices':capturedPrice[1:5]}, ignore_index=True)
#print(priceLog)

#priceLog.to_csv(r'LatestPrices.txt', header=['Product','Website','Prices'], index=None, sep=',', mode='w')
