import pandas as pd
from pprint import pprint as pp


class Weather:

    def __init__(self):
        self.weather_records = pd.read_csv('data.csv').to_dict(orient='records')
        self.temperatures = []
        self.lowest_temp = 0

    def find_lowest_temp(self):
        """
        Finds lowest reported temperature

        :arg:
            self.weather_records (dict): recorded temperature data

        :returns:
            info about the lowest recorded temperature
        """

        for record in self.weather_records:
            self.temperatures.append(record['temperature_c'])

        self.lowest_temp = min(self.temperatures)

        return next(entry for entry in self.weather_records if entry['temperature_c'] == self.lowest_temp)


if __name__ == '__main__':
    test = Weather()

    lowest_temp = test.find_lowest_temp()
    print(lowest_temp)
