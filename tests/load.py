from pysyun_chain import Chainable

from data_frame_to_time_line import DataFrameToTimeLine
from klines_source import BinanceKLinesSource

if __name__ == "__main__":
    symbols = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'SOLUSDT']
    interval = "30m"

    for symbol in symbols:
        json_timeline = (Chainable(BinanceKLinesSource(symbol, interval)) | Chainable(DataFrameToTimeLine())).process(
            symbol)
        print(f"JSON timeline for {symbol}:\n", json_timeline[:5])  # Print first 5 entries for brevity
