# visualization of proposal effect to debt-to-gdp ratio
import pandas as pd
import matplotlib.pyplot as plt

# 'National Healthcare Transparency Board', 'Affordable Care Act',

# data = {
#     'name': ['CBO Projection', 'Sovereign Wealth Fund', 'Payroll Tax', 'Increasing IRS Funding', 'Financial Transaction Tax', 'Child Tax Credit', 'Student Loan Debt Restructuring', 'National Healthcare Transparency Board', 'Affordable Care Act', 'MID/SALT', 'Expansion of Small Business Association', 'Earned Income Tax Credit', 'Incentivizing Registered Apprenticeships', 'Negotiated Drug Prices'],
#     'debtgdp': [136.832, 128.292, 120.146, 112.316, 106.3, 101.414, 98.4089, 95.9355, 93.7337, 91.9406, 90.1992, 88.5658, 87.6531, 87.9556]
# }
data = {
    'name': ['Negotiated Drug Prices', 'Incentivizing Registered Apprenticeships', 'Earned Income Tax Credit', 'Expansion of Small Business Association', 'MID/SALT', 'Affordable Care Act', 'National Healthcare Transparency Board', 'Child Tax Credit', 'Increasing IRS Funding', 'Payroll Tax', 'Sovereign Wealth Fund', 'Financial Transaction Tax', 'CBO Projection'],
    'debtgdp': [89.8912, 89.5887, 90.404, 92.0374, 93.7788, 95.572, 97.7738, 97.6986, 102.585, 110.414, 118.561, 127.1, 136.832]
}


df = pd.DataFrame(data)
# df = df.sort_values('debtgdp', ascending=True)
# df = df.sort_values('debtgdp')

colors = ['red' if name == 'CBO Projection' else '#1a7a1a' for name in df['name']]

fig, ax = plt.subplots(figsize=(13, 8))

bars = ax.barh(df['name'], df['debtgdp'], color=colors, linewidth=0.5)

# Value labels at end of each bar
for bar, val in zip(bars, df['debtgdp']):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2,
            f'{val}', va='center', ha='left', fontsize=9, fontweight="bold")

ax.set_xlabel('Debt-to-GDP Ratio', fontsize=11, fontweight="bold")
ax.set_xlim(0, df['debtgdp'].max() * 1.08)
ax.tick_params(axis='both', labelsize=10,)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontweight('bold')

plt.title('Debt-to-GDP Ratio Reduction by Policy Proposal',
          fontsize=13, fontweight='normal', pad=15)
plt.tight_layout()
plt.show()
