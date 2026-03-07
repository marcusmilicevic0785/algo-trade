import pandas as pd
import matplotlib.pyplot as plt

data = {
    'year': list(range(2026, 2057)),
    "CBO's Prediction": [99.4453, 101.049, 103.117, 104.821, 106.723, 108.56, 110.508, 112.94, 115.116, 116.887, 119.101, 121.738, 121.364, 122.637, 123.84, 124.978, 126.057, 127.081, 128.054, 128.98, 129.863, 130.705, 131.508, 132.277, 133.012, 133.716, 134.391, 135.038, 135.66, 136.258, 136.832],
    "Our Proposal Prediction": [98.2289, 98.5195, 99.16311, 99.38102, 99.72306, 99.95484, 100.1624, 100.7649, 101.1266, 101.1432, 101.5273, 101.7165, 100.1484, 99.66995, 99.14133, 98.57028, 97.96343, 97.32655, 96.66465, 95.98209, 95.28268, 94.56972, 93.8461, 93.11436, 92.3767, 91.63504, 90.89106, 90.14625, 89.40187, 88.65905, 87.91877]
}

df = pd.DataFrame(data)
categories = {
    "CBO's Prediction": '#e63946',
    "Our Proposal Prediction": '#2a9d8f',
}

fig, ax = plt.subplots(figsize=(15, 8))

for col, color in categories.items():
    ax.plot(df['year'], df[col], linewidth=2.5, color=color, label=col)

# Use numeric year ticks because `year` is an integer column, not datetimes.
ax.set_xticks([2026, 2031, 2036, 2041, 2046, 2051, 2056])
plt.xticks(rotation=0, fontsize=11)

ax.set_xlim(df['year'].min(), df['year'].max())
ax.set_ylim(80, df["CBO's Prediction"].max() * 1.05)
ax.set_ylabel('Percent of GDP', fontsize=12)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))
ax.tick_params(axis='both', labelsize=11, width=1)
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, color='grey', alpha=0.7)
ax.set_axisbelow(True)

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontweight('normal')

plt.title("Fiscal proposal effect compared to cbos projection",
          fontsize=14, fontweight='normal')
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
