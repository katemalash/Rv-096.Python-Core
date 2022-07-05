#Calculate the length of the hypotenuse on the two entered other sides of the right triangle

import math

sides_a = int(input('Enter sides a of the triangle : '))
sides_b = int(input('Enter sides b of the triangle : '))

hypotenuse = math.sqrt(sides_a**2 + sides_b**2)

print("The hypotenus of the triangle is %.2f" %hypotenuse)
