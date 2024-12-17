import pandas as pd
from pathlib import Path

def get_fundamental_data(symbol):
    # Simulated fundamental data; replace with API integration or scraping
    return {"P/E Ratio": 35.5, "Market Cap": "250B"}

def save_fundamental_data(symbol, data):
    file_path = Path("data/fundamentals") / f"{symbol}_fundamentals.csv"
    file_path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame([data])
    df.to_csv(file_path, index=False)
    print(f"Saved fundamentals for {symbol} to {file_path}")