# federal outlays linear regression of 20yr for CBO's 10yr projection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

data = {
    'year': list(range(2025, 2057)),
    'mandatory': [4168, 4529, 4783, 5005, 5067, 5375, 5582, 5835, 6277, 6437, 6545, 7028, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    'discretionary': [1872, 1880, 1882, 1929, 1948, 1989, 2024, 2063, 2111, 2147, 2187, 2244, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    'net_interest':  [970,  1039, 1108, 1218, 1324, 1432, 1548, 1670, 1784, 1904, 2019, 2144, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
}

df = pd.DataFrame(data)
df['t'] = np.arange(1, len(df) + 1)

categories = {
    'mandatory':     '#0073e6',
    'discretionary': '#e63946',
    'net_interest':  '#2a9d8f'
}

fig, ax = plt.subplots(figsize=(15, 8))

all_pred_max = 0

for col, color in categories.items():
    mask_known = df[col].notna()
    X = df.loc[mask_known, 't'].values.reshape(-1, 1)
    y = df.loc[mask_known, col].values

    model = LinearRegression().fit(X, y)
    df[f'{col}_pred'] = model.predict(df['t'].values.reshape(-1, 1))
    all_pred_max = max(all_pred_max, df[f'{col}_pred'].max())

    # Single continuous line: actual values where known, predicted where not
    df[f'{col}_plot'] = df[col].combine_first(df[f'{col}_pred'])

    ax.plot(df['year'], df[f'{col}_plot'],
            linewidth=2.5, color=color, label=col.replace('_', ' ').title())

# Divider line between actual and forecast
# last_known_year = df.loc[df['mandatory'].notna(), 'year'].max()
# ax.axvline(x=last_known_year, color='gray', linestyle=':', linewidth=1.5)
# ax.text(last_known_year + 0.2, all_pred_max * 0.98,
#         'Forecast →', fontsize=11, color='gray')

# Axes — use predicted max to ensure everything fits
ax.set_xlim(df['year'].min(), df['year'].max())
ax.set_ylim(0, all_pred_max * 1.1)
ax.set_ylabel('Billions of Dollars', fontsize=12)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))
ax.tick_params(axis='both', labelsize=11, width=1)
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, color='grey', alpha=0.7)
ax.set_axisbelow(True)

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontweight('normal')

plt.title("Federal Outlays - CBO's projections",
          fontsize=14, fontweight='normal')
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
