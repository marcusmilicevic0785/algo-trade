# --- CELSIUS Weekly Stock Chart ---
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib.ticker import FuncFormatter

# Download data
df = yf.download(['CELH'], period="max", auto_adjust=False)
df.dropna(inplace=True)

# Fix MultiIndex
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [col[0] for col in df.columns]

# Weekly resample
df = df.resample('W').agg({'Close': 'last', 'Volume': 'sum'})

# ✅ HARD FILTER: remove 2026 weeks
df = df[df.index.year <= 2025]
df = df[df.index.year >= 2020]

# Plot
fig, ax1 = plt.subplots(figsize=(15, 8))

ax1.plot(df.index, df['Close'],
         linewidth=3, color='#CB3133')
ax1.set_ylabel('Price (USD)', fontsize=16, fontweight='bold')

# Remove spines
for spine in ax1.spines.values():
    spine.set_visible(False)

# Year ticks only
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# ✅ LOCK AXIS RANGE (this is the key)
ax1.set_xlim(pd.Timestamp('2020-01-01'),
             pd.Timestamp('2025-12-31'))
plt.xticks(rotation=23, fontsize=10, fontweight='bold')


# Volume
ax2 = ax1.twinx()
ax2.bar(df.index, df['Volume'],
        color='#231F20', alpha=0.5, width=3)

def millions_formatter(x, pos):
    return f'{x/1e6:.0f}M'

ax2.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
ax2.set_ylabel('Volume', fontsize=16, fontweight='bold')

ax1.tick_params(axis='both', labelsize=14, width=2)
ax2.tick_params(axis='both', labelsize=14, width=2)

plt.show()
