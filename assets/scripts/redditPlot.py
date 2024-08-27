import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Date': ['2011-12-04', '2013-07-23', '2015-06-30', '2018-08-28', '2021-09-07', '2021-04-24', '2022-10-01', '2023-06-26', '2024-03-17'],
    'Subscribers': [46, 132, 225, 833, 5800, 5100, 7500, 8600, 10000]
}

# Convert to DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Subscribers'], marker='o', linestyle='-', color='b')
plt.title('Subscribers Growth for r/Baruch')
plt.xlabel('Date')
plt.ylabel('Subscribers')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
