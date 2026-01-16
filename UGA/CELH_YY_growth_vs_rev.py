import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Data
data = {
    'Year': list(range(2017, 2025)),
    'rev': [36, 53, 75, 131, 314, 654, 1318, 1356],
    'growth': [None, 47.2, 41.5, 74.7, 139.7, 108.3, 101.5, 2.9]
}

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

# Growth line (RIGHT axis)
ax2 = ax1.twinx()
ax2.plot(df['Year'], df['growth'], linewidth=3, color='#231F20', label='Growth')
ax2.set_ylabel('Growth (%)', fontsize=16, fontweight='bold')

# Tick formatting
ax1.tick_params(axis='y', labelsize=16)
ax2.tick_params(axis='y', labelsize=16)

plt.title('CELH Revenue and Growth Over Time', fontsize=18, fontweight='bold')

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()

ax1.legend(
    lines_1 + lines_2,
    labels_1 + labels_2,
    loc='upper left',
    fontsize=16
)

plt.show()
