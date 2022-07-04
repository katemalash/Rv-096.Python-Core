import math


first_leg = int(input('Enter the first leg of the triangle: '))
second_leg = int(input('Enter the second leg of the triangle: '))
hypotenuse = math.sqrt(first_leg**2 + pow(second_leg, 2))
print(f'The hypotenuse: {round(hypotenuse, 2)}')
