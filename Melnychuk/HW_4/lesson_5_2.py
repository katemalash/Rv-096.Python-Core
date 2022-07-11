user_choice = None
while user_choice not in {"rectangle", "triangle", "circle"}:
    user_choice = input("Enter the figure you've chosen: rectangle, triangle or circle: ").lower()
    
if user_choice == "rectangle":
    lenght = float(input("Enter the lenght of the rectangle: "))
    width = float(input("Enter the height of the rectangle: "))
    square = lenght * width

elif user_choice == "triangle":
    a = float(input("Enter the lenght of the first side othe triangle: "))
    b = float(input("Enter the lenght of the second side othe triangle: "))
    c = float(input("Enter the lenght of the third side othe triangle: "))
    half_perimeter = (a+b+c)/2
    square = (half_perimeter*(half_perimeter-a)*(half_perimeter-b)*(half_perimeter-c)) ** 0.5

elif user_choice == "circle":
    radius = float(input("Enter the radius of the circle: "))
    pi = 3.14
    square = pi * radius**2

print(f"The square of {user_choice} is {square}.")