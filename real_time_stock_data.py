"""
January 2nd 2023

@author: David Wang
"""
import bs4
import requests
from bs4 import BeautifulSoup


def parsePrice():
    """"
    use requests library to download webpage
    parse the data using beautifulsoup library
    find and return price data
    """
    r = requests.get('https://finance.yahoo.com/quote/TSLA?p=TSLA')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find('div',{'class':'D(ib) Mend(20px)'}).find('fin-streamer').text
    return price

while True:
    # call the parsePrice function to update the price in real time
    print('The current price is '+str(parsePrice()))

