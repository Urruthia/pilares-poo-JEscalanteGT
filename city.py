import requests
from datetime import datetime
from temperature import Temperature


class City:
    def __init__(self,
                 name: str,
                 latitude: float,
                 longitude: float):
        self.__name = name
        self.__latitude = latitude
        self.__longitude = longitude
        self.__temperatures: list(Temperature) = []
        self.__get_temperatures()

    def show(self):

        print(self.__name)
        print('Temperatura promedio: ')
        print('Listado de temperaturas:')
        for index, temperature in enumerate(self.__get_temperatures()):
            print(f'{index} {str(temperature.show())}')

    def __get_temperatures(self):
        response = requests.get(
            url='https://api.open-meteo.com/v1/forecast',
            params={
                "latitude": self.__latitude,
                "longitude": self.__longitude,
                "hourly": "temperature_2m",
                "forecast_days": 1
            }
        ).json()
        times: list[str] = response['hourly']['time']
        temperatures_2m: list[float] = response['hourly']['temperature_2m']

        temperatures: list[Temperature] = []

        for index, time in enumerate(times):
            print(index, time)
            measure = temperatures_2m[index]
            new_date = datetime.strptime(time, '%Y-%m-$dT%H:%M')
            temperature = Temperature(measure, new_date)
            temperatures.append(temperature)
