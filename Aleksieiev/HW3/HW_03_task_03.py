'''Aleksieiev Valentyn
30/07/2022 HomeWork#3, Task#3
Calculate the area and perimeter of the rectangle for an entered width and height.
'''
from cheker import variable_check

perimeter_calc = lambda a, b: a * 2 + b * 2
area_calc = lambda a, b: a * b

a, b = variable_check(float, 2, 'Input rectangle side')

print(f'Perimeter of rectangle with side a = {a}, side b = {b}: \033[1m{perimeter_calc(a, b)}\033[0m')
print(f'Area of rectangle with side a = {a}, side b = {b}: \033[1m{area_calc(a, b)}\033[0m')


