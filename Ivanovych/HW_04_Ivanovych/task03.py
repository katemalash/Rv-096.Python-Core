number = int(input("Enter number: "))

if number >= 0:
    if number < 10:
        print("positive one-digit")
    elif number >= 10 and number < 100:
        print("positive two-digit")
    else:
        print("positive three or more digit number")
else:
    if number > -10:
        print("negative one-digit")
    elif number <= -10 and number > -100:
        print("negative two-digit")
    else:
        print("negative three or more digit number")
