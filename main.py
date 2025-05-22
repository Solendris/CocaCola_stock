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
import numpy as np
import matplotlib
matplotlib.use("TkAgg")

# --- Wczytanie danych ---
df = pd.read_csv('cocacola_stock_data.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['Year'] = df['date'].dt.year
df['Month'] = df['date'].dt.month
df['adj_close'] = pd.to_numeric(df['adj_close'], errors='coerce')

# === PRZYGOTUJEMY LISTĘ FIGUR ===
figures = []

# === 1. Cena w czasie (high) ===
fig1, ax1 = plt.subplots(figsize=(14, 6))
ax1.plot(df['date'], df['high'], label='high')
ax1.set_title("Cena akcji w czasie (Matplotlib)")
ax1.set_xlabel("Date")
ax1.set_ylabel("Cena najwyższa")
ax1.legend()
ax1.grid(True)
figures.append(fig1)

# === 2. Średnie ruchome ===
df['SMA_50'] = df['close'].rolling(window=50).mean()
df['EMA_200'] = df['close'].ewm(span=200).mean()

fig2, ax2 = plt.subplots(figsize=(14, 6))
ax2.plot(df['date'], df['adj_close'], label='Adj Close', alpha=0.5)
ax2.plot(df['date'], df['SMA_50'], label='SMA 50', color='orange')
ax2.plot(df['date'], df['EMA_200'], label='EMA 200', color='green')
ax2.set_title("Cena i średnie ruchome")
ax2.set_xlabel("Data")
ax2.set_ylabel("Cena")
ax2.legend()
ax2.grid(True)
figures.append(fig2)

# === 3. Korelacja ===
fig3, ax3 = plt.subplots(figsize=(10, 8))
cols = ['open', 'high', 'low', 'close', 'adj_close', 'volume']
correlation = df[cols].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", ax=ax3)
ax3.set_title("Macierz korelacji")
figures.append(fig3)

# === 4. 10 wykresów miesięcznych (jako subploty) ===
selected_years = sorted(df['Year'].dropna().unique())[-10:]
fig4, axes4 = plt.subplots(nrows=5, ncols=2, figsize=(16, 18))
axes4 = axes4.flatten()
for i, year in enumerate(selected_years):
    monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()
    axes4[i].plot(monthly.index, monthly.values, marker='o')
    axes4[i].set_title(f"Średnia cena miesięczna - {year}")
    axes4[i].set_xlabel("Miesiąc")
    axes4[i].set_ylabel("Średnia Adj Close")
    axes4[i].set_xticks(range(1, 13))
    axes4[i].grid(True)
for j in range(i + 1, len(axes4)):
    fig4.delaxes(axes4[j])
figures.append(fig4)

# === 5. 10 lat na jednym wykresie ===
fig5, ax5 = plt.subplots(figsize=(14, 7))
for year in selected_years:
    monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()
    ax5.plot(monthly.index, monthly.values, marker='o', label=str(year))
ax5.set_title("Średnia miesięczna cena akcji – 10 lat na jednym wykresie")
ax5.set_xlabel("Miesiąc")
ax5.set_ylabel("Średnia Adj Close")
ax5.set_xticks(range(1, 13))
ax5.grid(True)
ax5.legend(title="Rok", loc='upper left', bbox_to_anchor=(1.02, 1))
fig5.tight_layout()
figures.append(fig5)

# === 6. 63 lata na jednym wykresie ===
selected_years_all = sorted(df['Year'].dropna().unique())[-63:]
fig6, ax6 = plt.subplots(figsize=(14, 7))
for year in selected_years_all:
    monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()
    ax6.plot(monthly.index, monthly.values, marker='o', label=str(year))
ax6.set_title("Średnia miesięczna cena akcji – 63 lat na jednym wykresie")
ax6.set_xlabel("Miesiąc")
ax6.set_ylabel("Średnia Adj Close")
ax6.set_xticks(range(1, 13))
ax6.grid(True)
ax6.legend(title="Rok", loc='center left', bbox_to_anchor=(1.01, 0.5), ncol=2)
fig6.tight_layout(rect=(0, 0, 0.75, 1))
figures.append(fig6)

# === 7–9. 3 grupy po 21 lat ===
all_years = sorted(df['Year'].dropna().unique())
chunks = [all_years[i:i + 21] for i in range(0, len(all_years), 21)]
colors = plt.cm.viridis(np.linspace(0, 1, 21))

for year_group in chunks:
    fig, ax = plt.subplots(figsize=(14, 6))
    for i, year in enumerate(year_group):
        monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()
        ax.plot(monthly.index, monthly.values, marker='o', label=str(year), color=colors[i])
    ax.set_title(f"Średnia miesięczna cena akcji – lata {year_group[0]}–{year_group[-1]}")
    ax.set_xlabel("Miesiąc")
    ax.set_ylabel("Średnia Adj Close")
    ax.set_xticks(range(1, 13))
    ax.grid(True)
    ax.legend(title="Rok", loc='center left', bbox_to_anchor=(1.01, 0.5), ncol=1)
    fig.tight_layout(rect=(0, 0, 0.85, 1))
    figures.append(fig)

# === INTERAKTYWNA NAWIGACJA STRZAŁKAMI ===
current = [0]


def show_current():
    fig = figures[current[0]]
    fig.canvas.manager.set_window_title(f"Wykres {current[0] + 1} z {len(figures)}")
    plt.show()


def on_key(event):
    if event.key == 'right':
        current[0] = (current[0] + 1) % len(figures)
        plt.close('all')
        show_current()
    elif event.key == 'left':
        current[0] = (current[0] - 1) % len(figures)
        plt.close('all')
        show_current()


# Podłącz klawiaturę do pierwszej figury
figures[0].canvas.mpl_connect('key_press_event', on_key)
show_current()
