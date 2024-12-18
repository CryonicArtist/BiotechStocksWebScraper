import requests
import csv
from datetime import datetime
from pathlib import Path

# Replace YOUR_API_KEY with your valid key
API_KEY = "YOUR_API_KEY"

def get_stock_price(symbol):
    """
    Fetches the latest stock price for a given symbol using Alpha Vantage API.
    """
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            price = float(data["Global Quote"]["05. price"])
            return price
        except (KeyError, ValueError):
            print(f"Error: Could not extract price for {symbol}.")
            return None
    else:
        print(f"Failed to fetch data for {symbol}. HTTP Status: {response.status_code}")
        return None

def save_to_csv(symbol, price):
    """
    Saves the stock price and timestamp to a CSV file.
    """
    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / "stock_prices.csv"

    timestamp = datetime.now()
    data = [symbol, price, timestamp]

    # Append data to the file
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Symbol", "Price", "Timestamp"])  # Write header
        writer.writerow(data)