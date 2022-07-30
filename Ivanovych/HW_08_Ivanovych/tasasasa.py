developer1 = {'Name': 'Aleksandr',  'City': 'Chernitsi', 'Skill': 'Python', 'Rate': 600,'Phone': '+380631234573'}
developer2 = {'Name':'Peter','City': 'Kyiv','Skill': 'Python','Rate': 1800,'Phone': '+380631234567'}
developer3 = {'Name': 'Vlad',  'City': 'Kyiv', 'Skill': 'Python', 'Rate': 1300, 'Phone': '+380631234570'}
developer4 = {'Name': 'Ivan',  'City': 'Kyiv', 'Skill': 'Python', 'Rate': 2800, 'Phone': '+380631234572'}
developer5 = {'Name': 'Alex',  'City': 'Lviv', 'Skill': 'Python', 'Rate': 4800, 'Phone': '+380631234574'}

devs = [developer1, developer2, developer3, developer4, developer5]


def get_rate_stat(developers):
    rates=[]
    stat = {'mean': None,'min': None,'max': None,'item_number': 0}
    for dev in developers:
        rates.append(dev['Rate'])
    stat.update(
          {'mean': sum(rates)/len(rates),
           'max': max(rates),
           'min': min(rates),
           'item_number': len(rates)
          }
         )

    return stat

print(get_rate_stat(devs))
