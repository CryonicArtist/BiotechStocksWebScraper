import pandas as pd

def calculate_moving_average(filename, window=3):
    data = pd.read_csv(filename)
    data['Moving Average'] = data['Price'].rolling(window=window).mean()
    return data

if __name__ == "__main__":
    data = calculate_moving_average("data/raw/stock_prices.csv")
    print(data.tail())