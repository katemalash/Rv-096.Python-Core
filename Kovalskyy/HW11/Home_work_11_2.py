user_choice = input("Enter 1 for rectangle, 2 for triangle or 3 for circle: ")
try:
    user_choice = int(user_choice)
except ValueError:
    print("Enter only numbers")

if user_choice == 1:
    try:
        height = float(input("Enter height value: "))
        width = float(input("Enter width value: "))
        area_rec = height * width
    except ValueError:
        print("Enter only numbers")
    else:   
        print("area of a rectangle =", area_rec)

elif user_choice == 2:
    try:
        side_a = float(input("Enter side_a value: "))
        side_b = float(input("Enter side_b value: "))
        side_c = float(input("Enter side_b value: "))
        s = (side_a + side_b + side_c) /2
        area_tri = (s * (s-side_a) * (s-side_b) * (s-side_c))**0.5
    except ValueError:
        print("Enter only numbers")
    else:
        print("area of a rectangle =", area_tri) 

elif user_choice == 3:
    try:
        radius = float(input("Enter radius value: "))
        pi = 3.14
        area_cir = pi*radius**2
    except ValueError:
        print("Enter only numbers")
    else:
        print("area of a circle =", area_cir)
        