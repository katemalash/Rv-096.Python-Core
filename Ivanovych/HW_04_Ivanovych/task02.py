import math


choice = input("What area do you want to count(rectangle, triangle or circle)? : ")

if choice == "rectangle":
    side_a = int(input("Enter a: "))
    side_b = int(input("Enter b: "))
    print("Area rectangle = ",side_a*side_b)
elif choice == "triangle":
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    print("Area rectangle = ", base * height * 0.5)
elif choice == "circle":
    radius = int(input("Enter radius: "))
    print("Area circle = ",math.pi * radius ** 2)
else:
    print("You choose nothing")
