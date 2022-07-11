# Depending on the user's choice, calculate the square of ​​either a rectangle, or a triangle, or a circle. If a rectangle or triangle is selected, the lengths of the sides should be invited; is circle, its radius.
#Для того щоб розрахувати площу трикутника (S), необхідно помножити ½ на його сторону і на висоту.
print("The area of what geometric shape do you want to determine: a rectangle, a triangle or a circle?")
name = str(input("Please, input the name of geometric shape: "))
if name == 'rectangle':
    first_side= float(input("Please, input the first side: "))
    second_side= float(input("Please, input the second side: "))
    area_of_the_rectangle = float(first_side * second_side)
    print("Area of the rectangle is", area_of_the_rectangle)
if name == 'circle':
    radius= float(input("Please, input the radius: "))
    area_of_the_circle = float(3.14 * pow(radius, 2))
    print("Area of the circle is", area_of_the_circle)
if name == 'triangle':
    first_side= float(input("Please, input the first side: "))
    second_side= float(input("Please, input the second side: "))
    third_side= float(input("Please, input the third side: "))
    half_perimeter= (first_side + second_side + third_side)/2
    area_of_the_triangle = (half_perimeter*((half_perimeter-first_side)*(half_perimeter-second_side)*(half_perimeter-third_side)))** 0.5
    print("Area of the triangle is", area_of_the_triangle)
