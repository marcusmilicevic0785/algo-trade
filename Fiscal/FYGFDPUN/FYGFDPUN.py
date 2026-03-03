# Federal Debt Held by the Public https://fred.stlouisfed.org/series/FYGFDPUN
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('Fiscal/FYGFDPUN/FYGFDPUN.csv')

# Ensure date column is datetime
df['observation_date'] = pd.to_datetime(df['observation_date'])

# Load recession data
rec = pd.read_csv('Fiscal/USREC.csv')
rec['observation_date'] = pd.to_datetime(rec['observation_date'])

fig, ax1 = plt.subplots(figsize=(15, 8))

# Plot line
ax1.plot(df['observation_date'], df['FYGFDPUN'],
         linewidth=2, color='#DF543B')

# Shaded area under the line
ax1.fill_between(df['observation_date'], df['FYGFDPUN'],
                 alpha=0.7, color='#E88473')

# Remove margins so line goes edge to edge
ax1.set_xlim(df['observation_date'].min(), df['observation_date'].max())

# Y-axis starts at 0 with no whitespace below
ax1.set_ylim(0, df['FYGFDPUN'].max() * 1.05)

# X-axis: years only, no bold
ax1.xaxis.set_major_locator(mdates.YearLocator(5))  # every 5 years
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=0, fontsize=11)


# Y-axis
ax1.set_ylabel('Millions of Dollars', fontsize=12)
ax1.tick_params(axis='both', labelsize=11, width=1)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, color='grey', alpha=0.7)
ax1.ticklabel_format(style='plain', axis='y')
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))

# Remove bold from tick labels
for label in ax1.get_xticklabels() + ax1.get_yticklabels():
    label.set_fontweight('normal')

# Filter to match main data's time range
start, end = df['observation_date'].min(), df['observation_date'].max()
rec = rec[(rec['observation_date'] >= start)
          & (rec['observation_date'] <= end)]

# Shade recession periods
in_recession = False
rec_start = None

for _, row in rec.iterrows():
    if row['USREC'] == 1 and not in_recession:
        rec_start = row['observation_date']
        in_recession = True
    elif row['USREC'] == 0 and in_recession:
        ax1.axvspan(rec_start, row['observation_date'],
                    color='grey', alpha=0.2, zorder=0)
        in_recession = False

# Catch any recession that extends to the end of the data
if in_recession:
    ax1.axvspan(rec_start, end, color='grey', alpha=0.2, zorder=0)

# Title - normal weight
plt.title("Federal Debt Held by the Public", fontsize=14, fontweight='normal')

plt.tight_layout()
plt.show()
