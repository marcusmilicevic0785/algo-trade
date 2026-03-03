# Federal Outlays: Interest as Percent of Gross Domestic Product https://fred.stlouisfed.org/series/FYOIGDA188S
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('Fiscal/FYOIGDA188S/FYOIGDA188S.csv')

# Ensure date column is datetime
df['observation_date'] = pd.to_datetime(df['observation_date'])

fig, ax1 = plt.subplots(figsize=(15, 8))

# Plot line
ax1.plot(df['observation_date'], df['FYOIGDA188S'],
         linewidth=2, color='#DF543B')

# Shaded area under the line
ax1.fill_between(df['observation_date'], df['FYOIGDA188S'],
                 alpha=0.7, color='#E88473')

# Remove margins so line goes edge to edge
ax1.set_xlim(df['observation_date'].min(), df['observation_date'].max())

# Y-axis starts at 0 with no whitespace below
ax1.set_ylim(0, df['FYOIGDA188S'].max() * 1.05)

# X-axis: years only, no bold
ax1.xaxis.set_major_locator(mdates.YearLocator(5))  # every 5 years
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=0, fontsize=11)

# Y-axis
ax1.set_ylabel('Percent of GDP', fontsize=12)
ax1.tick_params(axis='both', labelsize=11, width=1)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, color='grey', alpha=0.7)

# Remove bold from tick labels
for label in ax1.get_xticklabels() + ax1.get_yticklabels():
    label.set_fontweight('normal')

# Title - normal weight
plt.title("Interest as Percent of Gross Domestic Product",
          fontsize=14, fontweight='normal')

plt.tight_layout()
plt.show()
