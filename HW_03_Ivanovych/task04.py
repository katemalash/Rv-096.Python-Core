#Calculate the area and perimeter of the circle over an entered radius
import math


radius = int(input('Enter radius of the circle'))

area = math.pi * (radius ** 2)
perimeter = (2 * (math.pi * radius))

print("The area of the circle is %.2f" %area, 'square centimeters.')
print("Perimete of the cirkl is %.2f" %perimeter, 'square centimeters.')
