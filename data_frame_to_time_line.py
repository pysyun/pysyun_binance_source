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
