#Is it possible to place a round stage with radius R in a square hall of square S so that there is a passage was at least K from the wall to the stage?
#з квадрата вирахувати подвійтий радіус і перевірити з к
# Визначити чи можливо помістити сцену радіусом R у середину хола чи кімнати площою S так щоб залишався прохід між сценою і стіною не менше ніж К
# знайти s кола відняти від площі квадрати і попівняти із К
radius = int(input("Please, input the radius:"))
area_of_square= 2 * pow(radius, 2)
area_of_circle= 3.14 * pow(radius, 2)

print(area_of_square)
print(area_of_circle)
if area_of_square > area_of_circle:
    print('''it is possible to place a round stage in a square hall so that there is a passage was \
        at least K from the wall to the stage?''')
else:
        print('''it isn't possible to place a round stage in a square hall so that there is a \
            passage was at least K from the wall to the stage?''')
