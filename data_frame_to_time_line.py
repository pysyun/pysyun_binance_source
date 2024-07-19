class DataFrameToTimeLine:

    def process(self, data):
        """
        Convert the DataFrame into an array of JSON objects with 'time' in UNIX timestamp (milliseconds)
        and 'value' fields.

        :return: List of JSON objects
        """
        results = []
        for index, row in data.iterrows():
            unix_time_ms = int(row["time"].timestamp() * 1000)  # Convert time to UNIX timestamp in milliseconds
            json_obj = {
                "time": unix_time_ms,
                "value": {
                    "open": row["open"],
                    "high": row["high"],
                    "low": row["low"],
                    "close": row["close"],
                    "volume": row["volume"]
                }
            }
            results.append(json_obj)

        return results
