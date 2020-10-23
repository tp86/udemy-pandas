# %%
import pandas as pd
import numpy as np

# %% Create simple Series
s = pd.Series(4)

# %% Create with data and index
s_def = pd.Series(data=[21, 34, 54],
                  index=['adam', 'tomek', 'paweł'],
                  name='wiek')

# %% Create Series with random data
A = np.random.randn(10)
s = pd.Series(A)

# %% Create text Series
stocks = {'Apple': 'USA', 'CD Projekt': 'Poland', 'Amazon': 'USA'}
series = pd.Series(stocks, name='country')

# %% Stock price Series
stocks_price = {'Apple': 196, 'CD Projekt': 215, 'Amazon': 1877}
stocks_price_series = pd.Series(stocks_price, name='price')

# %% Series to numpy array
stocks_price_array = stocks_price_series.values

# %% Price for Apple (accessing values by index)
apple_price = stocks_price_series['Apple']

# %% is-element test for index
'Apple' in stocks_price_series
# %% is-element test for value
196 in stocks_price_series.values
