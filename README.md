# This is a weather forecast package


 Creates a weather object getting an api key as input
    and either a city name or lat and lon coordinates.

    package use example:

    # Create a weather object using a city name:
    # The api key below is not guaranteed to work.
    # Get your own api key from https://openweathermap.org
    # And wait a couple of hours for api key to be activated.

    > weather = Weather(apikey="insert your api here", city="Tallinn")

    # Using latitude and longitude coordinates
    > weather = Weather(apikey="insert your api here", lat=5.3, lon=42.2)

    # Get complete weather data for the next 12 hours:
    > weather.next_12h()

    # Simplified data for the next 12 hours:
    > weather1.next12h_simplified()