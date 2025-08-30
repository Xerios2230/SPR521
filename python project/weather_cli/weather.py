import requests

APPID = "40cb2f1fbd9a8b8a1fbad5c3261cc88d"
URL = "http://api.openweathermap.org/data/2.5/weather"

try:
    q = input("Введіть назву міста: ")
    ask_units = int(input("Виберіть 1 - metric;  2 - imperial: "))
    units = None
    match ask_units:
        case 1:
            units = "metric"
        case 2:
            units = "imperial"

    params = {
        "q": q,
        "appid": APPID,
        "units": units,
        "lang": "eng"
    }

    response = requests.get(URL, params=params)
    data = response.json()

    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    print(f"--- Місто: {city}, {country}")
    print(f"--- Температура: {temp}")
    print(f"--- Вологість: {humidity}")
    print(f"--- Вітер: {wind}")
    print(f"--- Погода: {description}")

except requests.exceptions.HTTPError as http_err:
    print("**HTTP error**")
except requests.exceptions.RequestException as req_err:
    print("**Conection error**")
except ValueError as val_err:
    print("**ValueError**")
except Exception as e:
    print("**Error**")