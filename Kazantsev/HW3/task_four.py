import math


def circle_calcs():
    circle_radius = int(input("Enter a circle radius: "))
    circle_perimeter = math.pi * circle_radius**2
    circle_area = 2 * math.pi * circle_radius
    return print(f'Your circle perimeter equals to {round(circle_perimeter, 2)}. Your circle area equals to \
{round(circle_area, 2)}')


circle_calcs()
