import yfinance as yf
import time
def get_crypto_data(ticker):
    ticker_yahoo = ticker+"-USD"
    ticker = yf.download(ticker_yahoo, period='5d')
    return ticker['Close']

file=open('crypto_currencies.txt', 'r')
ticker_list = file.read().splitlines()
while True:
    for ticker in ticker_list:
        print(ticker + " ")
        print(get_crypto_data(ticker))
    time.sleep(10)
