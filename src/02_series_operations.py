import pandas as pd
import numpy as np


# %% generating some data
np.random.seed(0)

A = np.random.randint(0, 10, 10)
series = pd.Series(A, name="los")

# %% attributes
series.dtype
series.iloc[3]
series.iloc[-1]
series.index
series.name
series.shape
array_A = series.values

# %% two series operations
np.random.seed(0)
N = np.random.randn(10)
M = np.random.randn(10)

series_N = pd.Series(N)
series_M = pd.Series(M)

series_N.abs()
series_N.add(series_M)
series_N.subtract(series_M)
series_N.divide(series_M)

series.drop_duplicates()
series[4] = np.nan
series.dropna()

series.idxmax()
series.idxmin()

series.count()

series_N.cumsum()
series_N.cummin()
series_N.cummax()

series.value_counts()
series.sum()
series.std()
series.describe()

# %% histogram
hist_data = pd.Series(np.random.randn(10000))
hist_data.hist(bins=80)

# %% top n
series_N.nlargest(3)

# %% quantiles
q_N = series_N.quantile(0.25)
median = series_N.quantile(0.5)

# %% rounding
series_N.round(3)

# %% shifting
shifted_1 = series.shift(1)
# will replace NA only for new values
shifted_2_replace_0 = series.shift(2, fill_value=0)
# will replace all NAs, even existing ones
shifted_2_replace_0 = series.shift(2).fillna(0)

# %% sorting
series.sort_values()
