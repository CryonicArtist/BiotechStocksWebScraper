import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def split_data_by_symbol(file_path):
    """
    Splits a single CSV file containing multiple stock symbols into separate files per symbol.
    """
    raw_data = pd.read_csv(file_path)
    grouped = raw_data.groupby("Symbol")
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    for symbol, group in grouped:
        symbol_file = output_dir / f"{symbol}_data.csv"
        group.to_csv(symbol_file, index=False)
        print(f"Saved data for {symbol} to {symbol_file}")


def calculate_moving_average_per_stock(directory, window=3):
    """
    Calculates the moving average for stock prices for each stock in the processed directory.
    """
    processed_dir = Path(directory)
    for file in processed_dir.glob("*_data.csv"):
        data = pd.read_csv(file)

        # Calculate the moving average
        data['Moving Average'] = data['Price'].rolling(window=window).mean()

        # Save the updated data
        data.to_csv(file, index=False)
        print(f"Updated moving averages for {file.stem}")


def plot_stock_data(directory):
    """
    Generates and saves plots of stock price and moving averages for each stock in the processed directory.
    """
    processed_dir = Path(directory)
    for file in processed_dir.glob("*_data.csv"):
        data = pd.read_csv(file)

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(data['Timestamp'], data['Price'], label='Price', marker='o')
        if 'Moving Average' in data.columns:
            plt.plot(data['Timestamp'], data['Moving Average'], label='Moving Average', linestyle='--')

        # Customize the plot
        plt.title(f"Stock Data: {file.stem.replace('_data', '')}")
        plt.xlabel("Timestamp")
        plt.ylabel("Price")
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()

        # Save the plot
        plot_file = processed_dir / f"{file.stem}_plot.png"
        plt.savefig(plot_file)
        plt.close()
        print(f"Saved plot for {file.stem} to {plot_file}")


def detect_alerts(directory, percentage_threshold=5):
    """
    Detects alerts based on percentage change in stock price between the two most recent entries.
    """
    processed_dir = Path(directory)
    alerts = []

    for file in processed_dir.glob("*_data.csv"):
        data = pd.read_csv(file)
        symbol = file.stem.replace("_data", "")

        # Check if there's enough data for comparison
        if len(data) > 1:
            latest_price = data['Price'].iloc[-1]
            previous_price = data['Price'].iloc[-2]

            # Calculate percentage change
            percentage_change = ((latest_price - previous_price) / previous_price) * 100

            # Trigger alert if percentage change exceeds the threshold
            if abs(percentage_change) > percentage_threshold:
                alerts.append((symbol, latest_price, percentage_change))

    # Print or log alerts
    for symbol, price, change in alerts:
        print(f"ALERT: {symbol} had a {change:.2f}% change! Latest Price: ${price:.2f}")