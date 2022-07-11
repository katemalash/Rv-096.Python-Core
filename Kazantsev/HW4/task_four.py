from math import sqrt

circle_radius = float(input("Enter circle radius: "))
hall_area = float(input("Enter hall area: "))
passage_length = float(input("Enter passage between wall and stage: "))

if circle_radius+passage_length <= sqrt(hall_area):
    print("It is possible to place a round stage in this hall!")
else:
    print("This hall is too small!")
