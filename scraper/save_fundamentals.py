import requests
from pathlib import Path
import json

def get_fundamental_data(symbol):
    """
    Fetches basic fundamental metrics such as market cap and P/E ratio.
    """
    # Simulated API endpoint for fundamental metrics
    api_url = f"https://api.example.com/fundamentals/{symbol}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()  # Assume JSON format
    else:
        print(f"Failed to fetch fundamentals for {symbol}")
        return None

def save_fundamental_data(symbol, data):
    """
    Saves fundamental data for a stock to a JSON file.
    """
    output_dir = Path("data/fundamentals")
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / f"{symbol}_fundamentals.json"

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Saved fundamental data for {symbol} to {file_path}")