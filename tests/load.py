from main import BinanceKLinesSource

if __name__ == "__main__":
    symbols = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'SOLUSDT']
    interval = "30m"

    for symbol in symbols:
        binance_klines_source = BinanceKLinesSource(symbol, interval)
        data = binance_klines_source.process()
        print(f"Fetched data for {symbol}:\n", data.head())

