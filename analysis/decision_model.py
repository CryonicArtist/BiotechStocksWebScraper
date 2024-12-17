import pandas as pd
import numpy as np

def moving_average_crossover_strategy(data, short_window=10, long_window=50):
    # Calculate short-term and long-term moving averages
    data['Short MA'] = data['Price'].rolling(window=short_window).mean()
    data['Long MA'] = data['Price'].rolling(window=long_window).mean()

    # Generate trading signals
    data['Signal'] = 0
    data['Signal'][short_window:] = np.where(
        data['Short MA'][short_window:] > data['Long MA'][short_window:], 1, -1
    )

    return data