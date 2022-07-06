

def rectangle_calcs():
    side_a = int(input("Enter length of the first side of the rectangle: "))
    side_b = int(input("Enter length of the second side of the rectangle: "))
    rect_perimeter = 2 * (side_a+side_b)
    rect_area = side_a*side_b
    return print(f'Your rectangle perimeter equals to {rect_perimeter}. Your rectangle area equals to {rect_area}')


rectangle_calcs()
