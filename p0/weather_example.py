import json
from urllib.parse import urlencode
from urllib.request import urlopen

# Open-Meteo API address
base_url = "https://api.open-meteo.com/v1/forecast"

# Choose the location and weather data to request
params = {
    "latitude": 47.653973,
    "longitude": -122.307396,
    "current": (
        "temperature_2m,relative_humidity_2m,"
        "precipitation,wind_speed_10m"
    ),
    "timezone": "America/Los_Angeles",
}

# Add the parameters to the URL
url = f"{base_url}?{urlencode(params)}"

# Send the request and read the JSON response
with urlopen(url, timeout=10) as response:
    data = json.load(response)

# Get the current weather and its units
current = data["current"]
units = data["current_units"]

# Print the weather information
print(f"Time: {current['time']} ({data['timezone']})")
print(
    f"Temperature: {current['temperature_2m']} "
    f"{units['temperature_2m']}"
)
print(
    f"Humidity: {current['relative_humidity_2m']} "
    f"{units['relative_humidity_2m']}"
)
print(
    f"Precipitation: {current['precipitation']} "
    f"{units['precipitation']}"
)
print(
    f"Wind speed: {current['wind_speed_10m']} "
    f"{units['wind_speed_10m']}"
)
