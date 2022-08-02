# Create a dictionary with the keys of which are the countries
#  and the values ​​of which are a list of the major cities of that country.
#  When user enters the city, the program should display the country in which it is located


countries_cities = {"Ukraine": ["Kyiv", "Kharkov", "Dnepr", "Lviv","Odesa"],"USA":["New York",
"Los Angeles","Chicago","Houston","Phoenix","Philadelphia"],"France": ["Paris","Marselle",
"Lyon","Toulouse","Nice","Nantes"]}

search_city=input("Enter interesting city ")

for country,city in countries_cities.items():
    for i in city:
        if i == search_city:
            print (f"{search_city} is lockated in {country} ")
