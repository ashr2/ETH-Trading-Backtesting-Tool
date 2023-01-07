import csv

for i in range(1,20):
    try:
        open("eth_usd_data/"+str(i)+"_"+str(i)+"Dec2022", newline='')
        print(str(i) + " Opened")
    except:
        print(str(i) + " doesn't exist")