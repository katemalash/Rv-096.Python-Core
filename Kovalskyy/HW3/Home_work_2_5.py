from math import sqrt

side_a = float(input("Enter side_a value: "))
side_b = float(input("Enter side_b value: "))

hypotenuse = sqrt(side_a**2 + side_b**2)

print("The hypotenuse of the right triangle is ", hypotenuse)