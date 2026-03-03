# Federal Debt: Total Public Debt as Percent of Gross Domestic Product https://fred.stlouisfed.org/series/GFDEGDQ188S
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_excel('Fiscal/GFDEGDQ188S/GFDEGDQ188S.xlsx',
                   sheet_name="Quarterly")

# Ensure date column is datetime
df['date'] = pd.to_datetime(df['date'])

fig, ax1 = plt.subplots(figsize=(15, 8))

# Plot line
ax1.plot(df['date'], df['GFDEGDQ188S'], linewidth=2, color='#DF543B')

# Shaded area under the line
ax1.fill_between(df['date'], df['GFDEGDQ188S'], alpha=0.7, color='#E88473')

# Remove margins so line goes edge to edge
ax1.set_xlim(df['date'].min(), df['date'].max())

# Y-axis starts at 0 with no whitespace below
ax1.set_ylim(0, df['GFDEGDQ188S'].max() * 1.05)

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
plt.title("Total Public Debt as Percent of Gross Domestic Product",
          fontsize=14, fontweight='normal')

plt.tight_layout()
plt.show()
