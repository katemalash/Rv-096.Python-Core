seat = int(input("Enter your seat number:  "))
if seat % 2 == 0:
    print("seat is top")
else: 
    print("seat is bottom")
if seat >= 37:
    print("seat is side")
else: 
    print("seat is compartment")