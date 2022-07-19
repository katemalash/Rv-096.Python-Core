mul_number = []
count= 0
while count <10:
    count +=1
    user_number = int(input("Enter ten natural numbers greater than 2: "))

    if user_number <2:
        print("Wrong number")
        count -=1
        continue

    print("You entered", count, "number")

    if user_number %5 ==0:
        mul_number.append(user_number)

print(mul_number)
