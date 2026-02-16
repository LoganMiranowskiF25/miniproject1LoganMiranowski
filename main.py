#Logan Miranowski
#INF601 - Spring 2026
#Mini-Project 1

import os 
import matplotlib.pyplot as plt
import numpy as np
import yfinance

# List of tickers
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']

#make sure 'charts' folder exists
if not os.path.exists('charts'):
    os.makedirs('charts')

# Loop through each ticker
for ticker in tickers:
    # Dowload last 10 trading days of data
    data = yfinance.download(ticker, period='10d')
    closing_prices = data['Close'].values
    days = np.arange(1, len(closing_prices) + 1)