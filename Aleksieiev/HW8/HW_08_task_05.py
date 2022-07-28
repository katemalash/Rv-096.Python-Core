'''Aleksieiev Valentyn
26/07/2022 HomeWork#8, Task#4
Create the function is_year_leap, that takes 1 argument - year,
and returns True if the year is high, and False otherwise. 
'''
from cheker import variable_check


is_year_leap = lambda year: not (2000-year)%4 and 3000 > year >= 0
    
while True:
    year = variable_check(int, 1, 'Year to calc it is leap or not: ')
    print(is_year_leap(year))
    print('============CALCULATION FINISH============')
    if input('Press enter to validate new year "0" to exit: ') == '0': break
    
print('Thanks for testing my function is_year_leap! Have a nice day:)')