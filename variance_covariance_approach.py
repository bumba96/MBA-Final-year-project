# -*- coding: utf-8 -*-
"""Variance_covariance_approach.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vYmyM1CRU5fFuuxIWboXjl2Lkm-LqcNW

Importing important Libraries
"""

import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm

"""Set Time to a certain number of years"""

years=5
endDate= dt.datetime(2023,10,16)
startDate=endDate-dt.timedelta(days=365*years)

"""Creating a list of Indexes"""

tickers = ['^NSEI', '^BSESN']

"""Download daily adjusted closing prices for the Indices"""

adj_close_df=pd.DataFrame()
for i in tickers:
  data=yf.download(i, start=startDate, end=endDate)
  adj_close_df[i]= data['Adj Close']
print(adj_close_df)

"""Calculate the simple daily returns and drop any NAs"""

daily_returns=adj_close_df/adj_close_df.shift(1) - 1
daily_returns=daily_returns.dropna()
print(daily_returns)

"""Create a Portfolio"""

weights=np.array([0.5,0.5])
print(weights)

"""Calculate the historical portfolio returns"""

historical_returns=(daily_returns*weights).sum(axis=1)
historical_returns_df = historical_returns.to_frame()
historical_returns_df.columns = ['Portfolio returns']
print(historical_returns_df)

"""Find required days historical returns"""

days=1
range_returns=historical_returns_df.rolling(window=days).sum()
range_returns=range_returns.dropna()
print(range_returns)

"""Calculate mean and standard deviation"""

portfolio_mean=range_returns['Portfolio returns'].mean()
portfolio_std_dev=range_returns['Portfolio returns'].std()
print(f'portfolio average Return: {portfolio_mean*100:.2f}%')
print(f'portfolio standard deviation: {portfolio_std_dev*100:.2f}%')

"""Confidence interval and Z-score"""

confidence_interval=0.99
z_score=norm.ppf(1-confidence_interval)
print(f'Z-Score: {z_score:.2f}')

"""Formula for VCV Var (X%) = (µ + Z(1-α)*σ);

µ = portfolio average return

Z = Z-score corresponding to particular interval level

1-α = significance level

σ = portfolio standard deviation

"""

VaR= portfolio_mean + (z_score*portfolio_std_dev)
print(f'VaR: {VaR*100:.2f}%')

"""Plot"""

plt.hist(historical_returns*100, bins=50, density=True)
plt.xlabel(f'{days}- Day Portfolio Return (percentage Value)')
plt.ylabel('Frequency')
plt.title(f'Distribution of Portfolio {days}-Day Returns (Percentage value)')
plt.axvline(VaR*100, color='r', linestyle='dashed', linewidth=2, label=f'VaR at {confidence_interval:.0%} confidence level: {VaR*100:.2f}%')
plt.legend()
plt.show()