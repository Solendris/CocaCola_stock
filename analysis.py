import pandas as pd
df = pd.read_csv('cocacola_stock_data.csv')


def analise():
    """Performs basic statistical analysis on stock data."""

    # Mean prices
    print(f"Opening price mean: {df['open'].mean():.2f}")
    print(f"Closing price mean: {df['close'].mean():.2f}")
    print(f"Adjusted closing price mean: {df['adj_close'].mean():.2f}")

    # Standard deviations
    print(f"Standard deviation for adjusted closing price: {df['adj_close'].std():.2f}")
    print(f"Standard deviation for volume: {df['volume'].std():.2f}")

    # Daily return (%)
    daily_returns_pct = df['adj_close'].pct_change()
    print(f"Daily return % mean: {daily_returns_pct.mean():.2%}")

    # Volume
    print(f"Average daily volume: {df['volume'].mean():.0f}")

    # Correlation
    correlation = df['close'].corr(df['adj_close'], method='pearson')
    print(f"Correlation between close and adj_close: {correlation:.2f}")
