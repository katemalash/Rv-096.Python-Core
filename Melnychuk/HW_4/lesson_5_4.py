# R is a radius of the round stage.
# S is a square of the square hall.
# K is a passage from the wall to the stage.
# a is a side of the square hall.

S = float(input("Enter the area of the hall: "))
R = float(input("Enter the radius of the stage: "))

a = S ** 0.5
K = a - 2*R
if K > 0:
    print(f"It's posible to place such stage in the hall.\nThere will be a passage {K} m.")
else:
    print(f"It's not posible to place such stage in the hall so that there was a passage.")