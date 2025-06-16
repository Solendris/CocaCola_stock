import pandas as pd
df = pd.read_csv('cocacola_stock_data.csv')


def analize():
    # Średnie wartości
    open_mean = df['open'].mean()
    print(f"Opening price mean: {open_mean:.2f}")
    close_mean = df['close'].mean()
    print(f"Closing price mean:{close_mean:.2f}")
    adj_close_mean = df['adj_close'].mean()
    print(f"Adjusted closing price mean: {adj_close_mean:.2f}")
    # Odchylenie standardowe
    standard_deviation_price = df['adj_close'].std()
    print(f"Standard deviation for adjusted closing price: {standard_deviation_price:.2f}")
    standard_deviation_volume = df['adj_close'].std()
    print(f"Standard deviation for volume: {standard_deviation_volume:.2f}")
    # Zwroty dzienne(średni %)
    daily_returns_pct = df['adj_close'].pct_change()
    daily_returns_mean = daily_returns_pct.mean()
    print(f"Daily return % mean for volume: {daily_returns_mean:.2f}")
    # Wolumen obrotu
    volume_mean = df['volume'].mean()
    print(f"Daily volume mean: {volume_mean:.0f}")
    # Korelacje
    close_adjclose_corr = df['adj_close'].corr(df['adj_close'], method='pearson')
    print(f"Corelation: {close_adjclose_corr}")
