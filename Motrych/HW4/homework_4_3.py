import math 

number =math.trunc( float(input("Enter number: ")))
if number < 0:
    a = "negative"
elif number == 0:
        a = "digit is 0"
elif number > 0:
        a = "positive"

b = len(str(number))             
print(f"Your number is {a} {b}-digits") 