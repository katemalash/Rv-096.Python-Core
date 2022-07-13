
first_character = input("Please, enter a character for an outline: ")
second_character = input("Please, enter a character for a fill: ")

rectangle_length = int(input("Enter you rectangle length: "))
rectangle_width = int(input("Enter you rectangle width: "))

line_counter = 0
first_last_row = first_character*rectangle_length

for side_a in range(1, rectangle_length+1):
    for side_b in range(1, rectangle_width+1):
        if side_a == 1 or side_a == rectangle_length or side_b == 1 or side_b == rectangle_width:
            print(first_character + ' ', end='')
        else:
            print(second_character + ' ', end='')
    print()
