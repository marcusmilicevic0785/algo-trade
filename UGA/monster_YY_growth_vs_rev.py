import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Data
data = {
    'Year': list(range(2014, 2025)),
    'rev': [2464, 2722, 3049, 3369, 3807, 4201, 4599, 5541, 6311, 7140, 7493],
    'growth': [None, 10.5, 12.0, 10.5, 13.0, 10.3, 9.5, 20.5, 13.9, 13.1, 4.9]
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

plt.title('Monsters Revenue and Growth Over Time', fontsize=18, fontweight='bold')

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()

ax1.legend(
    lines_1 + lines_2,
    labels_1 + labels_2,
    loc='upper left',
    fontsize=16
)

plt.show()
