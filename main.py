import requests
import pandas as pd


class BinanceKLinesSource:
    def __init__(self, symbol, interval, limit=1000):
        """
        Initialize the BinanceKLinesSource class

        :param symbol: Trading symbol (e.g., 'BTCUSDT')
        :param interval: Kline interval (e.g., '30m')
        :param limit: Number of klines to fetch per request (default: 1000)
        """
        self.symbol = symbol
        self.interval = interval
        self.limit = limit
        self.base_url = "https://api.binance.com/api/v3/klines"
        self.last_time = None

    def fetch_data(self):
        """
        Fetch klines data from Binance API

        :return: DataFrame containing kline data
        """
        url = f"{self.base_url}?symbol={self.symbol}&interval={self.interval}&limit={self.limit}"
        if self.last_time:
            url += f"&endTime={self.last_time}"

        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        data = response.json()
        if not data:
            return pd.DataFrame()  # Return empty DataFrame if no data

        self.last_time = data[0][0]  # Update last_time with the opening time of the fetched data
        return self._to_dataframe(data)

    def _to_dataframe(self, data):
        """
        Convert raw kline data into a pandas DataFrame

        :param data: Raw kline data
        :return: DataFrame containing processed kline data
        """
        df = pd.DataFrame(data, columns=[
            'Open time', 'Open', 'High', 'Low', 'Close', 'Volume',
            'Close time', 'Quote asset volume', 'Number of trades',
            'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'
        ])
        df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
        df['Close time'] = pd.to_datetime(df['Close time'], unit='ms')
        df = df[['Open time', 'Open', 'High', 'Low', 'Close', 'Volume']]

        # Convert columns to numeric values
        df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
        df['High'] = pd.to_numeric(df['High'], errors='coerce')
        df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
        df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
        df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')
        df = df.rename(columns={
            'Open time': 'time',
            'Open': 'open',
            'High': 'high',
            'Low': 'low',
            'Close': 'close',
            'Volume': 'volume'
        })

        return df

    def process(self):
        """
        Perform a single iteration of fetching data from the Binance API

        :return: DataFrame containing fetched kline data
        """
        return self.fetch_data()


class DataFrameToTimeLine:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def convert(self):
        """
        Convert the DataFrame into an array of JSON objects with 'time' and 'value' fields.

        :return: List of JSON objects
        """
        json_array = []
        for index, row in self.dataframe.iterrows():
            json_obj = {
                "time": row["time"],
                "value": {
                    "open": row["open"],
                    "high": row["high"],
                    "low": row["low"],
                    "close": row["close"],
                    "volume": row["volume"]
                }
            }
            json_array.append(json_obj)

        return json_array

