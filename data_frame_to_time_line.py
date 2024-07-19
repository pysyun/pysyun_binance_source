class DataFrameToTimeLine:

    def process(self, data):
        """
        Convert the DataFrame into an array of JSON objects with 'time' and 'value' fields.

        :return: List of JSON objects
        """
        results = []
        for index, row in data.iterrows():
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
            results.append(json_obj)

        return results
