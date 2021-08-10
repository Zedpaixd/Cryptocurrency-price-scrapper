from bs4 import BeautifulSoup
import requests

amount = int(input("How many different coins would you want to be displayed? "))

Website1 = "https://cryptoprices.com/"
Website2 = "?coins="

# 1 = 1-100  2 = 101-200 ... max 59
# Website3 is meant to be used to go through each page
# kinda WIP but very low on the "to finish" list

res = requests.get(Website1)
res1 = res.text
WebsiteData = BeautifulSoup(res1,'lxml')

CoinName = WebsiteData.find_all('div',class_="coin-name")
__CoinPrice__ = WebsiteData.find_all('tr')
CoinPrice=__CoinPrice__[2].find_all('span')

Prices = []

for i in range (0,amount):
    CoinPrice=__CoinPrice__[i+1].find_all('span')
    Prices.append(CoinPrice[1])

PureCoinPrices = []
PureCoinNames = []

for i in range (0,amount):
    a = list(Prices[i])
    PureCoinPrices.append(a[0])
    b = list(CoinName[i])
    PureCoinNames.append(b[0])
