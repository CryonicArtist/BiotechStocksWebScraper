import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_stock_price(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_tag = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
        if price_tag:
            return float(price_tag.text)
    return None

if __name__ == "__main__":
    symbol = "SPY"  
    price = get_stock_price(symbol)
    if price:
        print(f"The current price of {symbol} is ${price}")
    else:
        print(f"Failed to fetch stock price for {symbol}")


def save_to_csv(symbol, price, filename="data/raw/stock_prices.csv"):
    df = pd.DataFrame([{
        "Symbol": symbol,
        "Price": price,
        "Timestamp": datetime.now()
    }])
    df.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))
    print(f"Saved {symbol} price to {filename}")

if __name__ == "__main__":
    symbol = "SPY"
    price = get_stock_price(symbol)
    if price:
        save_to_csv(symbol, price)