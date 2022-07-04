height = float(input("press height(m): "))
width = float(input("press width(m): "))
action = input("perimeter or area? (p - a): ")
perimetr = 2*(height+width)
area = height*width
if action == "p":
    print (perimetr)
elif action == "a":
    print (area)
else:
    print ("not entered correctly")