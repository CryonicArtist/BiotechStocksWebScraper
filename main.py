from scraper.scrape_stocks import get_stock_price, save_to_csv
from analysis.trend_analysis import (
    split_data_by_symbol,
    calculate_moving_average_per_stock,
    plot_stock_data,
    detect_alerts,
)
from analysis.decision_model import moving_average_crossover_strategy
from scraper.save_fundamentals import get_fundamental_data, save_fundamental_data
import pandas as pd

def main():
    """
    Main workflow to scrape stock data, process it, analyze trends,
    plot results, generate alerts, and save fundamental data.
    """
    print("=== Starting Biotech Stock Analysis Workflow ===")
    
    # 1. Scrape and Save Stock Data
    print("\n--- Scraping Stock Prices ---")
    symbols = ["SPY", "VRTX", "IBB"]  # List of stock symbols to monitor
    for symbol in symbols:
        price = get_stock_price(symbol)
        if price:
            save_to_csv(symbol, price)
            print(f"Scraped and saved data for {symbol}.")
        else:
            print(f"Failed to fetch data for {symbol}. Check the scraper.")

    # 2. Fetch and Save Fundamental Data
    print("\n--- Fetching Fundamental Metrics ---")
    for symbol in symbols:
        fundamentals = get_fundamental_data(symbol)
        save_fundamental_data(symbol, fundamentals)

    # 3. Process Raw Data: Split by Symbol
    print("\n--- Processing Raw Stock Data ---")
    raw_data_path = "data/raw/stock_prices.csv"
    split_data_by_symbol(raw_data_path)

    # 4. Calculate Moving Averages
    print("\n--- Calculating Moving Averages ---")
    processed_data_dir = "data/processed"
    calculate_moving_average_per_stock(processed_data_dir, window=3)

    # 5. Plot Stock Data
    print("\n--- Generating Plots ---")
    plot_stock_data(processed_data_dir)

    # 6. Detect Alerts
    print("\n--- Detecting Price Change Alerts ---")
    detect_alerts(processed_data_dir, percentage_threshold=5)

    # 7. Apply Decision-Making Model
    print("\n--- Applying Decision Model ---")
    for symbol in symbols:
        data_file = f"data/processed/{symbol}_data.csv"
        data = pd.read_csv(data_file)
        
        # Apply a simple moving average crossover strategy
        decision_data = moving_average_crossover_strategy(data, short_window=3, long_window=5)
        
        # Show signal column (buy/sell)
        print(f"\nSignals for {symbol}:")
        print(decision_data[['Timestamp', 'Price', 'Short MA', 'Long MA', 'Signal']].tail())

    print("\n=== Workflow Complete! ===")

if __name__ == "__main__":
    main()