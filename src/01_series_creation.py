# %%
import pandas as pd
import numpy as np

# Example 1
s = pd.Series(4)

# Example 2
s_def = pd.Series(data=[21, 34, 54], index=[
                  'adam', 'tomek', 'paweł'], name='age')

# %% Example 3
A = np.random.randn(10)
s = pd.Series(A)

# %% Example 4
stocks = {
    'Apple': 'USA',
    'CD Projekt': 'Poland',
    'Amazon': 'USA'
}
series = pd.Series(stocks, name='country')

# %% Example 5
stocks_price = {
    'Apple': 196,
    'CD Projekt': 215,
    'Amazon': 1877
}
stocks_price_series = pd.Series(stocks_price, name='price')
stocks_price_array = stocks_price_series.values

apple_price = stocks_price_series['Apple']
'Apple' in stocks_price_series

# %% Example 6
np.random.seed(0)
A = np.random.randn(20)
s = pd.Series(A)

s[0]
s[1]
s[5:10]
s[:10]
s[5:]
