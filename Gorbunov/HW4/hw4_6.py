# UZ
place_number= int(input("Enter your place number: "))
if place_number<=36:
    if place_number%2==0:
        print("TOP COUPE SEAT")
    else: print("BOTTOM COUPE SEAT")
elif 37<=place_number<=54:
    if place_number%2==0:
        print ("TOP SIDE SEAT")
    else: print("BOTTOM SIDE SEAT")
else: print("Check you seat number.")