import pandas as pd
import requests
from bs4 import BeautifulSoup

productName = []
productPrice = []
description = []
reviews = []

for i in range(1,11):
    url = "https://www.flipkart.com/search?q=washing+machines+under+20000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")
    area = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    #FOR PRODUCT NAMES
    names = area.find_all("div", class_="_4rR01T")

    for i in names:
        txt = i.text
        productName.append(txt)


    #FOR PRICES OF THE PRODUCTS
    prices = area.find_all("div", class_="_30jeq3 _1_WHN1")

    for i in prices:
        txt = i.text
        productPrice.append(txt)


    #FOR DESCRIPTION OF THE PRODUCTS
    des = area.find_all("ul", class_="_1xgFaf")

    for i in des:
        txt = i.text
        description.append(txt)

    #FOR RATINGS OF THE PRODUCT
    ratings = area.find_all("div", class_="_3LWZlK")

    for i in ratings:
        txt = i.text
        reviews.append(float(txt))

    while(len(reviews)%24!=0):
        a = sum(reviews)/len(reviews)
        reviews.append(a)


df = pd.DataFrame({"Product Name":productName, "Price":productPrice, "Description":description, "Ratings":reviews})
df.to_csv("Washing Machines Under 20,000.csv")
