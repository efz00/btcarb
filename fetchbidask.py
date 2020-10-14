#fetch lowest bid and highest ask between bybit and bitmex 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import ccxt
import time
import datetime
import os
#initialize exchanges and load markets
exchange = ccxt.bitmex() 
exchange2 = ccxt.bybit()
markets = exchange.load_markets()
markets2 = exchange2.load_markets()
#find percent difference for every 5 seconds

#dictionary of exchanges
exchangedict = {}
while True:
    now = datetime.datetime.now()
    bitmex_fetch = exchange.fetch_ticker('BTC/USD')
    bybit_fetch = exchange2.fetch_ticker('BTC/USD')
    #scrape ticker fetch and add to lists
    exchangedict.update({'bitmex':(bitmex_fetch['bid'], bitmex_fetch['ask']),'bybit':(bybit_fetch['bid'], bybit_fetch['ask'])})

    #results
    print('=======================')
    print(now)
    print(exchangedict)
    print('=======================')

    #send results to plot file
    current_time = now.strftime("%H:%M:%S")
    send_data = open('plot.txt', 'a')
    send_data.write(str(current_time) + ',')
    send_data.write(str(exchangedict))
    send_data.write('\n')


    send_data.close()


  
    time.sleep(5)



