from main import BinanceKLinesSource, DataFrameToTimeLine

if __name__ == "__main__":
    symbols = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'SOLUSDT']
    interval = "30m"

    for symbol in symbols:
        binance_klines_source = BinanceKLinesSource(symbol, interval)
        data = binance_klines_source.process()
        print(f"Fetched data for {symbol}:\n", data.head())

        dataframe_to_timeline = DataFrameToTimeLine(data)
        json_timeline = dataframe_to_timeline.convert()
        print(f"JSON timeline for {symbol}:\n", json_timeline[:5])  # Print first 5 entries for brevity
