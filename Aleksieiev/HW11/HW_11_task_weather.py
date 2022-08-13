from api_key import API_KEY
import requests
from datetime import datetime


LANG = "ru"

def get_city_coord(city_name: str):
    '''Convert city_name to geo coors lat & lon'''
    try:
        r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}")
        if not r.ok: raise Exception
        data = r.json()
        lat = data[0]["lat"]
        lon = data[0]["lon"]
    except Exception:
        print("Ошибка в названии или неверное название города!")
        return None
    return (lat, lon)

def get_weather(lat:int, lon: int):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang={LANG}")
        if not response.ok: raise Exception
        data = response.json()
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.fromtimestamp(data["sys"]["sunset"])
        day_long = sunset - sunrise
        temp = f"{data['main']['temp']}˚C"
        windspeed = data["wind"]["speed"]
        humidity = data['main']['humidity']
        clouds = data["clouds"]["all"]
        city_name = data['name']
        country = data['sys']['country']
        сlouds_desc = data["weather"][0]["description"]
    except Exception:
        print("Ошибка в получении данных с сервиса openweathermap.org!")
        return False
    print(f'Погода в городе: {city_name}, Страна: {country}\nТемература: {temp}\nСкорость ветра: {windspeed}м/с\n'
          f'Влажность: {humidity}%, Облачность: {clouds}%, {сlouds_desc}\n'
          f'Восход солнца: {sunrise}\n'
          f'Закат солнца: {sunset}\n'
          f'Продолжительность дня: {day_long}')
    return True

def main():
    while True:
        city = input('Введите город (EN/RU/UA на любом языке) или 0 чтобы выйти: ')
        if city == '0': break
        coords = get_city_coord(city)
        if coords is None: continue
        get_weather(coords[0], coords[1])
        input('========================= PRESS ENTER =========================')
    print('Спасибо, что воспользовались этой программой, отличной погоды!')
if __name__ == '__main__':
    main()