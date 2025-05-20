# Downloading files from Kaggle (default location: C:\Users\<user name>>\.cache\kagglehub\datasets
# import kagglehub
#
# # Download latest version
# path = kagglehub.dataset_download("muhammadatiflatif/coca-cola-stock-data-over-100-years-of-trading")
#
# print("Path to dataset files:", path)
#######################################################################################################################

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
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
#############################################################################

# Wyodrębnienie roku i miesiąca
df['Year'] = df['date'].dt.year
df['Month'] = df['date'].dt.month
df['adj_close'] = pd.to_numeric(df['adj_close'], errors='coerce')

# Wybierz 10 lat z danymi (np. najnowsze)
selected_years = sorted(df['Year'].dropna().unique())[-10:]

# Przygotowanie subplotów
fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(16, 18))
axes = axes.flatten()

# Tworzenie wykresów dla każdego roku
for i, year in enumerate(selected_years):
    ax = axes[i]

    # Grupowanie po miesiącach danego roku
    monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()

    ax.plot(monthly.index, monthly.values, marker='o')
    ax.set_title(f"Średnia cena miesięczna - {year}")
    ax.set_xlabel("Miesiąc")
    ax.set_ylabel("Średnia Adj Close")
    ax.set_xticks(range(1, 13))
    ax.grid(True)

# Usunięcie pustych wykresów
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Wybierz 10 ostatnich lat
selected_years = sorted(df['Year'].dropna().unique())[-10:]

# Przygotowanie wykresu
plt.figure(figsize=(14, 7))

# Pętla po latach – jedna linia dla każdego roku
for year in selected_years:
    monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()
    plt.plot(monthly.index, monthly.values, marker='o', label=str(year))

# Oś i legenda
plt.title("Średnia miesięczna cena akcji – 10 lat na jednym wykresie")
plt.xlabel("Miesiąc")
plt.ylabel("Średnia Adj Close")
plt.xticks(range(1, 13))
plt.grid(True)
plt.legend(title="Rok", loc='upper left', bbox_to_anchor=(1.02, 1))
plt.tight_layout()
plt.show()

#tym razem wykres dla wszystkich lat

# Wybierz 10 ostatnich lat
selected_years = sorted(df['Year'].dropna().unique())[-63:]

# Przygotowanie wykresu
plt.figure(figsize=(14, 7))

# Pętla po latach – jedna linia dla każdego roku
for year in selected_years:
    monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()
    plt.plot(monthly.index, monthly.values, marker='o', label=str(year))

# Oś i legenda
plt.title("Średnia miesięczna cena akcji – 63 lat na jednym wykresie")
plt.xlabel("Miesiąc")
plt.ylabel("Średnia Adj Close")
plt.xticks(range(1, 13))
plt.grid(True)
plt.legend(title="Rok", loc='center left', bbox_to_anchor=(1.01, 0.5), ncol=2, borderaxespad=0)
plt.tight_layout(rect=(0, 0, 0.75, 1))
plt.show()

# Lista lat
all_years = sorted(df['Year'].dropna().unique())
chunks = [all_years[i:i + 21] for i in range(0, len(all_years), 21)]  # 3 grupy po 21 lat

# Kolory do powtarzania
colors = plt.cm.viridis(np.linspace(0, 1, 21))

# Tworzenie 3 wykresów
for idx, year_group in enumerate(chunks):
    plt.figure(figsize=(14, 6))

    for i, year in enumerate(year_group):
        monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()
        plt.plot(monthly.index, monthly.values, marker='o', label=str(year), color=colors[i])

    plt.title(f"Średnia miesięczna cena akcji – lata {year_group[0]}–{year_group[-1]}")
    plt.xlabel("Miesiąc")
    plt.ylabel("Średnia Adj Close")
    plt.xticks(range(1, 13))
    plt.grid(True)
    plt.legend(title="Rok", loc='center left', bbox_to_anchor=(1.01, 0.5), ncol=1)
    plt.tight_layout(rect=(0, 0, 0.85, 1))  # zostaw miejsce na legendę
    plt.show()

###########################################################################################
