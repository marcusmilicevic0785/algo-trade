import pandas as pd
import matplotlib.pyplot as plt

# --- Original data + hard-coded forecasts ---
data = {
    'year': ['2022', '2023', '2024', '2025', '2026', '2027'],
    'rivian_gpm': [-188.4, -45.8, -24.2, -5.2, 0.9, 0.5],
    "tesla_gpm": [25.6, 18.25, 17.9, 17.4, None, None],
    "ford_gpm": [10.9, 9.2, 8.4, 7.22, None, None],
    "hyundai_gpm": [23.91, 25.02, 25.84, 28.12, None, None]
}

df = pd.DataFrame(data)

# --- Plot ---
fig, ax1 = plt.subplots(figsize=(15, 8))

# Gas price
ax1.plot(df['year'], df['rivian_gpm'], color='#FFD700',
         marker='.', markersize='12', label="Rivian", linewidth='3')
ax1.set_ylabel('Gross Profit Margin', color='black',
               fontsize=18, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='black', labelsize=17, width=2)
ax1.plot(df['year'], df['tesla_gpm'], color='#e80909',
         marker='.', label="Tesla", markersize='12', linewidth='3')
ax1.plot(df['year'], df['ford_gpm'], markersize='12', color='#047AF2',
         marker='.', label="Ford", linewidth='3')
ax1.plot(df['year'], df['hyundai_gpm'], color='#002C5F',
         marker='.', label="Hyundai", markersize='12', linewidth='3')


# Highlight forecast region
ax1.axvline(x='2025', color='gray', linestyle=':', linewidth=2)
plt.text(len(df)-3, min(df['rivian_gpm']) * 1.05, 'Forecast →',
         color='black', fontsize=12, fontweight='bold', va='bottom')

# #FFD700uce clutter on X-axis: show only every 4th quarter
ax1.set_xticks(df.index[::1])
ax1.set_xticklabels(df['year'][::1], rotation=0,
                    fontsize=17, fontweight='bold')

# Title, legend
fig.suptitle('GPM of RIVN VS Competitors',
             fontsize=14, weight='bold')
ax1.legend(loc='upper right', bbox_to_anchor=(0.99, 0.4), fontsize='17')
plt.show()
