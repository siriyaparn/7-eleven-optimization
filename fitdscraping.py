import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

l = []

page = requests.get("https://fit-d.com/food/shop/OQ,,/7-eleven")
soup = BeautifulSoup(page.content, 'html.parser')

#select Div
div = soup.select_one("div.image_wrapper")

#get inner div 
inner = div.findChildren()

#print inner div
for el in inner:
    print(el)
    print("###")


for data in soup.find_all('div', class_='image_wrapper'):
    for a in data.find_all('a'):
        print(a.get('href')) #for getting link
        print(a.text) #for getting text between the link
        
        l.append(a.get('href'))
        print(l)
        