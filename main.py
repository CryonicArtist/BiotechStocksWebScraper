from scraper.scrape_stocks import get_stock_price, save_to_csv
from analysis.trend_analysis import calculate_moving_average

def main():
    symbol = "IBB"
    price = get_stock_price(symbol)
    if price:
        save_to_csv(symbol, price)
        print("Scraped and saved data successfully.")

        # Analyze trends
        data = calculate_moving_average("data/raw/stock_prices.csv")
        print("Latest data with moving average:")
        print(data.tail())

if __name__ == "__main__":
    main()