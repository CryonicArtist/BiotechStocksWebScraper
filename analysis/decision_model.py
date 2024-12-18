import pandas as pd

def moving_average_crossover_strategy(data, short_window=3, long_window=5):
    """
    Generates buy/sell signals using a moving average crossover strategy.
    """
    data['Short MA'] = data['Price'].rolling(window=short_window).mean()
    data['Long MA'] = data['Price'].rolling(window=long_window).mean()

    # Generate signals
    data['Signal'] = 0
    data.loc[data['Short MA'] > data['Long MA'], 'Signal'] = 1  # Buy
    data.loc[data['Short MA'] < data['Long MA'], 'Signal'] = -1  # Sell

    return data