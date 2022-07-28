'''Aleksieiev Valentyn
22/07/2022 HomeWork#7, Task#3
Create a dictionary with the keys of which are the countries and the values ​​of which are a list of the major cities of that country.
When user enters the city, the program should display the country in which it is located
'''

countries = ['Ukraine', 'USA', 'Germany']
cities = [['Kyiv', 'Kharkiv', 'Odessa', 'Dnipro'],
          ['New York', 'Washington', 'Los Angeles', 'Boston'],
          ['Berlin', 'Bonn', 'Munich', 'Stutgard']]
c_dict = (dict(zip(countries, cities)))
print('Dict of the cities and countries:', c_dict)

while True:
    city = input('Input name of the city or 0 to exit: ').title()
    if city == '0': break
    check = False
    for countrie, cities_ in c_dict.items():
        if city in cities_:
            print(f'The city {city} is in the {countrie}.')
            check = True
    if not check:
        print('No such city in the dictionary :(')
            
    

        