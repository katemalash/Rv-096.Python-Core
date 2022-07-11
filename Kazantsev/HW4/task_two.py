from math import pi

flag = 1
while flag:
    figure = input("Write down, what figure do you want to choose: rectangle, triangle or a circle?\n")
    if figure == 'rectangle':
        side_a = float(input("What's length of the first side?\n"))
        side_b = float(input("What's length of the second side?\n"))
        rectangle_area = side_b * side_b
        print(f'Your rectangle area is {rectangle_area}')
        break

    elif figure == 'triangle':
        triangle_width = float(input("What's your triangle width?\n"))
        triangle_height = float(input("What's your triangle height?\n"))
        triangle_area = (triangle_width * triangle_height) / 2
        print(f'Your triangle area is {triangle_area}')
        break

    elif figure == 'circle':
        circle_radius = float(input("What's your circle radius?\n"))
        circle_area = pi * circle_radius**2
        print(f'Your circle area is {circle_area}')
        break

    else:
        print("Wrong figure, you should choose from rectangle, square or a circle!")
