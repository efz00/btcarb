#fetch lowest bid and highest ask between bybit and bitmex 

import ccxt
#initialize exchanges and load markets
exchange = ccxt.bitmex() 
exchange2 = ccxt.bybit()
markets = exchange.load_markets()
markets2 = exchange2.load_markets()



#separate dictionaries of current bid and ask among exchanges
ask_list = {}
bid_list = {}

bitmex_fetch = exchange.fetch_ticker('BTC/USD')
bybit_fetch = exchange2.fetch_ticker('BTC/USD')
#scrape ticker fetch and add to lists
ask_list.update({'bitmex':bitmex_fetch['ask']})
ask_list.update({'bybit':bybit_fetch['ask']})
bid_list.update({'bitmex':bitmex_fetch['bid']})
bid_list.update({'bybit':bybit_fetch['bid']})

#results
highest_ask = max(ask_list, key=ask_list.get) 
lowest_bid = min(bid_list, key=bid_list.get) 

print('ask list: ' + str(ask_list), ('bid list: ' + str(bid_list)))
print('Lowest bid:' + lowest_bid, str(bid_list[lowest_bid]))
print('Highest ask:' + highest_ask, str(ask_list[highest_ask]))

