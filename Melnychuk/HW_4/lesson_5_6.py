place_number = int(input('Enter the number of your place: '))
if not 0 < place_number < 55:
    print('Wrong number!')
else:
    if place_number % 2 != 0:
        print('bottom')
    else:
        print('top')

    if place_number <= 36:
        print('compartment') 
    else:
        print('side')