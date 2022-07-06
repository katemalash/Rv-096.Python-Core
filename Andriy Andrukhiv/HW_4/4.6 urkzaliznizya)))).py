place = int(input('Enter your place: '))

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