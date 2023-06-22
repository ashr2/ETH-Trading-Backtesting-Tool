# ETH-Trading-Backtesting-Tool

## Key Usage
You need your own Binance API Key to run this application. 
To do this go to https://www.binance.us/ and create an account and generate a secret key and an api key.
Go to csv_getter.py and replace the strings on lines 4 and 5 with your api key and your secret key.

## Algorithm Implementation
If you'd like to see how your own algorithm would perform , implement algo1 with your own algorithm that takes in the following parameters
1. The current price
2. Amount of ethereum you hold in your account
3. Amount of USD you hold in your account
4. The initial amount of money you started with
 
and return data in the format of a list which contains the following elements in order

1. Ethereum held
2. USD held
3. Profit/loss after trading algorithm is run

## Seeing Live Test Results
After you have implemented algo1 (or using the default algorithm), you can run live_test.py from your directory and the results should be displayed in your command window.

## Seeing Past Data Backtesting Results
You can run generate_backtest_results.py from your directory to generate a csv file containing 2022 data and the results of your algorithm being tested in this time period.
