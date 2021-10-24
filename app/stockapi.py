import requests
from app import app

def GetStockData(symbol):
    APIKEY = app.config['API_KEY']

    FINAL_URL = f"http://api.marketstack.com/v1/intraday/latest?access_key={APIKEY}&symbols={symbol}"
    
    try:
        response = requests.request("GET", FINAL_URL).json()['data'][0]

        SYMBOL = response['symbol']
        DATE = response['date']
        TRADE_VOLUME = response['volume']
        HIGH_PRICE = response['high']
        LOW_PRICE = response['low']
        OPENING_PRICE = response['open']
        CLOSING_PRICE = response['close']
        CURRENT_PRICE = response['last']
        
        return ([DATE,SYMBOL,TRADE_VOLUME,HIGH_PRICE,LOW_PRICE,OPENING_PRICE,CLOSING_PRICE,CURRENT_PRICE])
    except:
        return None

    
