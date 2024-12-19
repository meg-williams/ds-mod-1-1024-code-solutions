# %%
import pandas as pd 
import numpy as np
import matplotlib as plt
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
from scipy.stats import yeojohnson

# %% [markdown]
# #### dataframe

# %%
df = pd.read_csv('time-series-1/AirPassengers.csv')
df.head(10)

# %%
df.info()

# %% [markdown]
# #### question 1

# %% [markdown]
# ##### month dtype from object to datetime

# %%
df['Month'] = pd.to_datetime(df['Month'])

# %% [markdown]
# ##### set month as index

# %%
df.set_index('Month', inplace=True)

# %%
df.head()

# %% [markdown]
# ##### rolling mean

# %%
mean_rolling_7 = df.rolling(7).mean()
mean_rolling_7.head(10)

# %% [markdown]
# ##### rolling standard deviation 

# %%
std_rolling_7 = df.rolling(7).std()
std_rolling_7

# %%
df.head(10)

# %% [markdown]
# ##### plot of dataframe

# %%
plt.plot(df.index, df['#Passengers']) 
plt.plot(df.index, std_rolling_7)
plt.plot(df.index, mean_rolling_7);

# %% [markdown]
# ##### this graph shows an upward trend in the mean over time as well as an increasing variance in standard deviation there for it is not stationary

# %% [markdown]
# #### question 2

# %% [markdown]
# ##### differences 

# %%
df['diff1'] = df['#Passengers'].diff()

# %%
df['diff2'] = df['#Passengers'].diff(2)

# %%
df['diff3'] = df['#Passengers'].diff(3)

# %% [markdown]
# ##### rolling for differences 

# %%
df['diff1_mean_rolling7'] = df['diff1'].rolling(7).mean()
df['diff1_std_rolling7'] = df['diff1'].rolling(7).std()

# %%
df['diff2_mean_rolling7'] = df['diff2'].rolling(7).mean()
df['diff2_std_rolling7'] = df['diff2'].rolling(7).std()

# %%
df['diff3_mean_rolling7'] = df['diff3'].rolling(7).mean()
df['diff3_std_rolling7'] = df['diff3'].rolling(7).std()

# %% [markdown]
# ##### plotting differences

# %%
plt.plot(df.index, df['diff1'])
plt.plot(df.index, df['diff1_mean_rolling7'])
plt.plot(df.index, df['diff1_std_rolling7']);

# %%
plt.plot(df.index, df['diff2'])
plt.plot(df.index, df['diff2_mean_rolling7'])
plt.plot(df.index, df['diff2_std_rolling7']);

# %%
plt.plot(df.index, df['diff3'])
plt.plot(df.index, df['diff3_mean_rolling7'])
plt.plot(df.index, df['diff3_std_rolling7']);

# %% [markdown]
# #### question 3

# %% [markdown]
# ##### log transform 

# %%
df['log_#Passengers'] = np.log(df['#Passengers'])

# %%
df['log_#Passengers'].plot();

# %%
df['log_diff1'] = df['log_#Passengers'].diff()

# %%
plt.plot(df.index, df['log_diff1']);

# %%
df['log_diff2'] = df['log_#Passengers'].diff(2)

# %%
plt.plot(df.index, df['log_diff2']);

# %%
df['log_diff3'] = df['log_#Passengers'].diff(3)

# %%
plt.plot(df.index, df['log_diff3']);

# %% [markdown]
# #### yeo johnson

# %%
yj_passengers, lmbd = yeojohnson(df['#Passengers'])

# %%
df['yj_passengers'] = yj_passengers

# %%
plt.plot(df.index, df['yj_passengers']);

# %%
df['yj_diff1'] = df['yj_passengers'].diff()

# %%
plt.plot(df.index, df['yj_diff1']);

# %%
df['yj_diff2'] = df['yj_passengers'].diff(2)

# %%
plt.plot(df.index, df['yj_diff2']);

# %%
df['yj_diff3'] = df['yj_passengers'].diff(3)

# %%
plt.plot(df.index, df['yj_diff3']);

# %% [markdown]
# #### question 4

# %% [markdown]
# ##### origian data adf

# %%
log_adf1 = adfuller(df['#Passengers'])
log_adf1

# %% [markdown]
# ##### just difference adf 

# %%
diff1_adf = adfuller(df['diff1'].dropna())
diff1_adf

# %%
diff2_adf = adfuller(df['diff2'].dropna())
diff2_adf

# %%
diff3_adf = adfuller(df['diff3'].dropna())
diff3_adf

# %% [markdown]
# ##### log difference adf

# %%
log_adf1 = adfuller(df['diff1'].dropna())
log_adf1

# %%
log_adf2 = adfuller(df['log_diff2'].dropna())
log_adf2

# %%
log_adf3 = adfuller(df['log_diff3'].dropna())
log_adf3

# %% [markdown]
# ##### yeo johnson adf

# %%
yj_adf1 = adfuller(df['yj_diff1'].dropna())
yj_adf1

# %%
yj_adf2 = adfuller(df['yj_diff2'].dropna())
yj_adf2

# %%
yj_adf3 = adfuller(df['yj_diff3'].dropna())
yj_adf3

# %%
df.info()

# %% [markdown]
# ##### data with adf < 0.05
# 
# ##### dff2: p=0.038629757676988535
# ##### diff3: p=0.04693983572510757
# ##### log_diff2: p=0.021919114564039187
# ##### yj_diff1: p=0.048640210532627966
# ##### yj_diff2: p=0.016657490283272496
# ##### yj_diff3: p=0.047300425499996704


