
flag = 1




while flag:
    place_in_a_train = int(input("Enter your place: "))

    if place_in_a_train % 2 == 0:
        position = 'top'
    else:
        position = 'bottom'

    if place_in_a_train < 1 or place_in_a_train > 54:
        print("Wrong place number!")
    elif 36 >= place_in_a_train >= 1:
        side_or_comp = 'compartment'
        break
    elif 54 >= place_in_a_train >= 37:
        side_or_comp = 'side'
        break

print(f"Your place in a train is a {position} {side_or_comp} place .")
