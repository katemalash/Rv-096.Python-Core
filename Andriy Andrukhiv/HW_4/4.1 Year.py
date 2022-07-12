year = int(input('Enter year: '))
century = year // 100

if(century%100 != 0):
    print (str(century) + 'century.')
else:
    print ()
if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print('Not Intercalary')
    else:
        print('Intercalary')
else:
    print('Not Intercalary')

