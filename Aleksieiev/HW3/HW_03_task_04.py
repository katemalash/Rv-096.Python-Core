'''Aleksieiev Valentyn
30/07/2022 HomeWork#3, Task#4
Calculate the area and perimeter of the circle over an entered radius.
'''
from cheker import variable_check
from math import pi

perimeter_circle = lambda r: 2 * r * pi
area_circle = lambda r: r * r * pi

r = variable_check(float, 1, 'Input radius')

print(f'Perimeter of the circle with radius r = {r}: \033[1m{round(perimeter_circle(r), 4)}\033[0m')
print(f'Area of the circle with radius r = {r}: \033[1m{round(area_circle(r), 4)}\033[0m')


