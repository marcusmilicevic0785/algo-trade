# First step is to import the three libraries used in this project
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import yfinance as yf
import numpy as np
plt.style.use('fivethirtyeight')
# %matplotlib inline use 'plt.show()' insted of that before

# INPUT THE DATA
stock = str(input("Stock name is: "))
num_days = int(
    input('Number of days the analysis needs to be done(Please enter an integer): '))

# Set start date of the analysis
start_date = (datetime.datetime.now() -
              datetime.timedelta(days=num_days)).strftime("%Y-%m-%d")

# Import data from yahoo finance
df = yf.download(stock, start=start_date)

# Remove rows having np.nan
df.dropna(how='any', inplace=True)

# Visualize data
plt.figure(figsize=(15, 8))
plt.plot(df['Close'], label=stock, linewidth=0.5)
plt.title(str(stock) + ' Adjacent close price history')
plt.xlabel('Previous ' + str(num_days) + ' days')
plt.ylabel('Adj. close price (₹)')
plt.legend(loc='upper left')
plt.show()

# Create SMA Indiacator
SMA20 = pd.DataFrame()
SMA20['Price'] = df['Close'].rolling(window=20).mean()
SMA50 = pd.DataFrame()
SMA50['Price'] = df['Close'].rolling(window=50).mean()

# Store all Data in new DataFrame
Data = pd.DataFrame()
Data['Price'] = df['Close']
Data['SMA20'] = SMA20['Price']
Data['SMA50'] = SMA50['Price']
Data['funds'] = 1000  # Initialize funds so that it could be later modified

# Create a function to signal when to buy and when to sell


def buy_sell_signal(data):
    buy_signal = []
    sell_signal = []
    open_position = []
    funds = [1000] * len(data)
    last_funds = 1000
    flag = 0  # flag = 0 means sell_flag and flag = 1 means buy_flag

    for i in range(len(data)):
        if data['SMA20'].iloc[i] > data['SMA50'].iloc[i]:
            if flag == 0:
                flag = 1
                buy_signal.append(data['Price'].iloc[i])
                last_pos = last_funds / data['Price'].iloc[i]
                funds[i] = last_funds
                # buy_quantity with 1 Lac Capital
                open_position.append(last_pos)
                sell_signal.append(np.nan)
            else:
                buy_signal.append(np.nan)
                last_funds = data['Price'].iloc[i] * last_pos
                funds[i] = last_funds
                open_position.append(last_pos)
                sell_signal.append(np.nan)
        elif data['SMA20'].iloc[i] < data['SMA50'].iloc[i]:
            if flag == 1:
                flag = 0
                buy_signal.append(np.nan)
                last_funds = last_pos * data['Price'].iloc[i]
                funds[i] = last_funds
                open_position.append(0)
                sell_signal.append(data['Price'].iloc[i])
            else:
                buy_signal.append(np.nan)
                funds[i] = last_funds
                open_position.append(0)
                sell_signal.append(np.nan)
        else:
            buy_signal.append(np.nan)
            open_position.append(0)
            sell_signal.append(np.nan)
    return buy_signal, sell_signal, open_position, funds, flag


# Store buy and sell in Data
buy_sell = buy_sell_signal(Data)
# print(buy_sell)
Data['Buy_price'] = buy_sell[0]
Data['Sell_price'] = buy_sell[1]
Data['Open_pos'] = buy_sell[2]
Data['live_pos'] = Data['Open_pos'].multiply(Data['Price'])
Data['funds'] = buy_sell[3]

# Visualize Data and strategy to buy and sell NIFTY
plt.figure(figsize=(15, 8))
plt.plot(Data['Price'], label=str(stock), linewidth=1)
plt.plot(Data['SMA20'], label='SMA20', linewidth=0.5)
plt.plot(Data['SMA50'], label='SMA50', linewidth=0.5)
plt.scatter(Data.index, Data['Buy_price'],
            label='Buy', marker='^', color='g', s=100)
plt.scatter(Data.index, Data['Sell_price'],
            label='Sell', marker='v', color='r', s=100)
plt.title(str(stock) + ' Buy-Sell Signals')
plt.xlabel(str(num_days) + ' days')
plt.ylabel('Close price (₹)')
plt.legend(loc='upper left')
plt.show()

# Visualize results / PnL
plt.figure(figsize=(15, 8))
plt.plot(Data['funds'], linewidth=1.0)
plt.xticks(rotation=45)
plt.title('Profit & Loss')
plt.xlabel('Date')
plt.ylabel('Funds')
plt.show()
print(Data['funds'])
