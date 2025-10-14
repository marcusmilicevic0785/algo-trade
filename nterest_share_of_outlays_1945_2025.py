import pandas as pd
import matplotlib.pyplot as plt

# --- 📊 US Federal Outlay Data (FY1945 - FY2025E) ---
# Data is annual, Fiscal Year, as a percentage of GDP.
# Source: US Office of Management and Budget (OMB) / FRED (FYONGDA188S, FYOIGDA188S) and CBO projections.
data = {
    'Year': list(range(1945, 2026)),  # 81 years

    # Federal Net Outlays as Percent of GDP (Total Outlays)
    'Total_Outlays_Percent_GDP': [
        44.7, 24.8, 14.2, 11.3, 12.8, 14.6, 13.4, 18.2, 19.4, 18.3, 16.6, 16.1, 16.7, 17.7, 18.7, 17.3,
        17.9, 18.2, 18.0, 17.9, 18.6, 18.3, 19.3, 19.7, 18.7, 19.0, 18.6, 19.0, 18.2, 18.4, 21.0, 21.1,
        20.4, 19.7, 19.8, 20.3, 21.4, 22.3, 22.9, 21.6, 22.2, 22.3, 21.8, 21.2, 21.2, 22.0, 22.4, 22.1,
        21.4, 20.7, 20.4, 19.9, 19.4, 19.4, 18.7, 18.2, 18.2, 19.0, 19.5, 19.7, 19.7, 19.3, 19.1, 20.8,
        24.4, 24.3, 24.0, 22.7, 21.2, 20.3, 20.5, 20.8, 20.6, 20.3, 21.0, 30.6, 28.7, 24.1, 22.1, 23.0,
        23.3
    ],
    # Federal Outlays: Interest as Percent of Gross Domestic Product (Net Interest)
    'Net_Interest_Percent_GDP': [
        1.9, 1.8, 1.3, 1.2, 1.1, 1.1, 1.2, 1.2, 1.3, 1.3, 1.4, 1.5, 1.6, 1.6, 1.6, 1.7,
        1.7, 1.7, 1.6, 1.6, 1.6, 1.5, 1.6, 1.7, 1.8, 1.9, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8,
        1.7, 1.7, 1.7, 1.8, 2.1, 2.4, 2.8, 3.1, 3.2, 3.2, 3.1, 3.1, 3.2, 3.2, 3.1, 2.9,
        2.8, 2.8, 2.7, 2.5, 2.4, 2.3, 2.2, 2.2, 2.0, 1.7, 1.5, 1.6, 1.8, 1.9, 1.8, 1.7,
        1.4, 1.5, 1.5, 1.6, 1.3, 1.3, 1.2, 1.4, 1.5, 1.7, 1.8, 1.6, 1.5, 1.8, 2.4, 3.0, 3.1
    ]
}

df = pd.DataFrame(data)

# 1. Calculate the Ratio: (Net Interest Outlays / Total Outlays) * 100
# This is the "percentage of net gov outlays going to net interest overlays"
df['Interest_Share_of_Outlays'] = (
    df['Net_Interest_Percent_GDP'] / df['Total_Outlays_Percent_GDP']) * 100

# 2. Create the plot
plt.figure(figsize=(12, 6))
plt.plot(df['Year'], df['Interest_Share_of_Outlays'],
         color='#FFD700', linewidth=2, marker='.', markersize=4)


# Add titles and labels
plt.title('Net Interest Outlays as a Percentage of Total Government Outlays (1945–2025E)',
          fontsize=14, pad=15, fontweight='bold')
plt.ylabel('Interest Share of Total Outlays (%)',
           fontsize=14, fontweight='bold')

# Set x-axis ticks to show labels every 5 years for readability
plt.xticks(range(1945, 2030, 10), rotation=0,
           ha='right', fontsize=12, fontweight='bold')
plt.yticks(fontsize=14)

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()
