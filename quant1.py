#First step is to import the three libraries used in this project
import matplotlib.pyplot as plt
import datetime
import pandas as pd
plt.style.use('fivethirtyeight')
from pandas_datareader import data as web
# %matplotlib inline use 'plt.show()' insted of that before

#INPUT THE DATA
stock = input("Stock name is: ")
num_days = int(input('Number of days the analysis needs to be done(Please enter an integer): '))

#Set start date of the analysis
start_date = (datetime.datetime.now() - datetime.timedelta(days = num_days)).strftime("%m-%d-%Y")


