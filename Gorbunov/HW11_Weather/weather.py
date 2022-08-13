from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from my_api import api

owm = OWM(api)

#owm = OWM('d41d024f8af9c2b95184b1e3fc95de91')
mgr = owm.weather_manager()

#observation = mgr.weather_at_zip_code(input("Enter zip code: "),input("Enter country code.\nExample: UA: "))
#observation = mgr.weather_at_coords(48.9309093,8.6292812) 
observation = mgr.weather_at_place(input("Insert city,country: ")) 
# не вышло )observation = mgr.weather_at_places_in_bbox () 

w=observation.weather

print(f"Wind: {w.wind()}")
print(w.temperature('celsius'))
print(f"Humidity is {w.humidity} %")
print(w.detailed_status)
print(w.rain)
print(f"Cloudy is {w.clouds} %")
print('----------------------')

"""forecast = mgr.forecast_at_place('Milan,IT', 'daily')
answer = forecast.will_be_clear_at(timestamps.tomorrow())

req = mgr.forecast_at_coords(49.8328261,23.8721505,'daily',3)
answer = req.forecast(timestamps.tomorrow())
print(f"The weather at the same time tomorrow will be: {answer}")"""




