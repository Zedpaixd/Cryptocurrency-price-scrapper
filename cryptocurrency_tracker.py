from scrapper import *

Prices = open("Prices.txt","w+")

with open("Prices.txt","w+") as Prices:
    for i in range (0,len(PureCoinNames)):
        print("Coin name:",PureCoinNames[i],"| Coin price:",PureCoinPrices[i],"\n", file=Prices)