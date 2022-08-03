'''Aleksieiev Valentyn
02/08/2022 HomeWork#10, Task#2
Task
Simulate the “Fishing” game.
Create the next classes:
Pond. It should have the next attributes: capacity – list that contains all fish from the Pond in the current moment;
state – ‘poor’, ‘normal’, ‘rich’. Pond is ‘poor’ if it’s capacity contains less then 5 fishes, ‘normal’,
if capacity contains from 5 to 10 fishes, and ‘rich’ if it has more than 10 fishes.
Pond can obtainFish() – it will be added to it’s capacity, and lostFish() – it will be taken from capacity.
The Pond state changes automatically when it’s capacity reaches the appropriate value. Pond also allows showPapacity()
and showState(). You can also add the optional attributes (as you wish).
Задача
Смоделируйте игру «Рыбалка».
Создайте следующие классы:
Пруд. Он должен иметь следующие атрибуты: вместимость – список, содержащий всю рыбу из пруда на текущий момент;
состояние – «бедное», «нормальное», «богатое». Пруд считается «бедным», если в нем содержится менее 5 рыб, «нормальным»,
если вместимость от 5 до 10 рыб, и «богатым», если в нем более 10 рыб. Пруд может получитьРыбу() — она будет добавлена
​​в его емкость, а потеряннаяРыба() — будет взята из емкости. Состояние пруда изменяется автоматически, когда
его вместимость достигает соответствующего значения. Pond также поддерживает функции showPapacity() и showState().
Вы также можете добавить дополнительные атрибуты (по вашему желанию).
User should have interactive menu:
1. View capacity;
2. View state of Pond;
3. Add fish(Carp or SheatFish);
4. Catch fish (concrete instance);
5. Create new fish (fill himself the creator)))
6. Finish the game.'''

from fish_classes import Fish, Carp, SheatFish, Pond
from cheker import variable_check
#from pprint import pprint

fish01 = Fish()
fish02 = Fish(15, 2)
fish03 = SheatFish(10, 12)
fish04 = SheatFish(8, 10)
fish05 = Carp(color='gold')
fish06 = Carp(color='black')

new_pound = Pond([fish01, fish02, fish03, fish04, fish05, fish06])
# print(new_pound)
while True:
    print('======================================================')
    print('''1. View capacity
2. View state of Pond
3. Add fish(Carp or SheatFish)
4. Catch fish (concrete instance)
5. Create new fish (fill himself the creator)))
6. Finish the game.''')
    match input('Input your choice: '):
        case '1':
            print('\033[41m1. View capacity\033[0m'); print(new_pound)
        case '2':
            print('\033[41m2. View state of Pond\033[0m')
            print(f'Pound state = {new_pound.state}. There are {len(new_pound.capacity)} fishes.')
        case '3':
            print('\033[41m3. Add fish(Carp or SheatFish)\033[0m')
            match variable_check(str, 1, 'Input 1 to add Carp fish or 2 to add SheatFish'):
                case '1':
                    new_pound.capacity.append(Carp(color='white'))
                    print(f'The wish was added to pound: {Carp(color="white")}')
                case '2':
                    new_pound.capacity.append(SheatFish(8, 10))
                    print(f'The wish was added to pound: {SheatFish(8, 10)}')
                case _: print('Please input only 1 or 2 to add new wish!')
        case '4':
            print('\033[41m4. Catch fish (concrete instance)\033[0m')
            index = variable_check(int, 1, 'Input index of fish to delete')
            print(new_pound.cath_fish(index))
        case '5':
            print('\033[41m5. Create new fish (fill himself the creator)))\033[0m')
            weight, age = variable_check(float, 2, 'Input weight-#1(0.1-30kg) float add age-#2(0.1-10 years) float to create new fish')
            name = variable_check(str, 1, 'Input your own fish name:')
            fish_new = Fish.create_from_data(weight, age)
            fish_new.__dict__['name'] = name
            new_pound.capacity.append(fish_new)
            print(f'New fish was added: {fish_new}')
        case '6':
            print('\033[41m6. Finish the game.\033[0m'); break
        case _: print("Your input something wrong :("); continue
    print('======================================================')
    input('\033[40m            PRES ENTER TO CONTINUE                    \033[0m')

print('\033[40m THANK YOU FOR PLAY MY GAME :) HAVE A NICE DAY!\033[0m')