
import yfinance as yf  # Yahoo finance to get stock data
import streamlit as st  # Streamlit to create the webapp
from PIL import Image  # Import Pillow to add icons
from urllib.request import urlopen  # To add URLS
st.write("""
# Cryptocurrency Monitoring
""")

file=open('crypto_currencies.txt', 'r')
ticker_list = file.read().splitlines()
period= "6d"
for ticker in ticker_list:
  data=yf.Ticker(ticker)
  data_ticker=data.history(period=period)
  title= " """" ##  """ + ticker + " """ """"""
  st.write(title)
  imagePath = "static_images/"+ticker+".png"
  image = Image.open(imagePath)
  st.image(image, use_column_width=False)
  st.line_chart(data_ticker.Close, use_container_width=True)
  st.line_chart(data_ticker.Open, use_container_width=True)
  st.line_chart(data_ticker.High, use_container_width=True)
  st.line_chart(data_ticker.Low, use_container_width=True)
  st.line_chart(data_ticker.Volume, use_container_width=True)




