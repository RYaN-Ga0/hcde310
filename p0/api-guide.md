# Open-Meteo: A Small Weather API Guide

## What it is and why a designer might care

Open-Meteo is a weather API that returns weather information as JSON, including temperature, humidity, precipitation, and wind speed. A designer could use it to build an interface that helps people make everyday decisions—for example, helping UW students decide whether to walk or bike to campus and whether to bring rain gear. The free API does not require an API key for non-commercial projects. [Official documentation](https://open-meteo.com/en/docs)

## Setup

This example uses Python's built-in libraries, so there is no extra package to install.

1. Make sure Python is installed.
2. Save the code below as `weather_example.py`.
3. Run it from a terminal with `python weather_example.py`.
4. An internet connection is needed because the script requests live data from Open-Meteo.

No API key or account is needed for this non-commercial example.

## One working example

The script asks Open-Meteo for current weather near the University of Washington and prints a few fields from the JSON response.

```python
import json
from urllib.parse import urlencode
from urllib.request import urlopen

base_url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 47.653973,
    "longitude": -122.307396,
    "current": (
        "temperature_2m,relative_humidity_2m,"
        "precipitation,wind_speed_10m"
    ),
    "timezone": "America/Los_Angeles",
}

url = f"{base_url}?{urlencode(params)}"

with urlopen(url, timeout=10) as response:
    data = json.load(response)

current = data["current"]
units = data["current_units"]

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
```

### Output

**Run the script yourself and paste the output from your terminal here.** The values and timestamp change as the API updates, so the output on your computer may be different.

Example of the output format:

```text
Time: [time returned by the API] (America/Los_Angeles)
Temperature: [value] °C
Humidity: [value] %
Precipitation: [value] mm
Wind speed: [value] km/h
```

## How the code works

1. `params` contains the location, weather variables, and timezone to request.
2. `urlencode(params)` turns those options into URL query parameters.
3. `urlopen()` sends the request, and `json.load()` reads the JSON response into a Python dictionary.
4. `data["current"]` gets the current-weather fields, while `data["current_units"]` provides the matching units.
5. The `print()` statements show only the values that are useful for this small example.

## Gotchas

- **No API key for this use:** The free API is for non-commercial use. Open-Meteo lists limits of fewer than 10,000 calls per day, 5,000 per hour, and 600 per minute. See the [terms](https://open-meteo.com/en/terms).
- **Check variable names:** API parameter names must match the documentation exactly. A misspelling can cause an error response.
- **Timezones matter:** If the timezone is not specified, the API defaults to GMT. This example requests `America/Los_Angeles` so the timestamp is easier to interpret in Seattle.
- **Forecasts are not guarantees:** Weather data may be inaccurate for a specific street or building, and current conditions are model-based data rather than a promise of exactly what someone will experience.

## Design angle

**Project idea:** A campus commute helper could show temperature, rain, and wind before a student walks or bikes to class, making it easier to decide what to wear or bring.

**Ethical / UX consideration:** The interface should show the update time and units, explain that forecasts can be wrong, and avoid making users think a prediction is certain. It should also credit Open-Meteo as required by its data license.

## AI use note

AI helped draft and explain this guide. **Before submitting, run the code yourself, check that it works on your computer, and replace the output template above with the actual output from your run.** Only after doing that, update this note to confirm that you ran the code sample yourself.
