#Calculate the length of the hypotenuse on the two entered other sides of the right triangle.

side_of_traingle_a = int(input("Please enter the side of the traingle (in centimeters): "))
side_of_traingle_b = int(input("Please enter the side of the traingle (in centimeters): "))
hypotenuse = float((pow(side_of_traingle_a, 2)+pow(side_of_traingle_b, 2))** 0.5)

print("The hypotenuse is " , end='')
print(hypotenuse, end='')
print (" centimeters")