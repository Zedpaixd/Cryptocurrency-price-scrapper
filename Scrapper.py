from bs4 import BeautifulSoup
import requests
from Cryptocurrency_tracker import amount

Website = "https://cryptoprices.com/"
res = requests.get(Website)
res1 = res.text
WebsiteData = BeautifulSoup(res1,'lxml')

CoinName = WebsiteData.find_all('div',class_="coin-name")
__CoinPrice__ = WebsiteData.find_all('tr')
CoinPrice=__CoinPrice__[2].find_all('span')

Prices = []

for i in range (0,int(amount)):
    CoinPrice=__CoinPrice__[i+1].find_all('span')
    Prices.append(CoinPrice[1])
   
#CoinName[] , CoinPrice[]
