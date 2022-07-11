#Calculate the area and perimeter of the rectangle for an entered width and height input=int("enter the metrics").

width = int(input("Please enter the width of the rectangle (in centimeters): "))
height = int(input("Please enter the height of the rectangle (in centimeters): "))
area = int(width + height)
perimeter = 2*(width + height)
print("The area is " , end='')
print(area, end='')
print (" centimeters squared")

print("The perimeter is " , end='')
print(perimeter, end='')
print (" centimeters squared")