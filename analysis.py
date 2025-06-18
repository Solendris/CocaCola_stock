import pandas as pd
import os
import json
df = pd.read_csv('cocacola_stock_data.csv')
os.makedirs("analysis", exist_ok=True)


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

    # === Save analysis results ===
    results = {
        "open_mean": round(df['open'].mean(), 2),
        "close_mean": round(df['close'].mean(), 2),
        "adj_close_mean": round(df['adj_close'].mean(), 2),
        "std_adj_close": round(df['adj_close'].std(), 2),
        "std_volume": round(df['volume'].std(), 2),
        "daily_return_mean_pct": round(df['adj_close'].pct_change().mean() * 100, 2),
        "volume_mean": round(df['volume'].mean(), 0),
        "close_adj_corr": round(df['close'].corr(df['adj_close']), 2)
    }

    with open("analysis/results.json", "w") as f:
        json.dump(results, f, indent=4)
