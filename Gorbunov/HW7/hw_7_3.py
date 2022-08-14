countries = {'Ukraine':['Kyiv', 'Kyiv','Harkiv', 'Dnipro', 'Lviv'],\
    'USA':['Los Angeles', 'New York', 'Chicago','Washington'],\
    'Poland':['Warshava', 'Krakiw', 'Katovice', 'Gdansk'],\
    'Turkey':['Side', 'Antalia', 'Alanya','Kemer','Marmaris','Fetfie', 'Bodrum','Istanbul', 'Ankara']}
city = str.capitalize(input("Enter city: "))
#if (isinstance(v,list) and city in v)or city==v
for k, v in countries.items():
    if city in v :
        print(f'{city} is in {k}')
        break
else: print(f'Can not find "{city}".')