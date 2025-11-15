import requests
import pandas as pd

# Koordinater för städerna
latitude_st = "59.30"
longitude_st = "18.02"
latitude_gb = "57.70"
longitude_gb = "11.97"
latitude_ma = "59.33"
longitude_ma = "11.07"

städer = {
    "stockholm": {
        "latitude": latitude_st,
        "longitude": longitude_st,
    },
    "göteborg": {
        "latitude": latitude_gb,
        "longitude": longitude_gb,
    },
    "malmö": {
        "latitude": latitude_ma,
        "longitude": longitude_ma,
    },
}


def get_weather_data(city: str) -> dict:
    """Hämtar väderdata från SMHI för given stad."""

    city = city.lower()
    if city not in städer:
        raise ValueError(f"Okänd stad: {city}. Tillåtna: {list(städer.keys())}")

    lat = städer[city]["latitude"]
    lon = städer[city]["longitude"]

    url = (
        "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/"
        f"geotype/point/lon/{lon}/lat/{lat}/data.json"
    )

    # Inga special-headers behövs normalt för SMHI
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()


def create_dict(stad: str) -> pd.DataFrame:
    """Returnerar en DataFrame med tid och temperatur (första 24 timmarna)."""

    data = get_weather_data(stad)
    degree_data = []
    time_data = []

    # Ta bara de första 24 tidsstegen
    for time_point in data.get("timeSeries", [])[:24]:
        for param in time_point.get("parameters", []):
            if param.get("name") == "t":
                time_data.append(time_point["validTime"])
                degree_data.append(param["values"][0])
                break  # klar med denna tidspunkt

    dict_test = {
        "time": time_data,
        "degree": degree_data,
    }

    return pd.DataFrame(dict_test)


if __name__ == "__main__":
    # Testkör bara när filen körs direkt, inte vid import
    print(create_dict(stad="göteborg"))
