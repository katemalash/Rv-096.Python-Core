map = {"Ukraine":["Kyiv", "Lviv", "Dnipro", "Kharkiv", "Odesa"],
       "USA":["Chicago", "New York", "Los Angeles", "Houston", "Phoenix"], 
       "Poland":["Warsaw", "Krakow", "Lodz", " Poznan", " Gdansk"],
       "United Kingdom":["London", "Manchester", "Newcastle", "Newport", "Bristol"],
       "Germany":["Berlin", "Hamburg", "Munich", "Frankfurt", "Dusseldorf"]
       }


user_input = input(f"Enter the city of Ukraine, USA, Paland, United Kingdom or Germany: ")
for key, values in map.items():
    if user_input in values:
        print(f"The country in which {user_input} is located is {key}")
        break
else:
    print(f"input is wrong or the city is not added to the country")
