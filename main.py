from scraper.scraper import get_stock_price, save_to_csv
from scraper.save_fundamentals import get_fundamental_data, save_fundamental_data
from analysis.trend_analysis import (
    split_data_by_symbol,
    calculate_moving_average_per_stock,
    plot_stock_data,
    detect_alerts
)
import pandas as pd

def main():
    symbols = ["XBI", "IBB"]  # List of biotech stocks to track

    # 1. Scrape stock prices
    print("--- Scraping Stock Prices ---")
    for symbol in symbols:
        price = get_stock_price(symbol)
        if price:
            save_to_csv(symbol, price)

    # 2. Fetch fundamental metrics
    print("--- Fetching Fundamental Metrics ---")
    for symbol in symbols:
        data = get_fundamental_data(symbol)
        if data:
            save_fundamental_data(symbol, data)

    # 3. Process Data
    print("--- Processing Data ---")
    split_data_by_symbol("data/raw/stock_prices.csv")
    calculate_moving_average_per_stock("data/processed", window=3)

    # 4. Analyze and Plot
    print("--- Analyzing and Plotting ---")
    plot_stock_data("data/processed")
    detect_alerts("data/processed", percentage_threshold=5)

    print("--- Workflow Complete ---")

if __name__ == "__main__":
    main()