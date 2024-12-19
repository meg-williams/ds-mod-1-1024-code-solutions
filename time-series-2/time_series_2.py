# %%
import pandas as pd
import numpy as np

# models 
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

#metrics
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
import itertools
from sklearn.metrics import root_mean_squared_error

# plots
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

# %% [markdown]
# #### dataframe

# %%
df = pd.read_csv('/Users/meganwilliams/Documents/GitHub/ds-mod-1-1024-code-solutions/time-series-2/AirPassengers.csv')

# %%
df

# %%
df.info()

# %%
df['Month'] = pd.to_datetime(df['Month'])

# %%
df.info()

# %%
df.set_index('Month', inplace=True)

# %%
df.info()

# %%
df

# %% [markdown]
# #### functions

# %%
def plotANDadf(data): 
    data.plot();
    print(adfuller(data.dropna())[1])

# %%
def arima_eval(noise, model): 
    noise.plot()
    model.fittedvalues.plot() 
    print('aic: ', model.aic) 
    print('bic: ', model.bic)



# %% [markdown]
# #### prep

# %%
plotANDadf(df['#Passengers'])

# %%
passenger_log = np.log(df['#Passengers'])

# %%
plotANDadf(passenger_log)

# %%
passenger_log_diff1 = passenger_log.diff()

# %%
plotANDadf(passenger_log_diff1)

# %%
passenger_log_diff2 = passenger_log.diff(2)

# %%
plotANDadf(passenger_log_diff2)

# %%
passenger_log_diff3 = passenger_log.diff(3)

# %%
plotANDadf(passenger_log_diff3)

# %% [markdown]
# #### question 1

# %%
passangers = df['#Passengers']
passangers

# %%
decomp = seasonal_decompose(passangers)

# %%
trend = decomp.trend
seasonal = decomp.seasonal
noise = decomp.resid

# %%
fig, ax = plt.subplots(nrows=4, ncols=1)
ax[0].plot(passangers.index, passangers.values)
ax[1].plot(passangers.index, trend)
ax[2].plot(passangers.index, seasonal)
ax[3].plot(passangers.index, noise)
fig.tight_layout()

# %%
plotANDadf(noise)

# %%
plot_acf(noise.dropna());

# %%
plot_pacf(noise.dropna());

# %%
noise_diff1 = noise.diff()

# %%
plotANDadf(noise_diff1)

# %%
plot_acf(noise_diff1.dropna());

# %%
plot_pacf(noise_diff1.dropna());

# %% [markdown]
# ##### arima 12

# %%
ar12 = ARIMA(noise, order=(12, 1, 0)).fit()
ma12 = ARIMA(noise, order=(0,1,12)).fit()
ar12ma12 = ARIMA(noise, order=(12,1,12)).fit()

# %%
arima_eval(noise, ar12)

# %%
arima_eval(noise, ma12)

# %%
arima_eval(noise, ar12ma12)

# %% [markdown]
# ##### arima 13

# %%
ar13 = ARIMA(noise, order=(13, 1, 0)).fit()
ma13 = ARIMA(noise, order=(0,1,13)).fit()
ar13ma13 = ARIMA(noise, order=(13,1,13)).fit()

# %%
arima_eval(noise, ar13)

# %%
arima_eval(noise, ma13)

# %%
arima_eval(noise, ar13ma13)

# %% [markdown]
# ##### search

# %%
p_vals = [1,5,6,7,11,12,13]
d_vals = [1,2,3]
q_vals = [1,5,6,7,11,12,13]

best_aic = np.inf
best_aic_pdq = (0,0,0)
best_bic = np.inf
best_bic_pdq = (0,0,0)

# %%
for pdq in itertools.product(p_vals, d_vals, q_vals): 
    
    model = ARIMA(noise, order=pdq).fit()
    aic = model.aic

    if aic < best_aic: 
        best_aic = aic
        best_aic_pdq = pdq



# %%
best_aic

# %%
best_aic_pdq

# %%
for pdq in itertools.product(p_vals, d_vals, q_vals): 
    
    model = ARIMA(noise, order=pdq).fit()
    bic = model.bic

    if bic < best_bic: 
        best_bic = bic
        best_bic_pdq = pdq

# %%
best_bic_pdq

# %%
best_bic

# %% [markdown]
# #### question 2

# %%
plotANDadf(seasonal)

# %%
plot_acf(seasonal);

# %%
plot_acf(seasonal, lags=np.arange(0, len(seasonal)));

# %%
plot_acf(seasonal, lags=np.arange(0,24));

# %%
sarima = SARIMAX(passangers, order=(11,1,5), seasonal_order=(2,0,3,12), trend='ct').fit()

# %%
passangers.plot()
sarima.fittedvalues.plot();

# %%
sarima_fitted = sarima.fittedvalues

# %%
root_mean_squared_error(passangers, sarima_fitted)


