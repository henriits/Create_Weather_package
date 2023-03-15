import requests


class Weather:
    def __init__(self, city=None, lat=None, lon=None, apikey=None):
        if not apikey:
            raise ValueError("API key not provided")

        try:
            if city:
                url = f"https://api.openweathermap.org/data/2.5/forecast?" \
                      f"q={city}" \
                      f"&APPID={apikey}" \
                      f"&units=metric"
                r = requests.get(url)
                r.raise_for_status()
                self.data = r.json()
            elif lat and lon:
                url = f"https://api.openweathermap.org/data/2.5/forecast?" \
                      f"lat={lat}&" \
                      f"lon={lon}&" \
                      f"APPID={apikey}" \
                      f"&units=imperial"
                r = requests.get(url)
                r.raise_for_status()
                self.data = r.json()
            else:
                raise TypeError("Provide either a city or lat and lon arguments")
        except requests.exceptions.RequestException as e:
            raise SystemExit(f"Error in URL \n {e}")

    def next_12h(self):
        return self.data["list"][:4]

    def next_12h_simplified(self):
        """returns date, temperature, sky"""
        simple_data = []
        for dicty in self.data["list"][:4]:
            simple_data.append((dicty["dt_txt"],
                                dicty["main"]["temp"],
                                dicty["weather"][0]["description"]))
        return simple_data


weather = Weather(apikey="b757238a027a9ba7413a3786589d37f2", city="Twadawddnn")
print(weather.next_12h_simplified())
