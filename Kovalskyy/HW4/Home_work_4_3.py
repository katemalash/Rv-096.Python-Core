check_digit = int(input("Enter a number: "))

if check_digit == 0:
    print("Number is zero")

elif check_digit >= 1 and check_digit <10:
    print("positive one-digit")

elif check_digit >= 10 and check_digit <100:
    print("positive two-digit")

elif check_digit <= -1 and check_digit >-10:
    print("negative one-digit")

elif check_digit <= -10 and check_digit >-100:
    print("negative two-digit")

else:
    print("Hight number")