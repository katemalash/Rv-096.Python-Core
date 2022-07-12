number = int(input('Enter number: '))
print('Введене число:')

if number > 0:
    print('додатнє,')
elif number < 0:
    print('від\'ємне,')
else:
    print('є нулем,')
if abs(number) < 10:
    print('однозначне,')
elif abs(number) >= 10 and abs(number) < 100:
    print('двозначне,')
else:
    print('багатозначне,')
if number%2 == 0:
    print ('парне')
else:
    print('непарне.')

