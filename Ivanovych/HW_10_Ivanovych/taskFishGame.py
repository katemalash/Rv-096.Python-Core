from class_fish import*
from class_pond import*


print('''It's a fish game. If you are ready, please choose the number:
1. View capacity
2. View state of the pond
3. Add the fish(carp or CatFish)
4. Catch the fish
5. Create a new fish
6. To finish this game ''')

user = Pond()
fish1 = UserFish('Salmon', 5, 2)
listFish = [fish1]

while True:
    inputUser = int(input('>> '))

    if inputUser == 1:
        user.showCapacity()
    elif inputUser == 2:
        user.showState()
    elif inputUser == 3:
        inputFish = input('Carp or CatFish or your own? ')
        if inputFish == 'Carp':
            inputFish == Carp()
            user.obtainFish(inputFish)
        elif inputFish == 'CatFish':
            inputFish == CatFish()
            user.obtainFish(inputFish)
        else:
            print(listFish)
            choice = int(input('Enter the number of the fish: '))
            user.obtainFish(listFish[choice - 1])
            listFish.pop(choice - 1)
    elif inputUser == 4:
        user.showCapacity()
        inputFish = int(input('Enter number: '))
        user.lostFish(inputFish-1)
    elif inputUser == 5:
        name = input('Enter the name of your fish: ')
        size = input('Enter the size of your fish: ')
        weight = input('Enter the weight of your fish: ')
        userFish = UserFish(name, size, weight)
        listFish.append(userFish)
    elif inputUser == 6:
        print('End of the game')
        break
