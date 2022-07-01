'''Aleksieiev Valentyn
30/07/2022 HomeWork#3, Task#5
Calculate the length of the hypotenuse on the two entered other sides of the right triangle.
'''
from cheker import variable_check
from math import pi

hypotenuse_calc = lambda a, b: (a**2 + b**2) ** 0.5

a, b = variable_check(float, 2, 'Input triangle side')

print(f'The hypotenuse in triangle whith side a: {a}, b: {b} = : \033[1m{round(hypotenuse_calc(a, b), 4)}\033[0m')



