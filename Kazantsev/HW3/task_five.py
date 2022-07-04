import math


def find_hypotenuse():
    first_cathetus = int(input("Enter length of the first cathetus: "))
    second_cathetus = int(input("Enter length of the second cathetus: "))
    hypotenuse_squared = first_cathetus**2 + second_cathetus ** 2

    return print(f'Your hypotenuse is {round(math.sqrt(hypotenuse_squared), 3)}')


find_hypotenuse()
