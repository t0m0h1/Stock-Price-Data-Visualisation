import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

symbol = 'AAPL' # Apple Inc, for example
stock = yf.Ticker(symbol)
data = stock.history(period='1y') # stock over the last year

