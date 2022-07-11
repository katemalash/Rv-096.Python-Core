place = int(input('Enter your place: '))
language = input('Ukrainian or English?(U - E): ')

if language == 'E' or 'e':
    if place<=36 and place%2 :
        print (f'Your place '+str(place)+ ' this is lower  place in coup! ')
    elif place<=36 and place != place/2:
        print (f'Your place is '+str(place)+ ' this is upper place in coup! ')
    else:
        print()
    if place>36 and place<=54 and place%2:
        print (f'Your place '+str(place)+ ' this is lower place in lateral! ')
    elif place>36 and place<=54 and place != place/2:
        print (f'Your place is '+str(place)+ ' this is upper in lateral! ')
    if place > 54:
        print (f'Place missing.')
    else:
        print ()
if language == 'U' or 'u':
    if place<=36 and place%2 :
        print (f'Ваше місце'+str(place)+ ' це нижнє місце в купе! ')
    elif place<=36 and place != place/2:
        print (f'Ваше місце '+str(place)+ ' це є верхнє місце в купе! ')
    else:
        print()
    if place>36 and place<=54 and place%2:
        print (f'Ваше місце '+str(place)+ ' це є нижнє місце, бокове! ')
    elif place>36 and place<=54 and place != place/2:
        print (f'Ваше місце '+str(place)+ ' це є верхнє місце, бокове! ')
    if place > 54:
        print (f'Такого місця не має.')
    else:
        print ()