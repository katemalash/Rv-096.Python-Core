
def rectangle_perimeter_calcs(side_a_length, side_b_length):
    rectangle_perimeter = 2 * (side_a_length+side_b_length)
    return rectangle_perimeter


def rectangle_area_calcs(side_a_length, side_b_length):
    rectangle_area = side_a_length * side_b_length
    return rectangle_area


side_a = int(input("Enter length of the first side of the rectangle: "))
side_b = int(input("Enter length of the second side of the rectangle: "))

result_perimeter = rectangle_perimeter_calcs(side_a, side_b)
result_area = rectangle_area_calcs(side_a, side_b)

print(f'Your rectangle perimeter equals to {result_perimeter}. Your rectangle area equals to {result_area}')

