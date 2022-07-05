import math


radius = int(input('Enter the radius of the circle: '))
circle_area = math.pi * radius**2
circle_perimeter = 2 * math.pi * radius
print(f'The area of the circle: {round(circle_area, 2)} \nThe perimeter of the circle: {round(circle_perimeter, 2)}')