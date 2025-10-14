import pandas as pd
import matplotlib.pyplot as plt

# --- Original data + hard-coded forecasts ---
data = {
    'Quarter': ['2015-Q1', '2015-Q2', '2015-Q3', '2015-Q4',
                '2016-Q1', '2016-Q2', '2016-Q3', '2016-Q4',
                '2017-Q1', '2017-Q2', '2017-Q3', '2017-Q4',
                '2018-Q1', '2018-Q2', '2018-Q3', '2018-Q4',
                '2019-Q1', '2019-Q2', '2019-Q3', '2019-Q4',
                '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4',
                '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4',
                '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4',
                '2023-Q1', '2023-Q2', '2023-Q3', '2023-Q4',
                '2024-Q1', '2024-Q2', '2024-Q3', '2024-Q4',
                '2025-Q1', '2025-Q2', '2025-Q3',
                # Forecasted quarters
                '2025-Q4', '2026-Q1', '2026-Q2', '2026-Q3', '2026-Q4'],
    'Gas_Price_USD': [2.27, 2.75, 2.62, 2.14, 1.98, 2.23, 2.25, 2.18, 2.30, 2.42, 2.56, 2.60, 2.61, 2.87,   2.91, 2.61, 2.5, 2.84, 2.73, 2.64, 2.5, 2.02, 2.24, 2.24, 2.67, 3.12, 3.29, 3.43, 4.01, 4.59, 4.03, 3.44, 3.59, 3.68, 3.78, 3.37, 3.47, 3.58, 3.33, 3.15, 3.27, 3.23, 3.16, 2.99, 2.93, 3.12, 3.16, 2.96],
    # 'EV_Demand_thousand': [14, 16, 17, 18, 19, 20, 21, 22, 23, 25, 27, 29, 32, 36, 40, 45, 78, 82, 80, 85, 56, 50, 67, 91, 104, 139, 158, 197, 210, 230, 263, 331, 257, 282, 348, 414, 346, 332, 356, 398, 375, 311, 438, 385, 350, 405, 455, 420],
    # 'Rivn_deliveries': [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 1.227, 4.467, 6.584, 8.054, 7.946, 12.640, 15.564, 13.972, 13.588, 13.790, 10.018, 14.183, 8.640, 10.661, 13.846, 9.508, 10.544, 12.008, 15.741, 18.375],
    'EV_Demand_thousand': [None, 14.2857, 6.25, 5.8824, 5.5556, 5.2632, 5.0, 4.7619, 4.5455, 8.6957, 8.0, 7.4074, 10.3448, 12.5, 11.1111, 12.5, 73.3333, 5.1282, -2.439, 6.25, -34.1176, -10.7143, 34.0, 35.8209, 14.2857, 33.6538, 13.6691, 24.6835, 6.599, 9.5238, 14.3478, 25.8555, -22.3565, 9.7276, 23.4043, 18.9655, -16.4251, -4.0462, 7.2289, 11.7978, -5.7789, -17.0667, 40.836, -12.1005, -9.0909, 15.7143, 12.3457, -7.6923],
    'Rivn_deliveries': [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 264.0587, 47.392, 22.3269, -1.3409, 59.0737, 23.1329, -10.2287, -2.7484, 1.4866, -27.3532, 41.5752, -39.082, 23.3912, 29.8752, -31.3303, 10.8961, 13.8847, 31.0876, 16.7334]
}

df = pd.DataFrame(data)

# --- Plot ---
fig, ax1 = plt.subplots(figsize=(14, 6))

# Gas price
ax1.plot(df['Quarter'], df['Gas_Price_USD'], color='#FFD700',
         marker='s', label='Gas Price ($/gal)')
ax1.set_ylabel('Gas Price ($/gal)', color='#bda104',
               fontsize=16, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='#bda104', labelsize=14, width=2)

# EV demand on secondary axis
ax2 = ax1.twinx()
ax2.plot(df['Quarter'], df['EV_Demand_thousand'], color='#004225',
         marker='^', label='EV Demand (Q/Q "%" change)')
ax2.plot(df['Quarter'], df['Rivn_deliveries'], color='#04a1bd',
         marker='o', label='Rivian Deliveries (Q/Q "%" change)')
ax2.set_ylabel('EV Demand (thousands)', color='#004225',
               fontsize=16, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='#004225', labelsize=14, width=2)

# Highlight forecast region
ax1.axvline(x='2025-Q4', color='gray', linestyle=':', linewidth=2)
plt.text(len(df)-5, min(df['EV_Demand_thousand']) * 1.05, 'Forecast →',
         color='black', fontsize=12, fontweight='bold', va='bottom')

# #FFD700uce clutter on X-axis: show only every 4th quarter
ax1.set_xticks(df.index[::4])
ax1.set_xticklabels(df['Quarter'][::4], rotation=0,
                    fontsize=10, fontweight='bold')

# Title, legend
fig.suptitle('Gas Prices VS EV Demand Analyst Forecast ',
             fontsize=14, weight='bold')
ax1.legend(loc='upper left', bbox_to_anchor=(0, 1.0))
ax2.legend(loc='upper left', bbox_to_anchor=(0, 0.88))
plt.show()
