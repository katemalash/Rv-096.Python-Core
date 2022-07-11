year = input('Enter the year: ')
if not year.isdigit():
    print('Not all characters you entered are digits.') 
elif int(year) < 1:
    print('The century is not defined. Enter the number grater than equals to 1.')
else:
    year = int(year)
    century = int(year/100) + 1
    print(f'The century of such year is {century}.')
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f'{year} year is intercalary.')
    else:
        print(f'{year} year is not intercalary.')