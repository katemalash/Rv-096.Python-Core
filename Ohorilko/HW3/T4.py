# Calculate the area and perimeter of the circle over an entered radius. area = 3.14*r*r, perimeter 2*3.14*r

radius = int(input("Please enter the radius of the circle (in centimeters): "))
area = 3.14 * pow(radius, 2)
perimeter = 2*3.14*radius
print("The area is " , end='')
print(area, end='')
print (" centimeters squared")

print("The perimeter is " , end='')
print(perimeter, end='')
print (" centimeters")