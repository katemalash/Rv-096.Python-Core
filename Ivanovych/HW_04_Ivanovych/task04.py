
radius_circle = int(input("Enter circle radius: "))
area_square = int(input("Enter area square: "))
hall = int(input("What hall do you want: "))

if (radius_circle+hall)*2 <= area_square**0.5:
    print("real")
else:
    print("unreal")
