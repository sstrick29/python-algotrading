import os.path
import pandas as pd
import numpy as np
import datetime
from datetime import datetime
import requests


# Bittrex REST API
# GET = https://api.bittrex.com/v3
bittrex_rest = 'https://api.bittrex.com/v3'
# GET /markets => https://api.bittrex.com/v3/markets
def bittrex_markets():
    t = eval(requests.get(bittrex_rest + '/markets').text)
    df = pd.DataFrame(t)
    df = df[df['status'] == 'ONLINE']
    df = df[df.astype(str)['prohibitedIn'] != '[\'US\']']
    
    return df

# GET /markets => https://api.bittrex.com/v3/markets/tickers
def bittrex_tickers():
    t = eval(requests.get(bittrex_rest + '/markets/tickers').text)
    df = pd.DataFrame(t)
    df_markets = bittrex_markets()
    df = df[df['symbol'].isin(df_markets['symbol'])]
    
    return df

# cleaning candle data
def clean_hist_data(df):
    df.columns = ['datetime','open','high','low','close','volume','quoteVolume'] 
    df = df.astype({'open':'float64',
                    'high': 'float64', 
                    'low': 'float64', 
                    'close': 'float64', 
                    'volume': 'float64', 
                    'quoteVolume': 'float64' })
    df['datetime'] = pd.to_datetime(df['datetime'], infer_datetime_format=True)
    return df

# Recent Market data for ticker
# GET /markets/{marketSymbol}/candles/{candleType}/{candleInterval}/recent => https://api.bittrex.com/v3//markets/{marketSymbol}/candles/{candleType}/{candleInterval}/recent
def bittrex_recent_candles(marketSymbol="ETH-USD",candleInterval="DAY_1"):
    # /markets/{marketSymbol}/candles/{candleType}/{candleInterval}/recent
    # marketSymbol arg: string ADA-USD
    # candleType may be omitted if trae based candles are desired
    # candleType args: string [TRADE, MIDPOINT]
    # candleInterval args: string [MINUTE_1, MINUTE_5, HOUR_1, DAY_1]
    
    t = requests.get(bittrex_rest + f'/markets/{marketSymbol}/candles/{candleInterval}/recent').json()
    
    df = pd.DataFrame(t)
    df = clean_hist_data(df)
    
    return df





# Binance REST API
# https://api.binance.com/api/v3 
binance_rest = 'https://api.binance.com/api/v3'

# GET /ping => test connectivity
def binance_ping():
    t = eval(requests.get(bittrex_rest + '/ping').text)
    return t

# GET /exchangeInfo => Current exchange trading rules and symbol information
def binance_markets():
    t = eval(requests.get(bittrex_rest + '/exchangeInfo').text)
    #df = pd.DataFrame(t)
    #df = df[df['status'] == 'ONLINE']
    #df = df[df.astype(str)['prohibitedIn'] != '[\'US\']']
    
    return t

# GET /markets => https://api.bittrex.com/v3/markets/tickers
def binance_tickers():
    t = eval(requests.get(bittrex_rest + '/markets/tickers').text)
    df = pd.DataFrame(t)
    df_markets = bittrex_markets()
    df = df[df['symbol'].isin(df_markets['symbol'])]
    
    return df

# cleaning candle data
def clean_hist_data(df):
    df.columns = ['datetime','open','high','low','close','volume','quoteVolume'] 
    df = df.astype({'open':'float64',
                    'high': 'float64', 
                    'low': 'float64', 
                    'close': 'float64', 
                    'volume': 'float64', 
                    'quoteVolume': 'float64' })
    df['datetime'] = pd.to_datetime(df['datetime'], infer_datetime_format=True)
    return df

# Recent Market data for ticker
# GET /markets/{marketSymbol}/candles/{candleType}/{candleInterval}/recent => https://api.bittrex.com/v3//markets/{marketSymbol}/candles/{candleType}/{candleInterval}/recent
def binance_candle_data(marketSymbol="ETH-USD", candleInterval="DAY_1"):
    # /markets/{marketSymbol}/candles/{candleType}/{candleInterval}/recent
    # marketSymbol arg: string ADA-USD
    # candleType may be omitted if trae based candles are desired
    # candleType args: string [TRADE, MIDPOINT]
    # candleInterval args: string [MINUTE_1, MINUTE_5, HOUR_1, DAY_1]
    
    t = requests.get(bittrex_rest + f'/markets/{marketSymbol}/candles/{candleInterval}/recent').json()
    
    df = pd.DataFrame(t)
    df = clean_hist_data(df)
    
    return df











