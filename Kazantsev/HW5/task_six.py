
user_numbers = []
print("Please, enter 5 numbers.\n")
numbers_pool = 5
negatives = 0
positives = 0

while numbers_pool > 0:
    print(f"Numbers left to enter: {numbers_pool}")
    number = input("Please, enter your number: ")
    if number.isdigit():
        number = int(number)
        user_numbers.append(number)
        positives += 1
        numbers_pool -= 1
        continue
    elif int(number) < 0:
        number = int(number)
        user_numbers.append(number)
        negatives += 1
        numbers_pool -= 1
        continue
    elif number == 0:
        user_numbers.append(number)
        numbers_pool -= 1
        continue
    else:
        print("Please, enter a number!")
        continue

print(f"Your numbers list is: {user_numbers}.\nPercentage of positives in it is: {(positives / 5) * 100}%.\nPercentage "
      f"of negatives in it is: {(negatives / 5) * 100}%")
