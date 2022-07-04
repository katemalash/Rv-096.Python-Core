from math import pi


def circle_perimeter_calcs(circle_radius):

    return pi * circle_radius**2


def circle_area_calcs(circle_radius):

    return 2 * pi * circle_radius


circle_radius_input = int(input("Enter a circle radius: "))

perimeter = circle_perimeter_calcs(circle_radius_input)
area = circle_area_calcs(circle_radius_input)

print(f'Your circle perimeter equals to {round(perimeter, 2)}. Your circle area equals to \
{round(area, 2)}')
