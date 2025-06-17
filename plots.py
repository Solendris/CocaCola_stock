import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib

matplotlib.use('TkAgg')


def plot_monthly_lines(df, years, title, legend_loc, bbox_anchor, tight_rect=None, col=1):
    """Creates a monthly average line plot for selected years"""
    fig, ax = plt.subplots(figsize=(14, 7))
    for year in years:
        monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()
        ax.plot(monthly.index, monthly.values, marker='o', label=str(year))
    ax.set_title(title)
    ax.set_xlabel("Month")
    ax.set_ylabel("Average Adj Close")
    ax.set_xticks(range(1, 13))
    ax.grid(True)
    ax.legend(title="Year", loc=legend_loc, bbox_to_anchor=bbox_anchor, ncol=col)
    fig.tight_layout(rect=tight_rect if tight_rect else None)
    plt.show()


def all_plots():
    df = pd.read_csv('cocacola_stock_data.csv')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['adj_close'] = pd.to_numeric(df['adj_close'], errors='coerce')
    df['Year'] = df['date'].dt.year
    df['Month'] = df['date'].dt.month

    # === High price plot ===
    plt.figure(figsize=(14, 6))
    plt.plot(df['date'], df['high'], label='High')
    plt.title("Stock Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("High Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # === Moving Averages ===
    df['SMA_50'] = df['adj_close'].rolling(window=50).mean()
    df['SMA_200'] = df['adj_close'].rolling(window=200).mean()

    plt.figure(figsize=(14, 6))
    plt.plot(df['date'], df['adj_close'], label='Adj Close', alpha=0.5)
    plt.plot(df['date'], df['SMA_50'], label='SMA 50', color='orange')
    plt.plot(df['date'], df['SMA_200'], label='SMA 200', color='green')
    plt.title("Price and Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # === Correlation matrix ===
    cols = ['open', 'high', 'low', 'close', 'adj_close', 'volume']
    correlation = df[cols].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()

    # === 10 yearly subplots ===
    selected_years = sorted(df['Year'].dropna().unique())[-10:]
    fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(18, 12))
    axes = axes.flatten()
    cmap = cm.get_cmap('tab10')
    colors = [cmap(i) for i in range(cmap.N)]
    i = -1

    for i, year in enumerate(selected_years):
        monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()
        axes[i].plot(monthly.index, monthly.values, marker='o', color=colors[i % len(colors)])
        axes[i].set_title(f"Monthly Avg Price - {year}")
        axes[i].set_xlabel("Month")
        axes[i].set_ylabel("Average Adj Close")
        axes[i].set_xticks(range(1, 13))
        axes[i].grid(True)

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.subplots_adjust(hspace=0.4, wspace=0.4)
    plt.tight_layout()
    plt.show()

    # === 10 years on one plot ===
    plot_monthly_lines(
        df=df,
        years=selected_years,
        title="Monthly Avg Price – Last 10 Years",
        legend_loc='upper left',
        bbox_anchor=(1.02, 1)
    )

    # === All years on one plot ===
    selected_years_all = sorted(df['Year'].dropna().unique())[-63:]
    plot_monthly_lines(
        df=df,
        years=selected_years_all,
        title="Monthly Avg Price – Last 63 Years",
        legend_loc='center left',
        bbox_anchor=(1.01, 0.5),
        tight_rect=(0, 0, 0.75, 1),
        col=2
    )

    # === 3 groups of 21 years ===
    all_years = sorted(df['Year'].dropna().unique())
    chunks = [all_years[i:i + 21] for i in range(0, len(all_years), 21)]
    cmap = plt.get_cmap("viridis")

    for year_group in chunks:
        colors = cmap(np.linspace(0, 1, len(year_group)))
        plt.figure(figsize=(14, 6))
        for i, year in enumerate(year_group):
            monthly = df[df['Year'] == year].groupby('Month')['adj_close'].mean()
            plt.plot(monthly.index, monthly.values, marker='o', label=str(year), color=colors[i])
        plt.title(f"Monthly Avg Price – Years {year_group[0]}–{year_group[-1]}")
        plt.xlabel("Month")
        plt.ylabel("Average Adj Close")
        plt.xticks(range(1, 13))
        plt.grid(True)
        plt.legend(title="Year", loc='center left', bbox_to_anchor=(1.01, 0.5), ncol=1)
        plt.tight_layout(rect=(0, 0, 0.85, 1))
        plt.show()

    # === Rolling Volatility ===
    df['volatility'] = df['adj_close'].rolling(30).std()
    plt.figure(figsize=(14, 6))
    plt.plot(df['date'], df['volatility'], label='30-day Rolling Volatility', color='red')
    plt.title("30-Day Rolling Standard Deviation of Adj Close Price", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Volatility", fontsize=12)
    plt.legend(loc='upper right')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.gca().set_facecolor("white")
    plt.tight_layout()
    plt.show()
