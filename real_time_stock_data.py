"""
January 3nd 2023
@author: David Wang

extract the prices of desired stocks in real time 
and save the price data labeled with date/time information 
to a csv file that can be processed later

"""
import bs4
import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup

def real_time_price(ticker):
    '''
    use requests library to download webpage
    parse data using beautiful soup library
    find and return price data
    '''
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'} # allows client and server to pass additional information
    url = ('https://finance.yahoo.com/quote/') + ticker + ('?p=') + ticker + ('&.tsrc=fin-srch')
    r = requests.get(url, headers = header)

    price_data = bs4.BeautifulSoup(r.text, "lxml") # create price_data object
    price_data = price_data.find('div', {'class' : 'D(ib) Mend(20px)'}) # locate class containing price data
    price_data = price_data.find('fin-streamer').text 

    return price_data

# list of stock tickers to track
tickers = ['AMZN', 'GOOG', 'TSLA', 'META']

# take 100 seperate samples of each stock's price and the time data was taken
# and save data to csv file 
for step in range(1,101):
    price = []
    col = []
    time_stamp = datetime.datetime.now() # get current date and time
    time_stamp = time_stamp.strftime("%Y-%m-%d, %H:%M:%S:") # format into string using strftime() method

    # go through each stock ticker
    for ticker in tickers:
        price.append(real_time_price(ticker))

    # add date/time information and price data to col list
    col = [time_stamp] 
    col.extend(price)

    # create dataframe and save data to csv file
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('real_time_stock_data.csv', mode = 'a', header = False)

    print(col)

