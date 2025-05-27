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


# Odchylenie standardowe	Miara zmienności (ryzyka)	df['close'].std()
# Zwroty dzienne (%)	Zmiana ceny dzień do dnia	df['return'] = df['close'].pct_change()
# Wolumen obrotu	Aktywność na rynku	df['volume'].mean()
# Korelacje	Współzależność np. open z close	df.corr()
# Średnie kroczące (MA)	Trendy w czasie	df['MA50'] = df['close'].rolling(50).mean()
# Zmienność (rolling std)	Ruchome odchylenie	df['volatility'] = df['return'].rolling(30).std()
