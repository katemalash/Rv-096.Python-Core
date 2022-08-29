from math import sqrt

side_a = input("Enter side_a value: ")
side_b = input("Enter side_b value: ")

try:
    side_a = float(side_a)
    side_b = float(side_b)
    hypotenuse = sqrt(side_a**2 + side_b**2)
except ValueError:
    print("Enter only numbers")
except :
    print("Something is wrong (not value)")
else:
    print("The hypotenuse of the right triangle is ", hypotenuse)