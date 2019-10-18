import time
import urllib.request
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup



url_NetBaby = 'https://netbaby.co.za/product/tommee-tippee-closer-nature-breast-feeding-starter-kit' 
response_NetBaby = requests.get(url_NetBaby)
soup = BeautifulSoup(response_NetBaby.text, "html.parser")
soup.findAll('span',class_="woocommerce-Price-amount amount")
capturedPrice = soup.findAll('span',class_="woocommerce-Price-amount amount")[1].text
print("Net Baby --> " + soup.findAll('span',class_="woocommerce-Price-amount amount")[1].text)

priceLog = np.array([['Websites','Prices'],['Netbaby',capturedPrice]])

#url_Loot = 'https://www.loot.co.za/product/tommee-tippee-closer-to-nature-breastfeeding-starter-ki/dkwm-3314-g410' 
#response_Loot = requests.get(url_Loot)
#print(response_Loot)
#soup = BeautifulSoup(response_Loot.text, "html.parser")
#soup.findAll('span',class_="woocommerce-Price-amount amount")
#print(soup.findAll('span'))

url_MyMomAndMe = 'https://www.mymomandme.co.za/products/tommee-tippee-closer-to-nature-breastfeeding-starter-kit' 
response_MyMomAndMe = requests.get(url_MyMomAndMe)
soup = BeautifulSoup(response_MyMomAndMe.text, "html.parser")
#soup.findAll('span',class_="product-price")
print("My Mom and Me  --> " + soup.findAll('span', itemprop="price")[0].text)

#BabyBoom
url_BabyBoom = 'https://www.babyboom.co.za/product/tommee-tippee-breastfeeding-starter-set/' 
response_BabyBoom = requests.get(url_BabyBoom)
soup = BeautifulSoup(response_BabyBoom.text, "html.parser")
#soup.findAll('span',class_="woocommerce-Price-amount amount")
print("Baby Boom --> " + soup.findAll('span',class_="woocommerce-Price-amount amount")[1].text)



#BabyShoppe
url_BabyBoom = 'https://thebabyshoppe.co.za/onlineshop/product_view.php?n=Tommee-Tippee-Breast-Feeding-Starter-Set&id=476' 
response_BabyBoom = requests.get(url_BabyBoom)
soup = BeautifulSoup(response_BabyBoom.text, "html.parser")
#soup.findAll('span',class_="woocommerce-Price-amount amount")
print("Baby Shoppe --> " + soup.findAll('span',class_="label label-danger")[0].text)


#Loot BidorBuy
url_BabyBoom = 'https://www.bidorbuy.co.za/item/396870822/Tommee_Tippee_Closer_to_Nature_Breastfeeding_Starter_Kit.html' 
response_BabyBoom = requests.get(url_BabyBoom)
soup = BeautifulSoup(response_BabyBoom.text, "html.parser")
#soup.findAll('span',class_="woocommerce-Price-amount amount")
print("Loot(BidorBuy) --> " + soup.findAll('span',class_="bigPriceText2")[0].text)


#Baby Fantasy
url_BabyBoom = 'http://babyfantasy.co.za/Tommee-Tippee-Breast-Feeding-Kit' 
response_BabyBoom = requests.get(url_BabyBoom)
soup = BeautifulSoup(response_BabyBoom.text, "html.parser")
#soup.findAll('span',class_="woocommerce-Price-amount amount")
print("Baby Fantasy --> " + soup.findAll('span',class_="price-new")[0].text)


print(priceLog)
