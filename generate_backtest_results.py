#Tool that generates csv for results on backtesting algorithm
import csv
from csv_getter import *
def algo1(curr_price, eth_held, usd_held, init_money):
    if(eth_held*curr_price > init_money):
        delta = eth_held*curr_price - init_money
        usd_held += delta
        eth_held -= delta/curr_price
    return([eth_held, usd_held, (usd_held) - (init_money-eth_held*curr_price)])

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov"]
y = "2022"
with open("eth_usd_data/algo1_profits", 'w', newline='') as file_writing:
    writer = csv.writer(file_writing)
    writer.writerow(["Date", "Profits"])
    for m in months:
        for date in range(1,20):
            start = str(date)
            end = str(date)
            file_exists = False
            try:
                open("eth_usd_data/"+start+"_"+end+m+"2022", newline='')
                file_exists = True
            except:
                file_exists = False
            if(not(file_exists)):
                print(get_data(start, end, m, y))
            else:
                print(m + start + " exists")
#     for i in range(1,20):
#         start = str(i)
#         end = str(i)
#         try:
#             print(get_data(start, end, m, y))
#         except Exception as e:
#             print(e)
#         profit = 0
#         init_money = 1000.0
#         usd_held = 0 #Liquid USD that user holds
#         delta = 0
#         eth_held = 0#init_money/float(resp.json()[499]['price'])
#         with open("eth_usd_data/"+start+"_"+end+m+y, newline='') as file:
#             csvFile = csv.reader(file)
#             i = 0
#             print(csvFile.__next__())
#             eth_held = init_money/float((csvFile.__next__())[1])
#             for line in csvFile:
#                 curr_price = float(line[1])
#                 result = algo1(curr_price, eth_held, usd_held, init_money)
#                 eth_held = result[0]
#                 usd_held = result[1]
#             writer.writerow([start, (curr_price*eth_held + usd_held) - init_money])
            