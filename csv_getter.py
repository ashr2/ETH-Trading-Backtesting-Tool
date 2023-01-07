#Tool to help get .csv file for ETH-USD data that we can use for backtesting
import csv
from binance.client import Client
api_key = "my_api_key" #Replace with actual api key
secret_key = "my_secret_api_key" #Replace with actual secret api key

def get_data(start_date, end_date, month, year):
    client = Client(api_key, secret_key, tld='us')
    with open("eth_usd_data/"+start_date+"_"+end_date+month+year, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Price", "Delay"])
        if(start_date != end_date):
            for kline in client.get_historical_klines_generator("ETHUSDT", Client.KLINE_INTERVAL_1MINUTE, start_date + " " + month + ", " + year, end_date + " " + month + ", " + year):
                writer.writerow([kline[0], kline[4], float(kline[2]) - float(kline[3])])
        else:
            for kline in client.get_historical_klines_generator("ETHUSDT", Client.KLINE_INTERVAL_1MINUTE, end_date + " " + month + ", " + year):
                writer.writerow([kline[0], kline[4], float(kline[2]) - float(kline[3])])
    return("eth_usd_data/"+start_date+"_"+end_date+month+year)

def command_interface():
    start_date = input("Start date: ")
    end_date = input("End date: ")
    month = input("First three letters of month: ")
    year = input("Year: ")
    return([start_date, end_date, month, year])
