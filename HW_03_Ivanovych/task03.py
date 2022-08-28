# Calculate the area and perimeter of the rectangle for an entered width and height.

width = float(input("Enter the width of the rectangle : "))
length = float(input("Enter the length of the rectangle : "))

area = width * length

perimeter = (width + length) * 2

print("Area of the Rectangle is %.2f" %area)
print("Perimete of the Rectangle is %.2f" %perimeter)
