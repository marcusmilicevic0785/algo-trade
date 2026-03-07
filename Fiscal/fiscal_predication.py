import pandas as pd
import matplotlib.pyplot as plt

data = {
    'year': list(range(2026, 2057)),
    "CBO's Prediction": [99.4453, 101.049, 103.117, 104.821, 106.723, 108.56, 110.508, 112.94, 115.116, 116.887, 119.101, 121.738, 121.364, 122.637, 123.84, 124.978, 126.057, 127.081, 128.054, 128.98, 129.863, 130.705, 131.508, 132.277, 133.012, 133.716, 134.391, 135.038, 135.66, 136.258, 136.832],
    "Our Proposal Prediction": [98.2289, 98.72642, 99.47177, 99.78839, 100.227, 100.5521, 100.8538, 101.5496, 101.9993, 102.0971, 102.5618, 102.8569, 101.3344, 100.9235, 100.4588, 99.94808, 99.39823, 98.81513, 98.20393, 97.56913, 96.91468, 96.24402, 95.56017, 94.86579, 94.1632, 93.45445, 92.74133, 92.02542, 91.30809, 90.59057, 89.87392]
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
