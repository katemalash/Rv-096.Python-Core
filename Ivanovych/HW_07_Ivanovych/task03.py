countries_cites = {"Ukraine": ["Kiev", "Kharkiv", "Dnipro", "Lviv"], "USA": ["Los Angeles", "New-York", "Washington"],
                   "China": ["Shanghai", "Beijing", "Guangzhou"], "Norway": ["Oslo", "Bergen", "Trondheim"]}
user_city = input("Enter your city: ")

for i in countries_cites:
    if user_city in countries_cites[i]:
        print(f"Coutry: {i}")
        break
