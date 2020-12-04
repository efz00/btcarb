#fetch lowest bid and highest ask between phemex and bitmex 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import ccxt
import time
import datetime
import os

test_mode = True 
#initialize exchanges
exchange = ccxt.bitmex()
exchange2 = ccxt.phemex()
#Depending on test mode, configures exchanges and  api keys
if test_mode == True:
    exchange2.set_sandbox_mode(True)
    if 'test' in exchange.urls:
        exchange.urls['api'] = exchange.urls['test']
    exchange.apiKey = 'lvSX7y8egJqSVz68fl2sQMSH'
    exchange.secret = 'MaK-UKQNEFBUz2mZEsbI8gPIi2dqYCcuqpWqpP-VJlj3rjqK'
    exchange2.apiKey = '70dc8e4d-ef5f-49b0-8d14-c58d65203d97'
    exchange2.secret = 'cIupY1__5mgXg01MTbLVASlp5vZHu7No_sxnu1RqBBNjYTViYTg4Yi1lYzg2LTQ0NjctOGY5MS0yOGZjNDJkZDMwYTY'
else:
    exchange.apiKey = 'WAX0woPHSd5XdsqpM361HqaB'
    exchange.secret = 'loDFqktFVo826ErMF8Dc5ioZYitevlYbuSdiBzBn91LJJTSH'
    exchange2.apiKey = 'd51e6c97-d3a6-41ee-82b3-224e3d439073'
    exchange2.secret = 'ZjEvIv1pGuYaDS1zOr1tj0ths0ESOE86p1rSiHDMpWFiNmE0MDk2My0zMzA5LTRmZTgtYTM4ZS1lNjY4ZTI3Zjc5ZGI'
#load markets
markets = exchange.load_markets()
markets2 = exchange2.load_markets()

#Log time, %difference, phemex bid, bitmex ask to csv
def logCSV(now, difference, updated_price):
    current_time = now.strftime("%H:%M:%S")
    send_data = open('plot.csv', 'a')
    send_data.write(str(current_time) + ',')
    send_data.write(str(difference) + ',')
    send_data.write(str(updated_price[0][0]) + ',')
    send_data.write(str(updated_price[1][1]))
    send_data.write('\n')
    send_data.close()

#Log time, %difference, phemex bid, bitmex ask to terminal
def logTerminal(now, difference, updated_price):
    print('=======================')
    print(now)
    print(difference)
    print(str(updated_price[0][0]) + ' ' + str(updated_price[1][1]))
    print('=======================')

def updatePrices():
    #request tickers
    bitmex_fetch = exchange.fetch_ticker('ETH/USD')
    phemex_fetch = exchange2.fetch_ticker('ETH/USD')
    #tickers to lists
    bitmex_price = [bitmex_fetch['bid'], bitmex_fetch['ask']]
    phemex_price = [phemex_fetch['bid'], phemex_fetch['ask']]
    return [phemex_price, bitmex_price]

#find percent difference between bitmex bid and phemex ask for every 5 seconds
def findPercentDifference(a , b):
    result = (b - a)/((a+b)/2)
    return result*100



exit_mode = False
while True:
    now = datetime.datetime.now()
    updated_price = updatePrices()
    difference = findPercentDifference(updated_price[0][0],updated_price[1][1])
    logCSV(now, difference, updated_price)
    logTerminal(now, difference, updated_price)

#TRADING LOGIC
    if exit_mode == False:
        exchange2.create_order(symbol = 'ETH/USD', type = 'StopLimit', side = 'buy', amount = 1, params = {
            'ordType': 'StopLimit',
            'pegPriceType': 'TrailingStopPeg',
            'pegOffsetValueEp': 0.5,
            'triggerType': 'ByLastPrice'
                        })
        exchange.create_order(symbol = 'ETH/USD', type = 'StopLimit', side = 'sell', amount = 1, params = {
            'ordType': 'StopLimit',
            'pegPriceType': 'TrailingStopPeg',
            'pegOffsetValue': .05 # distance in USD
            })
        exit_mode = True
    if exchange2.fetch_open_orders('ETH/USD') == True and exchange.fetch_open_orders('ETH/USD') == True and exit_mode == True:
        exchange2.create_order(symbol = 'ETH/USD', type = 'StopLimit', side = 'sell', amount = 1, params = {
        'ordType': 'StopLimit',
        'pegPriceType': 'TrailingStopPeg',
        'pegOffsetValueEp': .05 # distance in USD
        })
        exchange.create_order(symbol = 'ETH/USD', type = 'StopLimit', side = 'buy', amount = 1, params = {
        'ordType': 'StopLimit',
        'pegPriceType': 'TrailingStopPeg',
        'pegOffsetValue': -.05 # distance in USD
        })
        exit_mode = False



    


  
    time.sleep(5)




