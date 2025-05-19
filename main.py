# Downloading files from Kaggle (default location: C:\Users\<user name>>\.cache\kagglehub\datasets
# import kagglehub
#
# # Download latest version
# path = kagglehub.dataset_download("muhammadatiflatif/coca-cola-stock-data-over-100-years-of-trading")
#
# print("Path to dataset files:", path)
#######################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')


df = pd.read_csv('cocacola_stock_data.csv')
# print(df.head(10))
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# === 6. Wykres ceny w czasie (matplotlib) ===
plt.figure(figsize=(14, 6))
plt.plot(df['date'], df['high'], label='high')
plt.title("Cena akcji w czasie (Matplotlib)")
plt.xlabel("Date")
plt.ylabel("Cena najwyzsza")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

df['SMA_50'] = df['close'].rolling(window=50).mean()
df['EMA_200'] = df['close'].ewm(span=200).mean()

# === 8. Wykres średnich ruchomych ===
plt.figure(figsize=(14, 6))
plt.plot(df['date'], df['adj_close'], label='Adj Close', alpha=0.5)
plt.plot(df['date'], df['SMA_50'], label='SMA 50', color='orange')
plt.plot(df['date'], df['EMA_200'], label='EMA 200', color='green')
plt.title("Cena i średnie ruchome")
plt.xlabel("Data")
plt.ylabel("Cena")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# === 11. Korelacja między zmiennymi ===
cols = ['open', 'high', 'low', 'close', 'adj_close', 'volume']
correlation = df[cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Macierz korelacji")
plt.tight_layout()
plt.show()
