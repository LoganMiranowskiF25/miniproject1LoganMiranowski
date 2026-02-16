#Logan Miranowski
#INF601 - Advanced Programming in Python
#Mini-Project 1

import os 
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

# List of tickers
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']

#make sure 'charts' folder exists
if not os.path.exists('charts'):
    os.makedirs('charts')

# Loop through each ticker
for ticker in tickers:
    # Dowload last 10 trading days of data
    data = yf.download(ticker, period='10d')
    closing_prices = data['Close'].values #Convert to numpy array for easier plotting
    days = np.arange(1, len(closing_prices) + 1)

    # Plot graph
    plt.figure(figsize=(8,5))
    plt.plot(days, closing_prices, marker='o', linestyle='-', color='green')
    plt.title(f"{ticker} Closing Prices for Last 10 Trading Days")
    plt.xlabel("Trading Days Ago")
    plt.ylabel("Closing Price")
    plt.grid(True)

