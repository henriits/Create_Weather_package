import requests


class Weather:
    """
    Creates a weather object getting an api key as input
    and either a city name or lat and lon coordinates.

    package use example:

    # Create a weather object using a city name:
    # The api key below is not guaranteed to work.
    # Get your own api key from https://openweathermap.org
    # And wait a couple of hours for api key to be activated.

    > weather = Weather(apikey="b757238a027a9ba7413a3786589d37f2", city="Tallinn")

    # Using latitude and longitude coordinates
    > weather = Weather(apikey="b757238a027a9ba7413a3786589d37f2", lat=5.3, lon=42.2)

    # Get complete weather data for the next 12 hours:
    > weather.next_12h()

    # Simplified data for the next 12 hours:
    > weather1.next12h_simplified()

    """

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


weather = Weather(apikey="b757238a027a9ba7413a3786589d37f2", lat=5.3, lon=42.2)
print(weather.next_12h_simplified())
