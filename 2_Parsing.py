from bs4 import BeautifulSoup as bs
import os
import sys
import requests
import html5lib
from urllib.request import urlopen
import pandas as pd
import datetime

now = datetime.datetime.now()
pathlocal = os.getcwd()
# print pathlocal

pathhtml = os.path.abspath(os.getcwd())
pathhtml = pathhtml.replace("\\", "/")
pathfile = 'file:///' + pathhtml + "/"
# print pathfile
#<li class="priceGroupContainer price_group services" pricegroupindex="9">

Page = urlopen(pathfile + "Output.html", timeout=1.5)
soup = bs(Page, 'html5lib')
g_data_valor = soup.find_all('td', {'class': 'taxValueTotal'})
g_data_cia = soup.find_all('p', {'class': 'field-item cia-name'})
g_bloco = soup.find_all('li', {'class': 'priceGroupContainer price_group services'})


df = pd.DataFrame({'Price': [], 'Company': [], 'Date': []})


for li in g_bloco:
    #print li
    g_data_valor = li.find_all('td', {'class': 'taxValueTotal'})
    g_data_cia = li.find_all('p', {'class': 'field-item cia-name'})
    #print (g_data_valor[0].text)
    #print (g_data_cia[0].text)
    df = df.append({'Price': g_data_valor[0].text, 'Company':g_data_cia[0].text, 'Date': now.strftime("%Y-%m-%d")}, ignore_index=True)

df.drop_duplicates(subset=['Company','Price','Date'], keep="last").reset_index(drop=True)
df.to_csv('Prices.csv', header=False, mode = 'a')







#print g_data_valor[0].text
