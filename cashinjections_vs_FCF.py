import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': ['2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030'],
    'cash_injections': [],
    'fcf_millions': [1658, 4434, 4969, 5013, 5567, 7816, 9708, 11151, 12113]
}

df = pd.DataFrame(data)
