n = int(input('Введіть число: '))
print('Введене число:')

if n > 0:
    print('додатнє,')
elif n < 0:
    print('від\'ємне,')
else:
    print('є нулем,')
if abs(n) < 10:
    print('однозначне,')
elif abs(n) >= 10 and abs(n) < 100:
    print('двозначне,')
else:
    print('багатозначне,')
if n%2 == 0 :
    print('парне.')
else:
    print('непарне.')
