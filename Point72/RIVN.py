# --- RIVIAN Weekly Stock Chart ---
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib.ticker import FuncFormatter

# Download and clean data
df = yf.download(['RIVN'], period="max", auto_adjust=False)
df.dropna(how='any', inplace=True)

# --- FIX for MultiIndex Columns ---
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [col[0] for col in df.columns]

# Convert to weekly data
df = df.resample('W').agg({'Close': 'last', 'Volume': 'sum'})

# Create figure
fig, ax1 = plt.subplots(figsize=(15, 8))

# Plot weekly closing price (yellow line)
ax1.plot(df.index, df['Close'], label='RIVN Close',
         linewidth=3, color='#FFD700')
ax1.set_ylabel('Price (USD)', fontsize=16, fontweight='bold')

# Remove chart border (spines)
for spine in ax1.spines.values():
    spine.set_visible(False)

# --- X-Axis Formatting (Fewer Dates + Smaller Font) ---
ax1.xaxis.set_major_locator(mdates.MonthLocator(
    interval=8))  # show every 3 months
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=23, fontsize=10, fontweight='bold')

# Add volume bars on secondary y-axis (bottom spikes)
ax2 = ax1.twinx()
ax2.bar(df.index, df['Volume'], color='#004225',
        alpha=0.25, width=3, label="Volume")

# --- Clean up volume axis ---


def millions_formatter(x, pos):
    return f'{x/1e6:.0f}M'


ax2.yaxis.set_major_formatter(FuncFormatter(millions_formatter))

# Labels and ticks
ax2.set_ylabel('Volume', fontsize=16, fontweight='bold')
ax1.tick_params(axis='both', labelsize=14, width=2)
ax2.tick_params(axis='both', labelsize=14, width=2)


plt.show()
