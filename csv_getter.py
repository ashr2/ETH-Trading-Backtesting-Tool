#Tool to help get .csv file for ETH-USD data that we can use for backtesting
import pandas as pd
import csv
from binance.client import Client
api_key = "Qe9Im0C47NqNaU52Bs4hQsTrWoryROEU2L40T2YaxrUAPXr5A5tgySSUmmPm9gYY" #CREATE NEW API KEY IN THE FUTURE
secret_key = "rhMQ8mTcte4G7axxT9SIeWiD1qAF8pudE7MCCogBTgcFPgMjAePJwm3isjg0fxDg" #VERY IMPORTANT
print("Data ")
client = Client(api_key, secret_key, tld='us')
with open('data', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Price", "Delay"])
    for kline in client.get_historical_klines_generator("ETHUSDT", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC"):
        writer.writerow([kline[0], kline[4], float(kline[2]) - float(kline[3])])