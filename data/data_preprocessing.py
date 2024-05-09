# data/data_preprocessing.py
import pandas as pd
import logging
from config import DATA_SOURCE, START_DATE, END_DATE, TICKERS
from talib import RSI

logger = logging.getLogger(__name__)

def fetch_raw_data(symbol):
    try:
        if DATA_SOURCE == 'iexfinance':
            from iexfinance.stocks import get_historical_data
            raw_data = get_historical_data(symbol, START_DATE, END_DATE, output_format='pandas')
        else:
            logger.error(f"Unsupported data source: {DATA_SOURCE}")
            raise ValueError(f"Unsupported data source: {DATA_SOURCE}")
    except Exception as e:
        logger.error(f"Error fetching data for {symbol}: {e}")
        raise e
    return raw_data

def preprocess_data(raw_data):
    processed_data = raw_data.copy()
    processed_data['moving_average_20'] = processed_data['close'].rolling(window=20).mean()
    processed_data['moving_average_50'] = processed_data['close'].rolling(window=50).mean()
    processed_data['rsi'] = RSI(processed_data['close'].values, timeperiod=14)
    return processed_data

def calculate_rsi(prices, window=14):
    deltas = np.diff(prices)
    seed = deltas[:window+1]
    up = seed[seed >= 0].sum() / window
    down = -seed[seed < 0].sum() / window
    rs = up / down
    rsi = np.zeros_like(prices)
    rsi[:window] = 100. - 100. / (1. + rs)

    for i in range(window, len(prices)):
        delta = deltas[i - 1]
        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up * (window - 1) + upval) / window
        down = (down * (window - 1) + downval) / window
        rs = up / down
        rsi[i] = 100. - 100. / (1. + rs)

    return rsi

