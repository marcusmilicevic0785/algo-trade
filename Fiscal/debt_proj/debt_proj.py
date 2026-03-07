# fiscal 30 yr projection of debt held by the public
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('Fiscal/debt_proj/FY.csv')
df['observation_date'] = pd.to_datetime(df['observation_date'])

# Load recession data
rec = pd.read_csv('Fiscal/USREC.csv')
rec['observation_date'] = pd.to_datetime(rec['observation_date'])
rec = rec.set_index('observation_date').resample('QS').max().reset_index()

cutoff = pd.Timestamp('2026-01-01')

fig, ax1 = plt.subplots(figsize=(15, 8))

ax1.plot(df['observation_date'], df['debt'], linewidth=2, color='#DF543B')
ax1.fill_between(df['observation_date'], df['debt'],
                 alpha=0.8, color='#E88473')

# Remove margins so line goes edge to edge
ax1.set_xlim(df['observation_date'].min(), df['observation_date'].max())
ax1.set_ylim(0, df['debt'].max() * 1.05)

# Vertical forecast line
ax1.axvline(x=cutoff, color='#1E3A8A', linewidth=3)
ax1.text(cutoff, df['debt'].max() * 0.95,
         '  Forecast →', color='black', fontsize=12, fontweight="bold")

# X-axis: years only, no bold
# ax1.xaxis.set_major_locator(mdates.YearLocator(5))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=0, fontsize=11)

# Y-axis
ax1.set_ylabel('Percent of GDP', fontsize=12)
ax1.tick_params(axis='both', labelsize=11, width=1)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, color='grey', alpha=0.7)
ax1.set_axisbelow(True)

specific_x_ticks = ["1970-01-01", "1980-01-01", "1990-01-01",
                    "2000-01-01", "2010-01-01", "2020-01-01", "2026-01-01", "2030-01-01", "2040-01-01", "2050-01-01", "2056-01-01"]

ax1.set_xticks(specific_x_ticks)

# Remove bold from tick labels
for label in ax1.get_xticklabels() + ax1.get_yticklabels():
    label.set_fontweight('normal')

# Filter recession data to match main data's time range
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
                    color='grey', alpha=0.3, zorder=0)
        in_recession = False

# Catch any recession that extends to the end of the data
if in_recession:
    ax1.axvspan(rec_start, end, color='grey', alpha=0.3, zorder=0)

plt.title("Historical Public Held Debt to GDP Projections",
          fontsize=14, fontweight='normal')
plt.tight_layout()
plt.show()
