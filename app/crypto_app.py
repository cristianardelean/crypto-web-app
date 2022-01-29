
import yfinance as yf  # Yahoo finance to get stock data
import streamlit as st  # Streamlit to create the webapp
from PIL import Image  # Import Pillow to add icons
from urllib.request import urlopen  # To add URLS
st.write("""
# Cryptocurrency Monitoring
""")
tickers =[]
file=open('crypto_currencies.txt', 'r')
ticker_list = file.read().splitlines()

for ticker in ticker_list:
  tickers.append(ticker)
selectBox_key=0
inputText_key=0

option = st.selectbox(
         'Select Crypto Currency',
         (tickers), key = selectBox_key)
period= st.text_input('Please tell me for what period you want to see market data (example: 1d, 1mo, 1y)', '', key=inputText_key)
if (period == '[0-9]m')
if (option):
        data=yf.Ticker(option)
        data_ticker=data.history(period=period)
        title= " """" ##  """ + option + " """ """"""
        st.write(title)
        imagePath = "static_images/"+option+".png"
        image = Image.open(imagePath)
        st.image(image, use_column_width=False)
        st.line_chart(data_ticker.Close, use_container_width=True)
        st.line_chart(data_ticker.Open, use_container_width=True)
        st.line_chart(data_ticker.High, use_container_width=True)
        st.line_chart(data_ticker.Low, use_container_width=True)
        st.line_chart(data_ticker.Volume, use_container_width=True)
selectBox_key=0
inputText_key=0