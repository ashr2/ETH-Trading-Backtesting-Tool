import requests
import time
resp = requests.get('https://api.binance.us/api/v3/trades?symbol=ETHUSD')

init_money = 1000
usd_held = 0 #Liquid USD that user holds
delta = 0
eth_held = init_money/float(resp.json()[499]['price'])
print("ETH Held: " + str(eth_held))
rateLimitNotExceeded = True

def algo1(curr_price, eth_held, usd_held, init_money):
    if(eth_held*curr_price > init_money):
        delta = eth_held*curr_price - init_money
        usd_held += delta
        eth_held -= delta/curr_price
    return([eth_held, usd_held, (usd_held) - (init_money-eth_held*curr_price)])

while(rateLimitNotExceeded and eth_held > 0):
    try:
        resp = requests.get('https://api.binance.us/api/v3/trades?symbol=ETHUSD')
        curr_price = float(resp.json()[499]['price'])
        result = algo1(curr_price, eth_held, usd_held, init_money)
        eth_held = result[0]
        usd_held = result[1]
        print("ETH Held in USD: " + str(eth_held*curr_price) + " Profit: " + str(result[2]))
        time.sleep(2)
    except Exception as e:
        print(e)
        rateLimitNotExceeded = False