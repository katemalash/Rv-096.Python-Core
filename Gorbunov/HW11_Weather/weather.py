from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from datetime import datetime, tzinfo
#from pytz import datetime as dt
from my_api import api_

<<<<<<< HEAD

owm = OWM("d41d024f8af9c"+api_)
=======
owm = OWM("d41d024f8af9c2b"+api)
>>>>>>> 33e4af2f471b897ed3855a69e91bf098acda7b05

#owm = OWM('d41d024f8af9c2b95184b1e3fc95de91')
mgr = owm.weather_manager()

#observation = mgr.weather_at_zip_code(input("Enter zip code: "),input("Enter country code.\nExample: UA: "))
#observation = mgr.weather_at_coords(48.9309093,8.6292812) 
# не вышло )observation = mgr.weather_at_places_in_bbox () 

observation = mgr.weather_at_place(input("Insert city: "))
w=observation.weather

country = observation.location.__dict__['country']
city = observation.location.__dict__['name']
user_local_request_time = float(observation.__dict__['rec_time'])

def time_convert(float):
    #utc =datetime.utcfromtimestamp(int).strftime('%d.%m.%Y is %H:%M:%S')  возвращает время с 0:00 UTC
    utc = datetime.fromtimestamp(float)   # возвращает местное время
    return utc

def as_time_zone():
    t=datetime.astimezone(timezone.utc)
    return t
    pass

print()
print(f"Your local request time:  {time_convert(user_local_request_time)}")
print(f"Weather in {city}, {country}:")
print(f"Temperature:   {round(w.temp['temp']-273.15,1)} C*   |   Feels like {round(w.temp['feels_like']-273.15,1)} C*")
print(f"Wind speed:    {w.wnd['speed']} m/s.")
print(f"Humidity:      {w.humidity} %")

if w.status =="Clouds":
    print(f"{w.status} about {w.clouds}%. {str.capitalize(w.detailed_status)}.")  #статус может быть дождь.есть вопросы
elif w.status =="Rain":
    print(f"{w.status} with {w.rain['1h']*100} % chance. {str.capitalize(w.detailed_status)}.")
else:
    pass

print(f"Visibility distance: {w.visibility_distance/1000} km.")
print(f"Sunrise time:  {time_convert(w.sunrise_time())}")
#print(f"Sunrise time: {w.sunrise_time(timeformat='iso')}")
print(f"Sunset time:   {time_convert(w.sunset_time())}")
print()
print('-----------------------------------------------------')

"""dt = datetime.fromtimestamp(w.sunset_time())
print(dt.tzname())
new_dt = dt.astimezone()
new_dt.tzname()
print(new_dt.tzname())"""
# ниже принт __dict__
"""print('-----------------------------------------------------')

print("tzinfo.__doc__   --- ",tzinfo.__doc__)
print()
print("owm.__dict__   --- ",owm.__dict__)
print()
print("w.__dict__   --- ",w.__dict__)
print()
print("observation.__dict__  --- ",observation.__dict__)
print(w.temperature('celsius'))
print(w.detailed_status)
print(w.rain)
print('--------')
print("observation.location.__dict__  --- ",observation.location.__dict__)
"""
# ниже не разобрался
"""forecast = mgr.forecast_at_place('Milan,IT', 'daily')
answer = forecast.will_be_clear_at(timestamps.tomorrow())

req = mgr.forecast_at_coords(49.8328261,23.8721505,'daily',3)
answer = req.forecast(timestamps.tomorrow())
print(f"The weather at the same time tomorrow will be: {answer}")"""




