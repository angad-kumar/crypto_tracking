import requests
from datetime import datetime
import time

coin_data = ['shibinr', 'paxginr', 'zecinr', 'dcrinr','balinr','zrxinr','umainr','hntinr','dashinr','busdinr','batinr','usdtinr','ftminr','btcinr','lunainr','maticinr','adainr','xrpinr','ethinr','dogeinr','dockinr','atominr','wininr']
URL = "https://api.wazirx.com/api/v2/tickers"

def price():
    try:
        response = requests.get(URL.format()).json()
        return response
    except:
        return False

for i in range(0,23):
    d = price()
    coin = coin_data[i]
    high_price = float(d[coin]['high'])
    low_price = float(d[coin]['low'])
    current_price = float(d[coin]['last'])
    open_price = float(d[coin]['open'])
    average_price = (high_price - low_price)/2
    if current_price < low_price:
        print('Sell:', coin)
    else:
        profit = int(((high_price * 100)/current_price) - 100)
        print('Buy:', coin ,",", "Expected profit:" ,profit,"%")


# while True:
#     d = price()
#     current_price = float(d[coin]['last'])
#     high_price = float(d[coin]['high'])
#     low_price = float(d[coin]['low'])
#     open_price = float(d[coin]['open'])
#     average_price = (high_price - low_price)/2
#     if current_price > average_price:
#         print(high_price)
#         print(low_price)
#         print(current_price)
#         print('sell')
#     else:
#         print('buy')
#     # print(open_price)
#     time.sleep(1)

