
number = float(input("Enter a number: "))

if number > 0 and number/10 < 1:
    print("Positive one-digit")
elif number > 0 and number/10 > 1:
    print("Positive two-digit")
elif number < 0 and (number/10)*-1 < 1:
    print("Negative one-digit")
elif number < 0 and (number/10)*-1 > 1:
    print("Negative two-digit")
