from json.encoder import ESCAPE_DCT #(перед запуском: env\Scripts\activate)
import requests

def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": "d877d29bec52472e938163851222209",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params)
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try: 
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print("Cтевая ошибка")
        return False
    return False

if __name__ == "__main__":
    w = weather_by_city("Moscow,Russia")
    print(w)

    