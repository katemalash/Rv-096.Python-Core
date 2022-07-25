country_cities = {'Ukraine':['kyiv', 'lviv', 'rivne', 'ivano-frankivsk', 'kharkiv'],
                  'Ireland':  ['dublin', 'cork', 'galway', 'limeric', 'waterford'],
                  'Iceland': ['reykjavik', 'kópavogur', 'hafnarfjörður', 'reykjanesbær', 'akureyri'],
                  'Canada': ['halifax', 'edmonton', 'victoria', 'toronto', 'quebec city']}

city_input = input('Enter the city you are interested in: ')
city_input_lower = city_input.lower()
for country, city in country_cities.items():
    for answer_city in city:
        if answer_city == city_input_lower:
            print(f'{city_input_lower.capitalize()} is located in {country}.')
        
    