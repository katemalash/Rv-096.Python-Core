square = int(input("Input square: "))
radius = int(input("Input radius: "))
passage = int(input("Input passage: "))

area_square = square *square
area_circle = 3.14*radius**2

if area_circle < (area_square - passage):
    print(f"It is possible to place a round stage with radius {radius}m, \
    \nin a square hall of square {square}m with a passage {passage}m")

else:
    print("No, it is not possible")