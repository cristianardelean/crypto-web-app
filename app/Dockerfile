FROM python:3.6
ADD crypto_app.py crypto_currencies.txt static_images/
RUN pip install yfinance streamlit
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

# exposing default port for streamlit
EXPOSE 8051
COPY . .
CMD [ "streamlit", "run",  "crypto_app.py"]
