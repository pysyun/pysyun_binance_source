# Pysyun Timeline Binance Source

## Overview

The `Pysyun Timeline Binance Source` project is designed to fetch kline (candlestick) data from the Binance cryptocurrency exchange and convert this data into a structured JSON timeline format. This project integrates with the `pysyun_chain` for chainable data processing.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
  - [BinanceKLinesSource](#binanceklincessource)
  - [DataFrameToTimeLine](#dataframetotimeline)
- [Testing](#testing)
- [License](#license)

## Features

- Fetch kline data from Binance API for multiple trading symbols and intervals.
- Convert the kline data into a structured JSON format suitable for timeline visualizations.
- Chainable data processing using `pysyun_chain`.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/pysyun/pysyun_timeline_binance_source.git
    cd pysyun_timeline_binance_source
    ```

2. Install the requirements:
    ```sh
    pip install -r requirements.txt
    ```

3. Additionally, install the package locally:
    ```sh
    pip install -e .
    ```

## Usage

Below is a sample usage of the project:

1. Create a Python script (e.g., `load.py`):

    ```python
    from pysyun_chain import Chainable
    from data_frame_to_time_line import DataFrameToTimeLine
    from klines_source import BinanceKLinesSource

    if __name__ == "__main__":
        symbols = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'SOLUSDT']
        interval = "30m"
    
        for symbol in symbols:
            json_timeline = (Chainable(BinanceKLinesSource(symbol, interval)) | Chainable(DataFrameToTimeLine())).process(symbol)
            print(f"JSON timeline for {symbol}:\n", json_timeline)  # Print first 5 entries for brevity
    ```

2. Run the script:
    ```sh
    python load.py
    ```

## Modules

### BinanceKLinesSource

This module is responsible for fetching kline data from the Binance API. It is instantiated with the trading symbol, kline interval, and the number of klines to fetch per request.

#### Example:
```python
from klines_source import BinanceKLinesSource

binance_source = BinanceKLinesSource(symbol='BTCUSDT', interval='30m')
data = binance_source.fetch_data()
```

### DataFrameToTimeLine

This module processes the pandas DataFrame containing kline data and converts it into an array of JSON objects, where each object includes a 'time' field in UNIX timestamp (milliseconds) and 'value' fields for open, high, low, close, and volume.

#### Example:
```python
from data_frame_to_time_line import DataFrameToTimeLine

converter = DataFrameToTimeLine()
json_timeline = converter.process(data)
```

## Testing

To run the provided tests:
```sh
python tests/load.py
```
