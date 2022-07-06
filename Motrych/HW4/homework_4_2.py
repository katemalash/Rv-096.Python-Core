choice = int(input("Please choice the figure,1-rectangle,2-triangle,3-circle: "))
if choice > 3:
    choice = int(input("Please choice the figure,1-rectangle,2-triangle,3-circle: "))


if choice == 1:
    height = float(input("Please enter height: ")) 
    weight = float(input(" Please enter weight: "))
    square1 = height*weight
    print (f"Square of rectangle is: {square1} ")
elif choice == 2:
    leg1 = float(input("Please enter leg1: "))
    leg2 = float(input("Please enter leg2: "))
    leg3 = float(input("Please enter leg3: "))
    halfperimeter = (leg1+leg2+leg3)/2
    from math import sqrt
    square2= sqrt(halfperimeter*(halfperimeter-leg1)*(halfperimeter-leg2)*(halfperimeter-leg3))
    print (f"Square of triangle is: {square2} ")   
elif choice == 3:
    radius = float(input("Please enter radius: "))
    from math import pi
    square3 = pi*radius**2
    print (f"Square of circle is:{square3} ")     

