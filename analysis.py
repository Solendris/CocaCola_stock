import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import normaltest

df = pd.read_csv('cocacola_stock_data.csv')


def analize():
    # Zwroty
    df['return'] = df['close'].pct_change()

    # Histogram
    sns.histplot(df['return'].dropna(), bins=100)
    plt.title("Rozkład dziennych zwrotów")
    plt.show()

    # Test normalności
    stat, p = normaltest(df['return'].dropna())
    print(f'Statystyka: {stat}, p-value: {p}')  # p < 0.05 → rozkład NIE jest normalny
