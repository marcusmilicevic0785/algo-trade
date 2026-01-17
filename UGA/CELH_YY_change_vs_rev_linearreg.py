import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Data
data = {
    'Year': list(range(2020, 2031)),
    'rev': [131, 314, 654, 1318, 1356, 2169, 3037, 3644, 3826, 4017, 4137],
    'change': [None, 140.4, 108.0, 101.7, 2.9, 60.0, 40.0, 20.0, 5.0, 5.0, 3.0]
}
'''Year	2020	2021	2022	2023	2024	2025	2026	2027	2028	2029	2030
Revenue	131	314 	654 	1,318 	1,356	2,169 	3,037 	3,644	3,826 	4,017 	4,1378 
Y/Y change 		140.4%	108.0%	101.7%	2.9%	60.0%	40.0%	20.0%	5.0%	5.0%	3.0%
'''
df = pd.DataFrame(data)

# Plot
fig, ax1 = plt.subplots(figsize=(15, 8))

# Revenue line (LEFT axis)
ax1.plot(df['Year'], df['rev'], linewidth=3, color='#CB3133', label='Revenue')
ax1.set_ylabel('Revenue in MM(USD)', fontsize=16, fontweight='bold')

# Remove spines
for spine in ax1.spines.values():
    spine.set_visible(False)

# X-axis formatting
ax1.set_xticks(df['Year'])
plt.xticks(fontsize=16, fontweight='bold')
# plt.xticks(rotation=23, fontsize=12, fontweight='bold')

# highlighting linear reg
ax1.axvline(x=2024, color='gray', linestyle=':', linewidth=2)
ax1.text( 2024 + 0.2, ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.05, 'Forecast →', fontsize=16, fontweight='bold', color='black', va='bottom')

# Change line (RIGHT axis)
ax2 = ax1.twinx()
ax2.plot(df['Year'], df['change'], linewidth=3, color='#231F20', label='Change')
ax2.set_ylabel('Change (%)', fontsize=16, fontweight='bold')

# Tick formatting
ax1.tick_params(axis='y', labelsize=16)
ax2.tick_params(axis='y', labelsize=16)

plt.title('CELH 10  Year Revenue and Y/Y Change - linear regression', fontsize=18, fontweight='bold')

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()

ax1.legend(
    lines_1 + lines_2,
    labels_1 + labels_2,
    loc='upper left',
    bbox_to_anchor=(0.01, 0.7), 
    fontsize=16
)

plt.show()