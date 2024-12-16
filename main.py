from scraper.scrape_stocks import get_stock_price, save_to_csv
from analysis.trend_analysis import split_data_by_symbol, calculate_moving_average_per_stock

def main():
    # Scrape and save data
    symbols = ["SPY", "VRTX", "IBB"]
    for symbol in symbols:
        price = get_stock_price(symbol)
        if price:
            save_to_csv(symbol, price)
            print(f"Scraped and saved data for {symbol}.")

    # Split data by symbol
    split_data_by_symbol("data/raw/stock_prices.csv")

    # Calculate moving averages
    calculate_moving_average_per_stock("data/processed", window=3)

if __name__ == "__main__":
    main()