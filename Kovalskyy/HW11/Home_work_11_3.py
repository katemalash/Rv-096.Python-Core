place_number = input("Enter place number: ")
try:
    place_number = int(place_number)
    if 1<= place_number <= 54:
        if place_number %2 ==0:
            if place_number <=36:
                print(f"Your place №{place_number} is top in the compartment")
            else:
                print(f"Your place №{place_number} is top in the side")

        elif place_number <=35:
            print(f"Your place №{place_number} is bottom in the compartment")
        else:
            print(f"Your place №{place_number} is bottom in the side")
except ValueError:
    print("Enter only numbers")    
else:
    print("Wrong place number!")