import requests

# url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api}&units=imperial"
# r = requests.get(url)
# print(r.json())
api = "b757238a027a9ba7413a3786589d37f2"


class Weather:

    def __init__(self, apikey, city, lat=None, lon=None):
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units=imperial"
        r = requests.get(url)
        self.data = r.json()

    def next_12h(self):
        return self.data

    def next_12h_simplified(self):
        pass


weather = Weather(apikey="b757238a027a9ba7413a3786589d37f2", city="Valencia")
print(weather.data)
print(weather.next_12h())