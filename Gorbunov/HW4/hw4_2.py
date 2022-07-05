choise = int(input("Make your choise:\nFor choose rectangle, press 1: \nFor choose triangle, press 2: \nFor choose circle, press 3: "))
if choise ==1:
    a, b = map(float, input('Enter values of sides 1 and 2 by a space: ').split())
    rectangle_area = a*b
    print(f"Rectangle area is :{rectangle_area}") 
elif choise ==2:
    a, b, c = map(float, input('Enter three values "lengths of the sides" of a triangleby by space: ').split()) 
    p=(a+b+c)/2
    triangle_area = (p*(p-a)*(p-b)*(p-c))**0.5
    print(f"Triangle area is :{triangle_area}") 
elif choise ==3:
    radius = int(input("Enter radius: "))
    circle_area =  3.14 *radius**2 
    print(f"Circle area is :{circle_area}")
else: print("Input Error, try again.") 
