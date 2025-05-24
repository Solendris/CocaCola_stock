import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


def plot_monthly_lines(df, years, title, legend_loc, bbox_anchor, tight_rect=None, ncol=1):
    """Tworzy wykres miesięcznych średnich dla podanych lat"""
    fig, ax = plt.subplots(figsize=(14, 7))
    for year in years:
        monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()
        ax.plot(monthly.index, monthly.values, marker='o', label=str(year))
    ax.set_title(title)
    ax.set_xlabel("Miesiąc")
    ax.set_ylabel("Średnia Adj Close")
    ax.set_xticks(range(1, 13))
    ax.grid(True)
    ax.legend(title="Rok", loc=legend_loc, bbox_to_anchor=bbox_anchor, ncol=ncol)
    if tight_rect:
        fig.tight_layout(rect=tight_rect)
    else:
        fig.tight_layout()
    plt.show()


def all_plots():
    df = pd.read_csv('cocacola_stock_data.csv')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['adj_close'] = pd.to_numeric(df['adj_close'], errors='coerce')
    df['Year'] = df['date'].dt.year
    df['Month'] = df['date'].dt.month

    # === 1. Wykres ceny HIGH ===
    plt.figure(figsize=(14, 6))
    plt.plot(df['date'], df['high'], label='high')
    plt.title("Cena akcji w czasie (Matplotlib)")
    plt.xlabel("Date")
    plt.ylabel("Cena najwyższa")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # === 2. Średnie ruchome ===
    df['SMA_50'] = df['close'].rolling(window=50).mean()
    df['EMA_200'] = df['close'].ewm(span=200).mean()

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

    # === 3. Korelacja ===
    cols = ['open', 'high', 'low', 'close', 'adj_close', 'volume']
    correlation = df[cols].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Macierz korelacji")
    plt.tight_layout()
    plt.show()

    # === 4. 10 sub-wykresów rocznych ===
    selected_years = sorted(df['Year'].dropna().unique())[-10:]
    fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(16, 18))
    axes = axes.flatten()
    for i, year in enumerate(selected_years):
        monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()
        axes[i].plot(monthly.index, monthly.values, marker='o')
        axes[i].set_title(f"Średnia cena miesięczna - {year}")
        axes[i].set_xlabel("Miesiąc")
        axes[i].set_ylabel("Średnia Adj Close")
        axes[i].set_xticks(range(1, 13))
        axes[i].grid(True)
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    plt.tight_layout()
    plt.show()

    # === 5. 10 lat na jednym wykresie ===
    plot_monthly_lines(
        df=df,
        years=selected_years,
        title="Średnia miesięczna cena akcji – 10 lat na jednym wykresie",
        legend_loc='upper left',
        bbox_anchor=(1.02, 1)
    )

    # === 6. 63 lata na jednym wykresie ===
    selected_years_all = sorted(df['Year'].dropna().unique())[-63:]
    plot_monthly_lines(
        df=df,
        years=selected_years_all,
        title="Średnia miesięczna cena akcji – 63 lat na jednym wykresie",
        legend_loc='center left',
        bbox_anchor=(1.01, 0.5),
        tight_rect=(0, 0, 0.75, 1),
        ncol=2
    )

    # === 7–9. 3 grupy po 21 lat ===
    all_years = sorted(df['Year'].dropna().unique())
    chunks = [all_years[i:i + 21] for i in range(0, len(all_years), 21)]
    cmap = plt.get_cmap("viridis")

    for year_group in chunks:
        colors = cmap(np.linspace(0, 1, len(year_group)))
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
        plt.tight_layout(rect=(0, 0, 0.85, 1))
        plt.show()
