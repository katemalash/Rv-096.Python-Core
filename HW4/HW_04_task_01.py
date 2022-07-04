'''Aleksieiev Valentyn
04/07/2022 HomeWork#4, Task#1
The YEAR is known. Determine whether this year is intercalary and to what century this year belongs
'''
from cheker import variable_check

year_check = variable_check(int, 1, 'Input year to calculate in')
def get_intercalary(year):
    s = 'intercalary'
    return ('not ' + s, s)[not year % 4]

print(f'The {year_check} year is {get_intercalary(year_check)} and this is a {year_check//100 + 1} century.')
