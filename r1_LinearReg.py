# RIVIAN R1 Deliveries Linear Regression
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression
import numpy as np

# Input your historical deliveries

data = {
    'Quarter': ['2023-Q2', '2023-Q3', '2023-Q4',
                '2024-Q1', '2024-Q2', '2024-Q3', '2024-Q4', '2025-Q1', '2025-Q2', '2025-Q3', '2025-Q4', '2026-Q1', '2026-Q2', '2026-Q3', '2026-Q4'],
    'Deliveries_R1': [12640, 15564, 13472, 13588, 13790, 10018, 14183, 8640, 10661, 13201, None, None, None, None, None]
}

df = pd.DataFrame(data)

# Prepare regression
# Create numeric time index
df['t'] = np.arange(1, len(df) + 1)

# Keep only rows with known deliveries (no NaN)
mask_known = df['Deliveries_R1'].notna()
X = df.loc[mask_known, 't'].values.reshape(-1, 1)
y = df.loc[mask_known, 'Deliveries_R1'].values

# Fit linear regression
model = LinearRegression().fit(X, y)

# Predict for all quarters (known + forecast)
df['Predicted'] = model.predict(df['t'].values.reshape(-1, 1))

# Plot
plt.figure(figsize=(11, 6))

# Actual deliveries
plt.plot(df.loc[mask_known, 'Quarter'], df.loc[mask_known, 'Deliveries_R1'],
         marker='o', linewidth=2.5, color='#FFD700', label='Actual Deliveries')

# Regression forecast line
plt.plot(df['Quarter'], df['Predicted'],
         linestyle='--', linewidth=2.2, color='#004225', label='Linear Forecast')

# Highlight forecasted section
plt.axvline(x='2025-Q2', color='gray', linestyle=':', linewidth=2)
plt.text(8.5, df['Deliveries_R1'].max()*0.95,
         'Forecast →', color='black', fontsize=12)

# Titles & labels
plt.title('Rivian R1 Deliveries - Linear Regression Forecast',
          fontsize=12, weight='bold')
# plt.xlabel('Quarter', fontsize=16, weight='bold')
plt.ylabel('Deliveries (Units)', fontsize=16, weight='bold')
plt.xticks(rotation=23, fontsize=10, fontweight='bold')
plt.legend(fontsize=13)
plt.tight_layout()

# Display equation
coef = model.coef_[0]
intercept = model.intercept_
plt.text(0.02, 0.9, f'y = {coef:.2f}x + {intercept:.0f}',
         transform=plt.gca().transAxes, fontsize=12, color='black')
plt.text(0.02, 0.1, f"R² Score: {model.score(X, y):.4f}", transform=plt.gca(
).transAxes, fontsize=12, color='black')


plt.show()
