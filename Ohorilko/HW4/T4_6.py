#The number of a place in the reserved carriage is given. Determine which place it is: top or bottom, compartment or side.
number_of_place= int(input("Plase, input the seat number: "))
if number_of_place >0 and number_of_place <=54:
    if number_of_place %2== 0 and number_of_place <=36:
        print("It is a upper compartment coach!")
    elif number_of_place %2!= 0 and number_of_place <=36:
        print("It is a lower compartment coach!")
    elif (number_of_place) %2 != 0 and number_of_place >36:
        print("It is a lower side coach!")
    else:
        print("It is a upper side coach!")          
else:
    print("Wrong number ot the place!")
