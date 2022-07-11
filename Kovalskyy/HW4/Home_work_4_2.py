user_choice = (input("Enter rectangle, triangle or circle: "))

if user_choice == 'rectangle':
    height = float(input("Enter height value: "))
    width = float(input("Enter width value: "))
    area_rec = height * width
    print("area of a rectangle =", area_rec)

elif user_choice == 'triangle':
    side_a = float(input("Enter side_a value: "))
    side_b = float(input("Enter side_b value: "))
    side_c = float(input("Enter side_b value: "))
    s = (side_a + side_b + side_c) /2
    area_tri = (s * (s-side_a) * (s-side_b) * (s-side_c))**0.5
    print("area of a rectangle =", area_tri) 

elif user_choice == 'circle':
    radius = float(input("Enter radius value: "))
    pi = 3.14
    area_cir = pi*radius**2
    print("area of a circle =", area_cir) 

else:
    print("Wrong input")