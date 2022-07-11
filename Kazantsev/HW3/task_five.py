from math import sqrt


def find_hypotenuse(cathetus_a, cathetus_b):

    return cathetus_a**2 + cathetus_b ** 2


first_cathetus = float(input("Enter length of the first cathetus: "))
second_cathetus = float(input("Enter length of the second cathetus: "))


hypotenuse_squared = find_hypotenuse(first_cathetus, second_cathetus)
print(f'Your hypotenuse is {round(sqrt(hypotenuse_squared), 3)}')
