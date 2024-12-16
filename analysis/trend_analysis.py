import pandas as pd
from pathlib import Path

def split_data_by_symbol(filename):
    # Load the dataset
    data = pd.read_csv(filename)

    # Create a directory for separated data if it doesn't exist
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Group data by 'Symbol' and save each group to a separate file
    for symbol, group in data.groupby('Symbol'):
        symbol_file = output_dir / f"{symbol}_data.csv"
        group.to_csv(symbol_file, index=False)
        print(f"Saved data for {symbol} to {symbol_file}")

if __name__ == "__main__":
    split_data_by_symbol("data/raw/stock_prices.csv")
    
def calculate_moving_average_per_stock(directory, window=3):
    processed_dir = Path(directory)
    for file in processed_dir.glob("*_data.csv"):
        data = pd.read_csv(file)
        data['Moving Average'] = data['Price'].rolling(window=window).mean()

        # Save the updated data back to the same file
        data.to_csv(file, index=False)
        print(f"Updated moving average for {file.name}")

if __name__ == "__main__":
    calculate_moving_average_per_stock("data/processed", window=3)