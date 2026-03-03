import pandas as pd
import matplotlib.pyplot as plt

data = {
    'year': list(range(2025, 2057)),
    "CBO's Prediction": [97.42831, 99.4453, 101.049, 103.117, 104.821, 106.723, 108.56, 110.508, 112.94, 115.116, 116.887, 119.101, 121.738, 121.364, 122.637, 123.84, 124.978, 126.057, 127.081, 128.054, 128.98, 129.863, 130.705, 131.508, 132.277, 133.012, 133.716, 134.391, 135.038, 135.66, 136.258, 136.832],
    "Our Proposal Prediction": [97.42831, 97.64208, 97.39429, 97.54395, 97.31055, 97.23192, 97.07756, 96.92032, 97.16981, 97.21401, 96.95493, 97.06715, 96.89972, 95.24311, 94.57802, 93.88072, 93.11857, 92.33912, 91.54654, 90.74439, 89.93574, 89.13998, 88.34126, 87.5416, 86.7427, 85.94296, 85.147, 84.35585, 83.57039, 82.79138, 82.01943, 81.25508]
}

df = pd.DataFrame(data)
categories = {
    "CBO's Prediction": '#e63946',
    "Our Proposal Prediction": '#2a9d8f',
}

fig, ax = plt.subplots(figsize=(15, 8))

for col, color in categories.items():
    ax.plot(df['year'], df[col], linewidth=2.5, color=color, label=col)

ax.set_xlim(df['year'].min(), df['year'].max())
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
